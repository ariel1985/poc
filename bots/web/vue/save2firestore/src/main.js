import { createApp } from 'vue'
import App from './App.vue'
import { db } from './firebase'

// This line mounts the Vue app to the '#app' element in the HTML
createApp(App).mount('#app')

// Here we are connecting to Firestore and editing the 'testim' value to the current timestamp
// We first get a reference to the 'chatstorecollection' collection
var chatStoreCollection = db.collection('chatstorecollection')

// Then we get a reference to the 'testim' document and set its 'timestamp' field to the current server timestamp
// If the 'testim' document does not exist, it will be created
chatStoreCollection.doc('testim').set({
  timestamp: firebase.firestore.FieldValue.serverTimestamp()
})
