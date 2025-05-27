# tasks = []
# def add_task(task):
#     tasks.append(task)

# def complete_task(index):
#     tasks.pop(index)

# def show_task():
#     for i, t in enumerate(tasks):
#         print(f"{i}. {t}")

# print([[j for j in range(3)] for i in range(3)])


# numbers = [1, 2, 3, 4, 5]
# numbers[1:4] = [10, 20]
# print(numbers)

# def modify_list(lst):
#     lst.append(4)
#     lst = [7, 8, 9]
#     return lst

# original = [1, 2, 3]
# result = modify_list(original)
# print(original)
# print(result)

# matrix = [[0]*3] *3
# matrix[0][0] = 1
# matrix[1][1] = 2
# print(matrix)

########################################################


# get_max = lambda a,b : a  * b
# print(get_max(10,20))

# def multiplier(n):
#     return lambda x:x*n

# double = multiplier(2)
# print(double(11))

########################################################
# def validate_input(func):
#     def wrapper(x, y):
#         if x < 0 or y < 0:
#             raise ValueError('입력 값이 0보다 커야 한다.')
#         return func(x, y)
#     return wrapper

# @validate_input
# def divide(x, y):
#     return x / y

# try:
#     print(divide(10,-2))
# except ValueError as e:
#     print(e)

# import calculator

# add_result = calculator.add(10, 20)
# print(add_result)

# import sys
# print(sys.path)

##파일 입출력
# import os
# cwd = os.getcwd()
# print(cwd)

# os.mkdir("new_folders")
# os.rmdir("new_folders")

# files = os.listdir('.')
# print(files)

##json 파일 입출력
# import json

# person = {
#     "name" : "홍길동",
#     "age" : 25
# }

# # with open('person.json', 'w', encoding = 'utf-8') as f:
# #     json.dump(person, f, ensure_ascii=False, indent=2)

# with open('person.json', 'r', encoding = 'utf-8') as f:
#     loaded_person = json.load(f)

# print(loaded_person)

########################################################

# from datetime import datetime, date, time, timedelta

# #현재 날짜와 시간
# now = datetime.now()
# print(f"현재: {now}")

# #특정 날짜와 시간
# specific_date = datetime(2023, 12, 31, 23, 59, 59)
# print(f"특정 일시: {specific_date}")

# date_str = now.strftime("%Y-%m-%d %H:%M:%S")
# print(f"형식화된 날짜: {date_str}")

# parsed_date = datetime.strptime("2023-01-15", "%Y-%m-%d")
# print(f"파싱된 날짜: {parsed_date}")
########################################################
# class Car:
#     wheels = 4
#     total_cars = 0

#     def __init__(self, model, year):
#         self.model = model
#         self.year = year
#         Car.total_cars += 1

#     def accel(self, speed):
#         print(f"{speed}만큼 전진")

#     def brake(self, speed):
#         print(f"{speed}만큼 감속")

#     def get_spec(self):
#         print(f"모델 : {self.model}, 연식 : {self.year}")

#     @classmethod
#     def count_cars(cls):
#         print(f"total count : {cls.total_cars}")

#     @staticmethod
#     def get_car_type(model):
#         if model == '지바겐':
#             return "SUV"


# my_car = Car("지바겐",2022)
# my_car.accel(30)
# my_car.get_spec()
# Car.get_car_type("k5")
# your_car = Car("Sonata", 2001)
# Car.count_cars()

# class Benz(car):
#     def __init__(self, model, year, doors):
#         super().__init__(model,year)
#         self.doors = doors

########################################################
# from abc import ABC, abstractmethod

# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass

# class Rectangle(Shape):
#     def __init__(self, w, h):
#         self.w = w
#         self.h = h

#     def area (self):
#         return self.w * self.h

# rec = Rectangle(30,10)

########################################################

# 은행 계좌 관리 프로그램
# class BankAccount:
#     def __init__(self, owner, balance=0):
#         self.owner = owner
#         self.balance = balance
#         self.transaction_history = []
#         self._log_transaction('개설', balance)

#     #입금
#     def deposit(self, amount):
#         self.balance += amount
#         self._log_transaction('입금', amount)
#         print(f"{amount}가 입금되었습니다.")

#     #출금
#     def withdraw(self, amount):
#         self.balance -= amount
#         self._log_transaction('출금', amount)
#         print(f"{amount}가 출금되었습니다.")

    
#     def _log_transaction(self,type, amount):
#         self.transaction_history.append({
#             '타입' : type,
#             '금액' : amount,
#             '잔고' : self.balance
#         })

#     def print_transaction_history(self):
#         for transaction in self.transaction_history:
#             print(f"타입 : {transaction['타입']}, 금액 : {transaction['금액']}, 잔고 : {transaction['잔고']}")

# my_account = BankAccount("홍길동", 3000)
# my_account.deposit(5000)
# my_account.withdraw(2000)
# my_account.print_transaction_history()

########################################################

# file = open('example.txt', 'r')
# content = file.read()
# print(content)
# file.close()

# data = bytes([0x48,0x65,0x6C,0x6C,0x6F])
# with open('binary_data.bin', 'wb') as file:
#     file.write(data)

########################################################
# 이미지 복사
# with open('image.jpg', 'rb') as source:
#     image_data = source.read()

# print(image_data)

# with open('copy.jpg', 'wb') as destination:
#     destination.write(image_data)

########################################################
# 파일 암호화
#XOR 암호화 방식
# def xor_encrypt_decrypt(input_file, output_file, key):

#     with open(input_file, 'rb') as infile:
#         data = infile.read()

#     key_bytes = key.encode() if isinstance(key,str) else bytes([key])
#     key_len = len(key_bytes)

#     encrupted_data = bytearray(len(data))
#     for i in range(len(data)):
#         encrupted_data[i] = data[i] ^ key_bytes[i%key_len]             #암호화된 데이터

#     with open(output_file, 'wb') as outfile:
#         outfile.write(encrupted_data)

# xor_encrypt_decrypt('example.txt', 'secret.enc', 'mykey123')

# xor_encrypt_decrypt('secret.enc', 'decrypted.txt', 'mykey123')

########################################################
# 디렉토리 압축 및 백업
# import zipfile
# from pathlib import Path
# import datetime
# import os

# def backup_directory(source_dir, backup_dir=None, backup_name=None):

#     source_path = Path(source_dir)
#     if backup_dir is None:
#         backup_dir = Path.cwd()
#     else:
#         backup_dir = Path(backup_dir)
#         backup_dir.mkdir(parents=True, exist_ok=True)
    
#     if backup_name is None:
#         timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
#         backup_name = f"{source_path.name}_backup_{timestamp}.zip"
    
#     backup_path = backup_dir / backup_name

#     with zipfile.ZipFile(backup_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
#         for root, _, files in os.walk(source_dir):
#             for file in files:
#                 file_path = os.path.join(root, file)

#                 arc_name = os.path.relpath(file_path, os.path.dirname(source_dir))
#                 zipf.write(file_path, arc_name)
    

# backup_directory()

########################################################

# try:
#     num = int(input('숫자 입력:'))
#     result = 10 / num
#     print(f'결과 : {result}')

# except ValueError:
#     print('유효한 숫자 입력 필요')
# except ZeroDivisionError:
#     print('0으로 나눌 수 없습니다.')
# except:
#     print('예외 발생')

#######################################################

# from functools import partial

# def power(base, exponent, multiplier):
#     return (base ** exponent) * multiplier

# square_and_double = partial(power,2, multiplier=2)

# print(square_and_double(3))

# cube = partial(power, exponent=3)
# print(cube(2, multiplier=1))

#######################################################
# class Event:
#     def __init__(self, event_type, data):
#         self.event_type = event_type
#         self.data = data


# def handle_login(event_data):
#     return f"{event_data} 로그인 되었습니다"    

# def handle_logout(event_data):
#     return f"{event_data} 로그아웃 되었습니다"


# event_handlers = {
#     "LOGIN" : handle_login,
#     "LOGOUT" : handle_logout,
# }

# def process_event(event, handlers) :
#     if event.event_type in handlers:
#         return handlers[event.event_type](event.data)


# events = [
#     Event("LOGIN",{"username":"alice"}),
#     Event("LOGOUT",{"username":"alice"}),
# ]

# list = (map(lambda event:process_event(event, event_handlers), events))

# print(list)
#######################################################
# my_list = [1,2,3]
# iterator = iter(my_list)
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))

#######################################################

# def count_to_up(max):
#     count = 1
#     while count <=max:
#         yield count
#         count += 1

# counter = count_to_up(5)

# print(next(counter))
# print(next(counter))

# for num in count_to_up(5):
#     print(num)

#######################################################

# squre_list = [x**2 for x in range(1000)]
# squre_gen = (x**2 for x in range(10))

# import sys
# print(sys.getsizeof(squre_list))
# print(sys.getsizeof(squre_gen))

# for num in squre_gen:
#     print(num)

#######################################################

# def stateful_generate():
#     print("첫 번째")
#     yield 1

#     print("두 번째")
#     yield 2
#     return "종료"

#     print("세 번째")
#     yield 3

# gen = stateful_generate()

# try :
#     print(next(gen))
#     print(next(gen))
#     print(next(gen))

# except StopIteration :
#     print("종료")

#######################################################
# def nested():
#     yield 'A'
#     yield 'B'

# def main_generator():
#     yield 1
#     yield from nested()
#     yield 2
#     yield 3

# for v in main_generator():
#     print(v)

#######################################################
# import random
# import time
# #시계열 데이터
# def sensor_data_stream():
#     while True:
#         temperature = 20+random.uniform(-5,5)
#         yield f"온도 : {temperature:.2f}도\n시간 : {time.strftime('%H:%M:%S')}"
#         time.sleep(1)

# stream = sensor_data_stream()
# for _ in range(5):
#     print(next(stream))

#######################################################
# 스레드 백그라운드 작업
# import threading
# import time

# def background_task():
#     while True:
#         print("백그라운드 작업 실행 중")
#         time.sleep(1)

# my_thread = threading.Thread(target=background_task, daemon=True)
# my_thread.start()

# print('메인 스레드드 작업 중')
# time.sleep(3)
# print('메인 스레드 종료')

#######################################################
# 스레드드
# import threading
# import time

# event = threading.Event()

# def setter():
#     print('주문 설정 중')
#     time.sleep(3)
#     print('이벤트 설정')
#     event.set()

# def waiter():
#     print('waiter 대기 중')
#     event.wait()
#     print('이벤트 수신 후 처리')

# t1 = threading.Thread(target=waiter)
# t2 = threading.Thread(target=setter)

# t1.start()
# t2.start()

#######################################################
#데이터를 준비하고 대기하는 스레드
# import threading
# import time

# data = None
# condition = threading.Condition()


# def wait_for_data():
#     print('데이터를 대기 중')
#     with condition:
#         condition.wait()
#         print(f'데이터 : {data} 수신')


# def prepare_data():
#     global data
#     print('데이터 준비중')
#     time.sleep(2)
#     with condition:
#         data = '준비된 데이터'
#         print('데이터가 준비되었습니다.')
#         condition.notify()

# t1 = threading.Thread(target=wait_for_data)
# t2 = threading.Thread(target=prepare_data)

# t1.start()
# t2.start()

# t1.join()
# t2.join()

#######################################################

# import threading
# import time

# counter = 0
# counter_lock = threading.Lock()
# def increment(count):
#     global counter
#     for _ in range(count):
#         with counter_lock:
#             current = counter
#             time.sleep(0.001)
#             counter = current + 1
        
        

# t1 = threading.Thread(target=increment, args=(1000,))
# t2 = threading.Thread(target=increment, args=(1000,))

# t1.start()
# t2.start()

# t1.join()
# t2.join()

# print(counter)

#######################################################

#?

# import threading
# import time
# import queue
# import random

# # 작업 큐
# task_queue = queue.Queue()
# # 결과 큐
# result_queue = queue.Queue()

# #작업 생성
# def create_tasks():
#     print('작업 생성')
#     for i in range(10):
#         task = f"작업-{i}"
#         task_queue.put(task)
#         print(f"{task} 작업이 추가 됨")
#         time.sleep(random.uniform(0.1, 0.3))
#     for _ in range(3):
#         task_queue.put(None)
#     print('작업 생성 종료')

# def worker(worker_id):
#     print(f"{worker_id} 작업 시작")

#     while True:
#         task = task_queue.get()

#         if task is None:
#             print(f"워커 {worker_id} 작업 종료")
#             break
#         #작업 처리 중
#         print(f"워커 {worker_id} : {task} 처리중")
#         processing_time = random.uniform(0.5, 1)
#         time.sleep(processing_time)

#         result = print(f"워커 {worker_id}, {task} 처리 완료, 소요 : {processing_time:.2f}초")
#         result_queue.put(worker_id,result)

#         task_queue.task_done()

        
# def result_collector():
#     print('완료 보고 내용 수집')
#     results = []

#     for _ in range(10):
#         worker_id, result = result_queue.get()
#         print(f"수신 : {worker_id} -> {result}")
#         results.append(result)
#         result_queue.task_done()

# creater = threading.Thread(target = create_tasks)
# workers = [threading.Thread(target=worker, args=(i,)) for i in range(3)]
# collector = threading.Thread(target=result_collector)

# creater.start()
# for w in workers:
#     w.start()
# collector.start()

# creater.join()
# for w in workers:
#     w.join()
# collector.join()

#######################################################

# import threading
# import time
# import queue
# import random
# import concurrent.futures

# def task(params):
#     name, duration = params
#     print(f"작업{name} 시작")
#     time.sleep(duration)
#     print(f"작업{name} 완료")
#     return f"{name} 리턴값"
# #작업 목록
# params = [
#     ('A', 2),
#     ('B', 1),
#     ('C', 3)
# ]

# with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
#     results = list(executor.map(task,params))

#     for result in results:
#         print(result)


#######################################################

# import multiprocessing
# import time
# def count_up(name, max_count):
#     for i in range(1,max_count+1):
#         print(f"프로세스{name} : 카운트 : {i}")
#         time.sleep(0.5)

# if __name__== "__main__":
#     p1 = multiprocessing.Process(target=count_up, args=("A",5))
#     p2 = multiprocessing.Process(target=count_up, args=("B",3))

#     p1.start()
#     p2.start()

#     p1.join()
#     p2.join()

#     print('모든 프로세스 종료')
    

#######################################################
# import multiprocessing
# import time
# def add_to_shared(shared_value, lock, increment):
#     for i in range(5):
#         with lock:
#             shared_value.value += increment
#             print(f"프로세스{multiprocessing.current_process().name} 완료")
#             time.sleep(0.5)

# if __name__== "__main__":

#     shared_number = multiprocessing.Value('i',0)
#     lock = multiprocessing.Lock()

#     p1 = multiprocessing.Process(target=add_to_shared, args=(shared_number, lock,1))
#     p2 = multiprocessing.Process(target=add_to_shared, args=(shared_number, lock,2))

#     p1.start()
#     p2.start()

#     p1.join()
#     p2.join()

#     print(f'모든 프로세스 종료, 최종 값: {shared_number.value}')
    
#######################################################
#멀티프로세싱 큐 사용
# import multiprocessing
# import multiprocessing.process
# import multiprocessing.queues
# import time
# import random

# def producer_process(queue):
#     print(f"생산자 프로세스 {multiprocessing.current_process().name}")
#     for i in range(5):
#         item = f"데이터-{i}"
#         queue.put(item)
#         time.sleep(random.uniform(0.1, 1))
#         print(f"{item} 추가")
#     queue.put(None)
#     print("생산자 프로세스 종료")

# def consumer_process(queue):
#     print(f"소비자 프로세스 {multiprocessing.current_process().name}")
#     while True:
#         item = queue.get()
#         if item is None:
#             break
#         print(f"{item} 처리")
#         time.sleep(random.uniform(0.2, 0.8))
#     print("소비자 프로세스 종료")

# if __name__=="__main__":
#     q = multiprocessing.Queue()

#     prod = multiprocessing.Process(target=producer_process, args=(q,))
#     cons = multiprocessing.Process(target=consumer_process, args=(q,))
#     prod.start()
#     cons.start()

#     prod.join()
#     cons.join()

#     print("모든 프로세스 종료")
    
#######################################################
# Numpy 배열 처리
# import numpy as np
# import matplotlib.pyplot as plt
# import matplotlib

# print(np.__version__)


# arr1 = np.array([1,2,3,4,5])
# print(arr1.sum()) #합
# print(arr1.mean()) #평균
# print(arr1.std()) #표준편차
# print(arr1.var()) #분산
# print(arr1.max()) #최대값
# print(arr1.min()) #최소값
# print(arr1.argmax()) #최대값 인덱스
# print(arr1.argmin()) #최소값 인덱스
# print(arr1.cumsum()) #누적합
# print(arr1.cumprod()) #누적곱
# print(arr1[arr1%2==0])

# print(arr1)
# arr2 = np.array([[1,2,3],[4,5,6]])
# print(arr2.ndim) #차원
# print(arr2.shape) #행열
# print(arr2.size) #사이즈
# print(arr2.dtype) #데이터 타입
# print(arr2.itemsize) #바이트 크기
# print(arr2.nbytes) #총 바이트 크기
# print(arr2.T) #전치행렬
# arr1d = np.arange(12) # 0~11
# arr2d = arr1d.reshape(3,4)
# print(arr2d)
# print(arr2d.flatten()) # 평탄화

# zeros = np.zeros((3,4))
# print(zeros)

# range_arr = np.arange(10)
# print(range_arr)

# range_arr = np.arange(0, 10, 2)
# print(range_arr)
# linear_space = np.linspace(0,1,5)
# print(linear_space)

# random_arr = np.random.random((2,2))
# print(random_arr)

# a = np.array([[1,2],[3,4]])
# b = np.array([[5,6],[7,8]])

# print(a.dot(b)) #행렬 곱
# print(a*b) #요소 곱

# arr1 = np.array([1,2,3,4,5])
# print(arr1[0])

# arr2 = np.array([[1,2,3,4],[4,5,6,7]])
# print(arr2[1:,1:3])

# a = np.array([1,2,3,4])
# b = np.array([5,6,7,8])

# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b) 
# print(a)
# print(np.sum(a))
# print(np.sum(a, axis=0))#열 합
# print(np.sum(a, axis=1))#행 합




# celsius = np.array([[1,2,3,4],[5,6,7,8]])
# far = celsius * 9/5 +32
# print(far)

# arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
# reshape = arr.reshape(3,4)
# print(reshape)

# a = np.array([[1,2],[3,4]])
# b = np.array([[5,6],[7,8]])
# vertical = np.concatenate([a,b], axis=0) # 세로로 합치기
# v_stack = np.vstack([a,b]) # 세로로 합치기
# horizontal = np.concatenate([a,b], axis=1) # 가로로 합치기
# h_stack = np.hstack([a,b]) # 가로로 합치기

# print(vertical)
# print(v_stack)
# print(horizontal)
# print(h_stack)

# ages = np.array([23,16,45,61,52,14,92,58])

# adult_filter = ages >= 18 #조건부 필터 True, False
# print(adult_filter)
# adults = ages[adult_filter] #True인 값만 필터링
# print(adults)
# mz = ages[(ages >= 18) & (ages <= 40)] #조건 조합
# print(mz)

# ticket_prices = np.zeros_like(ages)

# ticket_prices[ages<18] = 5
# ticket_prices[(ages>=18) & (ages<=60)] = 10
# ticket_prices[ages>60] = 8
# print(ticket_prices)

# matplotlib.use('TkAgg')

# image = np.array([
#     [0,0,0,0,0],
#     [0,1,1,1,0],
#     [0,1,0,1,0],
#     [0,1,1,1,0],
#     [0,0,0,0,0],
    
# ])

# plt.figure(figsize=(8,4))
# plt.subplot(1,3,1)
# plt.imshow(image, cmap='gray',vmin=0,vmax=1)
# plt.title('Original')

# brightened = image + 0.5
# plt.subplot(1,3,2)
# plt.imshow(brightened, cmap='gray',vmin=0,vmax=1)
# plt.title('Brightened')

# inverted = 1 - image
# plt.subplot(1,3,3)
# plt.imshow(inverted, cmap='gray',vmin=0,vmax=1)
# plt.title('Inverted')

# plt.show()

#######################################################
# pandas 
# import numpy as np
# import pandas as pd

# popul = {
#     'seoul' : 977,
#     'busan' : 122,
#     'incheon' : 242
# }

# pop_series = pd.Series(popul)
# print(pop_series)

# s = pd.Series([1,np.nan,3,np.nan,5], index=['a','b','c','d','e'])
# print(s.values) # 값
# print(s.index) # 인덱스
# print(s.mean()) # 평균
# print(s[['a','c']]) # 인덱스 조회
# print(s[s>2]) # 조건 조회
# print(s.apply(np.sqrt)) # 함수 적용
# print(s * 2) # 연산
# print(s.isna()) # na 확인
# print(s.dropna()) # na 제거
# print(s.fillna(0)) # na 채우기


# df = pd.DataFrame({
#     'Name' : ['john', 'Anna', 'Peter', 'Linda', 'Bob'],
#     'Age' : [28,24,35,32,43],
#     'City' : ['New York', 'Paris', 'Berlin', 'London', 'Tokyo'],
#     'salary' : [50000,65000,75000,85000,60000],
#     'Department' : ['IT', 'HR', 'IT', 'Finance', 'IT'],
#     'year' : [2021,2022,2021,2022,2021]
# })

# print(df)# 데이터프레임 출력
# print(df.shape)# 행열 크기
# print(df.index)# 인덱스
# print(df.columns)# 컬럼
# print(df.dtypes)# 데이터 타입
# print(df.head(2))# 처음 2개
# print(df.tail(2))# 마지막 2개
# print(df.describe())# 요약 통계
# print(df[['Age','salary']])# 컬럼 조회
# print(df.iloc[0:3])# 위치 기반 조회
# print(df[df['Age']>30])# 조건 조회
# df['Age'] = df['Age']+1 # 연산
# df['Country'] = ['USA','France','Germany','UK','Japan'] # 컬럼 추가
# df.loc[5] = ['Charlie',29,'Sydney',70000,'IT','Australia'] # 행 추가
# df.drop('Country', axis=1, inplace=True) # 컬럼 삭제
# df.drop(5, axis=0,inplace=True) # 행 삭제
# print(df)

# print(df.iloc[0:3]) # 0-2행 조회
# print(df.loc[[1,2,3]]) # 인덱스 기반 조회
# print(df.loc[0:1, ['Name','Age']]) # 인덱스 기반 조회
# print(df[(df['Age']>=30) & (df["Department"]=="IT")]) # 조건 조회


# dept_groups = df.groupby('Department')
# df['Dept_Avg_Salary'] = dept_groups['salary'].transform('mean')
# print(df[['Department','salary','Dept_Avg_Salary']])

# high_salary_depts = dept_groups.filter(lambda x:x['salary'].mean()>70000)
# print(high_salary_depts)

# print(dept_groups.get_group('IT'))

# df['Date'] = pd.date_range(start='2022-01-01', periods=len(df),freq='M')
# print(df)

# print(df.groupby(df['Date'].dt.month)['salary'].mean()) # 월별 평균 급여
# print(df.groupby(df['Date'].dt.quarter)['salary'].mean()) # 분기별 평균 급여

# def experience_level(age):
#     if age < 30:
#         return 'Junior'
#     elif age < 40:
#         return 'Mid-level'
#     else:
#         return 'Senior'

# df['Experience'] = df['Age'].apply(experience_level)
# print(df.groupby('Experience')['salary'].mean())

# df = pd.DataFrame({
#     'Name' : ['Alice', 'Bob', 'Charlie', 'David', 'Eva','Frank'],
#     'Score' : [85,90,78,96,88,73],
#     'Attendance' : [95,80,90,75,85,92]
# })

# print('\n점수와 출석률의 상관관계:')
# print(df[['Score','Attendance']].corr())
# print('\n점수와 출석률의 공분산:')
# print(df[['Score','Attendance']].cov())

# customers = pd.DataFrame({
#     'customer_id' : [101,102,103,104,105],
#     'name' : ['Alice','Bob','Charlie','David','Eva'],
#     'email' : ['alice@example.com','bob@example.com','charlie@example.com',
#     'david@example.com','eva@example.com']
# })

# orders = pd.DataFrame({
#     'order_id' : [101,102,103,104,105],
#     'customer_id' : [1,2,1,2,3],
#     'product' : ['Laptop','Smartphone','Tablet','Smartphone','Laptop'],
#     'amount' : [1000,500,300,200,1000]
# })

# inner_join = pd.merge(customers, orders, on='customer_id') # 이너 조인인
# print(inner_join)

# left_join = pd.merge(customers, orders, on='customer_id', how='left') # 왼쪽 조인
# print(left_join)

# right_join = pd.merge(customers, orders, on='customer_id', how='right') # 오른쪽 조인
# print(right_join)

# outer_join = pd.merge(customers, orders, on='customer_id', how='outer') # 외부 조인
# print(outer_join)


# df1 = pd.DataFrame({
#     'A' : ['A0','A1','A2'],
#     'B' : ['B0','B1','B2']
# })

# df2 = pd.DataFrame({
#     'A' : ['A3','A4','A5'],
#     'B' : ['B3','B4','B5']
# })
# result_row = pd.concat([df1,df2])
# print(result_row)

# df3 = pd.DataFrame({
#     'C' : ['C0','C1','C2'],
#     'D' : ['D0','D1','D2']
# })

# result_cols = pd.concat([df1,df3], axis=1)
# print(result_cols)

#######################################################
# 결측치
# import pandas as pd
# import numpy as np


# df = pd.DataFrame({
#     'A' : [1,2,np.nan,4,5],
#     'B' : [np.nan,2,3,4,5],
#     'C' : [1,2,3,np.nan,np.nan]
# })

# # print(df.isna().sum()) # 결측치 확인
# #삭제
# df_dropped = df.dropna()
# print(df_dropped)
# #채우기
# df_filled = df.fillna(0)
# print(df_filled)
# #평균 채우기
# df_mean = df.fillna(df.mean())
# print(df_mean)

#######################################################
# 데이터 타입 변환

# import pandas as pd
# import numpy as np

# df = pd.DataFrame({
#     'A': ['1', '2', '3', '4', '5'],
#     'B': [1.1, 2.2, 3.3, 4.4, 5.5],
#     'C': ['2020-01-01', '2020-02-01', '2020-03-01',
#           '2020-04-01', '2020-05-01'],
#     'D': ['True', 'False', 'True', 'False', 'True']
# })

# df['A'] = df['A'].astype(int) #문자열 타입을 정수형으로 변환
# df['C'] = pd.to_datetime(df['C']) #날짜 타입으로 변환
# # df['D'] = df['D'].astype(bool) #문자열 타입을 불리언형으로 변환 이렇게 하면 값이 무조건 True로 바뀐다.
# # df['D'] = df['D'].map({'True': True, 'False': False}) #map 함수를 사용하여 불리언형으로 변환
# df['D'] = (df['D'] =='True') #조건문을 사용하여 불리언형으로 변환
# print(df.dtypes)
# print(df)


#######################################################
#이상치 처리
# import pandas as pd
# import numpy as np

# normal_data = np.random.normal(50,10,95)
# outliers = [120, 130, -20, -10, 150]
# data_with_outliers = np.concatenate([normal_data,outliers])

# df = pd.DataFrame({
#     'ID' : range(1,101),
#     'Score' : data_with_outliers,
#     'Category' : np.random.choice(['A','B','C'], 100)
# })

# print(df['Score'].describe())

# #IQR
# def detect_outriers_iqr(data):
#     Q1 = data.quantile(0.25)
#     Q3 = data.quantile(0.75)
#     IQR = Q3 - Q1

#     lower_bound = Q1 - 1.5 * IQR # 하한선
#     upper_bound = Q3 + 1.5 * IQR # 상한선

#     outliers = (data<lower_bound) | (data>upper_bound)
#     return outliers, lower_bound, upper_bound

# outliers_mask, lower, upper = detect_outriers_iqr(df['Score'])
# print(f"이상치 경계 : {lower:.2f}, {upper:.2f}")
# print(f"이상치 개수 : {outliers_mask.sum()}")
# print(f"이상치 값들 : {df[outliers_mask]['Score'].values}")

# df_no_outliers = df[~outliers_mask].copy()
# print(f"이상치 제거 전 데이터 크기: {len(df)}")
# print(f"이상치 제거 후 데이터 크기: {len(df_no_outliers)}")
# print(df_no_outliers['Score'].describe()) # 이상치 제거 후 데이터 통계

# df_replaced = df.copy()
# median_score = df['Score'].median()
# print(f"중앙값 : {median_score:.2f}")
# df_replaced.loc[outliers_mask, 'Score'] = median_score
# print(df_replaced['Score'].describe())



# #z-score
# def detect_outliers_zscore(data,threshold=3):
#     z_scores = np.abs((data - data.mean())/data.std()) #z-score 계산 및 절대값
#     outliers = z_scores > threshold
#     return outliers, z_scores

# outliers_zscore, z_scores = detect_outliers_zscore(df['Score'])
# print(f"이상치 개수 : {outliers_zscore.sum()}")
# print(f"이상치 값들 : {df[outliers_zscore]['Score'].values}")

#######################################################
#중복 데이터 제거

# import pandas as pd
# import numpy as np


# data = {
#     'Name': ['Alice', 'Bob', 'Charlie', 'Alice', 'David', 'Bob', 'Eve', 'Charlie'],
#     'Age': [25, 30, 35, 25, 40, 30, 28, 35],
#     'City': ['Seoul', 'Busan', 'Seoul', 'Seoul', 'Daegu', 'Busan', 'Seoul', 'Seoul'],
#     'Salary': [50000, 60000, 70000, 50000, 80000, 65000, 55000, 70000]
# }

# df = pd.DataFrame(data)
# print(len(df))

# #완전 중복 탐지
# duplicate_rows = df.duplicated() #중복 행 탐지
# print('완전 중복 탐지')
# print(duplicate_rows.sum())#중복 행 개수
# print(df[duplicate_rows]) #중복 행 조회

# #완전 중복제거
# df_no_duplicates = df.drop_duplicates()
# print('완전 중복 제거')
# print(df_no_duplicates) #중복 제거 후 데이터 크기

# #특정 열 중복 탐지
# name_duplicates = df.duplicated(subset=['Name'])
# print('이름 중복 탐지')
# print(df[name_duplicates]) #이름 중복 행 조회
# name_age_duplicates = df.duplicated(subset=['Name','Age'])
# print('이름과 나이 중복 탐지')
# print(df[name_age_duplicates]) #이름과 나이 중복 행 조회

#특정 열 중복제거
# print('특정열 중복 제거')
# df_unique_name = df.drop_duplicates(subset=['Name'],keep='last')
# print(df_unique_name)

#######################################################
# 데이터 정규화

# import pandas as pd
# import numpy as np
# from sklearn.preprocessing import StandardScaler, MinMaxScaler, RobustScaler

# np.random.seed(42)
# data = {
#     'Age': np.random.randint(20, 70, 100),
#     'Salary': np.random.normal(50000, 15000, 100),
#     'Experience': np.random.exponential(5, 100),
#     'Score': np.random.uniform(0, 100, 100)
# }

# df = pd.DataFrame(data)
# df['Salary'] = df['Salary'].clip(lower=20000)
# df['Experience'] = df['Experience'].clip(upper=20)
# print(df.describe())

# #표준화

# scaler_standard = StandardScaler()
# df_standardized = pd.DataFrame(
#     scaler_standard.fit_transform(df),
#     columns=df.columns
# )
# print('표준화')
# print(df_standardized.describe())

# # 정규화
# scaler_minmax = MinMaxScaler()
# df_normalized = pd.DataFrame(
#     scaler_minmax.fit_transform(df),
#     columns=df.columns
# )
# print('정규화화')
# print(df_normalized.describe())

# #로버스트 스케일링
# scaler_robust = RobustScaler()
# df_robust_scaled = pd.DataFrame(
#     scaler_robust.fit_transform(df),
#     columns=df.columns
# )
# print('로버스트 스케일링')
# print(df_robust_scaled.describe())

# # 사용자 정의 정규화 함수
# def minmax_normalize(series):
#     return (series - series.min()) / (series.max() - series.min())


#######################################################

# 예제
# import pandas as pd
# import numpy as np

# n_customers = 1000
# customer_data = {
#     'customer_id': range(1, n_customers + 1),
#     'name': [f'Customer_{i}' for i in range(1, n_customers + 1)],
#     'age': np.random.normal(35, 12, n_customers).astype(int),
#     'gender': np.random.choice(['M', 'F', 'Male', 'Female', 'm', 'f', ''], n_customers),
#     'city': np.random.choice(['Seoul', 'Busan', 'Daegu', 'Incheon', 'Gwangju', ''], n_customers),
#     'total_purchase': np.random.exponential(50000, n_customers),
#     'purchase_count': np.random.poisson(5, n_customers),
#     'last_purchase_days': np.random.randint(1, 365, n_customers),
#     'membership_level': np.random.choice(['Bronze', 'Silver', 'Gold', 'Platinum', ''], n_customers)
# }

# df = pd.DataFrame(customer_data)

# print(f'데이터 크기 : {df.shape}')
# print(f'데이터 타입 : {df.dtypes}')
# print(df.head())

# 데이터의 문제 확인
#결측치
#잘못된 예시시
# print('결측치 현황')
# missing_data = df.isnull().sum()
# missing_percentage = (missing_data/len(df))*100
# missing_summary = pd.DataFrame({
#     '결측치 개수' : missing_data,
#     '결측치 비율' : missing_percentage
# })
# print(missing_summary[missing_summary['결측치 개수']>0])

# 올바른 예시
#개별 데이터들의 문제점 확인
# print(f'나이 데이터 타입: {df["age"].dtype}')
# print(f'나이 데이터 범위 : {df["age"].min()}~{df["age"].max()}')
# print(f'비정상 나이 값 범위 : {df[(df["age"]<0) | (df["age"]>100)]["age"].tolist()}')

# print('성별 데이터 일관성 문제')
# print(f"성별의 고유값 : {df['gender'].unique()}")
# print(f"성별 값 개수 : {df['gender'].value_counts()}")


# print("구매 이상치 확인")
# # IQR
# Q1 = df['total_purchase'].quantile(0.25)
# Q3 = df['total_purchase'].quantile(0.75)
# IQR = Q3 - Q1

# outlier_threshold_low = Q1 - 1.5 * IQR
# outlier_threshold_high = Q3 + 1.5 * IQR
# outliers = df[(df['total_purchase'] < outlier_threshold_low) |
#             (df['total_purchase'] > outlier_threshold_high)]

# print(f"이상치 개수 : {len(outliers)}개 ({len(outliers)/len(df)*100:.1f}%)")
# print(f"이상치 범위 : {outlier_threshold_low} 미만 또는 {outlier_threshold_high} 초과")

# # 중복 데이터 확인
# print("중복 데이터 확인")
# duplicates = df.duplicated()
# print(f"완전 중복 행: {duplicates.sum()}개")
# name_duplicates = df.duplicated(subset=['name'])
# print(f"이름 중복 행: {name_duplicates.sum()}개")

# # 원본 데이터 백업

# df_original = df.copy()

# print("나이데이터 정제")
# median_age = df[(df['age']>=0) | (df['age']<=100)]['age'].median()
# df.loc[(df['age']<0) | (df['age']>100), 'age'] = median_age

# print(f"정제 후 나이 범위: {df['age'].min()} ~ {df['age'].max()}")
# print(f"중앙값 : {median_age}")

# print("성별데이터 표준화")
# gender_mapping = {
#     'M' : 'Male', 'm' : 'Male', 'Male' : 'Male',
#     'F' : 'Female', 'f' : 'Female', 'Female' : 'Female',
#     '': 'Unknown'
# }
# df['gender'] = df['gender'].map(gender_mapping).fillna('Unknown')
# print(f"표준화 후 성별 고유값 : {df['gender'].unique()}")
# print(f"표준화 후 성별 값 개수 : {df['gender'].value_counts()}")

# #최빈값으로 대체
# print("도시 빈 값 대체")
# df['city'] = df['city'].replace('', np.nan)
# most_common_city = df['city'].mode()[0]
# df['city'] = df['city'].fillna(most_common_city)
# print(f"도시 빈 값 대체 후 고유값 : {df['city'].unique()}")
# print(f"도시 빈 값 대체 후 값 개수 : {df['city'].value_counts()}")

# print("멤버십 레벨 결측 처리")
# df['membership_level'] = df['membership_level'].replace("", 'Bronze')
# print(f"표준화 후 멤버십 값 개수 : {df['membership_level'].value_counts()}")

# print("구매 이상치 처리")

# df.loc[df['total_purchase'] <outlier_threshold_low,'total_purchase'] = outlier_threshold_low
# df.loc[df['total_purchase'] > outlier_threshold_high,'total_purchase'] = outlier_threshold_high
# print(df['total_purchase'].describe())


# print("범주형 데이터 인코딩")
# print("라벨 인코딩")
# membership_order = {'Bronze':1, 'Silver':2, 'Gold':3, 'Platinum':4}
# df['membership_level_encoded'] = df['membership_level'].map(membership_order)
# print('멤버십 레벨 인코딩')
# print(df[['membership_level','membership_level_encoded']].head())



# print("원 핫 인코딩")
# df_encoded = pd.get_dummies(df, columns=['gender','city'],prefix=['gender','city'])
# print(f"인코딩 후 열 개수 : {len(df_encoded)}")
# print(f"새로 생성 된 열 {[col for col in df_encoded.columns if col not in df.columns]}")
# print(df_encoded.head())

#######################################################
# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt

# plt.plot([1,2,3,4],[1,4,9,16])
# plt.show()

# plt.rc('font', family='Malgun Gothic')
# x = np.linspace(0,10,20)
# plt.figure(figsize=(10,6))
# plt.plot(x,x, color = 'blue', linestyle = '-', linewidth=2, marker='o', markersize=8, label='선형형')
# plt.plot(x,x**2, color = 'red', linestyle = '--', linewidth=1.5, marker='s', markersize=6, label='제곱곱')

# plt.grid(True)
# plt.legend()
# plt.title('선 그래프')
# plt.xlabel('x값')
# plt.ylabel('y값')
# plt.show()

# plt.scatter([1,2,3,4],[1,4,9,16],c='red',alpha=0.5)
# plt.show()

# x = np.random.rand(50)
# y = np.random.rand(50)
# colors = np.random.rand(50)
# sizes =1000* np.random.rand(50) 

# plt.figure(figsize=(10,6))
# plt.scatter(x,y,s=sizes, c=colors, alpha=0.7, cmap = 'viridis', marker='o', edgecolors='black')
# plt.colorbar(label='색상 값')
# plt.title('산점도')
# plt.xlabel('x값')
# plt.ylabel('y값')
# plt.show()


# plt.rc('font', family='Malgun Gothic')

# categories = ['범주 A', '범주 B', '범주 C', '범주 D', '범주 E']
# values = [5, 7, 3, 8, 6]

# plt.figure(figsize=(10, 6))
# plt.bar(
#     categories, values, width=0.6,
#     color=['#5DA5DA', '#FAA43A', '#60BD68', '#F17CB0', '#B2912F'],
#     edgecolor='black', alpha=0.8, align='center'
# )

# plt.grid(True, axis='y')
# plt.title('막대 그래프 예제')
# plt.xlabel('범주')
# plt.ylabel('값')

# # 값 레이블 추가
# for i, v in enumerate(values):
#     plt.text(i, v + 0.1, str(v), ha='center')

# plt.show()

# plt.barh(categories, values, color= 'skyblue',edgecolor='black')
# plt.title('수평 막대')
# plt.xlabel('값')
# plt.ylabel('범주')
# plt.grid(True, axis='x')
# plt.show()

# plt.hist(np.random.normal(0,1,1000), bins=30)
# plt.rc('axes',unicode_minus=False) # 마이너스 표시 설정
# plt.show()
# data1 = np.random.normal(0,1,1000)
# data2 = np.random.normal(2,1.5,1000)



# plt.hist(data1, bins=30,cumulative=True, alpha=0.7,color= 'blue', label='데이터셋1',
#         density=True, histtype='step',edgecolor='black')
# # plt.hist(data2, bins=30, alpha=0.7,color= 'red', label='데이터셋2',
# #         density=True, histtype='stepfilled',edgecolor='black')
# plt.grid(True,alpha=0.3)
# plt.xlabel('값')
# plt.ylabel('누적 밀도도')
# plt.legend()
# # plt.axvline(np.mean(data1),color='blue',linestyle='dashed',linewidth=1)
# # plt.axvline(np.mean(data2),color='red',linestyle='dashed',linewidth=1)
# plt.show()


# labels = ['제품 A', '제품 B', '제품 C', '제품 D', '기타']
# sizes = [35, 25, 20, 15, 5]
# explode = [0.1, 0, 0, 0, 0]
# colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0']
# plt.figure(figsize=(10,8))
# plt.pie(sizes, explode=explode, labels=labels, colors=colors, 
#         autopct='%1.1f%%', shadow=True, startangle=90,
#         wedgeprops={'edgecolor':'black','linewidth':1})

# center_circle = plt.Circle((0,0),0.70, fc='white', edgecolor='black')
# fig = plt.gcf()
# fig.gca().add_artist(center_circle)
# plt.axis('equal')
# plt.legend(loc='upper left')
# plt.show()

#