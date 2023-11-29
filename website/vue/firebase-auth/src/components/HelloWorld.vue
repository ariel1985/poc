<script setup>
import { ref } from 'vue'
import { defineProps } from 'vue'
import { auth } from '@/firebase'
import {
  createUserWithEmailAndPassword,
  // signInWithEmailAndPassword,
  // signOut,
  // onAuthStateChanged
} from 'firebase/auth'

defineProps({
  title: String
})
const data = ref({
  email: '',
  password: '',
  user: null,
  error: null
})
const mode = ref('register')
// const user = ref(null)
const errors = ref(null)

function toggleMode(mode) {
  mode.value = mode
}

function login() {
  console.log('login')
  // signInWithEmailAndPassword(auth, data.value.email, data.value.password)
  //   .then(userCredential => {
  //     data.value.user = userCredential.user;
  //     console.log('userCredential', userCredential)
  //   })
  //   .catch(error => {
  //     console.log('error', error.message)
  //     data.value.error = error.message;
  //     errors.value = error.message;
  //   });
}

function register() {
  console.log('register')
  createUserWithEmailAndPassword(auth, data.value.email, data.value.password)
    .then(userCredential => {
      console.log('userCredential', userCredential)
      data.value.user = userCredential.user;
    })
    .catch(error => {
      console.log('error', error)
      data.value.error = error.message;
      errors.value = error;
    });
}

function logout() {
  console.log('logout')
  // signOut(auth)
  //   .then(() => {
  //     data.value.user = null;
  //   })
  //   .catch(error => {
  //     data.value.error = error.message;
  //     errors.value = error.message;
  //   });
}

function submit() {
  console.log('submit - mode value: ', mode.value)
  if (mode.value === 'login') {
    login()
    logout()
  } else {
    register()
  }
}

// onAuthStateChanged(auth, user => {
//   console.log('user', user)
//   data.value.user = user;
// })
</script>

<template>
  <div class="container">
    <h1 class="title"> {{ title }}</h1>
    <!-- <div v-if="user">
                      Welcome { { user?.email } }
                      <button @click="logout">Logout</button>
                    </div> -->
    <form @submit.prevent="submit" class="form">

      <div class="form-group">
        <label for="email"> Email </label>
        <input type="email" id="email" v-model="data.email" placeholder="Email" />
      </div>
      <div class="form-group">
        <label for="password"> Password </label>
        <input type="password" id="password" v-model="data.password" placeholder="Password" />
      </div>

      <button type="submit" class="submit-btn"> {{ mode === 'login' ? 'Login' : 'Register' }}</button>

      <div @click="toggleMode(mode === 'login' ? 'Login' : 'Register')" class="toggle-mode">
        {{ mode === 'login' ? 'Already a user? Login' : 'Not yet a user? Register' }}
      </div>

      <div class="error-message" v-if="errors">{{ errors }}</div>

    </form>
  </div>
</template>

<style scoped>
.title {
  text-align: center;
  margin-bottom: 20px;
  font-size: 2em;
  background: linear-gradient(to right, #007BFF, #00FFA3);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

.container {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  height: 100vh;
  background-color: #f4f4f4;
}

.form {
  background-color: #fff;
  padding: 20px;
  border-radius: 5px;
  box-shadow: 0px 0px 10px 0px rgba(0, 0, 0, 0.1);
  max-width: 500px;
  width: 100%;
}

.form-group {
  margin-bottom: 15px;
}

.form-group label {
  display: block;
  margin-bottom: 5px;
}

.form-group input {
  width: 99%;
  padding: 10px 0 10px 10px;
  border-radius: 5px;
  border: 1px solid #ddd;
}

.submit-btn {
  background-color: #007BFF;
  color: #fff;
  padding: 10px 15px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

.toggle-mode {
  margin-top: 15px;
  cursor: pointer;
  color: #007BFF;
}

.error-message {
  color: #ff0000;
  background-color: #ffe6e6;
  padding: 10px;
  border-radius: 5px;
  margin: 20px 0;
}
</style>
