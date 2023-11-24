<template>
  <main class="main container">
    <div class="user-profile">
      <div class="modal-header">
        <div class="profile">
          <hr>
          <p class="username">{{ accountStore.user.name }}</p>
          <hr>
          <div v-if="accountStore.user_username !== accountStore.user.username">
            <button @click="follow" v-if="isFollow === true" class="unfollow-btn">팔로우 취소</button>
            <button @click="follow" v-else class="follow-btn">팔로우</button>
          </div>
          <p @click="goFollowerList" class="follower-count" type="button">팔로워: {{ accountStore.user.followers?.length }}</p>
          <p @click="goFollowingList" class="following-count" type="button">팔로잉: {{ accountStore.user.followings?.length }}</p>
          <hr>
          <p>좋아하는 음악 장르: {{ accountStore.user.music.replace(/"/g, '') }}</p>
          <hr>
          <p>좋아요 한 영화</p>
          <div v-for="movie in accountStore.user.like_movies" :key="movie.id" class="liked-movie">
            <MovieCard :movie="movie" />
          </div>
          <div v-if="accountStore.user_username === accountStore.user.username" class="change-password-link">
            <RouterLink :to="{ name: 'change_password' }">비밀번호 변경</RouterLink>
          </div>
        </div>
      </div>
    </div>
  </main>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { useAccountStore } from '../stores/account'
import { useRouter, useRoute } from 'vue-router'
import axios from 'axios'
import MovieCard from '../components/MovieCard.vue'

const accountStore = useAccountStore()
console.log(accountStore.user.value)
const router = useRouter()
const route = useRoute()
const isFollow = ref(false)
const is_show = ref(false)
const selected = ref(1)

const props = defineProps({
  username: String
})

console.log(props.username)
onMounted(() => {
  accountStore.getUser(props.username)
  setTimeout(() => {
    if (accountStore.user.followers?.find((follower) => follower.id === accountStore.user_pk)) {
      isFollow.value = true
    }
    else {
      isFollow.value = false
    }
  }, 100)
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

const handle_toggle = function (event) {
  // console.log(this.is_show)
  this.is_show = !this.is_show
}

const goFollowerList = function () {
  router.push({name: follow, params: {username: accountStore.user.username}})
}

const goFollowingList = function () {
  selected.value = 3
}

const goUser = function (username) {
  selected.value = 1
  accountStore.getUser(username)
}

const goMain = function () {
  selected.value = 1
}
</script>

<style scoped>
.user-profile {
  margin-top: 20px;
  width: fit-content;
}

.modal-header {
  background-color: #f8f9fa; /* Light gray background */
  border-radius: 8px;
  padding: 20px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.profile {
  text-align: center;
}

.username {
  font-size: 1.5em;
  font-weight: bold;
  margin-bottom: 10px;
}

.follow-btn,
.unfollow-btn {
  padding: 8px 16px;
  border: none;
  border-radius: 4px;
  color: white;
  cursor: pointer;
  transition: background-color 0.3s;
}

.follow-btn {
  background-color: #007bff; /* Blue color for follow button */
}

.unfollow-btn {
  background-color: #dc3545; /* Red color for unfollow button */
}

.follower-count,
.following-count {
  cursor: pointer;
  margin-top: 10px;
  font-weight: bold;
}

.follower-count:hover,
.following-count:hover {
  text-decoration: underline;
}

.liked-movie {
  margin-bottom: 10px;
}

.change-password-link {
  margin-top: 20px;
}
</style>