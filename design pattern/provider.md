# Provider Pattern

[참고 링크](https://mortenbarklund.com/blog/react-architecture-provider-pattern/)

> 데이터를 자식 컴포너트들에서 사용할 수 있도록 만들어라

react에서는 context를 이용하면 provider pattern을 용이하게 디자인할 수 있다. 예제 코드를 한번 살펴보자.

```typescript
import { createContext } from "react";

const UserContext = createContext({});

function Name() {
  return (
    <UserContext.Consumer>
      {({ name }) => <p>Hello, {name}</p>}
    </UserContext.Consumer>
  );
}

function App() {
  const name = "World";
  const value = { name };

  return (
    <UserContext.Provider value={value}>
      <h1>Welcome</h1>
      <Name />
    </UserContext.Provider>
  );
}
```

역으로 생각하면 전역변수를 이용해도 된다는 소리기도 하지만 전역변수를 이용해 provider pattern을 이용한다면 다소 massive해질 수 있으니 주의하자

provider 패턴을 생각한다면 다크모드를 어렵지 않게 구현이 가능할 것이다. 아래와 같이 진행할 수 있을 것이다.

```typescript
enum themEnum {
  DARK = "dark",
  LIGHT = "light",
}

const ThemeProvider = () => {
  const [theme, setTheme] = useState<themEnum>(themEnum.DARK);

  const toggleTheme = () => {
    setTheme(
      themeEnum[theme === themeEnum.DARK ? themeEnum.LIGHT : themeEnum.DARK]
    );
  };

  return <ThemeContext.Provider theme={theme}>{child}</ThemeContext.Provider>;
};

const App = () => {
  return (
    <div>
      <ThemeContext>
        <child />
      </ThemeContext>
    </div>
  );
};
```
