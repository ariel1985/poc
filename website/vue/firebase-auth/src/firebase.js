// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getAuth } from "firebase/auth";

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
    apiKey: "AIzaSyAxh3ftiHVpPKuOtX9ZA9SBVlS-22BIyLM",
    authDomain: "chats-96d05.firebaseapp.com",
    projectId: "chats-96d05",
    storageBucket: "chats-96d05.appspot.com",
    messagingSenderId: "964263076072",
    appId: "1:964263076072:web:3c85e4974ec841bf4c695d",
    measurementId: "G-HB5ER5VQ2Q"
};

// Initialize Firebase
export const db = initializeApp(firebaseConfig);
export const auth = getAuth(db);