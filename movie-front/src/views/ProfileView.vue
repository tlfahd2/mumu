<template>
    <main class="main">
        <div>
        <h1>{{ accountStore.user.username }}의 프로필</h1>
        <button @click="follow" v-if="isFollow === true">팔로우 취소</button>
        <button @click="follow" v-else>팔로우</button>
        <p @click="follow_list()" type="button">팔로워 : {{ accountStore.user.followers?.length }}</p>
        <p>팔로잉 : {{ accountStore.user.followings?.length }}</p>
        <p v-for="follower in accountStore.user.followers"> {{follower.username }}</p>
        <!-- v-if="isFollowListModalVisible === true" 
        @close="closeFollowListModal"  -->
    </div>
    </main>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { useAccountStore } from '../stores/account'
import { useRouter, useRoute } from 'vue-router'
import axios from 'axios'
import FollowListModal from '../components/FollowListModal.vue'



const accountStore = useAccountStore()
const router = useRouter()
const route = useRoute()
const isFollow = ref(false)
const isFollowListModalVisible = ref(false)


onMounted(() => {
  accountStore.getUser(route.params.username)
  accountStore.user.followers.forEach((follower)=>{
    if( accountStore.user_username === follower.username ){
      isFollow.value = true
    }
  })
})


const follow = function () {
    axios({
      method: 'post',
      url: `${accountStore.API_URL}/api/v1/accounts/follow/${accountStore.user_pk}/${route.params.username}/`,
      headers: {
        Authorization: `Token ${accountStore.token}`
      }
    })
    .then((res) => {
      accountStore.getUser(route.params.username)
      isFollow.value = !isFollow.value
    })
    .catch((err) => {
      console.log(err)
    })
}


const openFollowListModal = function () {
  isFollowListModalVisible.value = true
}

const closeFollowListModal = function () {
  isFollowListModalVisible.value = false
}

const follow_list = function() {
    router.push({name: 'follow', params: {username: `${route.params.username}`}})
}
</script>

<style scoped>

</style>