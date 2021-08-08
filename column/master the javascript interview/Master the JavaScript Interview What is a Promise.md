# Master the JavaScript Interview: What is a Promise?

[칼럼 링크](https://medium.com/javascript-scene/master-the-javascript-interview-what-is-a-promise-27fc71e77261)

## 프라미스가 먼데?  ~~씹덕아~~

프라미스는 3가지 가능한 상태 중 하나이다. fulfilled, rejected, pending. 프라미스 유저들은 fulfilled한 밸류 또는 rejection의 이유를 조절하기 위해 콜백에 접근할 수 있다.

## 프라미스는 어떻게 작동하는가?

- Fulfilled: `onFulfilled()`로 부른다 (`resolve()`로도 부름)
- Rejected: `onRejected()`로 부른다 (`reject()`로도 부름)
- Pending: 위 두 상황이 아직 안왔음

네이티브 자바스크립트 프라미스는 프라미스 상태를 expose하지 않는다. 대신에 당신은 블랙박스로써 프라미스를 다루길 기대할 것이다. 프라미스를 만들기 위한 함수를 사용하려면 프라미스 상태에 대한 지식을 가지고 있어야 한다.

##  중요한 프라미스 룰

- 프라미스는 스텐다드 컴리언트한 `.then()`메소드를 공급하는 객체이다
- pending 프라미스는 fulfilled또는 reject 상태로 바뀐다
- fulfilled또는 rejected 프라미스는 정착되고 나면 다른 상태로 바뀔 수 없다
- 프라미스가 한번 정착된다면 값을 가질 수 밖에 없다. 그리고 바뀌지 않는다

이것이 프라미스의 큰 틀이고 아래는 `.then()`에 대한 규칙들이다

- `onFulfilled()`와 `onRejected()`는 선택적이다
- 공급된 인수들이 함수가 아니라면 무시된다
- `onFulfilled()`는 프라미스가 fulfilled된 후에 프라미스의 값의 첫번째 인자와 함께 호출된다.
- `onRejected()`도 마찬가지이다. 에러 객체를 이용해서 reject하는 것을 추천한다
- `.then()`도 새 프라미스 객체를 리턴한다

## 프라미스 체이닝

프라미스는 `.then()`을 계속해서 체이닝 하는 것이 가능하다.

## 에러 핸들링

결과값을 조절하는게 `.then()`이면 에러를 핸들링 하는 것은 `.catch()`가 있다. 에러종류를 받아서 에러에 대해서 핸들링이 가능하다