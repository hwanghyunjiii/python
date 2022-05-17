num = 10
num **= 2
print(num)
print()

string = "안녕하세요"
string += "!"
string += "!"
print("string:", string)
print()

# input()의 결과는 항상 문자열
num = input("숫자를 입력하세요> ")
print(num)
print(type(num)) #<class 'str'> 

# 문자열을 int로 변환
num2 = int(num)
print(type(num2))
print()

# int를 문자열로 변환
string = str(num2)
print(string)
print()