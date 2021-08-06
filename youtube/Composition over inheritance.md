# Composition over inheritance

[영상 링크](https://www.youtube.com/watch?v=wfMtDGfHWpA)

자 우리는 이런 것을 정의한다고 해보자

> - Dog
>   - .poop()
>   - .bark()
> - Cat
>   - .poop()
>   - .meow()

자 이제 조금씩 살펴보자 일단 이것이 정말 머저리 같은 구조임을 알 수 있다. poop이 반복하기 때문이다. 조금 수정을 가해보자

> - Animal
>
>   - .poop
>
>     > - Dog
>     >   - .bark()
>     > - Cat
>     >   - .meow()

조금은 이해되는 수준으로 내려왔다. 여기에 우리는 청소등 필요한 것이 있으니 청소도 해주고 기타 다양한 봇들을 일단 만들어 보자

> - Robot
>
>   - drive()
>
>     > - MurderRobot
>     >   - kill()
>     > - CleaningRobot
>     >   - clean()
>
> - Animal
>
>   - .poop
>
>     > - Dog
>     >   - .bark()
>     > - Cat
>     >   - .meow()

꽤나 논리적이고 필요한 것들이 뭉쳐있다. 이것에 대해 기분이 좋을 수 있지만 이것은 어떻게 보면 실패할 수 있다. 만약 고객이 MurderRobotDog를 원했다고 해보자!  구조적으로 합치면 필요없는 poop이 공용하게 된다. 이 구조형태에서 어떻게든 추가 시키겠다고 난리법석을 한번 부려보자! 그렇다 의도적으로 구린 구조를 만들어보자는 것이다

> - GameObject
>
>   - bark()
>
>     > - Robot
>     >
>     >   - drive()
>     >
>     >     > - MurderRobot
>     >     >   - kill()
>     >     > - CleaningRobot
>     >     >   - clean()
>     >     > - MurderRobotDog
>     >     >   - ~~bark()~~
>     >
>     > - Animal
>     >
>     >   - poop()
>     >
>     >     > - Dog
>     >     >   - ~~bark()~~
>     >     > - Cat
>     >     >   - Meow()

어..... 어... 그래... 그렇다. 전체에 bark를 줬고 이랬더니 전체에 쓸모없는 bark가 생기게 되었다. 그리고 만약 고릴라를 추가해보자. 그렇다면 고릴라에 bark가 추가되어있을 것이다 ㅋㅋㅋㅋ 이것이 우리가 인터페이스 분리 원칙이 필요한 이유다. 차라리 반복을 하는게 더 나은 구조를 만들 수 있다.

잠시 우리에게 필요한 것을 생각해보자

> - Dog = pooper + barker
> - Cat = pooper + meower
> - cleaningRobot = driver + cleaner
> - murderRobot = driver + killer
> - murderRobotDog = driver + killer + barker

자 구조가 간단하게 보이기 시작했다. 그렇다면 우리는 이제 인터페이스 분리 원칙을 이용하여 한번 코드를 짜볼 수 있도록 하자

```javascript
const barker = (state) => ({
    bark: () => console.log(`Woof, I am ${state.name}`);
})

const driver = (state) => ({
    driver: () => state.position = state.position + state.speed
})

const murderRobotDog = (name) => {
    let state = {
        name,
        speed: 100,
        position: 0
    }
    
    return Object.addign(
        {},
        barker(state),
        driver(state),
        killer(state)
    )
}

murderRobotDog('sniffles').bark();
```

