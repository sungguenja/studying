# Vue.js 면접 예상 질문

## 1. VueJS란 무엇인가

Vue.js는 사용자 인터페이스를 만들기 위한 진보적인 프레임워크이다. 핵심 라이브러리는 `뷰 레이어`만 초점을 맞추어, 다른 라이브러리나 기존 프로젝트와의 통합이 쉽다

## 2. VueJS의 주요 특징

1. 가상 DOM: 다른 프레임워크들과 비슷하게 가상 DOM을 사용하여 바뀐 부분만 바꾸는 방식을 취하고 있다.
2. 컴포넌트: 재사용할 수 있는 앨리먼트들을 만들 수가 있다
3. 템플릿: VueJS는 Vue인스턴스 데이터와 DOM에 접근할 수 있는 HTML 기반 템플릿을 제공
4. 라우팅: 페이지 전환에 vue-router를 이용
5. 저용량: 가볍다!

## 3. VueJS의 라이프사이클

1. Creation(초기화): Create 훅은 컴포넌트가 DOM에 추가되기 전에 실행되는 단계. 클라이언트와 서버가 렌더링 단계 전에 컴포넌트에 설정해야 할 것들이 있을 때 사용하는 단계. 다른 훅과는 다르게 Create 훅은 서버 사이드 렌더링에서도 지원되는 훅입니다

   1. beforeCreate: 컴포넌트 초기화 단계 중 가장 처음 실행. 컴포넌트의 data를 관찰하고, 이벤트를 초기화한다. 아직 data는 반응적이지 않고, 이벤트 역시 설정되지 않은 상태

      ```vue
      <script>
      export default {
          data() {
              return {
                  count: 10
              }
          },
          beforeCreate() {
              console.log(this.count); // count is undefined
          }
      }
      </script>
      ```

   2. created: data를 관찰할 때 발생. 템플릿은 아직 마운트되거나 렌더링은 안되있지만 이벤트들이 활성화되며 data에 반응적이다

      ```vue
      <script>
      export default {
          data() {
              return {
                  count: 10
              }
          },
          created() {
              console.log(this.count); // 10
          }
      }
      </script>
      ```

2. Mount(DOM 추가): 가장 많이 사용되는 단계. 렌더링 되기 직전 or 직후에 컴포넌트에 접근하는 단계

   1. beforeMount: 컴포넌트가 DOM에 추가되기 직전
   2. mounted: 반응적인 data, 템플릿, 렌더링된 DOM 모두에 접근이 가능. (그래서 가장 많이 쓰임) 흔히 컴포넌트에서 필요한 데이터를 외부에서 가져오는(fetch) 용도로 많이 사용

3. Updating(재 렌더링): 컴포넌트 내부의 반응적인 속성이 변했건, 그 외의 것들이 재 렌더링을 일으킬 때 실행되는 단계

   1. beforeUpdate: data가 변경되어 업데이트 사이클이 시작될 때 실행
   2. updated: data가 변하여 재 렌더링이 일어난 직후에 실행

4. Destruction(해체): 컴포넌트를 더 이상 사용하지 않을 때 사용하는 단계

   1. beforeDestroy: 컴포넌트가 해체되기 직전에 실행됩니다. 반응적인 이벤트들 or data들을 해체하는 훅으로 적합.

      ```vue
      <script>
      export default {
          data() {
              return {
                  count: 10
              }
          },
          beforeDestroy() {
              this.count = null;
              delete this.count;
          }
      }
      </script>
      ```

   2. destroyed: 컴포넌트가 해체되고 난 직후에 호출됩니다. 모든 지시자들의 바인딩이 해제되었고 이벤트 리스너가 제거된 상태

## 4. 조건부 지시자

조건이 true일 경우 해당 컴포넌트를 보여주는 지시자들이며 `v-if`,`v-else`,`v-else-if`,`v-show`가 있다.

1. v-if

   모든 언어들의 if와 같은 효과로 if안에 있는 것이 true일 경우 해당 DOM을 추가, false일 경우 제거하는 방식이다.

2. v-else

   if의 조건이 맞지 않을 경우 해당 컴포넌트를 보여주는 방식

3. v-else-if

   else if의 효과

4. v-show

   안에 있는 것이 true일 경우 보여주는데 이것의 특이점은 DOM에 추가된 상태로 보여주고 안보여주고를 진행한다. 즉, 자주 display가 on/off 전환되는 것을 이걸로 토글해주면 DOM조작을 하지 않는 장점이 있다.

   v-if에 비해 초기 비용이 들고 `<template>`태그에는 사용할 수 없다

## 5. v-for

반복적인 것을 렌더링 하는 경우 이용한다, `<template>`에도 이용이 가능하다

```vue
<!-- array -->
<ul id="list">
  <li v-for="(item, index) in items">
    {{ index }} - {{ item.message }}
  </li>
</ul>

var vm = new Vue({
  el: '#list',
  data: {
    items: [
      { message: 'John' },
      { message: 'Locke' }
    ]
  }
})

<!-- Object -->
<div id="object">
  <div v-for="(value, key, index) in user">
    {{ index }}. {{ key }}: {{ value }}
  </div>
</div>

var vm = new Vue({
  el: '#object',
  data: {
    user: {
      firstName: 'John',
      lastName: 'Locke',
      age: 30
    }
  }
})
```

직접 호출하는 방식도 가능 하다

```vue
<div>
    <span v-for="n in 20">{{ n }}</span>
</div>
```

## 6. Vue 인스턴스

모든 Vue 애플리케이션은 Vue 함수를 이용해 Vue 인스턴스를 생성하면서 동작한다. `vm(ViewModel의 약어)`이라는 변수를 이용해 Vue인스턴스를 참조한다

```javascript
var vm = new Vue({
    // options
})
```

## 7. 여러 엘리먼트들을 한 번에 조건부로 나타낼 때

```vue
<template v-if="isTrue">
	<h1>
        hi
    </h1>
	<p>
        adsfsadf
    </p>
</template>
```

## 8. key 속성을 이용해 엘리먼트를 재사용하는 방법

Vue는 가능한 한 효율적으로 렌더링하려한다. 그래서 생기는 문제점이 있는데 아래 코드를 보자

```vue
<template v-if="loginType === 'Admin'">
	<label>Admin</label>
	<input placeholder="Enter your ID">
</template>
<template v-else>
	<label>Guest</label>
	<input placeholder="Enter your name">
</template>
```

이럴 경우에 `input`태그는 조건문에 따라 바뀌지 않고 최초에 렌더링 된 엘리먼트의 상태를 유지하고 있는다. 그러니 이런 경우 재사용을 막기 위해서는 key속성을 이용해 두 개의 input태그가 별개의 것으로 취급되도록 해야한다

```vue
<template v-if="loginType === 'Admin'">
  <label>Admin</label>
  <input placeholder="Enter your ID" key="admin-id">
</template>
<template v-else>
    <label>Guest</label>
    <input placeholder="Enter your name" key="user-name">
</template>
```

## 9. v-for에서 key속성이 필요한 이유

vue는 재사용/재엉렬을 중요시 여긴다. v-for을 쓰면 모든 반복적으로 나온 노드들을 재사용하려고 하기 때문에 key값을 부여해서 구분해야 한다.

## 10. 배열,객체과 관련된 것들

vue는 배열,객체 변화에 대해 업데이트 일으키질 않는다. vue의 함수들을 이용해야 업데이트를 일으킨다.

1. push()
2. pop()
3. shift()
4. unshift()
5. splice()
6. sort()
7. reverse()
8. 사용법의 예: `vm.todos.push({ message: 'Baz' })`

배열을 대체하는 함수도 있다. 원본 배열을 수정하지 않고, 새로운 배열을 반환하는 것들이다.

1. filter()

2. concat()

3. slice()

4. ```javascript
   vm.todos = vm.todos.filter(function (todo) {
       return todo.status.match(/Completed/)
   })
   ```

어떠한 경우 vue는 배열의 변화를 감지 하지 못할까?

1. 인덱스로 배열에 있는 항목을 직접 할당하는 경우

   1. 업데이트 감지 하지 못하는 수정 방법

      `vm.todos[indexOfTodo] = newTodo`

   2. 업데이트를 감지하는 수정 방법

      1. `Vue.set(vm.todos, indexOfTodo, newTodoValue)`
      2. `vm.todos.splice(indexOfTodo, 1, newTodoValue)`

2. 배열의 길이를 수정하는 경우

   1. 업데이트를 감지 하지 못하는 수정 방법

      `vm.todos.length = todosLength`

   2. 감지하는 방법

      `vm.todos.splice(todosLength)`

객체도 위와 같은 상황을 보인다.

1. 직접 접근하여 업데이트를 감지하지 못하는 경우

   ```javascript
   var vm = new Vue({
     data: {
       user: {
         name: 'John'
       }
     }
   })
   
   // `vm.name` is now reactive
   
   vm.email = john@email.com // `vm.email` is NOT reactive
   ```

2. 업데이트를 감지시키는 방법

   1. `Vue.set(vm.user,'email', 'john@email.com')`
   2. `vm.user = Object.assign({}, vm.user, {john@email.com})`

## 11. 이벤트 핸들러

`$event` 변수를 이용해 이벤트 핸들러를 호출해 사용할 수 있다

```vue
<button v-on:click="show('Welcome to VueJS world', $event)">
    Submit
</button>

<script>
export default {
    methods: {
        show(message, event) {
            if (event) event.preventDefault()
            console.log(event,message);
        }
    }
}
</script>
```

원래 자바스크립트에는 `event.preventDefault()` 또는 `event.stopPropagation()`을 제공한다. Vue의 메소드 내부에서도 이 작어블 할 수 있찌만, DOM에서 발생한 이벤트와 메소드의 로직은 별개로 구분하는 것이 좋다. 이 문제를 해결하기 위해 `v-on`이벤트에 수식어를 제공하여 사용할 수 있다.

1. .stop

2. .prevet

3. .capture

4. .self

5. .once

6. .passive

7. 사용예

   ```vue
   <!-- the click event's propagation will be stopped -->
   <a v-on:clicl.stop="methodCall"></a>
   ```

   체이닝도 가능하다

   ```vue
   <!-- modifiers can be chained -->
   <a v-on:click.stop.prevent="doThat"></a>
   ```

그리고 키보드 이벤트에 대한 수식어로 키 수식어도 제공한다. 키코드를 이용할 수도 있고 특정 자주 사용되는 키보드들은 별칭도 제공하고 있다.

키 수식어를 커스터 마이징도 할 수가 있다. `config.keyCodes`객체를 이용하며 아래와 같은 규칙이 있다.

1. 카멜 케이스를 대신 쌍따옴표로 감싸진 케밥 케이스를 사용해야 한다

2. 배열을 이용해 한 번에 여러 값들을 정의할 수 있습니다.

   ```javascript
   Vue.config.keyCodes = {
       fi: 112,
       "media-play-pause": 179,
       down: [40,87]
   }
   ```

시스템 수식어도 이벤트 발생이 가능하다 `.ctrl`,`.alt`,`.shift`,`.meta` 가 있고 아래와 같이 사용이 가능하다

```vue
<!-- Ctrl + Click -->
<div @click.ctrl="doSomething">
    Do Something
</div>
```

마우스 버튼 수식어도 가능하다. `.left`,`.right`,`.middle`이 존재하며 아래와 같이 사용이 가능하다

```vue
<button
        v-if="button === 'right'"
        v-on:mousedown.right="increment"
        v-on:mousedown.left="decrement"
/>
```

## 12. v-model

v-model을 통해 데이터를 양방향 바인딩이 가능하다

```vue
<input v-model="message" placeholder="Enter input here">
<p>
    The message id: {{ message }}
</p>
```

v-model은 html속성으로 선언된 value, checked, selected를 무시한다. 그리고 수식어도 존재한다

1. lazy: 기본적으로 키입력하나마다 이벤트가 발생하지만 이를 방지하기 위해 `.lazy`수식어를 이용할 수 있따

   ```vue
   <!-- synced after "change" instead of "input" -->
   <input v-model.lazy="msg">
   ```

2. number: 인풋받는 모든 자료형을 `Number`로 변환한다. 숫자 자료형이 필요하다면 이용하면 좋다. 왜냐하면 type="number"을 이용해도 자료형은 문자열로 들어오기 때문이다

   ```vue
   <input v-model.number="age" type="number">
   ```

3. trim: `.trim` 수식어를 사용자 입력의 첫과 끝의 공백을 제거해준다

## 13. 컴포넌트?

재사용 가능하면서 이름이 명명된 Vue 인스턴스이다. 컴포넌트는 Vue처럼 data, computed, watch, methods, 라이프 사이클 옵션을 갖고 있다.

props를 통해 상위 컴포넌트의 정보를 하위 컴포넌트로 전달할 수도 있다.

```javascript
Vue.component('todo-item', {
    props: ['title'],
    template: '<h2>{{title}}</h2>'
})
```

```vue
<!-- 상위 컴포넌트 -->
<template>
	<ChildComponent :stats="stats"></ChildComponent>
</template>

<script>
import ChildComponent from '주소'
export default {
    data() {
        return {
            stats: []
        }
    },
    components: {
        ChildComponent
    }
}
</script>

<!-- 하위 컴포넌트 -->
<template>
	{{stats}}
</template>

<script>
export default {
    props: {
        stats: Array // 타입을 명시해줘야 함
    }
}
</script>
```

`$event`객체를 이용해 상위 컴포넌트로 이벤트를 발생시킬 수도 있다. 떠한 `$emit`을 이용해보자

```javascript
Vue.component('todo-tem', {
  props: ['todo'],
  template: `
    <div class="todo-item">
      <h3>{{ todo.title }}</h3>
      <button v-on:click="$emit('increment-count', 1)">
        Add
      </button>
      <div v-html="todo.description"></div>
    </div>
  `
})
```

이렇게 되어있는 경우 상위 컴포넌트에서는 `v-on`을 이용해 이벤트 리스닝이 가능하다

```vue
<ul v-for="todo in todos">
 <li>
   <todo-item
     v-bind:key="todo.id"
     v-bind:todo="todo"
     v-on:increment-count="total += 1">
   </todo-item>
 </li>
</ul>
<span> Total todos count is {{total}}</span>
```

