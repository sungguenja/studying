# react19

> 걍 새 훅들 정리

## useTransition

```typescript
const Transition = () => {
  const [firstThing, setFirstTing] = useState();
  const [secondThing, setSecondThing] = useState();
  const [isPending, startTransition] = useTransition();

  const update = () => {
    setFirstThing("do first");

    startTransition(() => {
      setSecondThing("do second");
    });
  };

  return (
    <div>
      <h1>{firstThing}</h1>
      <h2>{isPending ? "loading" : secondThing}</h2>
      <button onClick={update}>click</button>
    </div>
  );
};

const AsyncTransition = () => {
  const [firstThing, setFirstTing] = useState();
  const [secondThing, setSecondThing] = useState();
  const [isPending, startTransition] = useTransition();

  const update = () => {
    setFirstThing("do first");

    startTransition(async () => {
      await fetch();
      setSecondThing("do second");
    });
  };

  return (
    <div>
      <h1>{firstThing}</h1>
      <h2>{isPending ? "loading" : secondThing}</h2>
      <button onClick={update}>click</button>
    </div>
  );
};
```

## useActionState

> 비동기 처리와 관련된 상태

```typescript
const actionState = () => {
  const [actionResponse, submitAction, isPending] = useActionState(
    asyncAction,
    initialState
  );
};
```

## useOptimistic

> 긍정적 응답이 오는 것을 가정하고 업데이트

```typescript
import { useOptimistic, useState, useRef } from "react";

export async function deliverMessage(message) {
  await new Promise((res) => setTimeout(res, 1000));
  return message;
}

function Thread({ messages, sendMessage }) {
  const formRef = useRef();
  async function formAction(formData) {
    addOptimisticMessage(formData.get("message"));
    formRef.current.reset();
    await sendMessage(formData);
  }
  const [optimisticMessages, addOptimisticMessage] = useOptimistic(
    messages,
    (state, newMessage) => [
      ...state,
      {
        text: newMessage,
        sending: true,
      },
    ]
  );

  return (
    <>
      {optimisticMessages.map((message, index) => (
        <div key={index}>
          {message.text}
          {!!message.sending && <small> (Sending...)</small>}
        </div>
      ))}
      <form action={formAction} ref={formRef}>
        <input type="text" name="message" placeholder="Hello!" />
        <button type="submit">Send</button>
      </form>
    </>
  );
}

export default function App() {
  const [messages, setMessages] = useState([
    { text: "Hello there!", sending: false, key: 1 },
  ]);
  async function sendMessage(formData) {
    const sentMessage = await deliverMessage(formData.get("message"));
    setMessages((messages) => [...messages, { text: sentMessage }]);
  }
  return <Thread messages={messages} sendMessage={sendMessage} />;
}
```

## useFormStatus

> 폼 햄들링을 위한 훅
>
> 상위 form에 관한 상태 정보만 줌

## use

> promise, context 처리가 가능
>
> use는 if와 같은 조건문과 반복문에서도 호출 가능

```typescript
// promise 처리
async function someFetch(someValue) {
  const response = await fetch(`/api-url/${someValue}`);
  // 에러처리 알아서
  return response.json();
}
function FetchWrapper() {
  const fetchPromise = someFetch("test");
  return (
    <ErrorBoundary fallback={<p>에러에요</p>}>
      <Suspense fallback={<p>로딩중</p>}>
        <ChildComponent fetchPromise={fetchPromise} />
      </Suspense>
    </ErrorBoundary>
  );
}
function ChildComponent(fetchPromise) {
  const fetchData = use(fetchPromise); // promise 결과를 처리해줌
  return <div>{fetchData}</div>;
}
```

- async/await와 적당히 잘 구분해 써야함
  - await에서는 await를 만나면 아래 로직이 안돌지만
  - use는 돈다
  - 그걸 생각해보면 await는 서버 컴포넌트에서 use는 클라이언트 컴포넌트에서 쓰는게 좋다고 생각할 수 있다
- promise 객체는 서버 컴포넌트에서 생성해라
  - 클라이언트 컴포넌트는 리랜더링이 되면 promise를 다시 생성함
    - 왜냐고? 리랜더링 == 함수 재실행이니까
