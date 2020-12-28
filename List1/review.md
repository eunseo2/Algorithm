# 표준 입력 예제
```
a=input()                               줄바꿈 전까지 문자열로 입력 받음
a = int(input())                        정수형 변수 1개 입력 받는 예제
b, c = map(int, input().split())        정수형 변수 2개 입력 받는 예제 
d = float(input())                      실수형 변수 1개 입력 받는 예제
e, f, g = map(float, input().split())   실수형 변수 3개 입력 받는 예제
h = input()                             문자열 변수 1개 입력 받는 예제
```


# 표준 출력 예제
```
a, b = 6, 3
c, d, e = 1.0, 2.5, 3.4
f = "ABC"
print(a)                                정수형 변수 1개 출력하는 예제
print(b, end = " ")                     줄바꿈 하지 않고 정수형 변수와 공백을 출력하는 예제
print(c, d, e)                          실수형 변수 3개 출력하는 예제
print(f)                                문자열 1개 출력하는 예제
```


# 리스트에 map 사용하기
```
  >>> a = map(int, input().split()) 
  10 20 (입력)
  >>> a
  <map object at 0x03DFB0D0>
  >>> list(a)
  [10, 20]

```

# 정렬
```
a=['a','b']
원본 변경 x  new_list = sorted(a)
내림차순 new_list = sorted(a, reverse=True)
오름차순 new_list = sorted(a, reverse=False)
원본도 변경 a.sort()
내림차순 a.sort(reverse= True)

```

# count함수
a.count하면 그 문자열,리스트에 몇개 있는지 알려줌...!!!!! 대박 !!!

