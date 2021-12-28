# Container Presentational Pattern

> 로직을 view로 부터 분리 시켜라

이거는 꽤 많이 알려진 컨셉이다. 그리고 많은 분들이 이용해봤을 것이다. 하지만 절대적인 해법은 아니다. 그래도 괜찮은 패턴인 것은 맞다고 나는 생각한다.

react를 구상할 때 아래와 같이 두가지 파일로 나눈다고 생각하면 편하다.

1. Presentational Component: 데이터를 다루는 컴포넌트
2. Container Component: 뷰를 담당하는 컴포넌트

뷰와 관련된 로직이 아니라면 데이터와 관련된 로직은 모두 `Presentational Component`에게 맡긴다. 간단한 예시는 아래와 같이 볼 수가 있을 것이다.

```typescript
interface numberViewProps {
  nowNumber: number;
}

const numberView = ({ nowNumber }: numberViewProps) => {
  return (
    <div>
      <h1>{nowNumber}</h1>
    </div>
  );
};

const numberIndex = () => {
  const [nowNumber, setNowNumber] = useState<number>(0);

  useEffect(() => {
    setInterval(() => {
      setNowNumber((bfn) => bfn + 1);
    }, 1000);
  }, []);

  return <numberView nowNumber={nowNumber} />;
};
```

## 장점

- 관심도의 분리라는 아주 큰 장점을 가질 수가 있다.
- 잘하면 재사용성도 올릴 수가 있다.
- 테스팅이 쉽다.

## 단점

- 상태관리에 대한 실수 유발 가능
- 불필요한 리렌더링의 발생 (전체에 대한 상태를 조율해야해서 값의 변화로 상위 단에서 리랜더링을 일으킬 가능성도 있다)
