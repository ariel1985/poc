// src/boot/firebaseConfig.js

import firebase from 'firebase/app'
import 'firebase/database'
import { rtdbPlugin } from '@vuefire/core'

// Your web app's Firebase configuration
const firebaseConfig = {
  apiKey: 'YOUR_API_KEY',
  authDomain: 'YOUR_AUTH_DOMAIN',
  databaseURL: 'YOUR_DATABASE_URL',
  projectId: 'YOUR_PROJECT_ID',
  storageBucket: 'YOUR_STORAGE_BUCKET',
  messagingSenderId: 'YOUR_MESSAGING_SENDER_ID',
  appId: 'YOUR_APP_ID'
}

// Initialize Firebase
const firebaseApp = firebase.initializeApp(firebaseConfig)
const db = firebaseApp.database()

export default function (/* { app, router, Vue ... } */) {
  // In Vue 2, you need to manually install the plugin into the Vue instance
  Vue.use(rtdbPlugin)
}

export { db }
