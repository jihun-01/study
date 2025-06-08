from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
import numpy as np
import matplotlib.pyplot as plt

def sigmoid(z):
    return 1.0 / (1.0 + np.exp(-z))

def sigmoid_derivative(z):
    return sigmoid(z) * (1 - sigmoid(z))

def mini_mnist():
    """
    8x8 숫자 이미지 분류 (sklearn digits 데이터셋 사용)
    """
    
    # 데이터 로드
    digits = load_digits()
    X, y = digits.data, digits.target
    X = X / 16.0  # 정규화 (0-16 → 0-1)
    
    # 원-핫 인코딩
    y_onehot = np.eye(10)[y]
    
    # 훈련/테스트 분할
    X_train, X_test, y_train, y_test = train_test_split(
        X, y_onehot, test_size=0.2, random_state=42
    )
    
    print("미니 MNIST 과제")
    print(f"훈련 데이터: {X_train.shape}")
    print(f"테스트 데이터: {X_test.shape}")
    print(f"클래스 수: 10개 (0-9 숫자)")
    
    class DigitClassifier:
        def __init__(self, input_size=64, hidden_size=100, output_size=10):
            self.W1 = np.random.randn(input_size, hidden_size) * 0.5
            self.b1 = np.zeros((1, hidden_size))
            self.W2 = np.random.randn(hidden_size, output_size) * 0.5
            self.b2 = np.zeros((1, output_size))
        
        def softmax(self, z):
            exp_z = np.exp(z - np.max(z, axis=1, keepdims=True))
            return exp_z / np.sum(exp_z, axis=1, keepdims=True)
        
        def cross_entropy_loss(self, y_pred, y_true):
            return -np.mean(np.sum(y_true * np.log(y_pred + 1e-15), axis=1))
        
        def forward(self, X):
            self.z1 = np.dot(X, self.W1) + self.b1
            self.a1 = sigmoid(self.z1)
            self.z2 = np.dot(self.a1, self.W2) + self.b2
            self.a2 = self.softmax(self.z2)
            return self.a2
        
        def backward(self, X, y, learning_rate):
            m = X.shape[0]
            
            self.forward(X)
            
            dz2 = (self.a2 - y)
            dw2 = (1/m) * np.dot(self.a1.T, dz2)
            db2 = (1/m) * np.sum(dz2, axis=0, keepdims=True)
            
            dz1 = np.dot(dz2, self.W2.T) * sigmoid_derivative(self.z1)
            dw1 = (1/m) * np.dot(X.T, dz1)
            db1 = (1/m) * np.sum(dz1, axis=0, keepdims=True)

            self.W1 -= learning_rate * dw1
            self.b1 -= learning_rate * db1
            self.W2 -= learning_rate * dw2
            self.b2 -= learning_rate * db2
        
        def predict(self, X):
            return np.argmax(self.forward(X), axis=1)
        
        def accuracy(self, X, y):
            return np.mean(self.predict(X) == np.argmax(y, axis=1))
    
    model = DigitClassifier()
    
    print("\n학습 시작...")
    for epoch in range(1000):
        model.backward(X_train, y_train, 0.1)
        if epoch % 100 == 0:
            train_acc = model.accuracy(X_train, y_train)
            test_acc = model.accuracy(X_test, y_test)
            print(f"에포크 {epoch}: 훈련 정확도 {train_acc:.3f}, 테스트 정확도 {test_acc:.3f}")

    final_test_acc = model.accuracy(X_test, y_test)
    print(f"\n최종 테스트 정확도: {final_test_acc:.3f}")

    print("\n=== 숫자별 예측 성능 ===")
    y_pred = model.predict(X_test)
    y_true = np.argmax(y_test, axis=1)
    
    for digit in range(10):
        digit_indices = np.where(y_true == digit)[0]
        if len(digit_indices) > 0:
            digit_accuracy = np.mean(y_pred[digit_indices] == digit)
            digit_count = len(digit_indices)
            correct_count = np.sum(y_pred[digit_indices] == digit)
            print(f"숫자 {digit}: {correct_count}/{digit_count} = {digit_accuracy:.3f}")

mini_mnist()
