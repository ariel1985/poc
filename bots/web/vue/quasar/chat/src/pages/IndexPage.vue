<script setup>
import { ref } from 'vue'
import importedMessages from 'src/data/chat.json'

const text = ref('')
const errorMsg = ref('')
const messages = ref(importedMessages) // Making messages reactive

console.log(messages.value)

const sendMessage = () => {
  if (!text.value.trim()) {
    errorMsg.value = 'Error - no value..'
    return false
  }
  errorMsg.value = ''

  // Add new message to messages array
  messages.value.push({
    name: 'Bot',
    text: [text.value],
    stamp: new Date().toLocaleTimeString(),
    sent: true,
    avatar: 'logo_crcl.png'
  })

  console.log(text.value)
  text.value = '' // Clear the input after sending the message

  // Assuming sendMessage is successful
  return true
}
</script>

<template>
  <q-page class="column flex-center">
    <q-card style="max-width: 400px;" class="col full-width">
      <q-card-section>
        <!-- Iterate over messages -->
        <q-chat-message v-for="(message, index) in messages" :key="index"
          :sent="message.sent"
          :name="message.name"
          :avatar="message.avatar"
          :text="message.text"
          :stamp="message.stamp"
          :bg-color="message['bg-color']"
          :text-color="message['text-color']"
        />
      </q-card-section>

      <div class="sticky-container col">
        <!-- Footer section for input and send button -->
        <q-card-section class="row items-center q-pa-md">
          <q-input filled v-model="text" class="col" placeholder="Type your message here" @keyup.enter="sendMessage"/>
          <q-btn flat round icon="send" @click="sendMessage" class="q-ml-md" />
        </q-card-section>
        <div v-if='errorMsg' class='error'>
          {{ errorMsg }}
        </div>
      </div>
    </q-card>
  </q-page>
</template>

<style>
.sticky-container {
  position: absolute;
  bottom: 0;
  z-index: 10;
  width: 100%;
}
.error {
  padding: 1em;
  color: red;
}
</style>
