# 프론트엔드에서 TDD가 가능하다는 것을 보여드립니다

[영상 링크](https://www.youtube.com/watch?v=L1dtkLeIz-M) [영상 리뷰 컬럼 링크](https://velog.io/@muchogusto/FeConf2020-%EB%A6%AC%EB%B7%B0-%ED%94%84%EB%A1%A0%ED%8A%B8%EC%97%94%EB%93%9C%EC%97%90%EC%84%9C-TDD%EA%B0%80-%EA%B0%80%EB%8A%A5%ED%95%98%EB%8B%A4%EB%8A%94-%EA%B2%83%EC%9D%84-%EB%B3%B4%EC%97%AC%EB%93%9C%EB%A6%BD%EB%8B%88%EB%8B%A4)

참고할 만한 다른 링크들을 가져오겠다 [Vue3 에서 테스트](https://v3.vuejs.org/guide/testing.html) [Vue2에서 단위 테스트](https://kr.vuejs.org/v2/guide/unit-testing.html)

## TDD

- Test Driven Development
- 클린코드의 궁극적인 목표를 이루는 좋은 도구이다
- 하지만 어렵다! 왜?
  - 프론트엔드단은 코드 자체가 testable하지 않기 때문이다.
  - 즉, 우리는 코드를 test가능하게 짜야한다
  - 그렇다면 그것은 어떻게 짜는가?
    - 관심사의 분리! (클린 아키텍처와 클린 코드에 나온다)
    - 각 개별 요소는 개별 관심사만 다룰 것
    - 관심사의 분리가 제대로 이루어지지 않으면! 망한다 진짜로

## Redux

- 왜써요?
  - 상태관리 때문에 쓴다
  - 하지만 이 영상에서는 **react의 관심사 분리** 때문에 쓴다고 한다
- React의 관심사
  - react는 상태의 반영에 관심이 있다
  - ***상태 관리에는 관심이 없다!***

## 결론

즉, 우리가 테스트하지 못하는 것은 testable하게 짜지 못해서이다! 테스트를 가능하게 짤 수 있도록 노력해보자!