import Vue from 'vue';
import App from './App.vue';
// import firebase from 'firebase/app';
import { initializeApp } from "firebase/app";
// import 'firebase/database';

import { firebaseConfig } from './firebase_conn';

console.log(firebaseConfig);

// Initialize Firebase
firebase.initializeApp(firebaseConfig);

// Create a reference to your data
const db = firebase.database();
const myCollection = db.ref('path/to/collection');

// Vue instance
new Vue({
  el: '#app',
  firebase: {
    // Bind your collection to a Vue data property
    myCollectionData: myCollection
  },
  render: h => h(App)
});

// In your Vue component, you can now access the data with this.myCollectionData
