import { initializeApp } from "firebase/app";
import { firebaseConfig } from './firebase_conn';

console.log(firebaseConfig);

// Initialize Firebase
const firebase_app = initializeApp(firebaseConfig);

// If you later decide to use Firebase Analytics, you can reintroduce the getAnalytics import and initialization
// const analytics = getAnalytics(app);

// Export the Firebase app instance if you need to use it elsewhere in your application
export { firebase_app };
