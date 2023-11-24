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
import { onMounted, ref } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import axios from 'axios';
import { useAccountStore } from '../stores/account';


const accountStore = useAccountStore()
const router = useRouter()
const route = useRoute()
const visible = ref(false)
const user = ref({})


onMounted(() => {
  accountStore.getUser(route.params.username)
})


const moveProfile = function (username) {
    router.push({ name: 'profile', params: { username: accountStore.user.username}})
}
</script>

<style scoped>


</style>