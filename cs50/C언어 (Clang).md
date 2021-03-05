# C언어 Clang

> 1. C 기초
> 2. 문자열
> 3. 조건문과 루프
> 4. 자료형, 형식 지정자, 연산자
> 5. 사용자 정의 함수, 중첩루프
> 6. 하드웨어의 한계

# 1. C 기초

```c
#include <stdio.h>

int main(void)
{
    printf("hello, world\n");
}
```

`#include` 이것은 무슨 의미인가? `stdio.h`에 접근해서 함수를 쓴다는 이야기이다! (그러면 패키지를 설치하면 여기서 부르면 된다고 예상이 된다.)

언제나 생각하자 프로그래밍 언어는 정말 자신이 시킨 것만 한다. `\n`이 없다면 `hello, world$` 이런 식으로 출력이 될 것이다

실행을 시킬 때 `$ clang hello.c`이런 식으로 실행시킬 것이다 그러면 a.out이 나오는데 다른식으로 a.out이 아니라 다르게 만들고 싶다면?

```bash
$ clang -o hello hello.c
```

위와 같은 식으로 입력하면 hello라는 파일이 나온다

# 2. 문자열

```c
#include <cs50.h>
#include <stdio.h>

int main(void)
{
    string answer = get_string("what's your name?\n");
    printf("hello, %s\n", answer);
}
```

```bash
$ make getstring
```

`clang -o getstring getstring.c` 이렇게 써도 되지만 더 빠르게 짧게 하고 싶으면 위에처럼 하면 된다. 위의 소스코드는 cs50 sandbox에서 실행되는 코드이다. 실제로는 cs50.h를 안부르고 get_string대신 scanf를 이용할 수가 있다.

# 3. 조건문과 루프

C에서의 루프와 조건들은 다음과 같다

```c
if(x < y) 
{
    printf("dd");
}
else if (x == y)
{
    printf("ss");
}
else
{
    printf('sss');
}
```

```c
int i = 0;
while (i < 50)
{
    printf("ddd");
    i++;
}
```

```c
for (int i = 0; i<50; i += 1)
{
    printf("asdasd")
}
```

# 4. 자료형, 형식 지정자, 연산자

**데이터 타입**

아래 목록은 변수의 데이터 타입으로 사용할 수 있는 것들입니다.

- bool: 불리언 표현, (예) True, False, 1, 0, yes, no
- char: 문자 하나 (예) 'a', 'Z', '?'
- string: 문자열
- int: 특정 크기 또는 특정 비트까지의 정수 (예) 5, 28, -3, 0
- long: 더 큰 크기의 정수
- float: 부동소수점을 갖는 실수 (예) 3.14, 0.0, -28.56
- double: 부동소수점을 포함한 더 큰 실수


\* int는 대략 40억까지 셀 수 있기 때문에 40억게 이상의 데이터를 가진 일부 거대 기업과 같은 상황이 아닌 일반 사용자들은 대부분 정수에 int를 사용합니다.

**CS50 라이브러리 내의 get 함수**

CS50 라이브러리는 위와 같은 데이터 타입을 입력값으로 받을 수 있는 아래와 같은 함수들을 포함합니다.

(CS50 라이브러리에서 사용되는 함수이기 때문에 가볍게 알고 가시면 됩니다.)

- get_char
- get_double
- get_float
- get_int
- get_long
- get_string

**형식 지정자**

printf 함수에서는 각 데이터 타입을 위한 형식 지정자를 사용할 수 있습니다.

지난 강의에서 문자열(string)인 answer 변수의 인자를 **%s**로 불러온 것을 기억하시나요?

이번에는 여러가지 데이터 타입 마다 사용되는 형식 지정자를 알아보도록 하겠습니다.

- **%c** : char
- **%f** : float, double
- **%i** : int
- **%li** : long
- **%s** : string

**기타 연산자 및 주석**

그 외에도 아래 목록과 같이 다양한 수학 연산자, 논리 연산자, 주석 등이 기호로 정의되어 있습니다.

- +: 더하기
- -: 빼기
- *: 곱하기
- /: 나누기
- %: 나머지
- &&: 그리고
- ||: 또는
- //: 주석

# 5. 사용자 정의 함수, 중첩 루프

그냥 이건 아는대로 하면 된다....

# 6.하드웨어의 한계

