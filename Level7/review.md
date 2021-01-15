## 함수
- 값을 입력받아 특정 연산을 수행하여 결과를 반환
- 스코프는 함수간 작업의 완벽한 분담을 위해 존재함. (함수 서로 연관성x)

# 재귀함수
- 자기 자신을 부르는 함수
- ex)Factorial(n)
```
//getFactorail : n!을 반환하는 함수
int getFactorial(int n){
  if(n==0)
    return 1;
  else
    return n * getFactorial(n-1);
}

int main(){

  int n;
  scanf("%d",&n);
  printf("%d\n",getFactorial(n));
}

```
* 재귀함수의 의미는 무엇인가? 도대체 이걸 왜 쓰나?
* 재귀함수를 만들기 위해서는 어떤 절차를 따라야 하나?
  * 귀납적 계산 방법(귀납적 문제해결 방법)
    * 구하려고 하는 값을 f(x) 라고 하자
    * f(x)를 구하기 위하여 또 다시 f(x)를 활용한다
    * n! = 1 * 2 ...*n (순차적 x 이 방법은 잘못됨)
    * n! = n *(n-1)! 
    * 식 정의, 멈추라는 신호 정의 필요(ex) f(0)=1 
    
    
    - 귀납적 계산법 내의 가정 관
