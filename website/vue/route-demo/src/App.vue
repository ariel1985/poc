<template>
  <img alt="Vue logo" src="./assets/logo.png">
  <IndexComponent />
</template>

<script>
import IndexComponent from './components/IndexComponent.vue'

export default {
  name: 'App',
  components: {
    IndexComponent
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

#app img {
  width: 250px;
  opacity: 0.6;
}
</style>
