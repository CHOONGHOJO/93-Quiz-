# 감짝 퀴즈) 다음 코드를 실행하면 출력값이 어떻게 될까요?

def three():
    print("three", end=" ")
    return 3

def five():
    print("five", end=" ")
    return 5

def seven():
    print("seven", end=" ")
    return 7

# main code
three() > five() > seven() # three() 실행하여 3 이 나오고, five() 실행하여 5 나옴 : 3 > 5 => False => 다음 작업 실행하지 않음
# 그래서  three five 만 출력됨
# end=" " 라서 한 줄에 three five 를 print

# 답) three five

print( 3 > 5 > 7) # (3 > 5) and (5 > 7) => False

#####################################################33

def 서류심사(): print("1.서류심사"); return True
def 인적성검사(): print("2.인적성검사"); return True
def 코딩테스트(): print("3.코딩테스트"); return True
def 면접1차(): print("4.면접1차"); return True
def 면접2차(): print("5.면접2차"); return False
def 신체검사(): print("6.신체검사"); return True

if 서류심사() and 인적성검사() and 코딩테스트()  and 면접1차() and 면접2차() and 신체검사():
    print("최종 합격입니다.")
else:
    print("아쉽게도 탈락입니다.")