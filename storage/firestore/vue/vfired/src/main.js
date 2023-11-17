import { createApp } from 'vue'
import './style.css'
import App from './App.vue'
// Firebase imports
import { VueFire } from 'vuefire'
import { initializeApp } from "firebase/app";
import { getFirestore } from 'firebase/firestore'

const app = createApp(App)

// Firebase configuration
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
const firebaseApp = initializeApp(firebaseConfig);
export const db = getFirestore(firebaseApp);


app.use(VueFire, {
    // imported above but could also just be created here
    firebaseApp,
})

app.mount('#app')