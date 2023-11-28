<template>
  <div>
    <h1>Index Component</h1>

    <h3>Query Params</h3>
    <p>
      {{ queryParam }}
    </p>
  </div>
</template>

<script setup>
import { ref, watch } from 'vue';
import { useRoute } from 'vue-router';

const route = useRoute();
const queryParam = ref('');

watch(() => route.params.q, (newVal) => {
  console.log('q', newVal);
  queryParam.value = newVal;
});
</script>

<style>
p {
  color: tomato;
  font-size: 4em;
}
</style>
