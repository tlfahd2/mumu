<template>
    <main class="main">
      <div v-show="visible" class="modal">
        <div class="modal-content">
          <span class="close" @click="closeModal(event)">X</span>
          <ul v-for="follower in user.followers">
            <p @click="moveProfile(follower.username)" type="button">{{ follower.username }}</p>
          </ul>
        </div>
      </div>
    </main>
    </template>
  
  <script setup>
  import { ref } from 'vue'
  import { useRouter, useRoute } from 'vue-router'
  import axios from 'axios';
  import { useAccountStore } from '../stores/account';
  
  
  const accountStore = useAccountStore()
  const router = useRouter()
  const route = useRoute()
  const visible = ref(false)
  const user = ref({}
  )
  const closeModal = function(event) {
    this.visible = !this.visible
  }
  
  
  const getUser = function () {
      axios({
        method: 'post',
        url: `${accountStore.API_URL}/api/v1/accounts/${route.params.username}/`,
        headers: {
          Authorization: `Token ${accountStore.token}`
        }
      })
      .then((res) => {
        user.value = res.data
      })
      .catch((err) => {
        console.log(err)
      })
    }
  getUser()
  
  const moveProfile = function (username) {
      router.push({ name: 'profile', params: { username: username}})
  }
  </script>
  
  <style scoped>
  
  
  </style>