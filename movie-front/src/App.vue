<template>
  <div>
      <header class="header">
          <nav class="navbar">
            <RouterLink :to="{ name: 'main' }">Main</RouterLink> |
            <RouterLink v-if="accountStore.isLogin === false" :to="{ name: 'SignUpView' }">회원가입</RouterLink> |
            <RouterLink v-if="accountStore.isLogin === false" :to="{ name: 'LogInView' }">로그인</RouterLink> |
            <RouterLink v-if="accountStore.isLogin === true" @click="accountStore.logOut" :to="{ name: 'main' }">로그아웃</RouterLink>
            <RouterLink v-if="accountStore.isLogin === true" :to="{ name: 'change_password' }">비밀번호 변경</RouterLink>
            
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
.header {
  position: fixed;
}
</style>