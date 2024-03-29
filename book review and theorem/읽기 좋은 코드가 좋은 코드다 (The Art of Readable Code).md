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

즉, 코드에서 유추할 수 있는 내용은 주석으로 달지 않는 것이다. 아래와 같은 경우도 함수 이름으로 어떤 함수인지 알 수 있기 때문에 어떤 역할을 하는 함수인지 보단 세부사항을 적어두는 것이 좋다

```java
// 주어진 'name'으로 노드를 찾거나 아니면 NULL을 반환한다.
// 만약 depth <= 0 이면 subtree만 검색된다
// 만약 depth == N 이면 N 레벨과 그 아래만 검색된다.
Node* FindNodeInSubtree(Node* subtree, string name, int depth);
```

반대로 나쁜이름에 주석을 달지 말고 나쁜이름을 교정하는 것이 더 옳은 방식이다!

주석은 새 팀원을 위해서도 필요하다. 그러니 팀원이 새로 돌아온다면 다음과 같은 주석도 필요하다

1. 나올 것 같은 질문 예측하기
2. 큰 그림에 대한 주석

명확하고 간결한 주석은 중요하다. 다음과 같은 경우를 보자

```c++
// int는 CategoryType이다.
// 내부 페어의 첫 번째 float는 'score'다.
// 두 번째는 'weight'다.
typedef hash_map<int, pair<float,float> > ScoreMap;
```

위와 같이 굳이 주석에 세줄이나 이용할 필요가 없다. 읽기 귀찮아지기 까지 하니 다음과 같이 간단하게 나타내는 것이 최적이라고 생각한다.

```c++
// CategoryType -> (score, weight)
typedef hash_map<int, pair<float,float> > ScoreMap;
```

위와 같이 하는것은 좋은 아이디어이다.

모호한 대명사는 피하는 것이 좋다. 1루수가 누구야를 생각해봐라. 대명사로 인해 괜히 햇갈리는 상황이 오니 대명사는 피하고 명확하게 표현하는 것이 최대한 좋다. 또한 엉터리 문장도 정리해라. 그리고 함수의 동작을 명확하게 설명하는 것이 좋다. 어떠한 원리로 작동하는지 그것을 명확하게 하는 것이 좋다. `이 파일에 담긴 줄 수를 반환 한다` **VS** `파일 안에 새 줄을 나타내는 바이트('\n')가 몇개있는지 센다` 어떤 것이 더 명확한지 생각해보도록

코너케이스를 설명해주는 입/출력 예를 사용하라

함수를 사용할 때 변수에 대해 확정적으로 써주는 것이 조금 좋다. 근데 이것은 파이썬에서만 가능하다 다음과 같은 코드를 보자

```python
def Connect(timeout,use_encryption):
    .....
    
Connect(timeout=10,use_encryption=False)
```

파이썬은 이런 방식이 가능한데 다른 언어는 불가능하다! 그런데 이게 되게 명확해서 좋아보인다! 어떻게 이용할 수가 있을까? 주석의 힘이 있다 다음과 같이 사용해보자

```java
void Connect(int timeout, bool use_encryption) {
    ....
}

Connect(/* timeout = */ 10, /* use_encryption = */ false);
```



## 2. 루프와 논리를 단순화하기

기본적인 if문을 생각해보자 우리는 `if length >= 10` 과 `if 10 <= length` 둘 중 왼쪽이 더 편하다는 것을 본능적으로 느낀다.~~프로그래머의 본능인가?~~ 그런데 만약 왼쪽과 오른쪽 둘 다 변수라면? 기본적인 느낌은 다음과 같이 생각해도 될 것이다

- 왼쪽    : `값이 더 유동적이고` **`질문을 받는`** `표현`
- 오른쪽: `더 고정적인 값으로, 비교대상으로 사용되는 표현`

if/else의 경우에는 부정을 앞에 오게 할지 긍정을 앞에 오게 할 지는 다음과 같은 조건을 생각하자

1. 부정이 아닌 긍정을 다루어라. 즉, `if(!false)` 보단 `if(true)`를 선호하자
2. 간단한 것을 먼저 처리하라. 이렇게 하면 동시에 같은 화면에 if와 else 구문을 나타낼 수도 있다. 두 개의 주문을 동시에 보는 게 좋다
3. 더 흥미롭고, 확실한 것을 다루어라

if안에는 메소드를 넣지 마라 다음 코드에서 위에보다 아래가 더 직관적인 것을 알 수 있다. 

```python
if request.user.id == document.owner_id:
    .....

user_id = request.user.id
if user_id == document.owner_id:
    .....

# 3번째 코드 처럼 직관성이 더 좋다면 아래와 같이 진행해도 괜찮다
user_owns_document = request.user.id == document.owner_id
if user_owns_document:
    ....
```

[드모르간의 법칙](https://ko.wikipedia.org/wiki/%EB%93%9C_%EB%AA%A8%EB%A5%B4%EA%B0%84%EC%9D%98_%EB%B2%95%EC%B9%99)을 이용하는 것도 아주 좋은 방안이다

자주 사용되는 문자열은 변수로 등록해두는 것이 좋다 아래코드에서 윗단락보단 아래 단락이 더 읽기 편하다는 것을 직관적으로 알 수 있다

```javascript
var update_highlight = function (message_num) {
    if ($("#vote_value" + message_num).html() === "Up") {
        $("#thumbs_up" + message_num).addClass("highlighted");
        $("#thumbs_down" + message_num).removeClass("highlighted");
    } else if ($("#vote_value" + message_num).html() === "Down") {
        $("#thumbs_up" + message_num).removeClass("highlighted");
        $("#thumbs_down" + message_num).addClass("highlighted");
    } else {
        $("#thumbs_up" + message_num).removeClass("highlighted");
        $("#thumbs_down" + message_num).removeClass("highlighted");
    }
}

var update_highlight = function (message_num) {
    var thumbs_up = $("#thumbs_up" + message_num)
    var thumbs_down = $("#thumbs_down" + message_num)
    var vote_value = $("#vote_value" + message_num).html()
    var hi = "highlighted"
    
    if (vote_value === "Up") {
        thumbs_up.addClass("highlighted");
        thumbs_down.removeClass("highlighted");
    } else if (vote_value === "Down") {
        thumbs_up.removeClass("highlighted");
        thumbs_down.addClass("highlighted");
    } else {
        thumbs_up.removeClass("highlighted");
        thumbs_down.removeClass("highlighted");
    }
}
```

값을 한 번만 할당하는 변수를 선호하라

무슨 말이냐. 값이 변하지 않는 **상수**들을 지정해두라는 소리이다. 아래와 같이

```java
static const int NUM_THREADS = 10;
```

첫째로 코드를 읽는 사람은 상수 이름으로 이 코드를 쉽게 이해할 수가 있다. 두번째로 해당 값이 들어간 모든 값을 수정해야할 때 이렇게 지정을 해두면 우리는 저 코드만 수정을 하면 되는 것이다.

- 종합적으로 정리해보자

  ```html
  <input type="text" id="input1" value="Dustin">
  <input type="text" id="input2" value="Trevor">
  <input type="text" id="input3">
  <input type="text" id="input4" value="Melissa">
  ```

  우리는 여기서 이제 함수를 만들어보자. 함수는 변경된 DOM요소를 또는 비어있는 unoyt이 없으면 null을 반환하도록 하자. 그러면 무지성 코드는 다음과 같을 수가 있을 것이다.

  ```javascript
  var setFirstEmptyInput = function (new_value) {
      var found = false;
      var i = 1;
      var elem = document.getElementById('intput' + i);
      while (elem != null) {
          if (elem.value === '') {
              found = true;
              break;
          }
          i++;
          elem = document.getElementById('input'+i);
      }
      if (found) {elem.value = new_value;}
      return elem;
  }
  ```

  위 코드는 수행은 하지만 보기 좋지가 않다. `found`,`i`,`elem` 이것들이 계속해서 변경되며 혼란스럽게 만든다. 거기다 함수라면 굳이 break를 이용하지 않고 바로 끝낼 수가 있다. 그렇다면 일단 이 부분부터 수정해보도록 하자.

  ```javascript
  var setFirstEmptyInput = function (new_value) {
      var i = 1;
      var elem = document.getElementById('intput' + i);
      while (elem != null) {
          if (elem.value === '') {
              elem.value = new_value;
              return elem;
          }
          i++;
          elem = document.getElementById('input'+i);
      }
      return null;
  }
  ```

  함수가 끝나는 경우에 바로 끝낼 수 있게 해줘서 햇갈리지 않고 꽤 괜찮다. 하지만 while은 우리의 코드를 조금 햇갈리게 하는 감이 있다. 보통은 while문보다는 for문이 조금 더 가독성이 좋다 그러니 다음과 같이 수정해보도록 하자

  ```javascript
  var setFirestEmptyInput = function (new_value) {
      for (var i = 0; true; i++) {
          var elem = document.getElementById('intput' + i);
          if (elem === null) {
              return null;
          }
          
          if (elem.value === '') {
              elem.value = new_value;
              return elem;
          }
      }
  }
  ```

  코드도 압축이 되고 가독성도 더 좋아졌다고 볼 수가 있다. 어떠한 조건에서 어떤 값이 필요한지 한눈에 들어오기 때문에 매우 편해졌다! 주석까지 더 적절히 단다면 거의 완벽하다고 할 수가 있을 것이다!

요약 해보자

1. 방해되는 **변수를 제거**하라. 결과를 즉시 처리하는 방식으로 '증간 결과값'을 저장하는 변수를 제거하는 몇 가지 예를 살펴보았다.
2. **각 변수의 범위를 최대한 작게 줄여라** 각 변수의 위치를 옮겨서 변수가 나타나는 줄의 수를 최소화하라. 눈에 보이지 않으면 마음에서 멀어지는 버이다.
3. **값이 한 번만 할당되는 변수를 선호하라** 값이 한 번만 할당되는 변수는 훨씬 이해하기 쉽다.

## 3. 코드 재작성하기

상관이 없는 하위문제는 적극적으로 추출해야 한다. 큰 흐름과 관계가 적은 하위문제를 해결하는 코드는 코드의 가독성을 떨어뜨린다.

1. 주어진 함수나 코드 블록을 보고, 스스로에게 질문하라 "상위수준에서 보 이 코드의 목적은 무엇이가?"
2. 코드의 모든 줄에 질문을 더져라 "이 코드는 직접적으로 목적을 위해서 존재하는가? 혹은 목적을 위해서 필요하긴 하지만 목적 자체와 직접적으로 상관없는 하위문제를 해결하는가?"
3. 만약 상당히 원래의 목적과 직접적으로 관련되지 않은 하위무제를 해결하느 코드 분량이 많으면, 이를 추출해서 별도의 함수로 만든다

다음과 같은 예를 보자

```python
def findClosesteLocation(lat,lng,array):
    closest_dist = sys.maxsize
    closest = -1
    for i in range(len(array)):
        lat_rad = lat
        lng_rad = lng
        lat2_rad = array[i].latitude
        lng2_rad = array[i].longitude
        dis = cos(sin(lat_rad)*sin(lat2_rad)+cos(lat_rad)*cos(lat2_rad)*cos(lng2_rad-lng_rad))
        if dist < closest_dist:
            closest_dists = dist
            closest = arraay[i]
            
    return closest
```

위 코드는 가장 가까운 거리를 구하는 역할을 하긴 할 것이다. 그런데 for문에서 하는 거리를 구하는 것은 직접적으로 목적을 위해 존재하는 것은 안니다 즉, 해당 부분은 따로 함수로 추출하는 것이 더 가독성이 좋을것이다!

한 번에 하나씩 처리하는 코드도 중요하다

한번에 여러가지 일을 처리하는 함수는 이해하기가 어렵다 코테를 진행해보면 많이 경험해봤을 것이다. 예를 들어 추천 반대 시스템을 만든다고 해보자. 그러면 우리는 경우가 의외로 다양하다는 것을 깨달을 것이다. 전의 추천이 찬,반,무 그리고 지금 추천이 찬,반,무인지 대충 생각해도 9개의 경우가 나온다

하지만 약간 뒤집어서 생각하자. 옛 추천과 지금 추천으 수치값으로 해석되고 점수가 변경된다. 그렇다면 추천수를 보여주는 시스템은 복잡하게 하지 않고 함수를 보여주면 될 것이다.

```javascript
var vote_value = function (vote) {
    if (vote === 'Up') {
        return +1;
    }
    if (vote === 'Down') {
        return -1;
    }
    return 0;
}

var vote_changed = function (old_vote,new_vote) {
    var score = get_score();
    
    score -= vote_value(old_vote); // 옛 점수 제거
    socre += vote_value(new_vote); // 새 점수 더함
    
    set_score(score);
}
```

매우 간단하게 된다!

생각을 코드로 만들어라. 다음과 같은 과정을 가지고 코딩한ㄴ다고 생각을 해라

1. 코드가 할 일을 옆의 동료에게 말하듯이 평범한 영어로 묘사하라
2. 이 설명에 들어가느 핵심적인 단어와 문구를 포착하라
3. 설명과 부합한느 코드를 닥성하라

```php
$is_admin = is_admin_request();
if ($document) {
    if (!$is_admin && ($document['username'] != $_SESSION['username'])) {
        return not_authorized();
    }
} else {
    if (!$is_admin) {
        return not_auathorized();
    }
}
```

이 코드의 문제는 일단 커다란 논리의 트리는 이해하기 어렵다. 이 코드에 있는 논리를 단순화할 수 있을 것이다. 어떻게 해야할까? 다음과 같이 생각해보자

1. 관리자다
2. 만약 문서가 있다면 혀재 뭇서를 소유하고 있다.

이 두가지가 허락되는 케이스이다. 그렇다면 다음과 같이 바꿀 수가 있을 것이댜

```php
if (is_admin_reauest()) {
    // 허가
} elseif ($document && ($document['username'] == $_SESSION['username'])) {
    // 허가
} else {
    // 허가 하지 않음
}
```

이렇듯 코드를 짤 때는 생각의 순서를 정하고 간단하게 할 필요가 있다

코드의 분량을 줄일려고 노력하자

~~가장 읽기 쉬운 코드는 아무 것도 없는 것이다.~~ 장난이 아니긴 하다. 어떠한 긴능을 굳이 구현할 필요가 없다면 구현을 하지 말아야 한다. 우리는 요구사항에 질문을 던지고 그 질문을 잘게 나누어 분석하고 구현하면 된다.

## 4. 선택된 주제들

어.... 테스트 코드에 대한 말이 위주여서 그냥 읽으면서 봄

## 5. 후기

클린코드랑 비슷한 면이 있지만 자바 전용인 클린코드와는 달리 다양한 언어에 대해 다룸. 넓은 범위에서 크게 보자고 하면 이 책 괜찮은듯 합니다. 제대로 정독은 지금이서야 마무리 하지만 계속 두고 읽어볼 만 할 듯합니다.

클린 코드도 읽다 말았는데 클린 코드랑 클린 아키텍쳐도 한번 정주행 제대로 하고 후기 올릴 수 있도록 해야겠다.