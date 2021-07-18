# Vue.js 면접 예상 질문

[참고 깃허브](https://github.com/sudheerj/vuejs-interview-questions-korean/blob/master/README.md#VueJS%EC%9D%98-%EB%9D%BC%EC%9D%B4%ED%94%84%EC%82%AC%EC%9D%B4%ED%81%B4lifecycle-%ED%95%A8%EC%88%98%EB%8A%94)

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

## 14. 사용자 정의의 input컴포넌트에서 v-model을 사용하는 법은?

사용자 정의 input컴포넌트에서도 `v-model`은 활용할 수 있따. 아래와 같은 규칙을 지키자

1. input의 value를 props를 이용해 바인딩 한다

2. 새로운 값이 입력되는 input이벤트발생 시, 해당 값을 `emit`하여 상위 컴포넌트로 이벤트를 전달한다.

3. 사용 예시

   ```javascript
   Vue.component('custom-input', {
       props: ['value'],
       template: `
   		<input
   			v-bind:value="value"
   			v-on:input="$emit('input',$event.target.value)"
   		>
   	`
   })
   ```

   ```vue
   <custom-input v-model="searchInput"></custom-input>
   ```

위와같이 쉽게 바인딩 할 수 있다

## 15. slots?

부모 컴포넌트에서 자식 컴포넌트에게 html 탬플릿자체를 넘기고 싶을때 이용

```vue
<template>
	<!-- 부모 -->
	<ChildComponent>
    	<button slot="left">왼쪽 버튼</button>
        <button slot="right">오른쪽 버튼</button>
    </ChildComponent>
</template>
```

```vue
<template>
	<!-- 자식 -->
	<div>
        <slot name="left"></slot>
        <slot name="right"></slot>
    </div>
</template>
```

## 16. Transition

Vue에서는 항목들이 DOM에 추가, 갱신, 삭제될 때, 다양한 방법으로 트랜지션 효과를 입힐 수 있다

1. CSS 트랜지션과 애니메이션을 위한 클래스를 자동으로 적용
2. Animate.css와 같은 써드파티
3. 트랜지션 훅 중에 JavaScript를 사용해 DOM 조작
4. Velocity.js와 같은 애니매이션 라이브러리 통합

## 17. Vue router

Vue의 공식적인 라우팅 라이브러리

`<router-link>`태그로 간단히 이용 가능하고 아니면 직접 push하는 방식도 가능하다

동적 라우팅도 아주 쉽게 가능! 라우팅 우선 순위도 그냥 적는 순서대로 이다.

## 18. 관심사 분리

현대적인 UI 개발에서 코드베이스를 서로 얽혀있는 세 개의 거대한 레이어로 나누는 대신, 느슨하게 결합 된 컴포넌트를 나누고 구성하는 것이 더 중요하다.

싱글 파일 컴포넌트에 대한 아이디어가 마음에 안 들어도 JS, CSS 별도의 파일로 분리하여 핫 리로드 및 사전 컴파일 기능을 활용할 수 있다.

```vue
<template>
  <div>This section will be pre-compiled and hot reloaded</div>
</template>
<script src="./my-component.js"></script>
<style src="./my-component.css"></style>
```

## 19. 싱글 파일 컴포넌트의 필요 이유

1. 전역 정의: 모든 구성 요소에 대해 고유한 이름을 지정하도록 강요
2. 문자열 템플릿: 구문 강조가 약해 여러 줄로 된 HTML에 보기 안좋은 슬래시가 많이 필요합니다.
3. CSS 지원 없음: HTML 및 JS가 컴포넌트로 모듈화 되어 있으나 CSS가 빠져 있는 것을 말합니다.
4. 빌드 단계 없음: Pug 및 Babel과 같은 전처리기가 아닌 HTML 및 ES5 JavaScript로 제한

## 20. filter

텍스트 형식화를 위해 사용됩니다. 이 필터들은 자바스크립트 표현식에 파이프(`|`) 기호와 함께 추가 되어야 한다. 아래와 같은 경우에 사용할 수 있다. 첫 글자를 대문자로 만드는 예도 한번 보자

1. 중괄호 보간법
2. `v-bind` 표현식

```javascript
filters: {
    capitalize: function (value) {
        if (!value) return ''
        value = value.toString()
        return value.charAt(0).toUpperCase() + value.slice(1)
    }
}
```

이 필터를 중괄호 보간법 또는 v-bind를 이용해 사용할 수 있다

```vue
{{ username | capitalize }}

<div v-bind:id="username | capitalize"></div>
```

체이닝도 가능하다 `{{ message | filterA | filterB | .... }}`. 전역적 또는 지역적으로도 생성이 가능하다

1. 지역 필터: 컴포넌트의 옵션에서 정의할 수 있다. 이 경우, 필터는 해당 컴포넌트에서만 사용 가능

   위에 써놨던 것처럼 이용 가능하다

2. 전역 필터: Vue 인스턴스를 만들기 전에 전역적으로 필터를 정의할 수 있다. 이럴 경우 모든 컴포넌트에서 이용 가능

   ```javascript
   Vue.filter('capitalize', function (value) {
       if (!value) return ''
       value = value.toString()
       return value.charAt(0).toUpperCase() + value.slice(1)
   })
   ```

거기다 filter는 기본적으로 함수여서 인자를 전달하는 것도 가능하다. `{{ message | filterA('arg1', arg2) }}`

## 21. 플러그인

플러그인은 일반적으로 전역 수준 기능을 Vue 어플리케이션에 추가합니다

1. 전역 메소드 또는 속성 추가
2. 하나 이상의 글로벌 에셋 추가
3. 전역 믹스인으로 컴포넌트 옵션
4. `Vue.prototype`를 이용해 Vue에 인스턴스 메소드를 추가
5. 위의 기능과 함께 자체 API를 제공하는 라이브러리(vue-router)

만드는 방법은 플러그인에서 `install`메소드를 정의해야 한다. 이 메소드는 첫 번째 인자로 Vue 생성자와 외부에서 설정 가능한 옵션을 파라미터로 전달 받습니다.

```javascript
MyPlugin.install = function (Vue, options) {
    // 1. add global method or property
    Vue.myGlobalMethod = function () {
        // 로직 전개
    }
    
    // 2. add a global asset
    Vue.directive('my-directive', {
        bind (el, binding, vnode, oldVnode) {
            // 로직 전개
        }
    })
    
    // 3. inject some component options
    Vue.mixin({
        created: function () {}
    })
    
    // 4. add an instance method
    Vue.prototype.$myMethod = function (methodOptions) {
        
    }
}
```

사용하는 방법은 그저 vue.use를 이용하면 된다

```javascript
Vue.use(MyPlugin)

new Vue({
    // 옵션 나열
})
```

## 22. 믹스인

Mixins는 Vue 컴포넌트에 재사용 가능한 기능을 배포하는 유연한 방법입니다. 믹스인에 존재하는 기능들은 호출된 컴포넌트의 기능들과 합쳐집니다.

mixin 객체는 모든 구성 요소 옵션을 포함할 수 있다. 재사용될 수 있는 created라이프사이클 훅을 가진 믹스인을 예로 작성해보자

```javascript
const myMixin = {
  created(){
    console.log("Welcome to Mixins!")
  }
}
var app = new Vue({
  el: '#root',
  mixins: [myMixin]
})
```

전역 믹스인도 있다. Vue의 모든 컴포넌트에 영향을 줄 수 있다. 훅을 이용할 때는 조심해야한다

```javascript
Vue.mixin({
   created(){
     console.log("Write global mixins")
   }
})

new Vue({
  el: '#app'
})
```

cli환경에서는 `.js`파일로 작성하고 `export`키워드로 내보낸다고 선언해야 한다. 그리고 `import`로 가져올 수가 있다

충돌하는 경우는 다양하다

1. `data`는 재귀적으로 병합하되, 충돌되는 속성은 컴포넌트의 데이터가 우선적으로 병합

   ```javascript
   var mixin = {
     data: function () {
       return {
         message: 'Hello, this is a Mixin'
       }
     }
    }
   new Vue({
     mixins: [mixin],
     data: function () {
       return {
         message: 'Hello, this is a Component'
       }
     },
     created: function () {
       console.log(this.$data); // => { message: "Hello, this is a Component'" }
     }
   })
   ```

2. 라이프사이클 훅 함수는 믹스인 함수가 먼저 실행되고 컴포넌트 함수가 실행된다.

   ```javascript
   const myMixin = {
     created(){
       console.log("Called from Mixin")
     }
   }
   
   new Vue({
     el: '#root',
     mixins:[myMixin],
     created(){
       console.log("Called from Component")
     }
   })
   
   //Called from Mixin
   //Called from Component
   ```

3. `methods`, `components`, `directives`역시 재귀적으로 병합한다. 충돌하는 것이 있을 경우 컴포넌트가 우선권을 갖는다

그런데 병합 방법을 우리가 정의할 수도 있다. `Vue.config.optionMergeStrategied`에 함수를 추가할 필요가 있다. 아니면 Vuex를 이용하는 방법도 있다.

```javascript
Vue.config.optionMergeStrategies.myOption = function (toVal, fromVal) {
  // return mergedVal
}

// vuex이용해보기
const merge = Vue.config.optionMergeStrategies.computed
Vue.config.optionMergeStrategies.vuex = function (toVal, fromVal) {
  if (!toVal) return fromVal
  if (!fromVal) return toVal
  return {
    getters: merge(toVal.getters, fromVal.getters),
    state: merge(toVal.state, fromVal.state),
    actions: merge(toVal.actions, fromVal.actions)
  }
}
```

## 23. 사용자 정의 지시자

`v-`로 시작하는 것을 우리가 만들 수도 있다. 기본적으로 DOM 제어하기 위해 직접 접근해야할 필요가 있을 때 유용하게 사용된다. 페이지가 로드될 때 `input`에 자동으로 포커싱되는 사용자 정의 지시자를 전역으로 만들어봅시다.

```javascript
// Register a global custom directive called 'v-focus'
Vue.directive('focus', {
    // When the bound element is inserted into the DOM
    inserted: function (el) {
    	// Focus the element
   		el.focust
	}
})
```

```vue
<input v-focus>
```

등록을 할 때는 directives옵션을 이용하면 어렵지 않게 이용이 가능하다. 그리고 지시된 컴포넌트에서만 이용가능하다

```javascript
directives: {
    focus: {
        inserted: function (el) {
            el.focus()
        }
    }
}
```

지시자가 제공하는 라이프 사이클 훅은 아래와 같다

1. bind: 지시자가 처음 앨리먼트에 부착될 때 한 번 호출됩니다.
2. inserted: 지시자가 부착된 앨리먼트가 DOM에 삽입되었을 때 호출
3. ipdate: 해당 앨리먼트가 업데이트 될 때 호출. 하지만 아직 하위 앨리먼트는 업데이트 되지 않은 상태
4. componentUpdated: 하위 컴포넌트까지 업데이트 된 상태일 때 호출됩니다.
5. unbind: 지시자가 엘리먼트에서부터 삭제될 때 호출

전달인자는 다양하게 있고 보통 아래처럼 표현한다

1. el: 해당 지시자가 부착된 앨리먼트로, 이를 이용해 DOM을 조작할 수 있습니다.
2. binding: 아래의 속성을 가진 객체이다
   1. name: 지시자의 이름으로, v- 접두사가 제거된 이름
   2. value: 지시자에서 전달 받은 값. ex) `v-my-directive="1+1"`이라면 2를 전달받는다
   3. oldValue: 이전 값으로 update와 componentUpdated 훅에서만 사용할 수 있다. 이를 통해 값이 변경되었는지 아닌지 확인 가능
   4. expression: 문자열로 바인딩된 표현식. ex) `v-my-directive="1+1"`이라면 "1+1"를 전달받는다
   5. arg: 지시자의 전달인자이다.  ex) `v-my-directive:foo`이라면 foo가 된다
   6. modifiers: 수식어가 포함된 객체입니다. 만약 `v-my-directive.foo.bar`라면 `{ foo: true, bar: true }`가 됩니다.
3. vnode: Vue의 컴파일러에 의해 생성된 가상 노드
4. oldVnode: 이 전의 가상 노드, update와 componentUpdated 훅에서만 사용할 수 있다.

한번에 여러값을 인수받는 것도 가능하다 아래와 같은 대표적인 예

```vue
<div v-avatar="{ width: 500, height: 400, url: 'path/logo', text: 'Iron Man' }"></div>
```

```javascript
Vue.directive('avatar', function (el, binding) {
  console.log(binding.value.width) // 500
  console.log(binding.value.height)  // 400
  console.log(binding.value.url) // path/logo
  console.log(binding.value.text)  // "Iron Man"
})
```

## 24. render 함수

사용하는 이유? 일반적인 경우 HTML을 작성하는 것을 권장한다. 하지만 input이나 slot의 값을 이용해 동적인 컴포넌트가 필요할 경우 JS가 필요하다. 그럴 경우 render 함수를 사용하여 이용할 수가 있다

render함수는 `createElement`라는 함수를 첫번째 인자로 받아 가상 노드를 생성한다. 내부적으로 Vue의 탬플릿은 빌드 타임에서 render함수를 이용해 컴파일하고 있습니다. 아래의 예와 같이 작성이 가능하다.

```vue
<template>
 <div :class="{'is-rounded': isRounded}">
   <p>Welcome to Vue render functions</p>
 </div>
</template>
```

위 탬플릿을 아래와 같이 render함수를 이용해서 만들 수가 있다

```javascript
render: function (createElement) {
   return createElement('div', {
     'class': {
         'is-rounded': this.isRounded
     }
   }, [
     createElement('p', 'Welcome to Vue render functions')
   ]);
  },
```

그렇다면 `createElement`이 놈은 무엇인가? 몇가지 약속된 전달인자를 받아 탬플릿에 사용되는 기능을 코드로 작성할 수 있게 해주는 놈이다. 이것은 [공식문서](https://vuejs.org/v2/guide/render-function.html#The-Data-Object-In-Depth)를 읽어볼 수 있도록 하자

그렇다면 가상 노드를 여러번 사용할 수 있을까? 물론 가능하다! 여러번 사용하고 싶다면 팩토리 패턴을 이용해 작성해야 한다. 아래 두 예를 보자. 첫번째는 안되는 예고 두번째 예는 가능한 예이다

```javascript
render: function (createElement) {
  var myHeadingVNode = createElement('h1', 'This is a Virtual Node')
  return createElement('div', [
    myHeadingVNode, myHeadingVNode, myHeadingVNode
  ])
}
```

```javascript
render: function (createElement) {
  return createElement('div',
    Array.apply(null, { length: 3 }).map(function () {
      return createElement('h1', 'This is a Virtual Node')
    })
  )
}
// 이것이 팩토리 패턴이다.
```

## 25. Vue, React, Angular

1. Vue vs React

   1. 공통점

      1. 둘 다 가상 DOM 모델을 사용한다
      2. 반응적이고 조합 가능한 컴포넌트를 제공
      3. 코어 라이브러리에만 집중하고 있고, 라우팅 및 상태 관리와 같은 라이브러리가 부가적으로 존재

   2. 차이점

      | 특징              | Vue                       | React                   |
      | ----------------- | ------------------------- | ----------------------- |
      | 타입              | JavaScript MVC 프레임워크 | JavaScript 라이브러리   |
      | 플랫폼            | 웹을 우선                 | 웹과 네이티브 모두      |
      | 복잡도            | 상대적으로 간단           | 상대적으로 복잡         |
      | 빌드 어플리케이션 | Vue-cli                   | CRA(`Create-React-App`) |

   3. Vue가 나은점

      1. 가볍고 빠름
      2. 템플릿이 있어서 개발 과정을 쉽게 만들어준다
      3. JSX에 비해 가벼운 JavaScript 문법을 사용

   4. React가 나은 점

      1. 큰 규모의 어플리케이션을 유연하게 제작 가능
      2. 테스트가 쉬움
      3. 모바일 앱 제작에도 적합
      4. 생태계가 크고 풍부

2. Vue vs Angular

   1. 차이점

      | 특징          | Vue                      | AngularJS                                        |
      | ------------- | ------------------------ | ------------------------------------------------ |
      | 복잡도        | 배우기 쉬운 API와 디자인 | 프레임워크가 꽤 크고 타입스크립트 등의 지식 필요 |
      | 데이터 바인딩 | 양방향 바인딩            | 단방향 바인딩                                    |
      | 초기 릴리즈   | 2014                     | 2016                                             |
      | 모델          | 가상 DOM 기반            | MVC                                              |
      | 작성된 언어   | JavaScript               | TypeScript                                       |

## 26. 동적 컴포넌트

동적으로 컴포넌트를 선택해서 받는것도 가능하다. 아래와 같이 해보자. `v-bind:is`를 이용해 동적으로 선택 가능

```vue
<div id="app">
   <component v-bind:is="currentPage">
       <!-- component changes when currentPage changes! -->
       <!-- output: Home -->
   </component>
</div>

<script>
export default {
    data() {
    	return {currentPage: 'home'}
    },
    components: {
        home: {
            template: "<p>Home</p>"
        },
        about: {
          template: "<p>About</p>"
        },
        contact: {
          template: "<p>Contact</p>"
        }
  	}
}
</script>
```

