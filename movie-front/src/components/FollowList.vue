<template>
  <main class="main">
    <div v-for="follower in user.followers" :key="follower.username" class="list-item" @click="moveProfile(follower.username)">
      {{ follower.username }}
    </div>
  </main>
    </template>

<script setup>
import { onMounted, ref } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import { useAccountStore } from '../stores/account';


const accountStore = useAccountStore()
const router = useRouter()
const route = useRoute()
const user = ref({})


onMounted(() => {
  accountStore.getUser(route.params.username)
  user.value = accountStore.user
})


const moveProfile = function (username) {
    router.push({ name: 'profile', params: { username: username}})
}



</script>

<style scoped>
@font-face {
  font-family: "yeonsung";
  src: url("../fonts/BMYEONSUNG_ttf.ttf")
}
.main {
    padding-top: 5.8rem;
    max-width: 600px;
    margin: 0 auto;
    background-color: #f5f5f5;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    font-family: "yeonsung";
  }

  .list-item {
    cursor: pointer;
    padding: 10px;
    margin: 5px 0;
    background-color: #fff;
    border-radius: 5px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
    transition: background-color 0.3s ease-in-out;
  }

  .list-item:hover {
    background-color: #f0f0f0;
  }
</style>