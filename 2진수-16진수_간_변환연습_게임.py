from random import *
import winsound as ws

def beepsound():
    freq = 2000    # range : 37 ~ 32767
    dur = 500     # ms
    ws.Beep(freq, dur) # winsound.Beep(frequency, duration)

binaryList = ['0000', '0001', '0010', '0011', '0100', '0101', '0110', '0111', '1000', '1001', '1010', '1011', '1100', '1101', '1110', '1111']
hexaList = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']

if __name__== "__main__":
    print("이 프로그램은 2진수와 16진수의 변환연습을 돕기 위해 만들어졌습니다.\n")
    print("======  2진수 입력은 숫자 4자리에 맞춰 입력해주세요. (예 : '0'입력 시 -> \'0000\')")
    print("====== 16진수 입력은 숫자 1자리 또는 알파벳 1자리로 입력해주세요.")
    print()

    power = 1
    obj = 1
    totalCount = 0
    correctCount = 0

    while power != 0:
        obj = int(input(" 2진수 -> 16진수로 변환연습은 16을,\n16진수 -> 2진수로 변환연습은  2를,\n 종료하시려면 0을 입력해주세요 : "))
        print()

        if obj == 0:
            print("프로그램을 종료합니다!")
            print("오늘 푼 문제 수 : %d\t정답 수 : %d" % (totalCount, correctCount))
            quit()

        elif obj in [2, 16]:
            while obj == 2 or obj == 16:
                # 2진수 -> 16진수
                while obj == 16:
                    num = randrange(0, 16)
                    print(" 2진수 %s의 16진수는 무엇일까요? : " % binaryList[num], end='')
                    ans = input()

                    if hexaList[num] == ans:
                        totalCount += 1
                        correctCount += 1
                        print("정답입니다!\t문제 수 : %d\t정답 수 : %d\t\n" % (totalCount, correctCount))
                    else:
                        totalCount += 1
                        beepsound()
                        print("틀렸습니다!\t정답은 %s입니다.\t문제 수 : %d\t정답 수 : %d\t\n" % (hexaList[num], totalCount, correctCount))
                    
                    obj = int(input("계속하시겠습니까? 1 - 예 / 0 - 아니오 : "))
                    print()

                    if obj == 1 : obj = 16
                    else : break

                # 16진수 -> 2진수
                while obj == 2:
                    num = randrange(0, 16)
                    print("16진수 %s의  2진수는 무엇일까요? : " % hexaList[num], end='')
                    ans = input()

                    if binaryList[num] == ans:
                        totalCount += 1
                        correctCount += 1
                        print("정답입니다!\t문제 수 : %d\t정답 수 : %d\t\n" % (totalCount, correctCount))
                    else:
                        totalCount += 1
                        beepsound()
                        print("틀렸습니다!\t정답은 %s입니다.\t문제 수 : %d\t정답 수 : %d\t\n" % (binaryList[num], totalCount, correctCount))
                    
                    obj = int(input("계속하시겠습니까? 1 - 예 / 0 - 아니오 : "))
                    print()

                    if obj == 1 : obj = 2
                    else : break

        else : print("잘못 입력하셨습니다!")    # 에러코드