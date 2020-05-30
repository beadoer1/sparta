# print ('Hello, sparta')

a = 3      # 3을 a에 넣는다
b = a      # a를 b에 넣는다
a = a + 1  # a+1을 다시 a에 넣는다

num1 = a*b # a*b의 값을 num1이라는 변수에 넣는다
num2 = 99 # 99의 값을 num2이라는 변수에 넣는다

# 변수의 이름은 마음대로 지을 수 있음!
# 진짜 "마음대로" 짓는 게 좋을까? var1, var2 이렇게?

name = 'bob' # 변수에는 문자열이 들어갈 수도 있고,
num = 12 # 숫자가 들어갈 수도 있고,

is_number = True # True 또는 False -> "Boolean"형이 들어갈 수도 있습니다.

#########
# 그리고 List, Dictionary 도 들어갈 수도 있죠. 그게 뭔지는 아래에서!

a_list = []
a_list.append(1)     # 리스트에 값을 넣는다
a_list.append([2,3]) # 리스트에 [2,3]이라는 리스트를 다시 넣는다

# print 를 사용해서 아래 값을 확인해봅시다
# a_list의 값은? [1,[2,3]]
# a_list[0]의 값은? 1
# a_list[1]의 값은? [2,3]
# a_list[1][0]의 값은? 2

a_dict = {}
a_dict = {'name':'bob','age':21}
a_dict['height'] = 178

# print 를 사용해서 아래 값을 확인해봅시다
# a_dict의 값은? {'name':'bob','age':21, 'height':178}
# a_dict['name']의 값은? 'bob'
# a_dict['age']의 값은? 21
# a_dict['height']의 값은? 178

people = [{'name':'bob','age':20},{'name':'carry','age':38}]

# print 를 사용해서 아래 값을 확인해봅시다
# people[0]['name']의 값은? 'bob'
# people[1]['name']의 값은? 'carry'

person = {'name':'john','age':7}
people.append(person)

# print 를 사용해서 아래 값을 확인해봅시다
# people의 값은? [{'name':'bob','age':20},{'name':'carry','age':38},{'name':'john','age':7}]
# people[2]['name']의 값은? 'john'

# print (people) --> 지정해놓은 List 는 ''를 붙이지 않고 출력

def sum_all(a,b,c):
	return a+b+c

def mul(a,b):
	return a*b

result = sum_all(1,2,3) + mul(10,10)

# result라는 변수의 값은?
# print (result)

def oddeven(num):  # oddeven이라는 이름의 함수를 정의한다. num을 변수로 받는다.
	if num % 2 == 0: # num을 2로 나눈 나머지가 0이면
		 return True   # True (참)을 반환한다.
	else:            # 아니면,
		 return False  # False (거짓)을 반환한다.

result = oddeven(20)
# result의 값은 무엇일까요?
# print (result)

