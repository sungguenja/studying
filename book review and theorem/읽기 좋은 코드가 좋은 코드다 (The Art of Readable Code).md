# 읽기 좋은 코드가 좋은 코드다 (The Art of Readable Code)

> 목차
>
> 1. 표면적 수준에서의 개선
> 2. 루프와 논리를 단순화하기
> 3. 코드 재작성하기
> 4. 선택된 주제들
> 5. 내 후기

## 1. 표면적 수준에서의 개선

자주쓰이는 명칭은 피하자. for문에서 i,j,k부터 temp등 의미가 있도록 최대한 만들어라. getTodo같은 것도 좋다고 말할 수가 없다 메소드가 들어가 있어서 Todo를 얻는다는 것인지 get요청과 관련된 것인지 정확히 이해하기가 힘들다

변수 함수등 이름을 보면 무엇인지 어떤 행동을 하는지 알 수 있도록 이름을 정하자.

단어 완성 기능 단축어를 자주 이용하자

| 문서 편집기 | 명령어                |
| ----------- | --------------------- |
| Vi          | Ctrl + p              |
| emacs       | Meta + / (다음에 esc) |
| 이클립스    | Alt + /               |
| 인텔리제이  | Alt + /               |
| TextMate    | esc                   |

축약어는 좋은 아이디어가 아니다.

부정적인 단어는 피하는 것이 좋다. 햇갈림을 유도하기 때문이다.

미학적인 측면도 중요하다 다음과 같은 세가지 원리를 생각하자

- 코드를 읽는 사람이 이미 친숙한, 일관성 있는 레이아웃을 사용하라
- 비슷한 코드는 서로 비슷해 보이게 만들어라
- 서로 연관된 코드는 하나의 블록으로 묶어라

위 세가지를 지키기 위해 다음과 같은 것을 이용할 수 있다.

1. 일관성과 간결성을 위해서 줄 바꿈을 재정렬하기

   - 다음과 같은 코드 둘을 비교하면 아래가 좀 더 이해하기 쉽다는 것을 알 수가 있다. 클래스 안의 형태가 계속 반복된다고 생각해봐라

     ```java
     public class PerformanceTester {
         public static final TcpConnectionSimulator wifi = new TcpConnectionSimulator(
         500, /* kbps */
         80, /* millisecs 대기시간 */
         200, /* 흔들림 */
         1 /* 패킷 손실 % */);
         
         .....
     }
     ```

     ```java
     public class PerformanceTester {
         public static final TcpConnectionSimulator wifi = 
             new TcpConnectionSimulator(
         		500, /* kbps */
         		80, /* millisecs 대기시간 */
         		200, /* 흔들림 */
         		1 /* 패킷 손실 % */);
         
         .....
     }
     ```

2. 메소드를 활용하여 불규칙성을 정리하라

3. 도움이 된다면 코드의 열을 맞춰라.

   - 코드의 열을 맞춘다면 오타 또는 이탈자를 쉽게 찾는 것도 좋으며 함수에 어떤 변수가 들어갔는지 이해하기가 쉽다

4. 의미 있는 순서를 선택하고 일관성 있게 사용하라

   - 뭔가 순서있게 변수를 정했고 아래에서 그것들을 써야한다면 아래에서도 순서대로 이용할 수 있도록 하자

5. 선언문을 블록으로 구성하라

   - 논리적 영역으로 나누는 것이 좋다

     ```java
     class FrontendServer {
         public:
          FrontendServer();
         ~FrontendServer();
         
         // 핸들러들
         void 핸들러;
         ...
             
         // 유틸리티
             
         // 데이터 베이스 헬퍼들
     }
     ```

6. 코드를 문단으로 쪼개라

   - 논리적 순서대로 주석과 글 간격을 두는 것이 좋다는 이야기다

     ```python
     def suggest_new_friends(user,email_password):
         # 사용자 친구들의 이메일 주소를 읽는다.
         friends = user.friends()
         friend_emails = set(f.email for f in friends)
         
         # 이 사용자의 이메일 계정으로부터 모든 이메일 주소를 읽어들인다.
         함수 사용
         
         # 아직...
     ```

     위와 같이 나눠두면 읽기 편하다

7. 개인적인 스타일 대 일관성

주석에 담아야하는 대상! 아래와 같은 주석은 가치가 정말 없다!

```java
// 클래스 Account를 위한 정의
class Account {
    public:
    //생성자
    Account();
    
    // profit에 새로운 값을 설정
    void SetProfit(double profit);
    
    // 이 어카운트의 profit을 반환
    double GetProfit();
}
```

즉, 코드에서 유추할 수 있는 내용은 주석으로 달지 않는 것이다.