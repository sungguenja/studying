# Factory Functions in JavaScript

[영상 링크](https://www.youtube.com/watch?v=ImwrezYhw4w)

```javascript
class Dog {
    constructor() {
        this.sound = "woof";
    }
    talk() {
        console.log(this.sound);
    }
}
const sniffles = new Dog();
sniffles.talk(); // Outputs: "woof"

button_element.addEventListener("click", () => sniffles.talk()); // 굳이 이렇게 화살표 함수까지 해줘야 작동함
```

이것은 이제 이벤트라 묶으면 다양한 문제가 생기고 코드가 이쁘지 않다. 그렇다면 우리는 클로저를 이용해보자

```javascript
const dog = () => {
    const sound = "woof";
    return {
        talk: () => console.log(this.sound)
    }
}

const sniffles = dog();
sniffles.talk();
button_element.addEventListener("click",sniffles.talk); // 이렇게 깔끔하게 엮을 수가 있다
```

결과는 똑같이 나온다. 하지만 이것은 이벤트를 엮는데에 아주 큰 이득을 가진다. 코드의 가독성이 매우 좋아졌다. 클로저를 남발할 경우 퍼포먼스에 안좋아질 수도 있다. 실제로 함수의 경우 접근하는데 속도가 `0.0004ms`이지만 클래스는 `0.0002ms`이기 때문이다. ~~????~~

