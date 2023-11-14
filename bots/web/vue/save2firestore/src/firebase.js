import firebase from 'firebase/app'
import 'firebase/firestore'

// Your web app's Firebase configuration
const firebaseConfig = {
  apiKey: "AIzaSyAxh3ftiHVpPKuOtX9ZA9SBVlS-22BIyLM",
  authDomain: "chats-96d05.firebaseapp.com",
  projectId: "chats-96d05",
  storageBucket: "chats-96d05.appspot.com",
  messagingSenderId: "964263076072",
  appId: "1:964263076072:web:3c85e4974ec841bf4c695d",
  measurementId: "G-HB5ER5VQ2Q"
}

// Initialize Firebase
firebase.initializeApp(firebaseConfig)

export const db = firebase.firestore()


console.log('db', db)
