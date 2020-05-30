

# def oddeven(num):  # oddeven이라는 이름의 함수를 정의한다. num을 변수로 받는다.
# 	if num % 2 == 0: # num을 2로 나눈 나머지가 0이면
# 		 return True   # True (참)을 반환한다.
# 	else:            # 아니면,
# 		 return False  # False (거짓)을 반환한다.

# result = oddeven(20)
# # result의 값은 무엇일까요?
# print (result)


# def is_adult(age):
# 	if age > 20:
# 		print('성인입니다')    # 조건이 참이면 성인입니다를 출력
# 	else:
# 		print('청소년이에요')  # 조건이 거짓이면 청소년이에요를 출력

# is_adult(20)
# # 무엇이 출력될까요?


# fruits = ['사과','배','감','귤']

# for fruit in fruits:
# 	print(fruit)

# # 사과, 배, 감, 귤 하나씩 꺼내어 찍힙니다.


# fruits = ['사과','배','배','감','수박','귤','딸기','사과','배','수박']

# count = 0
# for fruit in fruits:
# 	if fruit == '사과':
# 		count += 1

# print(count)

# # 사과의 갯수를 세어 보여줍니다.

# def count_fruits(what):
# 	count = 0
# 	for fruit in fruits:
# 		if fruit == what:
# 			count += 1
# 	return count

# subak_count = count_fruits('수박')
# print(subak_count) #수박의 갯수

# gam_count = count_fruits('감')
# print(gam_count) #감의 갯수


# people = [{'name': 'bob', 'age': 20}, 
#           {'name': 'carry', 'age': 38},
#           {'name': 'john', 'age': 7}]

# # 모든 사람의 이름과 나이를 출력해봅시다.
# for person in people: # ★ for-in 문이 List 내 귀속되는 항목 지정
#     print(person['name'], person['age'])


# # 이번엔, 반복문과 조건문을 응용한 함수를 만들어봅시다.
# # 이름을 받으면, age를 리턴해주는 함수
# def get_age(myname):
#     for person in people:
#         if person['name'] == myname:
#             return person['age']
#     return '해당하는 이름이 없습니다'

# result = get_age('john')
# print(result)
# print(get_age('bob'))
# print(get_age('kay'))