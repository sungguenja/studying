# React Render Cheat Sheet - 3. Stable reference with useMemo

리랜더링을 막는 두가지 방법을 한번 봅시다

## 1. Flattening props

간단한 케이스라면 props로 내리기 전에 해당 값을 지정해서 내려주는 케이스이다. 아래와 같은 경우라고 보면 될 것 같다

```react
const Parent = () => {
    const user = useState<Object>({'name':'Alex','role':'Admin'});
    const showSidebar = user.role === 'Admin';
    
    return <child showSidebar={showSidebar} />
}
```

하지만 복잡한 케이스라면 힘들 것이다. 어떤 방법을 이용해봐야 할까?

## 2. useMemo

dependency와 관련된 것이다. 아주 좋은 방안이다. 메모이제이션을 이용해서 퍼포먼스에 불이익을 보는 경우가 아니라면 좋은 선택방안이다.

