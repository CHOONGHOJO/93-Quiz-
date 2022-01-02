# Quiz) Hangman game (영어 단어 퀴즈) program을 만드시오.
# -리스트에 3개 이상의 단어를 추가
# 예) apple, banana, orange
# - 위 리스트에서 랜덤으로 1개의 단어를 출력
# - 단어의 길이에 맞게 밑줄 출력
# 예) apple 경우 _____
# - 사용자로부터 1글자씩 입력을 받되, 단어에 입력값이 포함되면 'Correct'출력, 아니면 'Wrong'출력
# - 매번 입력을 받을 때마다 현재까지 맞힌 글자들 표시 (맞히지 못한 글자는 믿줄 출력)
# 예) a 입력시 : a____
#     p 입력시 : app__
#     c 입력시 : app__
# - 정답을 맞히면 Scuccess 출력 후 프로그램 종료 (단, 횟수 제한은 없음)



from random import *
words = ['apple', 'banana', 'orange']
word = choice(words)
print("answer : " + word)
letters = '' # 사용자로부터 지금까지 입력받은 모든 알파벳

while True:
    succeed = True
    print() # 줄바꿈
    for w in word:
        if w in letters:
            print(w, end=" ")
        else:
            print("_", end=" ")
            succeed = False
    print() # 줄바꿈

    if succeed:
        print("Success")
        break

    letter = input("Input letter > ") # 사용자 입력 받기
    if letter not in letters:
        letters += letter

    if letter in word:
        print("Correct")
    else:
        print("Wrong")