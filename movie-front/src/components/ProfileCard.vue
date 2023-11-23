<template>
    <main class="main container">
      <div>
        <button type="button" class="btn btn-primary" data-bs-target="#staticBackdrop">
          {{ accountStore.user.username }}
        </button>
        <div style="z-index: 3000;" class="modal fade" id="staticBackdrop" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1"
          aria-labelledby="staticBackdropLabel" aria-hidden="true">
          <div class="modal-dialog">
            <div class="modal-content">
              <div class="modal-header">
                <h1 class="modal-title fs-5" id="staticBackdropLabel">{{ accountStore.user.name }}님의 프로필</h1>
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
                      <p>좋아하는 음악 장르 : {{ accountStore.user.music.replace(/"/g, '') }}</p>
                      <hr>
                      <p>좋아요 한 영화</p>
                      <div v-for="movie in accountStore.user.like_movies">
                        {{ movie.title }}
                        <MovieCard :movie="movie" />
                      </div>
                      <div v-if="accountStore.user_username === accountStore.user.username">
                        <RouterLink class="nav-item" :to="{ name: 'change_password' }">비밀번호 변경</RouterLink>
                      </div>
                    </div>
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
  
  </style>