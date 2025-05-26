## 과제 : 리스트 학생 관리

# 기본값
# name = ["홍길동", "이순신", "강감찬"]
# score = [95, 87, 78]
# # 학생 추가
# def students_add():
#     name.append(input("이름을 입력하세요 :"))
#     score.append(int(input("점수를 입력하세요 :")))

# students_add()
# print(f"이름 : {name}, 점수 : {score}")

# # 학생 삭제
# def student_delete():
#     delete = name.index(input("삭제할 이름을 입력하세요 :"))
#     name.pop(delete)
#     score.pop(delete)

# student_delete()
# print(f"이름 : {name}, 점수 : {score}")

# # 학생 성적 수정

# def student_modify():
#     modify = name.index(input("수정할 이름을 입력하세요 :"))
#     score[modify] = int(input("수정할 점수를 입력하세요 :"))

# student_modify()
# print(f"이름 : {name}, 점수 : {score}")

# # 전체 목록 출력
# def student_list():
#     for i in range(len(name)):
#         print(f"이름 : {name[i]}, 점수 : {score[i]}")

# student_list()

# #통계 출력
# def student_statistics():

#     print(f"최고점 : {max(score)}")
#     print(f"최저점 : {min(score)}")
#     print(f"평균 : {sum(score) / len(score)}")

# student_statistics()

########################################################

# 과제 : 튜플 판매 데이터 분석
# 기본 데이터
# (연도, 분기, 제품, 가격, 판매량, 지역)
# sales_data = [
#     (2020, 1, "노트북", 1200, 100, "서울"),
#     (2020, 1, "스마트폰", 800, 200, "부산"),
#     (2020, 2, "노트북", 1200, 150, "서울"),
#     (2020, 2, "스마트폰", 1000, 250, "대구"),
#     (2020, 3, "노트북", 1300, 100, "인천"),
#     (2020, 3, "스마트폰", 850, 300, "서울"),
#     (2020, 4, "노트북", 1300, 130, "부산"),
#     (2020, 4, "스마트폰", 850, 350, "서울"),
#     (2021, 1, "노트북", 1400, 110, "대구"),
#     (2021, 1, "스마트폰", 900, 220, "서울"),
#     (2021, 2, "노트북", 1350, 150, "인천"),
#     (2021, 2, "스마트폰", 900, 270, "부산"),
#     (2021, 3, "노트북", 1500, 130, "서울"),
#     (2021, 3, "스마트폰", 950, 300, "대구"),
#     (2021, 4, "노트북", 1500, 140, "부산"),
#     (2021, 4, "스마트폰", 950, 370, "서울")
# ]

# # 연도별 판매량
# def sales_analysis():
#     years = sorted({index[0] for index in sales_data})
#     sum_sales = 0
#     print("\n연도별 판매량")
#     for i in years:
#         for j in sales_data:
#             if i == j[0]:
#                 sum_sales += j[4]
#         print(f"{i}년도 총 판매량 : {sum_sales}")
#         sum_sales = 0

# sales_analysis()

# # 제품별 평균 가격
# def product_analysis():
#     products = sorted({index[2] for index in sales_data})
#     sum_price = 0
#     print("\n제품별 평균 가격")
#     for i in products:
#         for j in sales_data:
#             if i == j[2]:
#                 sum_price += j[3]
#         print(f"{i}년도 총 판매량 : {sum_price // len(sales_data)}")
#         sum_price = 0

# product_analysis()


# # 최대 판매 지역
# def max_sales_region():
#     regions = sorted({index[5] for index in sales_data})
#     sum_sales = 0
#     max_sales = 0
#     max_region = ""
#     print("\n최대 판매 지역")
#     for i in regions:
#         for j in sales_data:
#             if i == j[5]:
#                 sum_sales += j[4]
#         if sum_sales > max_sales:
#             max_sales = sum_sales
#             max_region = i
#         sum_sales = 0

#     print(f"최대 판매 지역 : {max_region}, 판매량 : {max_sales}")

# max_sales_region()

# #분기별 매출
# def quarter_sales():
#     years = sorted({index[0] for index in sales_data})
#     quarters = sorted({index[1] for index in sales_data})
    
#     print("\n분기별 매출")
#     for i in years:
#         for j in quarters:
#             sum_sales = 0  
#             for k in sales_data:
#                 if i == k[0] and j == k[1]: 
#                     sum_sales += k[3]
#             print(f"{i}년도 {j}분기 총 매출 : {sum_sales}")
        
# quarter_sales()
########################################################

#과제 : 딕셔너리 

# users = {
#     "홍길동" : {
#         "phone" : [
#             "010-1234-5678",
#             "010-9876-5432"
#         ],
#         "email" : "test@test.com",
#         "address" : "서울시 강남구"
#     },
#     "예제1" : {
#         "phone" : [
#             "010-1234-5678",
#             "010-9876-5432"
#         ],
#         "email" : "test@test.com",
#         "address" : "서울시 강남구"
#     },
#     "예제2" : {
#         "phone" : [
#             "010-1234-5678",
#             "010-9876-5432"
#         ],
#         "email" : "test@test.com",
#         "address" : "서울시 강남구"
#     }
# }
# #연락처 추가
# def add_list():
#     name = input("이름을 입력하세요 :")
#     phone = input("전화번호를 입력하세요 :")
#     email = input("이메일을 입력하세요 :")
#     address = input("주소를 입력하세요 :")
#     users[name] = {
#         "phone" : list(phone.split(",")),
#         "email" : email,
#         "address" : address
#     }

# add_list()

# def delete_list():
#     name = input("삭제할 이름을 입력하세요 :")
#     if name in users:
#         del users[name]
#     else:
#         print("존재하지 않는 이름입니다.")

# delete_list()

# def search_list():
#     name = input("검색할 이름을 입력하세요 :")
#     if name in users:
#         print(f"\n{name}")
#         for values in users[name]:
#             print(values, users[name][values])
#     else:
#         print("존재하지 않는 이름입니다.")


# search_list()

# #모든 연락처 보기
# def show_list():
#     print("====전체 연락처 목록====")
#     for key in users:
#         print(f"\n{key}")
#         for values in users[key]:
#             print(values, users[key][values])

# show_list()

########################################################

#과제 : 집합
# 소셜 네트워크에서 사용자 간의 관계와 추천 시스템을
# 구현하는 프로그램을 작성
# 공통 관심사를 갖는 친구 응답
# 공통 관심사가 없는 친구 응답

# hobbies = {
#     "Alice": ["음악", "영화", "독서"],
#     "Bob": ["스포츠", "여행", "음악"],
#     "Charlie": ["프로그래밍", "게임", "영화"],
#     "David": ["요리", "여행", "사진"],
#     "Eve": ["프로그래밍", "독서", "음악"],
#     "Frank": ["스포츠", "게임", "요리"],
#     "Grace": ["영화", "여행", "독서"]
# }

# key_list = list(hobbies)
# @time_decorator
# def get_common_hobbies(key_list):
    
#     for other , interests in hobbies.items():
#         if other == key_list[0]:
#             continue
#         common_hobbies = set(interests) & set(hobbies[key_list[0]])
#         if common_hobbies:
#             print(f"{key_list[0]}와 {other}의 공통 취미 : {common_hobbies}")
# @time_decorator
# def get_no_common_hobbies(key_list):
    
#     for other , interests in hobbies.items():
#         if other == key_list[0]:
#             continue
#         no_common_hobbies = not(set(interests) & set(hobbies[key_list[0]]))
#         if no_common_hobbies:
#             print(f"{key_list[0]}와 {other}의 공통 취미가 없습니다.")

# get_common_hobbies(key_list)
# get_no_common_hobbies(key_list)


########################################################

# 여러 개의 숫자를 입력받아 합계를 계산하는 함수를 작성

# def sum_numbers():
#     sum_num = 0
#     while True:
#         number = input("숫자를 입력하세요. q를 누르면 종료 :")
#         if number == "q":
#             print(f"총합 : {sum_num}")
#             print("종료")
#             break
#         elif number.isdigit():
#             sum_num += int(number)
#         else:
#             print("문자는 사용할수 없습니다.")

#     return sum_num


# sum_numbers()
########################################################

# 과제 : 모든 함수 호출 시간을 측정하는 데코레이터 적용


# import datetime
# def time_decorator(func):
#     def wrapper(*args, **kwargs):
#         now = datetime.datetime.now()
#         print(f"호출 시간 : {now.year}년 {now.month}월 {now.day}일 {now.hour}시 {now.minute}분 {now.second}초")
#         return func(*args, **kwargs)
#     return wrapper

# @time_decorator
# def sum_numbers():
#     sum_num = 0
#     while True:
#         number = input("숫자를 입력하세요. q를 누르면 종료 :")
#         if number == "q":
#             print(f"총합 : {sum_num}")
#             print("종료")
#             break
#         elif number.isdigit():
#             sum_num += int(number)
#         else:
#             print("문자는 사용할수 없습니다.")

# sum_numbers()

# hobbies = {
#     "Alice": ["음악", "영화", "독서"],
#     "Bob": ["스포츠", "여행", "음악"],
#     "Charlie": ["프로그래밍", "게임", "영화"],
#     "David": ["요리", "여행", "사진"],
#     "Eve": ["프로그래밍", "독서", "음악"],
#     "Frank": ["스포츠", "게임", "요리"],
#     "Grace": ["영화", "여행", "독서"]
# }

# key_list = list(hobbies)
# @time_decorator
# def get_common_hobbies(key_list):
    
#     for other , interests in hobbies.items():
#         if other == key_list[0]:
#             continue
#         common_hobbies = set(interests) & set(hobbies[key_list[0]])
#         if common_hobbies:
#             print(f"{key_list[0]}와 {other}의 공통 취미 : {common_hobbies}")
# @time_decorator
# def get_no_common_hobbies(key_list):
    
#     for other , interests in hobbies.items():
#         if other == key_list[0]:
#             continue
#         no_common_hobbies = not(set(interests) & set(hobbies[key_list[0]]))
#         if no_common_hobbies:
#             print(f"{key_list[0]}와 {other}의 공통 취미가 없습니다.")

# get_common_hobbies(key_list)
# get_no_common_hobbies(key_list)

########################################################

# 계산기 모듈
# from calculator.arithmetic import add, subtract, multiply, divide, remainder, quotient

# def calculator():
#     a = int(input("첫번째 숫자를 입력하세요 :"))
#     b = int(input("두번째 숫자를 입력하세요 :"))
#     print(f"더하기 : {add(a, b)}")
#     print(f"빼기 : {subtract(a, b)}")
#     print(f"곱하기 : {multiply(a, b)}")
#     print(f"나누기 : {divide(a, b)}")
#     print(f"나머지 : {remainder(a, b)}")
#     print(f"몫 : {quotient(a, b)}")


# calculator()
########################################################

# 과제 : 클래스 구현

# • 다음 클래스를 구현하세요:
# • `Book`: 도서 정보(제목, 저자, ISBN, 출판연도 등)를 관리
# • `Library`: 도서 컬렉션을 관리하고 대출/반납 기능 제공
# • `Member`: 도서관 회원 정보와 대출 목록 관리
# • 다음 기능을 구현하세요:
# • 도서 추가/삭제
# • 도서 검색(제목, 저자, ISBN으로)
# • 도서 대출/반납
# • 회원 등록/관리
# • 회원별 대출 현황 확인
# • 객체 지향 설계 원칙(SOLID)을 최소한 2가지 이상 적용하세요.
# • 적절한 캡슐화를 통해 데이터를 보호하세요.

# 책 클래스
# class Books:
#     def __init__(self, title, author, isbn, publication_year,quantity=int):
#         self._title = title
#         self._author = author
#         self._isbn = isbn
#         self._publication_year = publication_year
#         self._quantity = quantity

#     @property
#     def title(self):
#         return self._title

#     @property
#     def author(self):
#         return self._author

#     @property
#     def isbn(self):
#         return self._isbn

#     @property
#     def publication_year(self):
#         return self._publication_year

#     @property
#     def quantity(self):
#         return self._quantity

#     # setter 메서드
#     @quantity.setter
#     def quantity(self, value):
#         if value < 0:
#             raise ValueError("수량은 0보다 작을 수 없습니다.")
#         self._quantity = value


# class Library:
    
#     def __init__(self):
#         self._books = []
#         self._members = []
#         self._rental_books = []

#     #도서 추가  
#     def add_book(self, title, author, isbn, publication_year,quantity=int):
#         print("도서 추가 중...")
#         for book in self._books:
#             if book.isbn == isbn:
#                 book.quantity += quantity
#                 print(f"도서 {title} 수량이 증가되었습니다.\n")
#                 return
#         else:
#             self._books.append(Books(title, author, isbn, publication_year,quantity))
#             print(f"도서 {title} 추가되었습니다.\n")

#     #도서 삭제
#     def remove_book(self,isbn):
#         print("도서 삭제 중...")
#         for book in self._books:
#             if book.isbn == isbn:
#                 self._books.remove(book)
#                 print("도서가 삭제되었습니다.\n")
#                 return
#         print("존재하지 않는 도서입니다.\n")

#     #도서 검색
#     def search_book(self, title= None, author= None, isbn= None):
#         print("도서 검색 중...")
#         found = False
            
#         for book in self._books:
#             if title and book.title == title:
#                 print(f"제목 검색 결과 : \n제목 : {book.title}\n저자 : {book.author}\nISBN : {book.isbn}\n출판연도 : {book.publication_year}\n")
#                 found = True
#             elif author and book.author == author:
#                 print(f"저자 검색 결과 : \n제목 : {book.title}\n저자 : {book.author}\nISBN : {book.isbn}\n출판연도 : {book.publication_year}\n")
#                 found = True
#             elif isbn and book.isbn == isbn:
#                 print(f"ISBN 검색 결과 : \n제목 : {book.title}\n저자 : {book.author}\nISBN : {book.isbn}\n출판연도 : {book.publication_year}\n")
#                 found = True
         
#         if not found:
#             print("존재하지 않는 도서입니다.\n")

#     #도서 대여
#     def rental_book(self,isbn,member_id):
#             print("대여 처리 중...")
#             for member in self._members:
#                 if member.member_id == member_id:
#                     break
#             else:
#                 print("존재하지 않는 회원입니다.\n")
#                 return

#             for book in self._books :
#                 if book.isbn == isbn and member_id not in self._rental_books:
#                     if book.quantity > 0:
#                         book.quantity -= 1
#                         self._rental_books.append({
#                             "member_id" : member_id,
#                             "isbn" : isbn,
#                             "title" : book.title,
#                         })
#                         print(f"{book.title} 도서가 {member_id}님에게 대출되었습니다.\n")
#                         return
#                     else:
#                         print(f"{book.title} 도서는 이미 대출중입니다.\n")
#                         return
#                 if book.isbn == isbn and member_id in self._rental_books:
#                     print(f"이미 대출중인 도서입니다.\n")
#                     return
                
#             print("존재하지 않는 도서입니다.\n")

#     #도서 반납
#     def return_book(self,isbn,member_id):
#         print("반납 처리 중...")
#         for member in self._members:
#                 if member.member_id == member_id:
#                     break
#                 else:
#                     print("존재하지 않는 회원입니다.\n")
#                     return
        
#         for book in self._books:
            
#             if book.isbn == isbn:
#                 if member_id in self._rental_books:
#                     book.quantity += 1
#                     self._rental_books.pop(member_id)
#                     print(f"{book.title} 도서가 {member_id}님에게 반납되었습니다.\n")
#                     return
#                 else:
#                     print(f"{book.title} 도서는 {member_id}님에게 대출되지 않았습니다.\n")
#                     return
#             print("존재하지 않는 도서입니다.\n")

#     #회원 등록
#     def add_member(self, member_name, member_id, member_phone, member_email):
#         print("회원 등록 중...")
#         if member_id in self._members:
#             print("이미 존재하는 회원입니다.\n")
#             return
#         self._members.append(Members(member_name, member_id, member_phone, member_email))
#         print(f"{member_name}님이 성공적으로 등록되었습니다.\n")

#     #대출 목록 조회

#     def rental_list(self):
#         print("대출 목록 조회회 중...")
#         for member in self._members:
#             member_rentals = [rental for rental in self._rental_books if rental["member_id"] == member.member_id]
#             if member_rentals:
#                 print(f"{member.member_name}님의 대출 목록 :")
#                 for rental in member_rentals:
#                     print(f"제목 : {rental['title']}")
#             else:
#                 print(f"{member.member_name}님의 대출 목록이 없습니다.\n")

# class Members:
#     def __init__(self, member_name, member_id, member_phone, member_email):
#         self._member_name = member_name
#         self._member_id = member_id
#         self._member_phone = member_phone
#         self._member_email = member_email
#         self._rental_books = []
#         self._return_books = []

    
#     @property
#     def member_name(self):
#         return self._member_name

#     @property
#     def member_id(self):
#         return self._member_id

#     @property
#     def member_phone(self):
#         return self._member_phone

#     @property
#     def member_email(self):
#         return self._member_email

#     @property
#     def rental_books(self):
#         return self._rental_books.copy()  # 복사본 반환하여 외부 수정 방지

#     # setter 메서드
#     def add_rental_book(self, book):
#         self._rental_books.append(book)

#     def remove_rental_book(self, book):
#         if book in self._rental_books:
#             self._rental_books.remove(book)




# library = Library()
# #예제 책 등록
# library.add_book("파이썬", "저자", "ISBN", "2024",1)
# library.add_book("자바", "저자2", "ISBN2", "2025",1)
# library.add_book("C++", "저자3", "ISBN3", "2024",1)
# library.add_book("파이썬", "저자", "ISBN", "2024",1)
# #예제 책 검색
# library.search_book(title="파이썬")
# library.search_book(author="저자2")
# library.search_book(isbn="ISBN3")
# #예제 회원 등록
# library.add_member("회원1", "회원1", "010-1234-5678", "test@test.com")
# library.add_member("회원2", "회원2", "010-1234-5678", "test@test.com")
# #예제 책 대출
# library.rental_book("ISBN", "회원1")
# library.rental_book("ISBN2", "회원1")
# library.rental_book("ISBN3", "회원1")
# library.rental_book("ISBN", "회원2")
# library.rental_book("ISBN", "회원3")
# #예제 책 반납
# library.return_book("ISBN", "회원1")
# library.return_book("ISBN", "회원3")
# #예제 대출 목록 출력
# library.rental_list()


########################################################

#파일 처리기 구현
# • 다양한 유형의 파일(텍스트, CSV, JSON, 바이너리)을 읽고 쓸 수 있어야 합니다
# • 파일이 존재하지 않거나, 권한이 없거나, 형식이 잘못된 경우 등 다양한 오류 상황을 적절히 처리
# • 사용자 정의 예외 계층 구조를 설계하고 구현
# • 오류 발생 시 로깅을 통해 문제를 기록
# • 모든 파일 작업은 컨텍스트 매니저(`with` 구문)를 사용
# import json
# import csv
# import logging

# logging.basicConfig(
#     level=logging.INFO,
#     format='%(asctime)s - %(levelname)s - %(message)s',
#     handlers=[
#         logging.FileHandler('file_handler.log'),
#         logging.StreamHandler()
#     ]
# )


# class FileHandler:
#      def __init__(self, file_path):
#          self._file_path = file_path
#      def read_text(self):
#           try:
#               with open(self._file_path, "r",encoding="utf-8") as file:
#                    content = file.readline()
#                    for line in content:
#                          print(line)
#           except Exception as e:
#                logging.error(f"txt 파일 읽기 오류 : {e}")

#      def write_text(self, content):
#           try:
#                with open(self._file_path, "w",encoding="utf-8") as file:
#                    file.write(content)
#           except Exception as e:
#                logging.error(f"txt 파일 쓰기 오류 : {e}")

#      def read_csv(self):
#           try:
#                with open(self._file_path, "r",encoding="utf-8") as file:
#                     #헤더 읽기
#                     header = file.readline().strip().split(",")
#                     print(f"헤더 : {header}")
#                     #데이터 읽기
#                     for line in file:
#                          values = line.strip().split(",")
#                          print(f"값 : {values}")
#           except Exception as e:
#                logging.error(f"csv 파일 읽기 오류 : {e}")
    
#      def write_csv(self, header, data):
#           try:
#               with open(self._file_path, "w",encoding="utf-8",newline="") as file:
#                    writer = csv.writer(file)
#                    writer.writerow(header)
#                    writer.writerows(data)
#           except Exception as e:
#                logging.error(f"csv 파일 쓰기 오류 : {e}")

#      def read_json(self):
#           try:
#                with open(self._file_path, "r",encoding="utf-8") as file:
#                     content = file.read()
#                     print(content)
#           except Exception as e:
#                logging.error(f"json 파일 읽기 오류 : {e}")
    
#      def write_json(self, content):
#           try:
#                with open(self._file_path, "w",encoding="utf-8") as file:
#                    file.write(content)
#           except Exception as e:
#                logging.error(f"json 파일 쓰기 오류 : {e}")

#      def read_binary(self):
#           try:
#                with open(self._file_path, "rb") as file:
#                     content = file.read()
#                     print(content)
#           except Exception as e:
#                logging.error(f"binary 파일 읽기 오류 : {e}")
    
#      def write_binary(self, content):
#           try:
#                with open(self._file_path, "wb") as file:
#                     file.write(content)
#           except Exception as e:
#                logging.error(f"binary 파일 쓰기 오류 : {e}")
        
# try:
#     file_handler = FileHandler("example.txt")
#     file_handler.write_text("Hello, World!")
#     file_handler.read_text()
#     file_handler = FileHandler("example.csv")
#     file_handler.write_csv(["Hello, World!"],["Hello, World!"])
#     file_handler.read_csv()
#     file_handler = FileHandler("example.json")
#     file_handler.write_json({"Hello, World!"})
#     file_handler.read_json()
#     file_handler = FileHandler("example.bin")
#     file_handler.write_binary(b"Hello, World!")
#     file_handler.read_binary()
    
# except FileNotFoundError as e:
#     logging.error(f"파일을 찾을 수 없습니다 : {e}")

# except PermissionError as e:
#     logging.error(f"파일 권한이 없습니다 : {e}")

# except Exception as e:
#     logging.error(f"오류 발생 : {e}")



















########################################################
# 과제
# • 로그 파일을 한 줄씩 읽는 제너레이터 함수 작성
# • 특정 패턴(예: 'ERROR', 'WARNING' 등)이 포함된 줄만 필터링하는 제너레이터 작성

# class Logger:
#     def __init__(self, file_path):
#         self._file_path = file_path

#     def log_generator(self):
#         try:
#             with open(self._file_path, "r",encoding="utf-8") as file:
#                 for line in file:
#                     yield line
#         except Exception as e:
#             print(f"오류 발생 : {e}")

#     def filter_log(self):
#         try:
#             with open("error.log", "a",encoding="utf-8") as error_file:
#                 for line in self.log_generator():
#                     if "ERROR" in line or "WARNING" in line:
#                         error_file.write(line)
#                         yield line
#         except Exception as e:
#             print(f"오류 발생 : {e}")

# Logger = Logger("test.log")

# for log_line in Logger.filter_log():
#     print(log_line, end="")



########################################################
#과제
#• 5개의 공개 API URL에 GET 요청을 보냄
# • 세 가지 방식으로 구현하고 성능을 비교합니다:
# • 순차 처리
# • ThreadPoolExecutor 사용
# • asyncio와 aiohttp 사용
# • API_URLS
# • "https://jsonplaceholder.typicode.com/posts/1",
# • "https://jsonplaceholder.typicode.com/posts/2",
# • "https://jsonplaceholder.typicode.com/posts/3",
# • "https://jsonplaceholder.typicode.com/posts/4",
# • "https://jsonplaceholder.typicode.com/posts/5"


# import asyncio
# import aiohttp
# import time
# import concurrent.futures
# import requests

# websites = [
#     "https://jsonplaceholder.typicode.com/posts/1",
#     "https://jsonplaceholder.typicode.com/posts/2",
#     "https://jsonplaceholder.typicode.com/posts/3",
#     "https://jsonplaceholder.typicode.com/posts/4",
#     "https://jsonplaceholder.typicode.com/posts/5"
# ]


# #requests용
# def fetch_sync(url):
    
#     try:
#         start_time = time.time()
#         response = requests.get(url, timeout=10)
#         response.raise_for_status()
#         content = response.text
#         elapsed = time.time() - start_time
#         print(f"{url} 요청 중...")
#         print(f"{url} 응답 완료: {len(content)} 바이트 (소요시간: {elapsed:.2f}초)")
#         return url, len(content), elapsed
#     except Exception as e:
#         print(f"{url} 요청 중...")
#         print(f"{url} 요청 실패: {e}")
#         return url, 0, 0


# #aiohttp용
# async def fetch(session, url):
#     print(f"{url} 요청 중...")
#     try:
#         start_time = time.time()
#         async with session.get(url, timeout=10) as response:
#             content = await response.text()
#             elapsed = time.time() - start_time
#             print(f"{url} 응답 완료: {len(content)} 바이트 (소요시간: {elapsed:.2f}초)")
#             return url, len(content), elapsed
#     except Exception as e:
#         print(f"{url} 요청 실패: {e}")
#         return url, 0, 0


# #순차 처리
# def fetch_sequential(urls):
#     start_time = time.time()
#     results = []
#     for url in urls:
#         result = fetch_sync(url)
#         results.append(result)

#     end_time = time.time()
#     elapsed = end_time - start_time
#     print(f"순차 처리 완료, 소요시간 : {elapsed}초")
#     return results, elapsed

# #ThreadPoolExecutor 사용
# def fetch_with_threads(urls):
#     start_time = time.time()
#     results = []

#     with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
#         future_to_url = {executor.submit(fetch_sync,url):url for url in urls}
#         for future in concurrent.futures.as_completed(future_to_url):
#             url = future_to_url[future]
#             try:
#                 result = future.result()
#                 results.append(result)
#             except Exception as e:
#                 print(f"{url} 요청 실패: {e}")

#     end_time = time.time()  
#     elapsed = end_time - start_time
#     print(f"ThreadPoolExecutor 사용 완료, 소요시간 : {elapsed}초")
#     return results, elapsed

        
# #aiohttp 사용
# async def fetch_aiohttp(urls):
#     start_time = time.time()
#     results = []

#     async with aiohttp.ClientSession() as session:
#         for url in urls:
#             result = await fetch(session, url)
#             results.append(result)

#     end_time = time.time()
#     elapsed = end_time - start_time
#     print(f"aiohttp 사용 완료, 소요시간 : {elapsed}초")
#     return results , elapsed



# async def main():
#     # print("순차 처리 시작")
#     # sequntial_results = await fetch_sequential(websites)    

#     print("순차 처리 시작")
#     sequntial_results = fetch_sequential(websites)

#     await asyncio.sleep(1)

#     print("ThreadPoolExecutor 사용 시작")
#     threadpool_results = fetch_with_threads(websites)

#     await asyncio.sleep(1)

#     #aiohttp 사용
#     print("\naiohttp 시작")
#     aiohttp_results = await fetch_aiohttp(websites)


#     #결과
#     print("\n 결과 출력")


#     sequntial_total_time = sequntial_results[1]
#     threadpool_total_time = threadpool_results[1]
#     aiohttp_total_time = aiohttp_results[1]

#     print(f"순차 처리 총 시간 : {sequntial_total_time}")
#     print(f"threadpool 총 시간 : {threadpool_total_time}")
#     print(f"aiohttp 총 시간 : {aiohttp_total_time}")

# if __name__ == "__main__":
#     asyncio.run(main())
