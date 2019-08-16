[TOC]



## 알고리즘: 문제를 풀기위한 절차나 방법

**문제이해**

**결과값에 대한 이해**

**제한 조건에 대한 이해**

**최대 입력값의 이해**

: 컴퓨터가 어떤 일을 수행하기 위한 단계적 방법 



무엇이 좋은 알고리즘인가?

1. **정확성**

2. 작업량: **시간 복잡도**

   연산의 개수(산술[+, /, //], 논리[or, and], 관계[<=, !=, ==], 함수호출식)

3. 메모리 사용량: 공간 복잡도

4. 단순성

5. 최적성



**알고리즘 작업량 == 시간복잡도(Time Complexity)**

빅-오(O) 표기법

![1564372713174](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1564372713174.png)



**배열**(Array)이란?

```python
Num1 = 1
Num2 = 2

# 상기와 같이 2개의 변수를 사용해야 하는 경우, 
# 하기와 동일하게 배열로 바꾸어 사용한다.

Num = [1, 2]
```

때문에 프로그램 내에서 여러개의 변수가 필요할때, 일일이 다른 변수명을 이용하여 자료에 접근하는 것은 비효율적이다.

배열을 사용하면 하나의 선언을 통해 여러 변수를 선언할 수 있다.

이로서 다수 변수로 하기 힘든 작업을 배열을 통해 쉽게 할 수 있다.



**1차원 배열과 그에 대한 접근**

```python
Arr = list()
Arr = []

Arr[0] = 10
>> [10]

Arr[0] = 20
>> [20, 10]
```



**배열 활용 예제: Gravity**

![1564372853790](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1564372853790.png)

![1564372890021](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1564372890021.png)

![1564372907377](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1564372907377.png)

```python
'''
처음박스에서 높이를 준다. 7 4 2 0 0 6 0 7 0

1)
앞에있는 것중에 자기자신보다 높은 것을 제외하고 빈칸에 대해서 
수를 센다면 몇칸을 이동할 수 있는지 알 수 있다.

2)
상자가 안쌓인 곳에는 0을 주고 상자가 쌓인 곳은 1을 준다.
그리고 0이 많은 가로줄에 대해 0을 세고, 
그 수가 많은 가로에 대하여 가장 max라고 생각한다.
'''
def build_data(data):
    for i in range(0, 100): # from 0 to 99
        data[i] # random number


if __name__ = "__main__":
    data = int(data[100])
    for i in range(0, 100): # from 0 to 9
        build_data(data)

        '''

        
        return result
        '''

        print(result)
```



**Baby-gin Game** (완전검색:Exaustive Search)

667767  666, 777

054060  456, 000

101123  123, 011



순열을 만들고,

앞 3개가 run **or** triplet인지 검사 후 최종적으로 baby-gin 판단 

하지만 이런 경우 1, 2, 3, 1, 2, 3 -> 1, 1, 2, 2, 3, 3 에서는 오히려 baby-gin 확인 실패



**순열** (Permutation)

- 서로 다른 것들 중 몇 개를 뽑아서 한 줄로 나열
- 서로 다른 n개 중 r개를 택하는 순열 **nPr**

```python
# 같은걸 빼고 for문 반복, 6개면 6개의 for문이다.
for i1 in range(1, 4): # [*, 2, 3]
    for i2 in range(1, 4): # [*, *, 3]
        if i2 != i1:
            for i3 in range(1, 4): # [*, *, 3]
                if i3 != i1 and i3 != i2:
                    print(i1, i2, i3)

>>>
1 2 3
1 3 2
2 1 3
2 3 1
3 1 2
3 2 1
```



**탐욕(Greedy) 알고리즘**

**최적해**(optimal solution)를 구하는데 사용되는 근시안적인 방법

여러 경우 중 하나를 결정해야 할 때마다 그 순간에 최적이라고 생각되는 것을 선택해 나가는 방식으로 진행하여 최종적인 해답에 도달

머릿속에 떠오르는 생각을 검증 없이 바로 구형하면 탐욕 알고리즘



**탐욕(Greedy) 알고리즘 동작과정**

1) **지역적인 해** 선택: 현재 상태에서 부분 문제의 최적 해를 구한뒤, 이를 부분해 집합에 추가한다.

2) 실행 가능성 검사:

3) 해 검사: 전체 문제의 해가 완성되지 않으면 1부터 다시 시작



```python
'''
https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PsIl6AXIDFAUq&categoryId=AV5PsIl6AXIDFAUq&categoryType=CODE
1970. 쉬운 거스름돈
2
32850
160
money = {50000 : 0, 10000 : 0, 5000 : 0, 1000 : 0, 500 : 0, 100 : 0, 50 : 0, 10 : 0}
10 <= N <= 1000000
N[-1] == 0
32850
0 3 0 2 1 3 1 0
나누기 /
몫 //
나머지 %
'''

for T in range(int(input())):
    money_input = int(input())
    money_dict = {
        50000: 0,
        10000: 0,
        5000: 0,
        1000: 0,
        500: 0,
        100: 0,
        50: 0,
        10: 0,
    }

    # 50000/돈 나누면, 50000//돈 몫 50000%돈 나머지가 나오고,
    for money, count in money_dict.items():
        change = money_input // money # 몫은 해당 원 단위의 거스름돈 개수이며,
        remainder = money_input % money # 나머지는 다음 원 단위로 다시 나눠야할 돈이된다.
        money_input = remainder # 그 나머지를 순환시키기 위해서 처음 받은 돈을 넣었던 매개변수에 할당한다.
        money_dict[money] = change

    print(f'#{T+1} ')
    for count in money_dict.values():
        print(f'{count}', end=' ')
    print()
```



counts배열의 각 원소를 체크, run과 triplet 및 baby-gin 여부를 판단![1564377386338](C:\Users\student\AppData\Roaming\Typora\typora-user-images\1564377386338.png)

```python
num = 456789
c = [0] * 12 # 6자리 수로 부터 각 자리 수를 추출하여 개수를 누적할 리스트

for i in range(6):
    c[num% 10] += 1
    num //= 10

i = 0
tri = run = 0

'''
triplet이 항상 먼저 조사 되어야 한다.
'''

while i < 10: 
    if c[i] >= 3: # triplet 조사 후 데이터 삭제
        c[i] -= 3
        tri += 1
        continue # 다시 while문으로 들어간다.
    if c[i] >= 1 and c[i+1] >= 1 and c[i+2] >= 1 : # run 조사
        c[i] -= 1
        c[i+1] -= 1
        c[i+2] -= 1
        run += 1
        continue
    i += 1

if run + tri == 2:
    print("Baby Gin")

else:
    print("Lose")
```



이처럼 프로그래밍이란 검색이다.

그래서 기본적으로 **정렬**을 해서 데이터를 사용



1. 큰 값, 내림차순
2. 키



[정렬 방식 종류](http://blog.naver.com/PostView.nhn?blogId=javaking75&logNo=220787766629&parentCategoryNo=&categoryNo=87&viewDate=&isShowPopularPosts=false&from=postView)

[정렬 알고리즘](https://www.fun-coding.org/DS&AL4-4.html)

[정렬 알고리즘](http://blog.naver.com/PostView.nhn?blogId=redwave102&logNo=80076259189)

[정렬 알고리즘, 쉬운 설명](https://bowbowbow.tistory.com/8)

1. **버블** 정렬
2. 카운팅 정렬
3. **선택** 정렬
4. 퀵 정렬
5. **삽입** 정렬
6. 병합 정렬



버블, 선택, 삽입 O(n**2)  64 * 64

퀵, 병합, 힙 O(n log n) 64 * 6정도 돈다.

카운팅 O(n)





- 버블 정렬 
  
  ![img](http://postfiles10.naver.net/20160815_265/javaking75_1471196569421uE8k0_PNG/draw.io_%B9%F6%BA%ED%C1%A4%B7%C4.png?type=w773)
  
  - 인접한 두 개의 원소를 비교하며 자리를 계속 교환하는 방식
  - 과정

1. 첫 번째 원소부터 인접한 원소끼리 계속 자리를 교환하면서 맨 마지막 자리까지 이동

2. 한 단계가 끝나면 가장 큰 원소가 마지막 자리로 정렬

   - 시간 복잡도 O(n**2)

```python
a = [20, 40, 10, 30]

for i in range(0, 5): # i값이 0부터 1씩 증가, 4가 될 때까지 반복
    for j in range(0, 5 - i): # j값이 0부터 1씩 증가, 5-i-1이 될때까지 반복
        if a[j] > a[j+1]: # a[j]가 a[j+1]보다 크면,
            temp = a[j] # a[j]와 a[j+1]을 교환
            a[j] = a[j+1]
            a[j+1] = temp

print(a)

>> [10, 20, 30, 40, 50, 60]
```

```python
def BubbleSort(a): # 정렬할 리스트
    for i in range(len(a)-1, 0, -1): # 범위의 끝 위치
        for j in range(0, i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
```



- 카운팅 정렬 (구현하고 이해하기)

  - 항목들의 순서를 결정하기 위해 집합에 각 항목이 몇 개씩 있는지 세는 작업을 하여, 선형 시간에 정렬하는 효율적인 알고리즘

  - 제한 사항: 

    정수나 정수로 표현할 수 있는 자료에만 적용(discontinuous한 값이 들어와야 한다.)
    
    1-4, 9-27 처럼 범위가 설정 되어야 한다. = 집합 내의 가장 큰 정수를 알아야 한다.
    
  - 시간 복잡도: O(n+k) n은 리스트 길이, k는 정수의 최대값
  
  - 과정
  
  1. Data에 각 항목들의 발생회수를 세고, 정수 항목들로 직접 인덱스 되는 카운트 배열 counts에 저장한다.

```python

def CountingSort(A, B, k):
    
   C = [0] * k
for i in range(0. len(B)):
    C[A[i]] += 1

for i in range(1, len(C)):
    C[i] += C[i-1]
    
for i in range(len(B)-1, -1, -1):
    B[C[A[i]]-1] = A[i]
    C[A[i]] -= -1
```



