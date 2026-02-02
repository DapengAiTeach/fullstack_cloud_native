<script setup>
import {useCounterStore} from "@/store/counter.js";

const store = useCounterStore()
</script>
<template>
  <h1>首页 {{store.count}}</h1>
  <button @click="store.increment">+</button>
</template>