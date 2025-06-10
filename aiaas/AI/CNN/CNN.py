import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras import layers, models



# 모델 선언 = CNN 아키텍쳐
def create_cnn():
    model = models.Sequential([
        # Block 1
        # 기본 저수준 특징 추출(엣지 등등)
        layers.Conv2D(32, (3, 3), padding='same', activation='relu', input_shape=(32, 32, 3)),
        # 32개의 필터 사용
        # 3x3 커널 사용
        # 패딩 사용
        # 활성화 ReLU 사용 : 0 이하의 값은 0으로 처리
        # 입력 형태 지정 : 32x32x3 (높이, 너비, 채널)
        layers.BatchNormalization(),
        # 배치 정규화 : 각 배치의 평균과 표준편차를 정규화
        layers.Conv2D(32, (3, 3), padding='same', activation='relu'),
        # 32개의 필터 사용
        # 3x3 커널 사용
        # 패딩 same : 입력 크기와 출력 크기가 같도록 패딩 추가  
        # 활성화 ReLU 사용 : 0 이하의 값은 0으로 처리
        layers.MaxPooling2D((2, 2)),
        # 2x2 풀링 윈도우 사용
        # 2칸씩 이동하면서 최대값 선택
        layers.Dropout(0.25),
        # 드롭아웃 : 25%의 뉴런을 랜덤하게 0으로 만듦
        # 과적합 방지

        # Block 2
        # 고수준 특징 추출(모양, 패턴 등등)
        layers.Conv2D(64, (3, 3), padding='same', activation='relu'),
        # 64개의 필터 사용
        # 3x3 커널 사용
        # 패딩 same : 입력 크기와 출력 크기가 같도록 패딩 추가  
        # 활성화 ReLU 사용 : 0 이하의 값은 0으로 처리
        # 필터를 늘림으로써, 
        # 풀링을 통해 공간정보가 줄었는데, 정보 표현력을 유지
        # 더 많은 필터를 사용하여 더 복잡하고 다양한 패턴을 학습
        layers.BatchNormalization(),
        layers.Conv2D(64, (3, 3), padding='same', activation='relu'),
        layers.MaxPooling2D((2, 2)),
        layers.Dropout(0.25),

        # Block 3 (추가)
        # 더 복잡한 특징 추출(모양, 패턴 등등)
        layers.Conv2D(128, (3, 3), padding='same', activation='relu'),
        layers.BatchNormalization(),
        layers.Conv2D(128, (3, 3), padding='same', activation='relu'),
        layers.MaxPooling2D((2, 2)),
        layers.Dropout(0.4),

        # Global Average Pooling 대신 Flatten도 가능
        layers.GlobalAveragePooling2D(),
        # 전역 평균 풀링 : 풀링 영역의 평균값을 출력
        # 특징맵의 "각 채널"마다 평균값 1개만 뽑는 전역 풀링 기법

        # 예를 들어 입력이 (8, 8, 128)이라면 → 출력은 (128,)
        # → 공간 정보(8×8)는 사라지고, 채널별 요약 정보만 남음?  
        # Flatten()보다 파라미터 수가 훨씬 적음
        # 오버피팅 방지, 간결함, 구조 단순화        
        layers.Dense(256, activation='relu'),
        # 뉴런 256개 → 모델이 고차원 특징을 학습할 수 있게 함
        # 활성화 ReLU 사용 : 0 이하의 값은 0으로 처리
        layers.BatchNormalization(),
        layers.Dropout(0.5),
        layers.Dense(10, activation='softmax')
        # 10개의 뉴런 사용
        # 소프트맥스 활성화 함수 사용 : 출력값이 0~1 사이의 확률로 변환
    ])
    
    return model

(x_train, y_train), (x_test, y_test) = tf.keras.datasets.cifar10.load_data()

x_train = x_train / 255.0
x_test = x_test / 255.0
print(x_train)
print(y_train)

model = create_cnn()
model.summary()
# 모델 컴파일 = 손실함수, 평가 지표, 최적화 알고리즘
model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

# 모델 학습
model.fit(x_train, y_train, epochs=20, batch_size=64, validation_split=0.2)

# 모델 평가
test_loss, test_acc = model.evaluate(x_test, y_test, verbose=2)
print(f'정확도 : {test_acc:.2%}')

# 모델을 활용해서 예측 / 정답 데이터하고 비교

# import numpy as np
# import matplotlib.pyplot as plt

# # 테스트 데이터에서 랜덤하게 이미지 선택
test_images = x_test[np.random.choice(x_test.shape[0], size=5, replace=False)]  

# # 예측 결과 출력
predictions = model.predict(test_images)
predicted_labels = np.argmax(predictions, axis=1)

# 시각화        
plt.figure(figsize=(12, 4))

for i in range(5):
    plt.subplot(1, 5, i+1)
    plt.imshow(test_images[i])
    plt.title(f"True: {y_test[i]}, Pred: {predicted_labels[i]}")
    plt.axis('off') 

plt.tight_layout()
plt.show()