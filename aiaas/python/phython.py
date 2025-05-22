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

