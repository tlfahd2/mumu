<template>
  <main class="main">
    <div>
      <h1>{{ user.username }}의 프로필</h1>
      <div v-if="accountStore.user_username !== user.username">
        <button @click="follow" v-if="isFollow === true">팔로우 취소</button>
        <button @click="follow" v-else>팔로우</button>
      </div>
      <p @click="follow_list()" type="button">팔로워 : {{ user.followers?.length }}</p>
      <p>팔로잉 : {{ user.followings?.length }}</p>
      <p v-for="follower in user.followers"> {{ follower.username }}</p>
      <p>좋아요 한 영화 목록</p>
      <div v-for="like_movie in user.like_movies">
        <p @click="moveDetail(like_movie.id)">
          {{ like_movie.title }}
        </p>
      </div>
      <p>내가 쓴 리뷰 목록</p>
      <div v-for="review in user.reviews">
        <p @click="moveReviewDetail(review.id)">
          {{ review }}
        </p>
      </div>
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
const isFollow = ref('')
const isFollowListModalVisible = ref(false)

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
      isFollow.value = res.data
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

const follow_list = function () {
  router.push({ name: 'follow', params: { username: `${route.params.username}` } })
}

const moveDetail = (movie_id) => {
  router.push({ name: 'movieDetail', params: { movie_id: movie_id } })
}

const moveReviewDetail = (review_id) => {
  router.push({ name: 'reviewDetail', params: { review_id: review_id } })
}
</script>

<style scoped></style>