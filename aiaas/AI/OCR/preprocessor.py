import cv2
import numpy as np
import matplotlib.pyplot as plt




class OCRPreprocessor:

    def __init__(self):
        pass

    def convert_to_grayscale(self, image):

        if len(image.shape) == 3:
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        else:
            gray = image.copy()

        return gray

    def apply_threshold(self, image, method='adaptive'):

        gray = self.convert_to_grayscale(image)

        if method == 'simple':
            _, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

        elif method == 'adaptive':
            # 적용적 임계값: 각 픽셀 주변 영역의 가중 평균을 기준으로 임계값 결정
            # 11x11 영역의 가우시안 가중 평균에서 2를 뺀 값을 임계값으로 사용
            thresh = cv2.adaptiveThreshold(
                gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                cv2.THRESH_BINARY, 11, 2
            )
            # adaptiveThreshold 매개변수 : 그레이스케일 이미지, 최대값, 임계값 방법, 이진화 방법, 영역 크기, 상수 값
            # gray : 그레이스케일 이미지
            # 255 : 최대값
            # cv2.ADAPTIVE_THRESH_GAUSSIAN_C : 가우시안 가중 평균 임계값
            # cv2.THRESH_BINARY : 이진화 방법
            # 11 : 영역 크기
            # 2 : 상수 값
            # thresh : 이진화된 이미지

        elif method == 'otsu':
            # Otsu 방법: 히스토그램 분석으로 최적의 임계값 자동 선택
            # 히스토그램 분석 : 이미지의 픽셀 값 분포를 분석하여 최적의 임계값을 찾는 방법
            _, thresh = cv2.threshold(
                gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU
            )
            # threshold 매개변수 : 그레이스케일 이미지, 임계값, 최대값, 이진화 방법
            # cv2.THRESH_BINARY + cv2.THRESH_OTSU : 이진화 방법
            # _ : 임계값 반환
            # thresh : 이진화된 이미지 반환

        return thresh

    def remove_noise(self, image):
        """
        이진화된 이미지에서 노이즈를 제거
        """
        # 1x1 구조 요소 생성 (모폴로지 연산용)
        # 모폴로지 연산 : 이미지의 픽셀 값을 변경하는 연산
        kernel = np.ones((1, 1), np.uint8)

        # 열림 연산 적용: 작은 노이즈 점들을 제거
        # 먼저 침식으로 작은 객체를 제거하고, 팽창으로 원래 크기 복원
        # 침식 : 이미지의 픽셀 값이 0인 경우 주변 픽셀 값을 0으로 변경
        # 팽창 : 이미지의 픽셀 값이 0이 아닌 경우 주변 픽셀 값을 0이 아닌 값으로 변경
        opening = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)

        # 가우시안 블러 적용: 1x1 커널로 미세한 노이즈 제거
        # sigma=0으로 설정하면 커널 크기에서 자동으로 sigma 계산
        # sigma : 가우시안 분포의 표준 편차
        denoised = cv2.GaussianBlur(opening, (1, 1), 0)

        return denoised


    def correct_skew(self, image):
        """
        이미지의 기울기를 자동으로 보정
        """
        # Canny 에지 검출: 50-150 임계값으로 윤곽선 추출
        edges = cv2.Canny(image, 50, 150, apertureSize=3)
        # Canny 매개변수 - 그레이스케일 이미지, 최소 임계값, 최대 임계값, 커널 크기
        # 50 : 최소 임계값
        # 150 : 최대 임계값
        # apertureSize=3 : 커널 크기
        # edges : 에지 이미지

        # 허프 변환으로 직선 검출
        lines = cv2.HoughLines(edges, 1, np.pi/180, threshold=100)
        # HoughLines 매개변수 : 에지 이미지, 거리 해상도, 각도 해상도, 최소 투표 수
        # 1 : 거리 해상도 (1픽셀 단위로 거리를 측정)
        # np.pi/180 : 각도 해상도 1도 (파이/180도, 즉 1도 단위로 각도를 측정)
        # threshold=100 : 최소 투표 수 (최소 100개의 점이 있어야 직선으로 인식)
        # lines : 직선 검출 결과

        if lines is not None:
            # 검출된 직선들의 기울기 각도 계산
            angles = []
            for rho, theta in lines[:, 0]:
                # 허프 변환에서 theta의 의미:
                # theta = 0도 (0 radian) -> 수직선 (|)
                # theta = 90도 (π/2 radian) -> 수평선 (-)
                # theta = 180도 (π radian) -> 다시 수직선
                # 이미지 회전에서 각도의 의미:
                # 0도 -> 수평선 기준 (-)
                # 90도 -> 수직선 기준 (|)
                # 양수 -> 시계방향 회전
                # 음수 -> 반시계방향 회전
                # 즉, 허프 변환은 수직선을 0도로 보지만, 이미지 회전은 수평선을 0도로 보기 때문에 -90도 보정
                angle = np.degrees(theta) - 90
                angles.append(angle)

            # 중앙값으로 기울기 보정 (이상값에 강건함)
            # 이상 각도가 있을 수 경우, 평균 값이 왜곡될 수 있기 때문에 중앙값을 사용
            median_angle = np.median(angles)

            # 이미지 중심점을 기준으로 회전 변환 행렬 생성
            (h, w) = image.shape[:2]
            center = (w // 2, h // 2)
            M = cv2.getRotationMatrix2D(center, median_angle, 1.0)

            # INTER_CUBIC: 고품질 보간, BORDER_REPLICATE: 가장자리 복제
            rotated = cv2.warpAffine(
                image, M, (w, h),
                flags=cv2.INTER_CUBIC,
                borderMode=cv2.BORDER_REPLICATE
            )
            # warpAffine 매개변수 : 이미지, 회전 행렬, 출력 이미지 크기, 보간법, 테두리 처리
            # image : 입력 이미지
            # M : 회전 행렬 (getRotationMatrix2D로 생성)
            # (w, h) : 출력 이미지 크기
            # flags=cv2.INTER_CUBIC : 보간법 (회전 시 새로운 좌표의 픽셀 값 계산 방법)
            # INTER_CUBIC : 3차 보간법 (주변 4x4=16개 픽셀의 3차 함수로 고품질 계산)
            # borderMode=cv2.BORDER_REPLICATE : 테두리 처리 (이미지 경계 밝은 가장자리 픽셀로 채움)
            # rotated : 회전된 이미지

            return rotated

        # 직선을 검출하지 못한 경우 원본 반환
        return image
    

    def resize_image(self, image, target_height=800):
        """
        OCR 최적화를 위한 이미지 크기 조정
        OCR은 일정 크기 이상에서 성능이 좋아짐
        INTER_CUBIC 보간법으로 고품질 확대
        """
        # 현재 이미지의 높이와 너비 획득
        h, w = image.shape[:2]

        if h < target_height:
            # 이미지가 너무 작은 경우 크기 증가
            # 높이 기준으로 스케일 비율 계산
            scale = target_height / h
            new_w = int(w * scale)

            # INTER_CUBIC 보간법으로 고품질 리사이징
            resized = cv2.resize(image, (new_w, target_height),
                                interpolation=cv2.INTER_CUBIC)
        else:
            # 이미지가 충분히 큰 경우 원본 유지
            resized = image

        return resized

    def visualize_preprocessing_steps(self, steps, step_names):
        """
        전처리 과정을 단계별로 시각화
        """
        # 2행 3열 서브플롯 생성 (15x10 인치 크기)
        plt.rc('font', family='Malgun Gothic')
        fig, axes = plt.subplots(2, 3, figsize=(15, 10))
        axes = axes.ravel()  # 2차원 배열을 1차원으로 변환

        # 각 처리 단계별로 이미지 출력
        for i, (step, name) in enumerate(zip(steps, step_names)):
            if i < len(axes):  # 서브플롯 개수 초과 방지
                if len(step.shape) == 3:
                    # 컬러 이미지: BGR을 RGB로 변환하여 출력
                    axes[i].imshow(cv2.cvtColor(step, cv2.COLOR_BGR2RGB))
                else:
                    # 그레이스케일 이미지: gray 컬러맵 사용
                    axes[i].imshow(step, cmap='gray')

                # 각 서브플롯에 제목 설정 및 축 숨김
                axes[i].set_title(name)
                axes[i].axis('off')

        # 레이아웃 자동 조정 및 출력
        plt.tight_layout()
        plt.show()

    def preprocess_pipeline(self, image, visualize=False):
        """
        전체 이미지 전처리 파이프라인 실행
        """
        # 각 처리 단계별 결과 저장용 리스트
        steps = []
        step_names = []

        # 0. 원본 이미지 보존
        steps.append(image.copy())
        step_names.append('원본 이미지')

        # 1. 그레이스케일 변환
        gray = self.convert_to_grayscale(image)
        steps.append(gray)
        step_names.append('그레이스케일')

        # 2. OCR 최적화를 위한 크기 조정
        resized = self.resize_image(gray)
        steps.append(resized)
        step_names.append('크기 조정')

        # 3. 적용적 이진화 처리 (지역적 밝기 변화에 강건)
        thresh = self.apply_threshold(resized, method='adaptive')
        steps.append(thresh)
        step_names.append('이진화')

        # 4. 모폴로지 연산으로 노이즈 제거
        denoised = self.remove_noise(thresh)
        steps.append(denoised)
        step_names.append('노이즈 제거')

        # 5. 허프 변환 기반 기울기 자동 보정
        corrected = self.correct_skew(denoised)
        steps.append(corrected)
        step_names.append('기울기 보정')

        # 시각화 옵션이 활성화된 경우 처리 과정 출력
        if visualize:
            self.visualize_preprocessing_steps(steps, step_names)

        return corrected

def create_noisy_sample_image():
    """
    테스트용 노이즈가 있는 샘플 이미지 생성
    """
    # 300x800 크기의 흰색 배경 이미지 생성 (RGB)
    image = np.ones((300, 800, 3), dtype=np.uint8) * 255

    # 다양한 크기와 위치에 텍스트 추가
    font = cv2.FONT_HERSHEY_SIMPLEX

    # 제목 텍스트 (크기 1.5, 굵기 2)
    cv2.putText(image, 'Noisy OCR Test Image', (50, 100), font, 1.5, (0, 0, 0), 2)
    # 부제목 텍스트 (크기 1.0, 굵기 2)
    cv2.putText(image, 'Preprocessing improves accuracy', (50, 150), font, 1, (0, 0, 0), 2)
    # 내용 텍스트 (크기 1.0, 굵기 2)
    cv2.putText(image, 'Machine Learning & AI', (50, 200), font, 1, (0, 0, 0), 2)

    # 0-50 범위의 랜덤 노이즈 생성 및 추가
    noise = np.random.randint(0, 50, image.shape, dtype=np.uint8)
    noisy_image = cv2.add(image, noise)

    # 문서 스캔 상황을 모방한 5도 기울기 적용
    h, w = noisy_image.shape[:2]
    center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, 5, 1.0)
    skewed_image = cv2.warpAffine(noisy_image, M, (w, h))

    return skewed_image

def preprocessing_example():
    """
    OCR 전처리 예제 실행 함수
    """
    # OCR 전처리기 인스턴스 생성
    preprocessor = OCRPreprocessor()

    # 노이즈와 기울기가 있는 샘플 이미지 생성
    image = create_noisy_sample_image()

    # 전체 전처리 파이프라인 실행 (시각화 포함)
    processed_image = preprocessor.preprocess_pipeline(image, visualize=True)

    # OCR 라이브러리가 있는 경우 전후 비교
    try:
        import pytesseract

        # 전처리 전 OCR 결과
        original_text = pytesseract.image_to_string(image)
        # 전처리 후 OCR 결과
        processed_text = pytesseract.image_to_string(processed_image)

        print("전처리 전 OCR 결과:")
        print(repr(original_text))
        print("\n전처리 후 OCR 결과:")
        print(repr(processed_text))

    except ImportError:
        print("pytesseract가 설치되지 않아 OCR 비교를 건너뜁니다.")
        print("설치: pip install pytesseract")

    return processed_image

preprocessing_example()