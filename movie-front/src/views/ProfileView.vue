<template>
    <div>
        <h1>{{ user.username }}의 프로필</h1>
        <div v-if="accountStore.user_username !== user.username ">
            <button @click="follow" v-if="isFollow === false">팔로우</button>
            <button @click="follow" v-if="isFollow === true">팔로우 취소</button>
        </div>
        <p>팔로워 : {{ user.followers?.length }}</p>
        <p>팔로잉 : {{ user.followings?.length }}</p>
        
    </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { useAccountStore } from '../stores/account'
import { useRoute } from 'vue-router'
import axios from 'axios'

const accountStore = useAccountStore()
const route = useRoute()
const user = ref('')
const isFollow = ref(false)

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


const follow = function () {
    axios({
      method: 'post',
      url: `${accountStore.API_URL}/api/v1/accounts/follow/${accountStore.user_pk}/${route.params.username}/`,
      headers: {
        Authorization: `Token ${accountStore.token}`
      }
    })
    .then((res) => {
        getUser()
        isFollow.value = !isFollow.value
    })
    .catch((err) => {
      console.log(err)
    })
}

</script>

<style scoped>

</style>