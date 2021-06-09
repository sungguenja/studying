# K사 인턴 면접 후기

- 결과: 떨

- window resize event

  ```javascript
  window.addEventListener('resize',function(){console.log('resize event')})
  ```

  위코드는 문제가 있다. 텀없이 변화되는 모든 순간에 이벤트를 발생 시킨다. 해결 방법은 `setTimeout`을 이용하면 된다.

  ```javascript
  var delay = 300;
  var timer = null;
  
  window.addEventListener('resize', function() {
      clearTimeout(timer);
      timer = setTimeout(function(){
          console.log('resize event');
      },delay);
  })
  ```

  원리를 살펴보자

  1. resize 이벤트 발생
  2. clearTimeout이 실행됨
  3. timer가 setTimeout으로 다시 바뀜
     1. delay 시간 내에 resize 이벤트 발생
     2. clearTimeout으로 timer의 이벤트 삭제
     3. timer가 재정의
  4. delay시간이 지남
  5. timer에 지정해줬던 setTimeout내부가 실행됨

- methods vs computed

  - 공통점

    함수처럼 지정하고 실행시키기 가능하다

  - 차이점

    - methods

      methods는 진짜 함수이다. 화면에 return값으로 보여줄 수도 있고 원할때 실행도 시킬 수 있다. 하지만 해당 vue파일에서 랜더링될 때 무조건 실행이 되게 되어있다. 즉, 뭔가 랜더링이 다시 일어나면 무조건 다시 실행시키는 것이 있다. (return 값을 랜더링 시킬 경우)

    - computed

      화면에 보여줄 때 자주 이용하는데 관련된 변수에 계산된 캐싱값이라고 생각하는 것이 편하다. 즉, 참고하고 있는 값이 변경될 때만 재실행이 된다.

    - watch

      데이터가 바뀌면 특정 함수를 실행하라는 조건

- composition api

  - 컴포넌트 로직을 유연하게 구성할 수 있는 API 모음으로 로직의 **재사용성과 가독성**을 높여줍니다.
  - 각 컴포넌트들도 이름이 바뀐다
    - **beforeCreate -> setup()
      created -> setup()**
      beforeMount -> **on**BeforeMount
      mounted -> **on**Mounted
      beforeUpdate -> **on**BeforeUpdate
      updated -> **on**Updated
      beforeDestroy -> **on**BeforeUnmount
      destroyed -> **on**Unmounted
      activated -> **on**Activated
      deactivated -> **on**Deactivated
      errorCaptured -> **on**ErrorCaptured
  - 예제 코드는 올려둘테니 확인하자
  - 반응형 데이터라는 것에 주목을 하자
  - [이거 보면서 잘 따라해보자](https://geundung.dev/102)

