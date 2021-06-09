<template>
  <div>
    <h1>{{ countWithUnit }}</h1>
    <button @click="increase">Increas</button>
    <button @click="decrease">Decreas</button>
  </div>
</template>

<script>
import { ref, computed } from '@vue/composition-api'

const useCount = () => {
  const count = ref(0);
  const countWithUnit = computed(() => count.value + ' 입니다!')

  const increase = () => { count.value++ }
  const decrease = () => { count.value-- }

  return { countWithUnit, increase, decrease }
}

export default {
  setup() {
    const { countWithUnit, increase, decrease } = countWithUnit()

    return {
      countWithUnit,
      increase,
      decrease
    }
  },
}
</script>
