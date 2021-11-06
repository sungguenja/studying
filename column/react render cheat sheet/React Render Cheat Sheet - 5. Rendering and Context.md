# React Render Cheat Sheet - 5. Rendering and Context

좋은 두개면 이제 직접적으로 내리는 두가지는 제어가 쉽게 가능하다는 것을 알았다. 하지만.... 우리에겐 아직 몇 문제가 남아있다. 전역관리를 생각해보자. redux나 다른 서드파티는 다른 이야기이다. 그것은 거기에 맡긴다! 우리가 볼 부분은 context를 이용하는 부분디아.

```react
const App = () => {
  // ...
  return (
    <AppContext.Provider ...>
      <ComponentA />
    </AppContext.Provider>
  )
}

const ComponentA = () => <ComponentB />
const ComponentB = () => <ComponentC />
```

위의 경우 일반적으로는 상태가 변하면 속해있는 컴포넌트는 전체가 re-render가 일어난다

## Context and React rendering

사실 어렵지 않다! context도 `useMemo`, `useCallback`을 이용하면 된다! 그러면 적절하게 이용이 가능하고 적절하게 리렌더링이 안일어난다!