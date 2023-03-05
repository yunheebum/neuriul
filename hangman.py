import time
import random
import csv

#  초기 화면 구성
print('o'*50)
print('낱말 맞추기 게임을 시작 하겠습니다. \n'
      '주어진 기회 안에 맞추어야 합니다.')
print('o'*50)

print('loading .......')
time.sleep(0.5)

print()
print()
print()
print()

# word='answer' # 테스트 정답
#파일에서 퀴즈 문제 가져오기
words=[]
with open('quiz.csv','r') as q:
    reader=csv.reader(q)

    for c in reader:
        words.append(c)
        
    # print(word)

# f=open('quiz.csv','w')
# f.close
# 파일 생성을 위해 임시 작성

# with open('quiz.csv','w') as q:
#     q.write('danger\n')
#     q.write('test\n')
#     q.write('interest')


# 낱말 맞추기 게임 변수 정리

#문제 섞기
random.shuffle(words)
quiz=random.choice(words)

word=quiz[0]
# print(word)

turns=3 # 주어진 게임 기회(10회 정도)
blank=' '

for i in word:
    print('_', end=" ")


while turns > 0:
    answer=input(blank*2*len(word) +'낱말을 입력하세요')
    for i in word:
        for j in answer:
            if i==j:
                print(i,end=" ")
                break
        else:
            print('_',end=" ")
    
    print(blank+'기회가 한번 줄었습니다.')
    if turns==1:
        print(blank+ '기회가 1  남앗습니다.\\')
    turns -= 1