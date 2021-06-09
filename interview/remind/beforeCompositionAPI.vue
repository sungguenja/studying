<template>
  <div>
    <h1>{{ countWithUnit }}</h1>
    <button @click="increase">Increas</button>
    <button @click="decrease">Decreas</button>
  </div>
</template>

<script>
export default {
  data() {
    return {
      count: 0
    }
  },
  computed: {
    countWithUnit() {
      return this.count + ' 입니다.'
    }
  },
  methods: {
    increase() {
      this.count++
    },
    decrease() {
      this.count--
    }
  }
}
</script>
