# Composition API

[vue3에서](https://v3.vuejs-korea.org/ko-kr/api/composition-api.html) [실제예에서의 composition api](https://velog.io/@ausg/Vue2-%EC%93%B0%EC%84%B8%EC%9A%94-Composition-API-%ED%95%9C%EB%B2%88-%EB%93%9C%EC%85%94%EB%B3%B4%EC%84%B8%EC%9A%94) [참고자료](https://chodragon9.github.io/blog/composition-api-rfc-migration/#%ED%94%8C%EB%9F%AC%EA%B7%B8%EC%9D%B8) [참고자료2](https://m.blog.naver.com/dndlab/221952030079)

npm을 이용해 쉽게 설치가 가능하다 `npm install @vue/composition-api` 플러그인을 아래와 같이 사용 가능

```javascript
import Vue from 'vue'
import VueCompositionApi from '@vue/composition-api'

Vue.use(VueCompositionApi)
```

`@vue/composition-api`가 변경 되었을 때 이를 사용하는 개발자는 API 변경/삭제에 대한 권한이 없다. 그래서 업데이트가 되는 순간 프로젝트에 직접적인 영향을 전파하게 된다. 의존성을 낮추기 위해 Wrapper패턴을 사용할 수가 있다

사용할 기능만 따로 만들어서 export하도록 하는 방법이다

```javascript
export {
  defineComponent,
  onMounted,
  onBeforeMount,
  ref,
  reactive,
  toRefs,
  computed,
  watch
} from '@vue/composition-api'
```

그리고 이제 사용받는 쪽에서는 필요한 것만 받는 것이다

```vue
<template>
</template>

<script lang="ts">
import { defineComponent, ref } from '~/vue-wrapper'

export default defineComponent({
  props: {
    id: String,
    label: String,
    disabled: Boolean,
    checked: Boolean
  },
  setup(props, context) {
    const isChecked = ref(props.checked)
    const toggleCheckBox = (): void => {
      isChecked.value = !isChecked.value
      context.emit('on-change', isChecked.value)
    }

    return { isChecked, toggleCheckBox }
  }
})
</script>
```

Wrapper 패턴을 적용하면 앞서 언급한 형태는 `Custom Component => Vue Wrapper => Vue` 이렇게 변경되기에 Vue Wrapper만 수정하면 된다. 적용하지 않으면 Custom Component를 수정해야 한다는 문제점이 크다

기존 vue와 composition api를 도입한 vue와 비교해보자

```vue
<template>
    <div>
        <h1>Count: {{ count }}</h1>
        <h1>Double: {{ double }}</h1>
        <button @click="increase">increase</button>
        <button @click="decrease">decrease</button>
    </div>
</template>

<script>

export default {
    data () {
        return {
            count: 0,
        }
    },
    methods: {
        increase () {
            ++this.count;
        },
        decrease () {
            --this.count;
        }
    },
    computed: {
        double () {
            return this.count * 2;
        }
    }
}
</script>
```

```vue
<template>
    <div>
        <h1>Count: {{ count }}</h1>
        <h1>Double: {{ double }}</h1>
        <button @click="increase">increase</button>
        <button @click="decrease">decrease</button>
    </div>
</template>

<script>
import { reactive, computed } from '@vue/composition-api';

const useCount = () => {
    const count = ref(0);
    const double = computed(() => count.value * 2);

    const increase = () => ++state.count;
    const decrease = () => --state.count;

    return { count, double, increase, decrease }
}

export default {
    setup () {
        const { count, double, increase, decrease } = useCount();

        return {
            count,
            double,
            increase,
            decrease
        }
    }
}
</script>
```

setup은 새로 추가된 라이프 사이클 훅으로써, Composition API를 사용하기 위한 초기화 지점. 각 훅은 아래와 같이 수정된다.

- ~~beforeCreate~~ => setup
- ~~created~~ => setup
- beforeMount => onBeforeMount
- mounted => onMounted
- beforeUpdate => onBeforeUpdate
- updated => onUpdated
- beforeDestroy => onBeforeUnmount
- destroyed => onUnmounted
- errorCaptured => onErrorCaptured
- 새로 추가된 훅
  - onRenderTracked
  - onRenderTriggered

## reactive

reactive는 반응형 상태를 선언해 주는 역할을 합니다. `const getObject = reactive({ index: 1 })` 같은 형태로 쓸 수가 있다. 객체만을 받을 수가 있고 인자로 받은 객체와 동일한 프록시 객체를 반환합니다.

## ref

```javascript
const count = ref(0);
console.log(count.value); // 0

count.value++;
console.log(count.value); // 1
```

ref는 내부 값을 가져와 반응, 변경 가능한 객체를 반환한다. value로 내부 값에 접근

## computed

```javascript
const count = ref(1);
const plusOne = computed(() => count.value + 1);

console.log(plusOne.value); // 2

plusOne.value++; // error
```

computed는 getter함수를 가져오고 getter에서 반환된 값에 대한 변경 불가능한 반응성 참조 객체를 반환합니다.

## 템플릿에서 액세스하는 방법

```vue
<template>
    <div>{{ count }}</div>
</template>

<script>
export default {
    setup() {
        return {
            count: ref(0)
        }
    }
}
</script>
```

랜터 컨텍스트(setup에서 반환된 객체)에서 ref가 속성으로 반환되고 템플릿에서 액세스 하게 되면 자동으로 내부 값으로 래핑이 해제되므로 따로 템플릿에서 액세스 할 때는 .value를 추가할 필요는 없고 기존과 동일하게 사용하면 됩니다.

