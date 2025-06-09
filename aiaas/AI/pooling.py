import numpy as np


# 입력 데이터
input_data = np.array([
    [1, 3, 2, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
])


def max_pooling_2d(input_array, pool_size=(2, 2), stride=2):
    """
    2D 최대 풀링 구현
    
    Args:
        input_array: 입력 배열 (H, W)
        pool_size: 풀링 윈도우 크기
        stride: 스트라이드
    
    Returns:
        풀링된 배열
    """
    h, w = input_array.shape
    pool_h, pool_w = pool_size
    
    # 출력 크기 계산 (패딩 없다고 가정)
    out_h = (h - pool_h) // stride + 1
    out_w = (w - pool_w) // stride + 1
    
    # 출력 배열 초기화
    output = np.zeros((out_h, out_w))
    
    # 풀링 연산 수행
    for i in range(out_h):
        for j in range(out_w):
            # 현재 윈도우 영역
            h_start = i * stride
            h_end = h_start + pool_h
            w_start = j * stride
            w_end = w_start + pool_w
            
            # 2x2 풀링 윈도우 영역
            # 2차원 이동하면서 최대값 선택
            # 4x4 이미지에 2x2 풀링 적용 시
            # 첫번째 윈도우 : 0~1행, 0~1열
            # 두번째 윈도우 : 0~1행, 2~3열  
            # 세번째 윈도우 : 2~3행, 0~1열
            # 네번째 윈도우 : 2~3행, 2~3열
            # 최대값 선택
            window = input_array[h_start:h_end, w_start:w_end]
            output[i, j] = np.max(window)
    
    return output

def average_pooling_2d(input_array, pool_size=(2, 2), stride=2):
    """
    2D 평균 풀링 구현
    
    Args:
        input_array: 입력 배열 (H, W)
        pool_size: 풀링 윈도우 크기
        stride: 스트라이드
    
    Returns:
        풀링된 배열
    """
    h, w = input_array.shape
    pool_h, pool_w = pool_size
    
    # 출력 크기 계산
    out_h = (h - pool_h) // stride + 1
    out_w = (w - pool_w) // stride + 1
    
    # 출력 배열 초기화
    output = np.zeros((out_h, out_w))
    
    # 풀링 연산 수행
    for i in range(out_h):
        for j in range(out_w):
            # 현재 윈도우 영역
            h_start = i * stride
            h_end = h_start + pool_h
            w_start = j * stride
            w_end = w_start + pool_w
            
            # 평균값 계산
            window = input_array[h_start:h_end, w_start:w_end]
            output[i, j] = np.mean(window)
    
    return output
print("원본 입력:")
print(input_data)
print()

# 최대 풀링 적용
max_pooled = max_pooling_2d(input_data)
print("최대 풀링 결과:")
print(max_pooled)
print()

# 평균 풀링 적용
avg_pooled = average_pooling_2d(input_data)
print("평균 풀링 결과:")
print(avg_pooled)
