def profile(name, age, main_lang):
    print(name, age, main_lang)

profile(name = "유재석", main_lang = "파이썬", age = 20)
profile(main_lang = "자바", age = 25, name = "김태호")

#'키워드 = 값'을 하면 이렇게 출력이 잘됨

def profile(name, age=24, birth=981102):
    print("회원님의 이름: {0} 나이 :{1} 생일 :{2}".format(name, age, birth))

profile("함도윤")
