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


class Books:
    def __init__(self, title, author, isbn, publication_year,quantity):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.publication_year = publication_year
        self.quantity = quantity


class Library:
    def __init__(self):
        self.books = []
        self.members = []
        self.rental_books = {}

    def add_book(self, title, author, isbn, publication_year,quantity):
        self.books.append(Books(title, author, isbn, publication_year,quantity))
    
    def remove_book(self,isbn):
        for book in self.books:
            if book.isbn == isbn:
                self.books.remove(book)
                print("도서가 성공적으로 삭제되었습니다.")
                return
        print("존재하지 않는 도서입니다.")

    def search_book(self, title= None, author= None, isbn= None):

        found = False
            
        for book in self.books:
            if title and book.title == title:
                print(f"제목 검색 결과 : \n제목 : {book.title}\n저자 : {book.author}\nISBN : {book.isbn}\n출판연도 : {book.publication_year}\n")
                found = True
            elif author and book.author == author:
                print(f"저자 검색 결과 : \n제목 : {book.title}\n저자 : {book.author}\nISBN : {book.isbn}\n출판연도 : {book.publication_year}\n")
                found = True
            elif isbn and book.isbn == isbn:
                print(f"ISBN 검색 결과 : \n제목 : {book.title}\n저자 : {book.author}\nISBN : {book.isbn}\n출판연도 : {book.publication_year}\n")
                found = True
         
        if not found:
            print("존재하지 않는 도서입니다.\n")

    def rental_book(self,isbn,member_id):
            
            for member in self.members:
                if member.member_id == member_id:
                    break
            else:
                print("존재하지 않는 회원입니다.")
                return

            for book in self.books :
                if book.isbn == isbn and member_id not in self.rental_books:
                    if book.quantity > 0:
                        book.quantity -= 1
                        self.rental_books[member_id] = book.title
                        print(f"{book.title} 도서가 {member_id}님에게 대출되었습니다.")
                        return
                    else:
                        print(f"{book.title} 도서는 이미 대출중입니다.")
                        return
                if book.isbn == isbn and member_id in self.rental_books:
                    print(f"이미 대출중인 도서입니다.")
                    return
                
            print("존재하지 않는 도서입니다.")

    def return_book(self,isbn,member_id):

        for member in self.members:
                if member.member_id == member_id:
                    break
                else:
                    print("존재하지 않는 회원입니다.")
                    return
        
        for book in self.books:
            if book.isbn == isbn:
                if member_id in self.rental_books:
                    book.quantity += 1
                    self.rental_books.pop(member_id)
                    print(f"{book.title} 도서가 {member_id}님에게 반납되었습니다.")
                    return
                else:
                    print(f"{book.title} 도서는 {member_id}님에게 대출되지 않았습니다.")
                    return
            print("존재하지 않는 도서입니다.")
    
    def add_member(self, member_name, member_id, member_phone, member_email):
        if member_id in self.members:
            print("이미 존재하는 회원입니다.")
            return
        self.members.append(Members(member_name, member_id, member_phone, member_email))
        print(f"{member_name}님이 성공적으로 등록되었습니다.")



    def rental_list(self):

        for member in self.members:
            if member.member_id in self.rental_books:
                print(f"{member.member_name}님의 대출 목록 : {self.rental_books[member.member_id]}")
            elif member.member_id not in self.rental_books:
                print(f"{member.member_name}님의 대출 목록이 없습니다.")
            else:
                print("존재하지 않는 회원입니다.")

class Members:
    def __init__(self, member_name, member_id, member_phone, member_email):
        self.member_name = member_name
        self.member_id = member_id
        self.member_phone = member_phone
        self.member_email = member_email
        self.rental_books = []
        self.return_books = []




library = Library()
#예제 책 등록
library.add_book("파이썬", "저자", "ISBN", "2024",1)
library.add_book("자바", "저자2", "ISBN2", "2025",1)
library.add_book("C++", "저자3", "ISBN3", "2024",1)
#예제 책 검색
library.search_book(title="파이썬")
library.search_book(author="저자2")
library.search_book(isbn="ISBN3")
#예제 회원 등록
library.add_member("회원1", "회원1", "010-1234-5678", "test@test.com")
#예제 책 대출
library.rental_book("ISBN", "회원1")
library.rental_book("ISBN2", "회원1")
library.rental_book("ISBN3", "회원1")
#예제 책 반납
library.return_book("ISBN", "회원1")
library.return_book("ISBN", "회원2")
#예제 대출 목록 출력
library.rental_list()


