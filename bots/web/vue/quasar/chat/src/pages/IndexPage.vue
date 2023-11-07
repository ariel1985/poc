<template>
  <q-page class="column flex-center">
    <q-card style="max-width: 400px;" class="col full-width">
      <q-card-section>
        <q-chat-message
          sent
          name="Bot"
          avatar="logo_crcl.png"
          :text="['Hey there']"
          stamp="6:30pm"
          />
          <q-chat-message
          name="User 1"
          avatar="bot-icon-7.png"
          :text="['Hey, been trying to reach you...']"
          stamp="6:34pm"
        />
        <q-chat-message
          name="User 2"
          avatar="user_icon_female.png"
          :text="['Here I am!']"
          stamp="6:34pm"
          bg-color="purple-8"
          text-color="white"
        />
        <q-chat-message label="yesterday"></q-chat-message>
        <q-chat-message
          sent
          name="Bot"
          avatar="logo_crcl.png"
          :text="['Hello']"
          stamp="3 minutes ago"
        />
        <q-chat-message
          name="User 1"
          avatar="bot-icon-7.png"
          :text="['Wanna buy something?']"
          stamp="2 minutes ago"
        />
        <q-chat-message
          name="User 2"
          avatar="user_icon_female.png"
          :text="['Yes!']"
          stamp="6:34pm"
          bg-color="purple-8"
          text-color="white"
        />
      </q-card-section>
    </q-card>
  </q-page>
</template>

<script>
import { defineComponent } from 'vue'

export default defineComponent({
  name: 'IndexPage'
})
</script>
