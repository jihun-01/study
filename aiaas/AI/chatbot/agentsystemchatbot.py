import json
from enum import Enum
from typing import List, Dict, Any, Optional
from dataclasses import dataclass
import os
import dotenv
from openai import OpenAI

dotenv.load_dotenv()
api_key = os.getenv('OPENAI_API_KEY')

class TaskStatus(Enum):
    PENDING = "pending"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"

@dataclass
class Task:
    id: str
    description: str
    action: str
    parameters: Dict[str, Any]
    status: TaskStatus = TaskStatus.PENDING
    result: Optional[Any] = None
    error: Optional[str] = None

class PlanningAgent:
    def __init__(self, llm_client):
        self.llm_client = llm_client
        self.available_actions = [
            "web_search", "calculate", "send_email", "save_file", "analyze_data"
        ]

    def create_plan(self, user_goal: str) -> List[Task]:
        actions_description = """
사용 가능한 액션들:
- web_search: 웹에서 정보 검색 (parameters: {"query": "검색어"})
- calculate: 수학 계산 (parameters: {"expression": "1+1"})
- send_email: 이메일 발송 (parameters: {"to": "email", "subject": "제목", "body": "내용"})
- save_file: 파일 저장 (parameters: {"filename": "파일명", "content": "내용"})
- analyze_data: 데이터 분석 (parameters: {"data_source": "데이터소스", "analysis_type": "분석타입"})
"""
        system_prompt = f"""
당신은 전문적인 계획 수립 에이전트입니다.
사용자의 목표를 분석하고 단계별 작업 계획을 세우세요.

{actions_description}
중요: 반드시 위의 5가지 액션 중에서만 선택해야 합니다.
각 작업은 구체적이고 실행 가능해야 합니다.
응답 형식 (반드시 JSON 형태로):
[
{{
    "id": "task_1",
    "description": "작업 설명",
    "action": "web_search",
    "parameters": {{"query": "검색어"}}
}}
]
"""
        try:
            response = self.llm_client.chat.completions.create(
                model="gpt-4.1-nano",
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": f"목표: {user_goal}"}
                ],
                temperature=0.1
            )
            content = response.choices[0].message.content.strip()
            if "```json" in content:
                content = content.split("```json")[1].split("```")[0].strip()
            elif "```" in content:
                content = content.split("```")[1].strip()
            tasks_data = json.loads(content)
            tasks = []
            for i, task_data in enumerate(tasks_data):
                action = task_data.get("action", "")
                if action not in self.available_actions:
                    print(f"경고: 유효하지 않은 액션 '{action}'을 'web_search'로 변경")
                    action = "web_search"
                    task_data["parameters"] = {"query": task_data.get("description", "")}
                task = Task(
                    id=task_data.get("id", f"task_{i+1}"),
                    description=task_data.get("description", ""),
                    action=action,
                    parameters=task_data.get("parameters", {})
                )
                tasks.append(task)
            return tasks
        except Exception as e:
            print(f"계획 수립 중 오류 발생: {e}")
            return [
                Task(
                    id="task_1",
                    description=f"{user_goal}에 대한 정보 검색",
                    action="web_search",
                    parameters={"query": user_goal}
                )
            ]

class ExecutionEngine:
    def __init__(self):
        self.actions = {
            "web_search": self._web_search,
            "calculate": self._calculate,
            "send_email": self._send_email,
            "save_file": self._save_file,
            "analyze_data": self._analyze_data
        }

    def execute_task(self, task: Task) -> Task:
        try:
            task.status = TaskStatus.RUNNING
            if task.action in self.actions:
                result = self.actions[task.action](task.parameters)
                task.result = result
                task.status = TaskStatus.COMPLETED
            else:
                task.error = f"알 수 없는 액션: {task.action}"
                task.status = TaskStatus.FAILED
        except Exception as e:
            task.error = str(e)
            task.status = TaskStatus.FAILED
        return task

    def _web_search(self, params: Dict[str, Any]) -> Dict[str, Any]:
        query = params.get("query", "")
        print(f"웹 검색: {query}")
        return {
            "query": query,
            "results": [
                {"title": f"{query} 관련 정보 1", "url": "https://example1.com"},
                {"title": f"{query} 관련 정보 2", "url": "https://example2.com"},
                {"title": f"{query} 관련 정보 3", "url": "https://example3.com"}
            ]
        }

    def _calculate(self, params: Dict[str, Any]) -> Dict[str, Any]:
        expression = params.get("expression", "0")
        try:
            if any(char in expression for char in ['import', 'exec', 'eval', '__']):
                raise ValueError("보안상 허용되지 않는 수식입니다.")
            result = eval(expression)
            print(f"계산: {expression} = {result}")
            return {"expression": expression, "result": result}
        except Exception as e:
            raise ValueError(f"계산 오류: {str(e)}")

    def _send_email(self, params: Dict[str, Any]) -> Dict[str, Any]:
        to = params.get("to", "")
        subject = params.get("subject", "")
        body = params.get("body", "")
        print(f"이메일 발송: {to} / {subject}")
        return {
            "status": "sent",
            "to": to,
            "subject": subject,
            "timestamp": time.time()
        }

    def _save_file(self, params: Dict[str, Any]) -> Dict[str, Any]:
        filename = params.get("filename", "output.txt")
        content = params.get("content", "")
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"파일 저장: {filename}")
            return {
                "filename": filename,
                "size": len(content),
                "saved": True
            }
        except Exception as e:
            raise Exception(f"파일 저장 실패: {str(e)}")

    def _analyze_data(self, params: Dict[str, Any]) -> Dict[str, Any]:
        data_source = params.get("data_source", "")
        analysis_type = params.get("analysis_type", "basic")
        print(f"데이터 분석: {data_source} / {analysis_type}")
        return {
            "data_source": data_source,
            "analysis_type": analysis_type,
            "summary": f"{data_source}에 대한 {analysis_type} 분석 완료",
            "insights": [
                f"{data_source}의 주요 트렌드 파악",
                f"{analysis_type} 분석을 통한 인사이트 도출",
                "향후 개선 방향 제시"
            ]
        }

class AdvancedAgent:
    def __init__(self, llm_client):
        self.planner = PlanningAgent(llm_client)
        self.executor = ExecutionEngine()
        self.llm_client = llm_client

    def solve_problem(self, user_goal: str) -> Dict[str, Any]:
        print(f"목표: {user_goal}")
        print("1단계: 계획 수립")
        tasks = self.planner.create_plan(user_goal)
        if not tasks:
            return {"error": "계획 수립에 실패했습니다.", "success": False}
        print(f"생성된 작업: {len(tasks)}개")
        for task in tasks:
            print(f"- {task.description} [{task.action}]")
        print("\n2단계: 작업 실행")
        completed_tasks = 0
        for i, task in enumerate(tasks, 1):
            print(f"작업 {i}/{len(tasks)}: {task.description}")
            tasks[i-1] = self.executor.execute_task(task)
            if task.status == TaskStatus.FAILED:
                print(f"실패: {task.error}")
            else:
                print(f"완료")
                completed_tasks += 1
        success_rate = (completed_tasks / len(tasks)) * 100
        goal_achieved = completed_tasks > 0
        print(f"\n결과 요약")
        print(f"성공률: {success_rate:.1f}%")
        print(f"완료 작업: {completed_tasks}/{len(tasks)}")
        if completed_tasks > 0:
            results_summary = []
            for task in tasks:
                if task.status == TaskStatus.COMPLETED:
                    results_summary.append(f"성공 {task.description}: 완료")
                else:
                    results_summary.append(f"실패 {task.description}: 실패")
            final_result = "\n".join(results_summary)
        else:
            final_result = "모든 작업이 실패했습니다."
        return {
            "goal": user_goal,
            "tasks": tasks,
            "success_rate": success_rate,
            "completed_tasks": completed_tasks,
            "total_tasks": len(tasks),
            "success": goal_achieved,
            "summary": final_result
        }

if __name__ == "__main__":
    if not api_key:
        print("OPENAI_API_KEY가 설정되지 않았습니다.")
        print("환경 변수를 설정하거나 .env 파일을 확인하세요.")
        exit(1)
    try:
        client = OpenAI(api_key=api_key)
        agent = AdvancedAgent(client)
        test_goals = [
            "파이썬 프로그래밍 학습 자료 찾기",
            "회사 매출 데이터 분석 보고서 작성",
            "프로젝트 진행 상황 팀에 공유"
        ]
        for goal in test_goals:
            result = agent.solve_problem(goal)
            print(f"\n최종 결과: {'성공' if result['success'] else '실패'}")
            print("-" * 50)
    except Exception as e:
        print(f"오류 발생: {e}")
        print("API 키나 네트워크 연결을 확인해주세요.")