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

#과제 : 집합
# 소셜 네트워크에서 사용자 간의 관계와 추천 시스템을
# 구현하는 프로그램을 작성
# 공통 관심사를 갖는 친구 응답
# 공통 관심사가 없는 친구 응답

hobbies = {
    "Alice": ["음악", "영화", "독서"],
    "Bob": ["스포츠", "여행", "음악"],
    "Charlie": ["프로그래밍", "게임", "영화"],
    "David": ["요리", "여행", "사진"],
    "Eve": ["프로그래밍", "독서", "음악"],
    "Frank": ["스포츠", "게임", "요리"],
    "Grace": ["영화", "여행", "독서"]
}

key_list = list(hobbies)
print(key_list)










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



