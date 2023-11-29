import { initializeApp } from "firebase/app";
import { getAuth } from "firebase/auth";
import { getFirestore } from 'firebase/firestore';

const firebaseConfig = {
    apiKey: "AIzaSyAxh3ftiHVpPKuOtX9ZA9SBVlS-22BIyLM",
    authDomain: "chats-96d05.firebaseapp.com",
    projectId: "chats-96d05",
    storageBucket: "chats-96d05.appspot.com",
    messagingSenderId: "964263076072",
    appId: "1:964263076072:web:3c85e4974ec841bf4c695d",
    measurementId: "G-HB5ER5VQ2Q"
};

// Initialize Firebase apps (theres also one for analytics)
export const firebase = initializeApp(firebaseConfig);
export const db = getFirestore(firebase);
export const auth = getAuth(firebase);