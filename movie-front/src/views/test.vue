<template>
  <transition name="modal">
    <div class="modal-mask">
      <div class="modal-wrapper">
        <div class="modal-container">
          <div class="modal-header">
            <div class="modal-body">
              <div class="container-md m-3 p-3">
                <!-- <div v-if="selected === 1"> -->
        <!-- <div class="modal-header"> -->
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
        <!-- </div> -->
      <!-- </div> -->

      <!-- 팔로우 리스트 -->
      <!-- <div v-if="selected === 2">
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
      </div> -->

                <button
                  type="button"
                  class="btn btn-outline-danger"
                  data-bs-dismiss="modal"
                  @click="$emit('close')"
                >
                  취소
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </transition>
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

<style>
.modal-mask {
  position: fixed;
  z-index: 9998;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
  display: table;
  transition: opacity 0.3s ease;
}

.modal-wrapper {
  display: table-cell;
  vertical-align: middle;
  color: #555555;
}

.modal-container {
  width: 700px;
  margin: 0px auto;
  padding: 20px 30px;
  background-color: #fff;
  border-radius: 2px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.33);
  transition: all 0.3s ease;
  font-family: Helvetica, Arial, sans-serif;
}

.modal-header h3 {
  margin-top: 0;
  color: #42b983;
}

.modal-body {
  margin: 20px 0;
}

.modal-default-button {
  float: right;
}

.modal-enter {
  opacity: 0;
}

.modal-leave-active {
  opacity: 0;
}

.modal-enter .modal-container,
.modal-leave-active .modal-container {
  -webkit-transform: scale(1.1);
  transform: scale(1.1);
}
</style>
