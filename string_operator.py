print("문자 선택 연산자")
print("안녕하세요"[-1])
print("안녕하세요"[-2])
print("안녕하세요"[-3])
print("안녕하세요"[-4])
print("안녕하세요"[-5])
print()

# Traceback (most recent call last):
#   File "D:\Git\WebHosting\#hwanghyunjiii\python\string_operator.py", line 6, in <module>
#     print("안녕하세요"[5])
# IndexError: string index out of range

#마지막 숫자를 포함하지 않음
print("안녕하세요"[1:4])
print()

hello = "안녕하세요"
print(hello[:3])
print(hello[3:])
print(len(hello))
print()

print(type(25))
print(type(52.273))
print()

print("5 + 7 = ", 5+7)
print("5 * 7 = ", 5*7)


print("3 / 2 = ", 3/2)
print("3 // 2 = ", 3//2) #정수 나누기 연산자
print("3 % 2 = ", 3%2)
print("3 ** 2 = ", 3**2) # 제곱