<template>
  <div>
      <header>
          <nav class="navbar fixed-top">
              <RouterLink :to="{ name: 'main' }">Main</RouterLink>
              <RouterLink :to="{ name: 'communitymain' }">커뮤니티</RouterLink>
              <RouterLink v-if="accountStore.isLogin === false" :to="{ name: 'SignUpView' }">회원가입</RouterLink>
              <RouterLink v-if="accountStore.isLogin === false" :to="{ name: 'LogInView' }">로그인</RouterLink>
              <RouterLink v-if="accountStore.isLogin === true" @click="accountStore.logOut" :to="{ name: 'main' }">로그아웃</RouterLink>
              <RouterLink v-if="accountStore.isLogin === true" :to="{ name: 'change_password' }">비밀번호 변경</RouterLink>
              <form class="d-flex" role="search">
                <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search">
                <button class="btn btn-outline-success" type="submit">Search</button>
              </form>
          </nav>
      </header>
  <RouterView/>
  </div>
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router'
import { ref, computed, onMounted } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import { useAccountStore } from './stores/account.js'
import { useMovieStore } from './stores/movie.js'
import axios from 'axios'


const movieStore = useMovieStore()
onMounted(() => {
  movieStore.getMovieList(1)
})

const accountStore = useAccountStore()
</script>

<style  scoped>
.main{
  padding-top: 5.8rem;
}
</style>