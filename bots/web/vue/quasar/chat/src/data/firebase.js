// Import the functions you need from the SDKs you need
import { initializeApp } from 'firebase/app'
import { getAnalytics } from 'firebase/analytics'
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: 'AIzaSyCuclf7U-GAxjpg4gLzKczj-Q8OVDMwyRc',
  authDomain: 'gamerim-m3.firebaseapp.com',
  projectId: 'gamerim-m3',
  storageBucket: 'gamerim-m3.appspot.com',
  messagingSenderId: '735691002025',
  appId: '1:735691002025:web:7ce8288474858d533699b8',
  measurementId: 'G-HQE49HZLXR'
}

// Initialize Firebase
const app = initializeApp(firebaseConfig)
console.log(app)
const analytics = getAnalytics(app)
console.log(analytics)
