#!/bin/bash
VERSION="1.0.0"
SCRIPT_NAME=$(basename "$0")

# 기본 설정값
DEFAULT_MODEL="gpt-4.1-nano"
DEFAULT_ERR_LOG="/tmp/thehelp_err.log"
DEFAULT_OUT_LOG="/tmp/thehelp_out.log"
DEFAULT_HISTORY_FILE="$HOME/.bash_history"
ZSH_HISTORY_FILE="$HOME/.zsh_history"
DEFAULT_MAX_TOKENS=500
DEFAULT_TEMPERATURE=0.7

# 환경 변수 설정 (환경 변수가 없으면 기본값 사용)
MODEL=${THEHELP_MODEL:-$DEFAULT_MODEL}
ERR_LOG=${THEHELP_ERR_FILE:-$DEFAULT_ERR_LOG}
OUT_LOG=${THEHELP_OUT_FILE:-$DEFAULT_OUT_LOG}
MAX_TOKENS=${THEHELP_MAX_TOKENS:-$DEFAULT_MAX_TOKENS}
TEMPERATURE=${THEHELP_TEMPERATURE:-$DEFAULT_TEMPERATURE}

# 색상 설정
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
BLUE='\033[0;34m'
PURPLE='\033[0;35m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

# 필수 의존성 확인
check_dependencies() {
    local missing_deps=()
    
    if ! command -v curl &> /dev/null; then
        missing_deps+=("curl")
    fi
    
    if ! command -v jq &> /dev/null; then
        missing_deps+=("jq")
    fi
    
    if [ ${#missing_deps[@]} -ne 0 ]; then
        echo -e "${RED}오류: 다음 의존성 패키지가 설치되어 있지 않습니다:${NC} ${missing_deps[*]}"
        echo -e "다음 명령어로 설치할 수 있습니다:"
        echo -e "${YELLOW}sudo apt update && sudo apt install -y ${missing_deps[*]}${NC}"
        exit 1
    fi
}

# API 키 확인
check_api_key() {
    if [ -z "$OPENAI_API_KEY" ]; then
        echo -e "${RED}오류: OPENAI_API_KEY 환경 변수가 설정되지 않았습니다.${NC}"
        echo -e "다음 명령어로 설정해 주세요:"
        echo -e "${YELLOW}export OPENAI_API_KEY=\"your-api-key\"${NC}"
        echo -e "영구적으로 설정하려면 ~/.bashrc 또는 ~/.zshrc 파일에 추가하세요."
        exit 1
    fi
}

# 도움말 표시
show_help() {
    cat << EOF
사용법: $SCRIPT_NAME [옵션] [명령어]

설명:
  터미널 명령어 실행 시 발생하는 에러나 출력 메시지를 AI로 분석하여
  문제 원인과 해결책을 제공하는 CLI 어시스턴트입니다.

옵션:
  -v, --verbose   상세 제안 모드 (최대 3가지 해결책 제안)
  -h, --help      이 도움말 메시지 표시
  -V, --version   버전 정보 표시

환경 변수:
  OPENAI_API_KEY    (필수) OpenAI API 키
  THEHELP_MODEL     (선택) 사용할 모델명 (기본값: $DEFAULT_MODEL)
  THEHELP_ERR_FILE  (선택) stderr 로그 경로 (기본값: $DEFAULT_ERR_LOG)
  THEHELP_OUT_FILE  (선택) stdout 로그 경로 (기본값: $DEFAULT_OUT_LOG)

사용 예시:
  $SCRIPT_NAME                         # 이전 명령어 자동 분석
  $SCRIPT_NAME git branc               # 명령어 실행 후 결과 분석
  $SCRIPT_NAME -v ls -la /no/such/dir  # 상세 분석 모드로 실행

자동 로그 캡처 설정:
  다음 내용을 ~/.bashrc 또는 ~/.zshrc에 추가:
  
  exec 2> >(tee -a $DEFAULT_ERR_LOG >&2)
  exec 1> >(tee -a $DEFAULT_OUT_LOG >&1)
EOF
}

# 버전 정보 표시
show_version() {
    echo -e "${CYAN}$SCRIPT_NAME${NC} 버전 ${GREEN}$VERSION${NC}"
    echo "Copyright (c) $(date +%Y)"
}

# 로그 파일 설정 확인 및 생성
setup_log_files() {
    # 로그 디렉토리 확인
    local err_dir=$(dirname "$ERR_LOG")
    local out_dir=$(dirname "$OUT_LOG")
    
    if [ ! -d "$err_dir" ]; then
        mkdir -p "$err_dir" || { 
            echo -e "${RED}오류: 로그 디렉토리 '$err_dir'를 생성할 수 없습니다.${NC}"; 
            exit 1; 
        }
    fi
    
    if [ ! -d "$out_dir" ]; then
        mkdir -p "$out_dir" || { 
            echo -e "${RED}오류: 로그 디렉토리 '$out_dir'를 생성할 수 없습니다.${NC}"; 
            exit 1; 
        }
    fi
    
    # 로그 파일 접근 권한 확인
    touch "$ERR_LOG" 2>/dev/null || { 
        echo -e "${RED}오류: 로그 파일 '$ERR_LOG'에 쓰기 권한이 없습니다.${NC}"; 
        exit 1; 
    }
    
    touch "$OUT_LOG" 2>/dev/null || { 
        echo -e "${RED}오류: 로그 파일 '$OUT_LOG'에 쓰기 권한이 없습니다.${NC}"; 
        exit 1; 
    }
    
    # 로그 파일이 너무 크면 정리 (1MB 초과 시)
    if [ -f "$ERR_LOG" ] && [ $(stat -c%s "$ERR_LOG") -gt 1048576 ]; then
        echo "" > "$ERR_LOG"
    fi
    
    if [ -f "$OUT_LOG" ] && [ $(stat -c%s "$OUT_LOG") -gt 1048576 ]; then
        echo "" > "$OUT_LOG"
    fi
}

# 최근 명령어 가져오기
get_last_command() {
    # fc 명령어를 사용하여 명령어 히스토리 가져오기
    # -l: 목록 형식, -n: 명령어 번호 제외, 마지막 20개 명령어 가져오기
    local history_cmds=$(fc -ln -20 2>/dev/null)
    local cmd=""
    local found_non_thehelp=false
    
    # 각 명령어를 역순으로 확인
    while IFS= read -r line; do
        # 앞뒤 공백 제거
        line=$(echo "$line" | sed 's/^[ \t]*//;s/[ \t]*$//')
        
        # 비어있지 않고 thehelp를 포함하지 않는 명령어 찾기
        if [ -n "$line" ] && [[ "$line" != *"thehelp"* ]]; then
            cmd="$line"
            found_non_thehelp=true
            break
        fi
    done <<< "$(echo "$history_cmds" | tac)"  # tac으로 역순 처리
    
    # 적절한 명령어를 찾지 못한 경우 기본값 반환
    if [ "$found_non_thehelp" = false ]; then
        echo "history"
    else
        echo "$cmd"
    fi
}

# 명령어 실행 및 결과 캡처
execute_command() {
    local cmd="$*"
    local temp_err_file="/tmp/thehelp_temp_err_$$.log"
    local temp_out_file="/tmp/thehelp_temp_out_$$.log"
    
    echo -e "${BLUE}실행 중:${NC} $cmd"
    
    # 명령어 실행 및 출력 캡처
    eval "$cmd" > "$temp_out_file" 2> "$temp_err_file"
    local exit_code=$?
    
    # 결과 표시
    if [ -s "$temp_err_file" ]; then
        echo -e "${RED}오류 출력:${NC}"
        cat "$temp_err_file"
    fi
    
    if [ -s "$temp_out_file" ]; then
        echo -e "${GREEN}표준 출력:${NC}"
        cat "$temp_out_file"
    fi
    
    # 반환 코드 표시
    if [ $exit_code -eq 0 ]; then
        echo -e "${GREEN}명령어 실행 완료 (종료 코드: $exit_code)${NC}"
    else
        echo -e "${RED}명령어 실행 실패 (종료 코드: $exit_code)${NC}"
    fi
    
    # 분석할 로그 선택
    if [ -s "$temp_err_file" ]; then
        analyze_output "$cmd" "$(cat "$temp_err_file")" "error"
    elif [ -s "$temp_out_file" ]; then
        analyze_output "$cmd" "$(cat "$temp_out_file")" "output"
    else
        echo -e "${YELLOW}분석할 출력이 없습니다.${NC} 명령어 실행 시 아무런 출력이 생성되지 않았습니다."
    fi
    
    # 임시 파일 삭제
    rm -f "$temp_err_file" "$temp_out_file"
}

# 자동 모드 - 마지막 명령어 및 로그 분석
auto_analyze() {
    local last_cmd=$(get_last_command)
    
    echo -e "${BLUE}마지막 명령어:${NC} $last_cmd"
    
    # 직접 마지막 명령어의 오류 가져오기 (더 신뢰성 있는 방법)
    local last_err=""
    if [ "$last_cmd" != "history" ]; then
        # 마지막 명령어 재실행하여 오류 캡처
        last_err=$(eval "$last_cmd" 2>&1 1>/dev/null)
    fi
    
    # 직접 캡처한 오류가 있으면 분석
    if [ -n "$last_err" ]; then
        analyze_output "$last_cmd" "$last_err" "error"
        return
    fi
    
    # stderr 로그 확인 (기존 방법)
    if [ -f "$ERR_LOG" ] && [ -s "$ERR_LOG" ]; then
        local last_err=$(tail -n 50 "$ERR_LOG")
        if [ -n "$last_err" ]; then
            analyze_output "$last_cmd" "$last_err" "error"
            return
        fi
    fi
    
    # stderr가 없으면 stdout 로그 확인
    if [ -f "$OUT_LOG" ] && [ -s "$OUT_LOG" ]; then
        local last_out=$(tail -n 50 "$OUT_LOG")
        if [ -n "$last_out" ]; then
            analyze_output "$last_cmd" "$last_out" "output"
            return
        fi
    fi
    
    echo -e "${YELLOW}분석할 로그가 없습니다.${NC} 로그 캡처 설정을 확인해 주세요."
    echo "다음 내용을 ~/.bashrc 또는 ~/.zshrc에 추가했는지 확인하세요:"
    echo "  exec 2> >(tee -a $ERR_LOG >&2)"
    echo "  exec 1> >(tee -a $OUT_LOG >&1)"
}

# AI 프롬프트 생성
generate_prompt() {
    local cmd="$1"
    local output="$2"
    local type="$3"  # error 또는 output
    local verbose="$4"  # 상세 모드 여부
    
    local system_prompt=""
    local user_prompt=""
    
    # 시스템 프롬프트 설정
    system_prompt="당신은 리눅스 명령어와 프로그래밍 환경을 전문적으로 다루는 AI 터미널 어시스턴트입니다. 사용자가 제공한 명령어와 출력/에러 메시지를 분석하고, 문제 원인과 해결책을 정확하게 제시해주세요. 답변은 항상 한국어로 해주세요."
    
    # 상세 모드 여부에 따라 프롬프트 조정
    if [ "$verbose" = "true" ]; then
        system_prompt+=" 상세 모드가 활성화되어 있으므로, 최대 3가지 가능한 해결책을 제시하고 각각의 장단점을 설명해주세요. 필요하다면 명령어 구문 오류나 대체 명령어도 추천해주세요."
    else
        system_prompt+=" 간결하고 핵심적인 해결책 한 가지를 명확하게 제시해주세요. 가능하면 실행 가능한 명령어 형태로 제안해주세요."
    fi
    
    # 사용자 프롬프트 설정
    if [ "$type" = "error" ]; then
        user_prompt="다음 명령어 실행 중 에러가 발생했습니다.\n\n명령어: $cmd\n\n에러 메시지:\n$output\n\n이 에러의 원인과 해결 방법을 알려주세요."
    else
        user_prompt="다음 명령어와 그 출력 결과를 분석해주세요.\n\n명령어: $cmd\n\n출력 결과:\n$output\n\n이 출력이 의미하는 바와 필요하다면 추가적인 조치 방법을 알려주세요."
    fi
    
    # JSON 형식의 프롬프트 생성
    local json_data=$(jq -n \
        --arg model "$MODEL" \
        --arg sys "$system_prompt" \
        --arg user "$user_prompt" \
        --argjson max_tokens "$MAX_TOKENS" \
        --argjson temperature "$TEMPERATURE" \
        --argjson stream "true" \
        '{
            model: $model,
            messages: [
                {role: "system", content: $sys},
                {role: "user", content: $user}
            ],
            max_tokens: $max_tokens,
            temperature: $temperature,
            stream: $stream
        }')
    
    echo "$json_data"
}

# 출력 분석 및 AI 응답 처리
analyze_output() {
    local cmd="$1"
    local output="$2"
    local type="$3"  # error 또는 output
    
    # 상세 모드 여부 확인
    local verbose="false"
    if [ "$VERBOSE_MODE" = "true" ]; then
        verbose="true"
    fi
    
    # 프롬프트 생성
    local prompt=$(generate_prompt "$cmd" "$output" "$type" "$verbose")
    
    echo -e "\n${PURPLE}AI 분석 중...${NC} 문제 원인과 해결책을 찾고 있습니다."
    echo -e "${CYAN}----------------------------------------${NC}"
    
    # API 호출 및 스트리밍 응답 처리
    curl -s "https://api.openai.com/v1/chat/completions" \
        -H "Content-Type: application/json" \
        -H "Authorization: Bearer $OPENAI_API_KEY" \
        -d "$prompt" | process_streaming_response
    
    echo -e "\n${CYAN}----------------------------------------${NC}"
}

# 스트리밍 응답 처리
process_streaming_response() {
    local buffer=""
    local content=""
    
    while IFS= read -r line; do
        # "data: [DONE]" 메시지 확인
        if [[ "$line" == "data: [DONE]" ]]; then
            break
        fi
        
        # data: 접두사 확인
        if [[ "$line" == data:* ]]; then
            # JSON 데이터 추출
            buffer="${line#data: }"
            
            # JSON 파싱이 가능한지 확인
            if jq -e . >/dev/null 2>&1 <<< "$buffer"; then
                # content 필드 추출 시도
                content=$(echo "$buffer" | jq -r '.choices[0].delta.content // ""')
                
                # content가 있으면 출력
                if [ -n "$content" ]; then
                    printf "%s" "$content"
                fi
            fi
        fi
    done
}

# 로그 캡처 설정 확인
check_log_capture_setup() {
    local shell_config=""
    
    # 사용 중인 쉘 확인
    if [ -n "$ZSH_VERSION" ]; then
        shell_config="$HOME/.zshrc"
    else
        shell_config="$HOME/.bashrc"
    fi
    
    # 설정 파일 존재 확인
    if [ ! -f "$shell_config" ]; then
        return 1
    fi
    
    # 로그 캡처 설정 확인
    if ! grep -q "exec.*tee.*$ERR_LOG" "$shell_config" || ! grep -q "exec.*tee.*$OUT_LOG" "$shell_config"; then
        return 1
    fi
    
    return 0
}

# 로그 캡처 설정 추가
setup_log_capture() {
    local shell_config=""
    
    # 사용 중인 쉘 확인
    if [ -n "$ZSH_VERSION" ]; then
        shell_config="$HOME/.zshrc"
    else
        shell_config="$HOME/.bashrc"
    fi
    
    echo -e "${YELLOW}로그 캡처 설정을 추가합니다.${NC} ($shell_config)"
    
    # 설정 파일에 추가
    cat << EOF >> "$shell_config"

# thehelp 로그 캡처 설정
exec 2> >(tee -a $ERR_LOG >&2)
exec 1> >(tee -a $OUT_LOG >&1)
EOF
    
    echo -e "${GREEN}설정이 추가되었습니다.${NC} 새 터미널 세션 또는 다음 명령어로 적용하세요:"
    echo -e "${YELLOW}source $shell_config${NC}"
}

# 메인 함수
main() {
    local VERBOSE_MODE="false"
    local COMMAND=""
    
    # 옵션 파싱
    while [ "$#" -gt 0 ]; do
        case "$1" in
            -h|--help)
                show_help
                exit 0
                ;;
            -V|--version)
                show_version
                exit 0
                ;;
            -v|--verbose)
                VERBOSE_MODE="true"
                shift
                ;;
            *)
                COMMAND="$*"
                break
                ;;
        esac
    done
    
    # 의존성 확인
    check_dependencies
    
    # API 키 확인
    check_api_key
    
    # 로그 파일 설정
    setup_log_files
    
    # 로그 캡처 설정 확인 및 제안
    if ! check_log_capture_setup; then
        echo -e "${YELLOW}경고:${NC} 로그 캡처 설정이 되어있지 않습니다."
        read -p "로그 캡처 설정을 자동으로 추가하시겠습니까? (y/n): " add_setup
        if [[ "$add_setup" =~ ^[Yy]$ ]]; then
            setup_log_capture
        else
            echo -e "${YELLOW}알림:${NC} 자동 분석 모드를 사용하려면 로그 캡처 설정이 필요합니다."
        fi
    fi
    
    # 명령어 유무에 따라 실행 모드 결정
    if [ -z "$COMMAND" ]; then
        # 자동 모드 - 마지막 명령어 및 로그 분석
        auto_analyze
    else
        # 명령어 실행 모드
        execute_command "$COMMAND"
    fi
}

# 스크립트 실행
main "$@"