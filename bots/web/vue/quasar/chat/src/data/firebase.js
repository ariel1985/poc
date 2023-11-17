// Import the functions you need from the SDKs you need
import { initializeApp } from 'firebase/app'
// import { getAnalytics } from 'firebase/analytics'

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
// const firebaseConfig = {
//   apiKey: 'AIzaSyCuclf7U-GAxjpg4gLzKczj-Q8OVDMwyRc',
//   authDomain: 'gamerim-m3.firebaseapp.com',
//   projectId: 'gamerim-m3',
//   storageBucket: 'gamerim-m3.appspot.com',
//   messagingSenderId: '735691002025',
//   appId: '1:735691002025:web:7ce8288474858d533699b8',
//   measurementId: 'G-HQE49HZLXR'
// }
const firebaseConfig = {
  apiKey: 'AIzaSyAxh3ftiHVpPKuOtX9ZA9SBVlS-22BIyLM',
  authDomain: 'chats-96d05.firebaseapp.com',
  projectId: 'chats-96d05',
  storageBucket: 'chats-96d05.appspot.com',
  messagingSenderId: '964263076072',
  appId: '1:964263076072:web:3c85e4974ec841bf4c695d',
  measurementId: 'G-HB5ER5VQ2Q'
}

// Initialize Firebase
const app = initializeApp(firebaseConfig)
console.log('firebase app', app)

// const analytics = getAnalytics(app)
// console.log(analytics)
