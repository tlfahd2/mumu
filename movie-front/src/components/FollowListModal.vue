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
.modal {
  /* 모달 전체 스타일 */

  position: fixed;
  z-index: 1;
  left: 0;
  top: 0;
  width: 100%;
  height: 100%;
  overflow: auto;
  background-color: rgba(0, 0, 0, 0.4);
}

.modal-content {
  /* 모달 내용 스타일 */
  position: relative;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 760px;
  background: #fff;
  border-radius: 10px;
  padding: 20px;
  box-sizing: border-box;
}



</style>