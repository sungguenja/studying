# React Render Cheat Sheet - 1. Standard rendering and memo

[모음 링크](https://alexsidorenko.com/blog/react-render-cheat-sheet/) [part-1](https://alexsidorenko.com/blog/react-render-always-rerenders/)

리액트는 상위 컴포넌트의 state가 바뀌면 하위 컴포넌트들도 같이 리랜더링 되는 문제가 하나 있다. 그렇다면 우리는 이것을 어떻게 피할 수 있을까?

## 리랜더링 피하기

`React.memo`에 한번 집중해보자. 하위 컴포넌트에서 memo로 저장된 컴포넌트가 변경이 일어나지 않는다면 상위 컴포넌트의 state가 변경이 된다고 해도 변경되지 않는다.

여기서 이것을 거꾸로 wrap해주고 있는 컴포넌트에서 prop해주는 변수에 memo로 주게 된다면 해당 숫자가 변하지 않는이상 리랜더를 막을 수가 있다.

그러면 리랜더링을 피하기 위해서 매번 써야하는가? 그것은 또 아니다. memo는 어찌되었든 메모이제이션을 이용하니 메모리와 퍼포먼스를 조금씩 사용할 수 밖에 없다. 적당히 사용하는 것이 가장 좋아 보인다.

[참고할 만한 글](https://react.vlpt.us/basic/19-React.memo.html)