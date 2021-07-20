# Vuex 간단 정리

## 상태

store를 가져와 상태를 모든 자식 컴포넌트에 저장소를 주입하는 메커니즘을 제공한다

getter를 사용해야하는 경우 계산된 속성을 모두 선언하면 반복적이고 커진다. 이를 처리하기 위해 계산된 getter함수를 생성하는 `mapState`를 이용해 줄일 수가 있다.

```javascript
// 독립 실행 형 빌드에서 헬퍼가 Vuex.mapState로 노출됩니다.
import { mapState } from 'vuex'

export default {
    // ...
    computed: mapState({
        // 화살표 함수는 코드를 매우 간결하게 만든다 (하지만 상황을 잘 조심해야함. this고려)
        count: (state) => {state.count},
        
        // 문자열 값 'count'를 전달하는 것은 `state => state.count`와 같다
        countAlias: 'count',
        
        // 'this'를 사용하여 로컬 상태에 액세스하려면 일반적인 함수를 사용해야 한다.
        countPlusLocalState (state) {
            return state.count + this.localCount;
        }
    })
}
```

## Getter

때로는 저장소 상태를 기반하는 상태를 계산해야 할 수도 있다. 중요한 점은 getter로는 상태를 변경시킬 수 없다!

```javascript
computed: {
  doneTodosCount () {
    return this.$store.state.todos.filter(todo => todo.done).length
  }
}
```

저장소에서 저장을 할 수가 있다. 저장소의 계산된 속성으로 생각할 수 있습니다. 계산된 속성처럼 ㅁgetter의 결과는 종속성에 따라 캐쉬되고, 일부 종속성이 변경된 경우에만 다시 계산됩니다.

```javascript
const store = new Vuex.Store({
  state: {
    todos: [
      { id: 1, text: '...', done: true },
      { id: 2, text: '...', done: false }
    ]
  },
  getters: {
    doneTodos: state => {
      return state.todos.filter(todo => todo.done)
    }
  }
})
```

`store.getters` 객체에 노출되고, 속성으로 값에 접근이 가능. 그래서 getter로 쉽게 접근이 가능합니다.

```javascript
computed: {
  doneTodosCount () {
    return this.$store.getters.doneTodosCount
  }
}
```

mapGetter 헬퍼를 이용해 매핑도 가능하다

```javascript
import { mapGetters } from 'vuex'

export default {
  // ...
  computed: {
    // getter를 객체 전개 연산자(Object Spread Operator)로 계산하여 추가합니다.
    ...mapGetters([
      'doneTodosCount',
      'anotherGetter',
      doneCount: 'doneTodosCount' // 다른 이름으로 매핑하기
      // ...
    ])
  }
}
```

## Mutation

상태를 변이 시키는 핸들러로 이용한다. 보통은 동기적인 로직을 정의하는데 이용하고 비동기적인 로직은 Actions에서 많이 다룬다.

즉, Mutation안에서는 로직들이 순차적으로 일어나야 각 컴포넌트의 반영 여부를 제대로 추적할 수가 있다.

등록은 getters와 마찬가지로 mutations속성에 추가해주면 그만

```javascript
const store = new Vuex.Store({
  state: {
    count: 1
  },
  mutations: {
    increment (state) {
      // 상태 변이
      state.count++
    }
  }
})
```

해당 핸들러를 이용하고 싶다면 `store.commit("increment")`를 이용하면 된다. Mutation은 변수를 받을 수도 있는데 아래와 같이 이용하면 된다. 두번째 예제처럼 객체를 넣을 수도 있다

```javascript
// ...
mutations: {
  increment (state, n) {
    state.count += n
  }
}

store.commit('increment', 10)

// ...
mutations: {
  increment (state, payload) {
    state.count += payload.amount
  }
}

store.commit('increment', {
  amount: 10
})
```

import해서 매핑을 하는 방식도 어렵지 않다

```javascript
import { mapMutations } from 'vuex'

export default {
  // ...
  methods: {
    ...mapMutations([
      'increment' // this.increment()를 this.$store.commit('increment')에 매핑합니다.
    ]),
    ...mapMutations({
      add: 'increment' // this.add()를 this.$store.commit('increment')에 매핑합니다.
    })
  }
}
```

## Actions

Mutation과 유사하다(공식문서조차 이렇게 말한다). 몇가지 다른 점은

- 상태를 Mutation시키는 대신 Action으로 Mutation에 대한 커밋을 한다
- 작업에는 임의의 비동기 작업이 포함될 수 있다.

간단한 코드는 아래와 같다

```javascript
const store = new Vuex.Store({
  state: {
    count: 0
  },
  mutations: {
    increment (state) {
      state.count++
    }
  },
  actions: {
    increment (context) {
      context.commit('increment')
    }
  }
})
```

액션의 호출은 `store.dispatch('increment')`식으로 호출이 가능하다. 근데 이걸 굳이 왜 이용할까? Mutation은 동기적으로 처리할 때 좋고 Actions는 비동기적인 작업을 수행하는데 이용하는 것이 좋다.

Actions또한 Mutation처럼 파라미터를 받을 수 있다. 컴포넌트 내부에서 쓰는 것도 여타 다른 것들과 마찬가지로 이용하기 수비다

```javascript
import { mapActions } from 'vuex'

export default {
  // ...
  methods: {
    ...mapActions([
      'increment' // this.increment()을 this.$store.dispatch('increment')에 매핑

      // mapActions는 페이로드를 지원합니다.
      'incrementBy' // this.incrementBy(amount)를 this.$store.dispatch('incrementBy', amount)에 매핑
    ]),
    ...mapActions({
      add: 'increment' // this.add()을 this.$store.dispatch('increment')에 매핑
    })
  }
}
```

