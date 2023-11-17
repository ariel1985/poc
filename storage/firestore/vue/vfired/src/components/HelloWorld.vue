<script setup>
import {collection, doc, setDoc, addDoc, deleteDoc} from 'firebase/firestore'
import {useCollection} from 'vuefire'
import {db} from '../main.js'

const COLLECTION = 'firestore_collection' // TODO - get COLLECTION from queryParam
const KEY = 'example' // TODO each doc should have multiple keys

const currentCollection = collection(db, COLLECTION)
console.log(currentCollection);

/*
  Create
 */


async function handleInputCreate() {

  console.time(`handleInputCreate`)

  await addDoc(currentCollection, {
    [KEY]: 'enter text...'
  }).catch(console.error)


  console.timeEnd(`handleInputCreate`)
}


/*
  Read
 */


const docs = useCollection(currentCollection)
// const someTodo = useDocument(doc(collection(db, 'test'), 'someId'))
// Each of these composables return a Vue Ref containing the data.
// Note this is a readonly data, you shouldn't mutate it directly,
// you should instead use the Firebase SDK. VueFire will automatically
// keep the data in sync with the database:


/*
  Update
 */


async function handleInputChange(id, event) {
  console.time(`handleInputChange`)

  await setDoc(doc(db, COLLECTION, id), {
    [KEY]: event.target.value
  }).catch(console.error)


  console.timeEnd(`handleInputChange`)
}


/*
  Delete
 */

async function handleInputDelete(targetId) {
  console.time(`handleInputDelete`)

  await deleteDoc(doc(currentCollection, targetId))
      .catch(console.error)

  console.timeEnd(`handleInputDelete`)
}


</script>

<template>
  <ul class="live-list">


    <template v-if="!docs.length">
      <li class="empty">
        <input type="text" value="➕" @click="handleInputCreate">
      </li>
    </template>
    <template v-else>
      <li v-for="(doc, index) of docs" :key="doc.id">
        <input
            class="live"
            :value="doc[KEY]"
            type="text"
            @input.lazy="handleInputChange(doc.id, $event)"
        />
        <input type="button" value="➕" @click="handleInputCreate"/>
        <input type="button" value="➖" @click="handleInputDelete(doc.id)"/>
      </li>
    </template>

  </ul>

</template>

<style>
.live-list {

  list-style: none;
  display: flex;
  flex-direction: column;
  gap: 1rem;

  li {
    display: flex;
    flex-direction: row;
    gap: .25rem;

    & > input {

      &:is([type="button"]) {
        opacity: 0;
        pointer-events: none;


        &:hover {
          cursor: pointer;
        }
        &:focus {
          opacity: 1;
          pointer-events: initial;
        }
      }

      &:is([type="text"].live) {
        &:focus {
          background: #213547;
          color: white;

          ~ input[type="button"] {
            opacity: 1;
            pointer-events: all;
          }

        }

        border: none;
        background: transparent;
        font-size: 1.5em;
        font-family: monospace;
        color: #646cff;
        width: 100%;
        padding: 0.5em;
        outline: none;
        transition: color 300ms;
      }


    }
  }
}
</style>