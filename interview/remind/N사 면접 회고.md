# N사 면접 회고

1. reflow, repaint

   랜더 트리를 구성하고 난 이후에 dom요소에 영향을 미치면 reflow가 일어난다. 그리고 reflow에 의해서 repaint가 일어나는데 repaint는 reflow없이도 발생할 수가 있다. css조작이 dom을 조작할 정도가 아니면 repaint만 일어난다

2. csr, ssr

   [참고자료](https://velog.io/@ru_bryunak/SPA-%EC%82%AC%EC%9A%A9%EC%97%90%EC%84%9C%EC%9D%98-SSR%EA%B3%BC-CSR)

   csr 클라이언트 사이드 랜더링: 클라이언트에서 랜더링이 일어나는 방식

   ssr 서버 사이드 랜더링: 서버에서 랜더링이 일어나는 방식이다

3. http

   [공식 문서](https://developer.mozilla.org/ko/docs/Web/HTTP/Overview)

4. 핸드쉐이킹

   [참고자료](https://mindnet.tistory.com/entry/%EB%84%A4%ED%8A%B8%EC%9B%8C%ED%81%AC-%EC%89%BD%EA%B2%8C-%EC%9D%B4%ED%95%B4%ED%95%98%EA%B8%B0-22%ED%8E%B8-TCP-3-WayHandshake-4-WayHandshake)

   아 반대로 말했네 ㅋㅋㅋㅋㅋ

5. 로컬스토리지, 세션스토리지

   [참고자료](https://www.zerocho.com/category/HTML&DOM/post/5918515b1ed39f00182d3048)

   로컬과 세션의 가장 큰 차이: 영구성, 로컬은 영구적이고 세션은 탭을 닫으면 제거된다

   용량 차이도 존재

6. event validation

   뭔데 이거?

7. 자바스크립트 primitive, object

   [참고자료](https://ddalpange.github.io/2017/10/03/js-immutable-mutable/)

   [참고자료2](https://developer.mozilla.org/ko/docs/Glossary/Primitive)

   그냥 일반적인 타입이었다. 시바 어려운게 아니었는데 자살각

8. 스코프

   [참고자료](https://www.nextree.co.kr/p7363/)

   이건 좀 정확히 알아야할 필요가 있을 것 같다. 클로저와 연관되니 꼭 알아볼 수 있도록 하자

9. 화살표와 일반함수 차이

   [참고자료](https://shinsangeun.github.io/categories/Nodejs/arrow-function)

   [참고자료2](https://poiemaweb.com/es6-arrow-function)

   [참고자료3](https://poiemaweb.com/js-this)

   1. this
      - 일반 함수는 this가 동적으로 바인딩
      - 화살표 함수는 상위 스코프의 this와 같다
   2. 생성자 함수로 사용 여부
      - 일반 함수는 사용 가능
      - 화살표 함수는 불가능
   3. arguments 사용 가능
      - 일반 함수에서는 함수가 실행 될 때 암묵적으로 araguments변수가 전달되어 사용할 수 있습니다
      - 화살표 함수에서는 argument변수가 전달되지 않는다

10. 뷰 라이플사이클

    [참고자료](https://medium.com/witinweb/vue-js-%EB%9D%BC%EC%9D%B4%ED%94%84%EC%82%AC%EC%9D%B4%ED%81%B4-%EC%9D%B4%ED%95%B4%ED%95%98%EA%B8%B0-7780cdd97dd4)

    1. cretion: 컴포넌트 초기화 단계
       1. beforeCrete
       2. created: dta, events가 활성화되어 접근 가능
    2. mounting: dom 삽입 단계
       1. beforeMount: 템플릿과 렌더함수들이 컴파일된 후에 **첫 렌더링이 일어나기 직전에 실행**, 쓰지말도록 하자
       2. mounted: 컴포넌트, 템플릿, 렌더링된 돔에 접근이 가능. 주의할점) 부모자식관계의 컴포넌트에서 생각한 순서대로 mounted가 발생되지 않는다
    3. updating: diff 및 재 렌더링 단계
       1. beforeUpdate: 데이터가 변경되어 사이클이 시작될 때 실행됨
       2. updated: 재 렌더링이 일어난 후에 실행
    4. destruction: 해체 단계
       1. beforeDestroy: 뷰 인스턴스가 제거되기 직전에 호출. 이벤트리스너 제거 또는 reactive subscription을 제거하고자 한다면 여기가 제격
       2. destroyed: 뷰 인스턴스가 제거된 후에 호출.

11. vue 바인딩

    [bind & on](https://kr.vuejs.org/v2/guide/syntax.html)

    [model](https://kr.vuejs.org/v2/guide/forms.html)

12. 플러그인

    [공식문서](https://kr.vuejs.org/v2/guide/plugins.html)

13. watch와 computed

    [참고자료](https://jeongwooahn.medium.com/vue-js-watch%EC%99%80-computed-%EC%9D%98-%EC%B0%A8%EC%9D%B4%EC%99%80-%EC%82%AC%EC%9A%A9%EB%B2%95-e2edce37ec34)

    watch: 반응형 콜백, 변경을 감시한다, vue인스턴스의 특정 프로퍼티가 수정될 때 사용, 아무 프로퍼티도 생성하지 않고 단순히 콜백

    computed: 반응형 getter

    - getter: computed의 프로퍼티가 정의될때 실행됨
    - 반응형: 속한 프로퍼티의 변경여부를 추적

    둘의 차이

    - 위의 예시처럼 인스턴스의 data에 할당된 값들 사이의 종속관계를 자동으로 세팅하고자 할때는 `computed`로 구현하는것이 좋다. 그러니까 `reverseMessage` 는 `message` 값에 따라 결정되어진다. 이 종속관계가 조금이라도 복잡해지면 `watch`로 구현할 경우 중복계산이 일어나거나 코드 복잡도가 높아질 것이다. 이는 오류도 더 많이 발생시킬 것이다.
    - `watch`는 특정 프로퍼티의 변경시점에 특정 액션(call api, push route …)을 취하고자 할때 적합하다.
    - `computed`의 경우 종속관계가 복잡할 수록 재계산 시점을 예상하기 힘들기 때문에 종속관계의 값으로 계산된 결과를 리턴하는 것 외의 사이드 이펙트가 일어나는 코드를 지양해야한다.
    - 더 쉽게 판단하는 방법: 만약 `computed`로 구현가능한 것이라면 `watch`가 아니라 `computed`로 구현하는것이 대게의 경우 옳다.

14. vuex

    1. strict모드

       [참고자료](https://vuex.vuejs.org/kr/guide/strict.html)

    2. actions: 사용자의 입력에 따라 반응할 methods

    3. state: 컴포넌트 간 공유할 data

    4. view: 데이터가 표현될 template

    5. getters: vuex의 데이터를 접근할 때 중복된 코드를 반복호출하게 되는 것

       예제코드

       ```javascript
       // getters 적용전
       // App.vue
       computed: {
         doubleCounter() {
           return this.$store.state.counter * 2;
         }
       },
       
       // Child.vue
       computed: {
         doubleCounter() {
           return this.$store.state.counter * 2;
         }
       },
       ```

       ```javascript
       // getters 적용후
       // store.js (Vuex)
       getters: {
         doubleCounter: function (state) {
           return state.counter * 2;
         }
       },
       
       // App.vue
       computed: {
         doubleCounter() {
           return this.$store.getters.doubleCounter;
         }
       },
       
       // Child.vue
       computed: {
         doubleCounter() {
           return this.$store.getters.doubleCounter;
         }
       },
       ```

    6. mutations: vuex의 데이터, 즉 state값을 변경하는 로직들을 의미

       getters와 차이점

       1. 인자를 받아 vuex에 넉며줄 수 있고
       2. computed가 아닌 mothods에 등록

    7. actions: 비 순차적 또는 비동기 처리 로직들을 선언한다.