print("나는 %d살입니다." %20) # %d(d는 정수를 의미함)의 값을 뒤에있는 %20의 값으로 넣는다는 뜻
print("나는 %d살입니다." %20)
print("나는 %s을 좋아해요." %"파이썬")
print("나는 %s을 좋아해요." %"파이썬")# %s는 string(문자)를 넣겠다는 뜻
print("Apple 은 %c로 시작해요." %"A")
print("Apple 은 %c로 시작해요." % "A") # %c는 문자하나를 의미해

print("나는 %s살입니다." %20)
print("나는 %s색과 %s색을 좋아해요." %("빨간", "파란"))

print("나는 {}살입니다." .format(20)) # {}과 .format()으로 할 수 있어
print("나는 {0}색과 {1}색을 좋아해요." .format("파란", "빨간")) 
print("나는 {1}색과 {0}색을 좋아해요." .format("파란", "빨간"))


print("나는 {}살입니다." .format(5))