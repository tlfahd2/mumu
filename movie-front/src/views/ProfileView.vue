<template>
  <main class="main container">
    <div>


<!-- Modal -->
<div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
  <div class="modal-dialog">
    <div class="modal-content">
      <div class="modal-header">
        <h1 class="modal-title fs-5" id="exampleModalLabel">Modal title</h1>
        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
      </div>
      <div class="modal-body">
        <div v-if="selected === 1">
        <div class="modal-header">
          <div class="profile">
            <hr>
            <p>{{ accountStore.user.name }}</p>
            <hr>
            <div v-if="accountStore.user_username !== accountStore.user.username">
              <button @click="follow" v-if="isFollow === true">팔로우 취소</button>
              <button @click="follow" v-else>팔로우</button>
            </div>
            <p @click="goFollowerList" type="button">팔로워 : {{ accountStore.user.followers?.length }}</p>
            <p @click="goFollowingList" type="button">팔로잉 : {{ accountStore.user.followings?.length }}</p>
            <hr>
            <p>좋아하는 음악 장르 : {{ accountStore.user.music.replace(/"/g, '')}}</p>
            <hr>
            <p>좋아요 한 영화</p>
            <div v-for="movie in accountStore.user.like_movies">
              {{ movie.title }}
                <MovieCard :movie="movie"/>
            </div>
            <div v-if="accountStore.user_username === accountStore.user.username">
              <RouterLink class= "nav-item" :to="{ name: 'change_password' }">비밀번호 변경</RouterLink>
            </div>
          </div>
          <i class="bi bi-x-octagon" @click="handle_toggle(event)"></i>
        </div>
      </div>

      <!-- 팔로우 리스트 -->
      <div v-if="selected === 2">
        <div class="modal-header">
          <i class="bi bi-arrow-left-circle" @click="goMain"></i>
          <div class="profile">
            <hr>
            <div v-for="follower in accountStore.user.followers" style="max-width: fit-content;">
              <p @click="goUser(follower.username)" style="cursor: pointer;">{{ follower.username }}</p>
              <hr>
            </div>
          </div>
          <i class="bi bi-x-octagon" @click="handle_toggle(event)"></i>
        </div>
      </div>

      <div v-if="selected === 3">
        <div class="modal-header">
          <i class="bi bi-arrow-left-circle" @click="goMain"></i>
          <div class="profile">
            <hr>
            <div v-for="following in accountStore.user.followings" style="max-width: fit-content;">
              <p @click="goUser(following.username)" style="cursor: pointer;">{{ following.username }}</p>
              <hr>
            </div>
          </div>
          <i class="bi bi-x-octagon" @click="handle_toggle(event)"></i>
        </div>
      </div>
    </div>
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
    console.log(accountStore.user)
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
  selected.value = 2
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
.modal-header {
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-bottom: 10px;
    overflow: hidden;
    /* Hide overflowing content in the header */
}


.modal-header img {
    flex-shrink: 0;
}

.header-content {
    flex-grow: 1;
}

.content-rank-container {
    display: flex;
    flex-direction: column;
}

textarea {
    width: 100%;
    margin-bottom: 5px;
}

.rank-create-container {
    display: flex;
    justify-content: space-between;
}

.select-container {
    display: inline-block;
    width: 80px;
}

select {
    width: 100%;
    padding: 5px;
    box-sizing: border-box;
}

button {
    flex-shrink: 0;
}

.modal-header i {
    background: none;
    border: none;
    font-size: 16px;
    cursor: pointer;
    margin-bottom: 150px;
}
</style>