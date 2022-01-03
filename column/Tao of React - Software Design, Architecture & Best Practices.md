# Tao of React - Software Design, Architecture & Best Practices

[글 원본 링크](https://alexkondov.com/tao-of-react/)

## Components

- Favor Functional Components

  - 간단한 신텍스를 가진다. 라이프사이클 메소드, constructors, boilerplate를 쓰지 않는다
  - 에러 바운드는 좀 처리 해야한다
  - 예시

    ```typescript
    class Counter extends React.Compontn {
      state = {
        counter: 0,
      };

      constructor(props) {
        super(props);
        this.handleClick = this.handleClick.bind(this);
      }

      handleClick() {
        this.setState({ counter: this.state.counter + 1 });
      }

      render() {
        return (
          <div>
            <p>counter: {this.state.counter}</p>
            <button onClick={this.handleClick}>Increment</button>
          </div>
        );
      }
    }
    function Counter() {
      const [counter, setCounter] = useState(0);
      handleClick = () => setCounter(counter + 1);
      return (
        <div>
          <p>counter: {counter}</p>
          <button onClick={handleClick}>Increment</button>
        </div>
      );
    }
    ```

- Write Consistent Components
  - 컴포넌트들에 같은 스타일을 적용 시켜라
  - helper 함수들은 같은 위치에, 같은 방식으로 export시키고 네이밍 패턴을 가져가라
  - 실질적인 이득은 없지만 코드의 규칙은 볼 수 있다
- Name Components

  - 컴포넌트에는 항상 이름을 지어야한다.
  - 에러 추적에 도움을 준다
  - 리액트 개발 툴은 잘 써라

    ```typescript
    // avoid this
    export default () => <form></form>;

    // Name Your Function
    export default function Form() {
      return <form></form>;
    }
    ```

- Organize Helper Functions

  - 컴포넌트에 대한 클로져를 가지고 있을 필요가 없는 helper 함수들은 밖으로 움직이는게 좋다

    ```typescript
    // 이런 방식으로 밖으로 꺼낼 수 있는 함수는 밖에다 두는 것이 좋다
    function parseDate(date) {
        ...
    }

    function Component({date}) {
        return <div>Date is {parseDate(date)}</div>
    }
    ```

- Don't Hardcode Markup
  - 마크업을 하드코딩 하지 말자
  - 특히 반복되는 li태그 같은 경우는 그냥 map을 잘 이용해보자
- Write Comments in jsx
  - jsx 내부에 코멘트를 기록하는 것이 좋다
- Use Error Boundaries

  - 한 컴포넌트에서의 에러는 하위 전체 ui를 가져오지 못하게 한다.
  - 에러 바운더리를 통해 에러에 대한 상황을 대비하는 것이 좋을 것이다

    ```typescript
    function Component() {
      return (
        <Layout>
          <ErrorBoundary>
            <CardWidget />
          </ErrorBoundary>

          <ErrorBoundary>
            <FiltersWidget />
          </ErrorBoundary>

          <div>
            <ErrorBoundary>
              <ProductList />
            </ErrorBoundary>
          </div>
        </Layout>
      );
    }
    ```

- Desturcture Props

  - 이것은 리팩터링에도 나오는 말이기도 하다
  - 코드 리뷰에서도 자주 보이는 말이기도 하고
  - 하나의 객체로 내려서 하위에서 destructuring을 하는 것이 더 좋다

    ```typescript
    // 👎 Don't repeat props everywhere in your component
    function Input(props) {
      return <input value={props.value} onChange={props.onChange} />;
    }

    // 👍 Destructure and use the values directly
    function Component({ value, onChange }) {
      const [state, setState] = useState("");

      return <div>...</div>;
    }
    ```

- Number of Props
  - 너무 많이 내려주진 말자
  - 글쓴이가 추천해주는 것은 5을 넘어가면 분리해주는 작업을 한다
- Pass Objects Instead of Primitives

  - 객체를 쪼개서 넣어야 한다면 오히려 불편하다
  - 그냥 하나의 객체를 넘겨주는 것이 더 좋다
  - 타입스크립트라면 더욱더 그렇게 하는 것을 추천한다

    ```typescript
    // 이렇게 말고
    <UserProfile
      bio={user.bio}
      name={user.name}
      email={user.email}
    />

    // 이렇게 하는 것을 추천한다
    <UserProfile user={user} />
    ```

- Conditional Rendering

  - 숏 서킷 오퍼레이션은 나쁘지 않은 판단이다.
  - 하지만 ternary를 더 추천한다

    ```typescript
    // 피하자
    function Component() {
      const count = 0;
      return <div>{count && <h1>Messages: {count}</h1>}</div>;
    }

    // 이걸 더 추천한다
    function Component() {
      const count = 0;
      return <div>{count ? <h1>Messages: {count}</h1> : null}</div>;
    }
    ```

- Avoid Nested Ternary operatores

  - 하지만 그렇다고 너무 ternary에 심취하지 말자
  - 엮고 엮고 엮고 하면 오히려 더 보기 안좋아진다

    ```typescript
    // 이건 에바참치
    isSubscribed ? (
      <ArticleRecommendations />
    ) : isRegistered ? (
      <SubscribeCallToAction />
    ) : (
      <AnotherComponent />
    );

    // 차라리 아래와 같이 하는게 더 보기 좋다
    function CallToActionWidget({ subscribed, registered }) {
      if (subscribed) {
        return <ArticleRecommendations />;
      }

      if (registered) {
        return <SubscribeCallToAction />;
      }

      return <RegisterCallToAction />;
    }

    function Component() {
      return (
        <CallToActionWidget subscribed={subscribed} registered={registered} />
      );
    }
    ```

- Assign Default Props When Destructuring
  - 이상한 방식으로 디폴트값을 지정하지 말자
  - 그냥 함수에서 디폴트값을 지정하듯 디폴트값을 지정하자

## State Management

- Use Reducers
  - redux의 리듀서를 이용하듯이 상태관리 함수를 만들자
- Prefer Hooks to HOCs and Render Props

  ```typescript
  // 👎 Avoid using render props
  function Component() {
    return (
      <>
        <Header />
        <Form>
          {({ values, setValue }) => (
            <input
              value={values.name}
              onChange={e => setValue('name', e.target.value)}
            />
            <input
              value={values.password}
              onChange={e => setValue('password', e.target.value)}
            />
          )}
        </Form>
        <Footer />
      </>
    )
  }

  // 👍 Favor hooks for their simplicity and readability
  function Component() {
    const [values, setValue] = useForm()

    return (
      <>
        <Header />
        <input
          value={values.name}
          onChange={e => setValue('name', e.target.value)}
        />
        <input
          value={values.password}
          onChange={e => setValue('password', e.target.value)}
        />
      )}
        <Footer />
      </>
    )
  }
  ```

- Use Data Fetching Libraries
- State Management Libraries
