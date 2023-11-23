<template>
    <main class="main">
        <div>
        <h1>{{ user.username }}의 프로필</h1>
        <div v-if="accountStore.user_username !== user.username ">
            <button @click="follow" v-if="accountStore.isFollow === true">팔로우 취소</button>
            <button @click="follow" v-else>팔로우</button>
        </div>
        <p @click="follow_list()" type="button">팔로워 : {{ accountStore.user.followers?.length }}</p>
        <p>팔로잉 : {{ accountStore.user.followings?.length }}</p>
        <p v-for="follower in user.followers"> {{follower.username }}</p>
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
const user = ref({})
const isFollowListModalVisible = ref(false)

onMounted(() => {
  accountStore.getUser(route.params.username)
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
      accountStore.isFollow = !accountStore.isFollow
      accountStore.getUser(route.params.username)
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