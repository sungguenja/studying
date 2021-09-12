# 리액트 훅스 컴포넌트에서 setInterval 사용 시의 문제점

[컬럼 링크](https://overreacted.io/making-setinterval-declarative-with-react-hooks/) [번역본 링크](https://velog.io/@jakeseo_me/%EB%B2%88%EC%97%AD-%EB%A6%AC%EC%95%A1%ED%8A%B8-%ED%9B%85%EC%8A%A4-%EC%BB%B4%ED%8F%AC%EB%84%8C%ED%8A%B8%EC%97%90%EC%84%9C-setInterval-%EC%82%AC%EC%9A%A9-%EC%8B%9C%EC%9D%98-%EB%AC%B8%EC%A0%9C%EC%A0%90) 

[다른 방식으로 간단하게 이용하는 방법](https://haesoo9410.tistory.com/168)

[다른 참고 링크](https://velog.io/@vagabondms/React%EC%97%90%EC%84%9C-setInterval-%EC%82%AC%EC%9A%A9%ED%95%98%EA%B8%B0)

## Making setInterval Declarative with React Hooks

리액트 훅스를 가지고 논다면 `setInterval`을 사용했을 시 예상과 다르게 작동하는 문제가 있다. 이것은 사실 모든 비동기의 문제이긴 하다

일단 예시 코드를 한번 보자

```react
// counter.js
import React, { useState, useEffect, useRef } from 'react';

function Counter() {
  let [count, setCount] = useState(0);

  useInterval(() => {
    // Your custom logic here
    setCount(count + 1);
  }, 1000);

  return <h1>{count}</h1>;
}

// useInterval.js
import React, { useState, useEffect, useRef } from 'react';

function useInterval(callback, delay) {
  const savedCallback = useRef();

  // Remember the latest callback.
  useEffect(() => {
    savedCallback.current = callback;
  }, [callback]);

  // Set up the interval.
  useEffect(() => {
    function tick() {
      savedCallback.current();
    }
    if (delay !== null) {
      let id = setInterval(tick, delay);
      return () => clearInterval(id);
    }
  }, [delay]);
}
```

자 이 코드를 보면 이제 누군가가 말할 것이다

> 얌마! 이 코드는 전혀 타당치 않지! 리액트 훅스가 편의성과 가독성을 망쳤어!

잠시 이 이야기를 다루기 전에 클래스형 컴포넌트를 생각하면 조금 이상하다는 것을 생각하긴 할 것이다. 클래스형에서는 그냥 간단하게 라이프사이클에서 적절히 쓰면 되는 것이다. 아래 예시 코드와 같을 것이다

```react
// class형
class Counter extends React.Component {
  state = {
    count: 0,
    delay: 1000,
  };

  componentDidMount() {
    this.interval = setInterval(this.tick, this.state.delay);
  }
  componentDidUpdate(prevProps, prevState) {
    if (prevState.delay !== this.state.delay) {
      clearInterval(this.interval);
      this.interval = setInterval(this.tick, this.state.delay);
    }
  }
  componentWillUnmount() {
    clearInterval(this.interval);
  }
  tick = () => {
    this.setState({
      count: this.state.count + 1
    });
  }

  handleDelayChange = (e) => {
    this.setState({ delay: Number(e.target.value) });
  }

  render() {
    return (
      <>
        <h1>{this.state.count}</h1>
        <input value={this.state.delay} onChange={this.handleDelayChange} />
      </>
    );
  }
}
```

약간 길기는 하지만 납득이 가기는 한다.

함수형을 생각해보자. 이것은 생각을 바꿔야 한다! 명령형 프로그래밍에서 이제 우리는 선언형으로 넘어와야 이것에 대해 납득이 가고 이해가 될 것이다.

사실 조금 돌아가지 않고 바로 적용하는 방법이 있기는 하다. 아래를 확인해보자

```react
function Counter() {
  let [count, setCount] = useState(0);

  useEffect(() => {
    let id = setInterval(() => {
      setCount(count + 1);
    }, 1000);
    return () => clearInterval(id);
  });

  return <h1>{count}</h1>;
}
```

그런데 이 코드의 문제는 매 렌더링마다 계속 작용이 된다. 사양에 대해 문제가 크게 생긴다

랜더링이 너무 일어난다. 그래서 의존성을 한번 줘서 렌더링을 덜 일으키게 해보자

```react
function Counter() {
  let [count, setCount] = useState(0);

  useEffect(() => {
    let id = setInterval(() => {
      setCount(count + 1);
    }, 1000);
    return () => clearInterval(id);
  }, []);

  return <h1>{count}</h1>;
}
```

아니 이제는 1이 되고 그때부터 업데이트가 안된다. ㅋㅋㅋㅋ 난리네 ㅋㅋㅋㅋㅋ 그럼 어떻게 해야하죠? Refs를 이용해봅시다

- `setInterval(fn, delay)`에서 함수가 `savedCallback`을 호출하게 만들 것입니다.
- 첫 렌더링에서 `savedCallback`을 `callback1`로 설정합니다.
- 두번째 렌더링에서 `savedCallback`을 `callback2`로 설정합니다.
- ???
- 굿

위와 같은 흐름으로 일차 답안지가 나온다

```react
function Counter() {
  const [count, setCount] = useState(0);
  const savedCallback = useRef();

  function callback() {
    setCount(count + 1);
  }

  useEffect(() => {
    savedCallback.current = callback;
  });

  useEffect(() => {
    function tick() {
      savedCallback.current();
    }

    let id = setInterval(tick, 1000);
    return () => clearInterval(id);
  }, []);

  return <h1>{count}</h1>;
}
```

근데 사실 위 코드가 좀 직관성이 없긴 하다. 그렇다면 어떻게 해결할 수가 있을까? 꺼내서 모듈화시키자!

그것은 이제 우리의 몫이다. 잘해볼 수 있도록 하고 참고 링크는 꼭 다시 읽어볼 수 있도록 하자.