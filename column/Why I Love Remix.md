# Why I Love Remix

[원글 링크](https://kentcdodds.com/blog/why-i-love-remix)

## 한문장으로

글쓴이가 한문장으로 왜 remix에 사랑이 빠지게 되었는지 설명해준다

> Remix enables me to build amazing user experiences and still be happy with the code I had to write to get there
> 리믹스는 엄청난 유저 경험성과 코드를 쓰면서 행복을 유지할 수 있게 만들어 줬다
> 엄청난 기능이 있나보다 그럼 좀더 설명하는 글을 읽어보자

## 유저 경험성 (User Experience)

우리가 만든 소프트를 이용할 때 유저 경험에 큰 임팩트를 줄만한 것들이 참으로 많다. 많은 사람들은 퍼포먼스/속도를 신경쓰는데 많은 시간을 소비하며 중요한 면이기도 하다. 하지만 이것들은 그런 중요한 것들 중에 하나일 뿐이다. 유저경험성은 많은 것이 있고 그중에는 아래와 같은 것들도 있따

- 접근성
- 성능
- 콘탠트 리플로우
- 안정성 및 가용성
- 에러 핸들링
- 펜딩 관리
- 상태 관리
- 점진적 개선
- 복원력
- 레이아웃
- 콘텐트 클래러티

기능 개발의 속도도 유저 경험성에 영향을 줄 수가 있다. 그래서 유저 경험성은 우리의 코드 유지보수성에 간접적으로 영향을 받는다
<br/>
리믹스는 많은 것을 돕는다. 상태관리의 어려움도 어렵지 않게 도와준다. 유저들은 리프래쉬할 필요가 없다. 리믹스로 많은 것을 도와줄 수가 있다.
<br/>
리믹스는 웹사이트를 빠르게 만드는데에도 도움을 준다. `<link/>` 태그를 이용해서 어셋과 데이터를 프리로드한다. 가끔 사이트가 CDN에 올라가있는 정적파일이라고 느낄 만큼 빠름에 놀라지만 이것은 서버랜더링되고 모든 페이지는 모든 유저에게 유니크하다.
<br/>
리믹스의 플랫폼 API사용은 가능하게 하는 것들이 있다. 그리고 이러한 점은 리믹스가 탄력적이며 점진적인 개선에도 매우 좋은 이유이다. 자바스크립트를 로드하는 속도가 느리거나 오류가 발생하는 열악한 네트워크 환경에서도 리믹스는 앱에 물이 공급되기도 전에 작동한다. 온클릭 핸들러가 아직 로드되지 않은 완전 무응답 버튼보다 좋다.
<br/>
리믹스의 선언적 에러 핸들링은 에러 핸들링이 더 쉽게 되었다는 것을 의미한다.

> 리믹스는 훌륭한 사용자 경험성을 기본으로 만든다. 그리고 그것이 내가 리믹스를 사랑하는 주된 이유이다.

## The Code

전 세계를 넘어 수백만의 사람들이 사용하는 내가 만든 앱이 사용된다. 리믹스를 이용해서 웹사이트를 만드는 코드를 만들면서 진정으로 행복했다고 말할 수 있는 첫 기회였다. 가장 큰 이유는 리믹스를 사용하기 이전에 유저 경험성 이슈와 딜을 하는 것에 많은 시간을 써왔다는 것이다. 왜냐하면 리믹스는 유저 경험성에 엄청난 도움을 주고 나는 복잡한 코드를 관리하지 않아도 되었다. 그래서 리믹스, 리액트가 나에게 준 선언적 api들만 사용하면 되는 것만이 남았다 앱을 만드는 것에 있어서!
<br/>

```typescript
const loader: LoaderFunction = async ({ request, params }) => {
  // this runs on the server
  // unexpected runtime errors will trigger the ErrorBoundary to be rendered
  // expected errors (like 401s, 404s, etc) will render the CatchBoundary
  // otherwise I can return a response and that'll render the default component
  return json(data);
};

export default function AttendeesRoute() {
  const data = useLoaderData();
  return <div>{/* render the data */}</div>;
}

export function ErrorBoundary({ error }) {
  return <div>{/* render an "unexpected error" message */}</div>;
}

export function CatchBoundary() {
  const caught = useCatch();
  return <div>{/* render the error for 400-status level responses */}</div>;
}

const transition = useTransition();

const text =
  transition.state === "submitting"
    ? "Saving..."
    : transition.state === "loading"
    ? "Saved!"
    : "Ready";
```

이것은 선언적으로 HTTP와 관련없고 포인트를 써둔 리액트 코드를 간단화 시킨다. 클리아언트 서버 커뮤니케이션은 리믹스에 의해 완벽히 관리가 되고 유저 경험성을 위해 최적화시키는 방안으로 관리한다. 그리고 클라이언트/서버 바운더리도 모두 입력할 수 있어서 브라우저와 프로그래머를 오가며 바보 같은 실수를 고치는데에 시간을 많이 안쓰게 해준다.

또한 웹 API에서 리믹스를 이용하는 것도 좋아한다. 위에서 말하는 json함수는 로더에서? response객체를 만드는 함수를 만드는 것이 간단하다. 리믹스랑 무언가를 하는 것을 배우기를 원한다면, 리믹스 공식문서에서 하는 것처럼 mdn에 많은 시간을 쏟게 될 것이고 리믹스를 사랑하게 되는 또다른 이유가 될 것이다.

리믹스가 웹 플랫폼을 너무 많이 사용하고 웹 플랫폼 API를 최대한 방어하기 때문에 자연스럽게 이런 일이 일어난다. (이는 리액트로 더 잘 할수록 자바스크립트를 더 잘하게 된다는 제 생각과 비슷하다.)

리믹스는 서버의 공통 인터페이스로 웹 API를 기반으로 동일한 앱을 모든 플랫폼에 배포할 수 있다. 사용할 어댑터를 변경하기만 하면 된다. 서버리스에서 실행하든 도커에서 실행하든 리믹스가 해결해준다.

또다른 놀라운 파트는 로더에 있다. 이것은 서버에서 돌아가고 api에 요청을 보내서 많은 데이터를 받고 필요한 데이터만 골라서 얇게 만들 수가 있다. 이것은 과하게 팻칭한 데이터 요청을 자연적으로 제거할 수 있다는 의미이다.

서버가 클라이언트로 보내는 데이터보다 더 많은 데이터가 필요할 경우 파일을 위로 스크롤하여 로더를 변경하여 필요한 추가 데이터를 포함하면 된다. 모두 입력하고 클라이언트 쪽 코드를 사용할 준비가 되었으면 정말 멋지다.

사용자 경험에 매우 좋다. 개발자의 경험에도 좋다. 코드에 대해 쓸데없는 말을 많이 할 필요가 없다. 일반적으로 쓰이는 다양한 함수들을 한번에 이용가능한 onSubmit이 있다. 리믹스에서는 모든 것이 사라지고 선언적인 API만이 남았다.
