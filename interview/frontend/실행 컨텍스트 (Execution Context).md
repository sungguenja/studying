# 실행 컨텍스트 (Execution Context)

종류가 세가지이다.

1. Global execution context

   전역 실행 컨텍스트. 무조건 한개만 존재가 가능하다. 왜냐하면 싱글 스레드 언어이기 때문이다. 

2. Functional execution context

   함수 단위로 생성되는 함수 실행 컨텍스트. 호출되는 함수에 대해서 생성되는 실행 컨텍스트라고 이해해도 된다. 함수가 필요한 변수들이 있는 곳.

3. Eval

   `eval` 함수를 이행할때 생성되는 컨택스트인데 이것은 좀 특이한 케이스

```javascript
var a = 10;

function functionA() {
    console.log("start function A",this);
    
    function functionB() {
        console.log("In function B",this);
    }
    
    functionB();
}

functionA();
```

순서를 생각해보자

1. 일단 전역 실행 컨텍스트가 쌓인다.
2. functionA를 호출
3. 호출의 결과로 functionA에 대한 함수 실행 컨텍스트가 생성
4. `console.log("start function A")`
5. functionA내부의 functionB호출
6. `console.log("In function B")`
7. functionB 실행 컨텍스트가 생성
8. functionB 컨텍스트 해체
9. functionA 컨텍스트 해체
10. 전역컨텍스트 해체

전반적으로 콜 스택을 생각해도 된다.