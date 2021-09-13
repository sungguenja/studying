# React.memo() 현명하게 사용하기

[해당 칼람](https://ui.toast.com/weekly-pick/ko_20190731)

UI성능 증가를 위해 react는 고차 컴퍼넌트(HOC) `react.memo()` 를 제공한다. 랜더링 결과를 메모이징 함으로써, 불필요한 리렌더링을 건너뛰는 방식으로 리렌더링을 멈춘다. 한번 살펴볼 수 있도록 하자.

1. `React.memo()`

   React는 먼저 컴퍼넌트를 렌더링한 뒤, 이전 렌더된 결과와 비교하여 DOM 업데이트를 결정한다. 만약 렌더 결과가 이전과 다르다면, React는 DOM을 업데이트한다.

   다음 렌더링 결과와 이전 결과의 비교는 빠르다. 하지만 어떤 상황에서는 이 과정의 속도를 좀 더 높일 수 있다!

   1. 얕은 비교를 통해 가보자

      ```react
      function moviePropsAreEqual(prevMovie, nextMovie) {
       return (
         prevMovie.title === nextMovie.title &&
         prevMovie.releaseDate === nextMovie.releaseData
      );
      }
      
      const MemoizedMovie2 = React.memo(Movie, moviePropsAreEqual);
      ```

      위와 같이 수동으로 비교도 가능하다.

2. 그래서 언제 쓰죠?

   간단하다! 위 예시를 보지 않았는가? 바로 **props로 렌더링이 자주 일어나는 컴포넌트**이다.

   상위 컴포넌트가 랜더링하려고 해도 하위 컴포넌트에서 체크를 해서 랜더링을 멈추기 때문이다.

   ```react
   function MovieViewsRealtime({ title, releaseDate, views }) {
    return (
      <div>
        <MemoizedMovie title={title} releaseDate={releaseDate} />
       Movie views: {views}
      </div>
   );
   }
   ```

   이런 컴포넌트가 있다고 해보자. 그런데 views만 변경이 일어나면 굳이 렌더링이 다시 일어나지 않아도 되지 않을까? 그렇다면 그 위에 썼던 예시 코드를 이용하는 것이다. 그렇다면 views만 변경되는 상황에서는 리랜더링이 일어나지 않을 것이다

3. 그럼 언제 쓰지 말아야 하죠?

   굳이 성능의 이점을 얻지 못한다면 안쓰는 것이 좋다. 왜냐하면 오히려 이런 경우에는 메모이제이션을 하느라 성능을 저하하기 때문이다.

   그리고 쓸모 없는 props를 비교하면 그것도 이점을 얻기 어렵다.

4. `React.memo`와 콜백 함수

   자 잠시 체크 아래 코드를 보고 주석과 같이 나온다는 것을 안다면 당신은 일단 잘 알고 있는 것이다

   ```react
   function sumFactory() {
    return (a,b) => a+b;
   }
   
   const sum1 = sumFactory();
   const sum2 = sumFactory()2
   
   console.log(sum1===sum2);// false
   console.log(sum1===sum1);// true
   console.log(sum2===sum2);// true
   ```

   그렇다면 내가 무엇을 말할 지 예상이 되는가? 그렇다 props로 내려오는 함수는 이렇게 비교가 불가하다! 즉, 아무생각없이 memo를 이용할 경우 함수가 다르다고 도출하기때문에 계속해서 리렌더링이 일어나게 될 것이다.

   이런 경우에는 필요한 것만 체크하도록 하는 것이 좋을 것이다.

5. `React.memo()`는 성능 개선의 도구다.

   성능 개선에 좋지만 너무 의존하지 마라. 렌더링을 막기 위해 메모이제이션에 의존하면 안된다.

6. 결론

   `React.memo()`는 함수형 컴포넌트에서도 메모이제이션의 장점을 얻게 해주는 도구다.