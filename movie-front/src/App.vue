<template>
  <div>
      <header>
        <div>
          <nav class="navbar fixed-top">
              <RouterLink class= "nav-item" :to="{ name: 'main' }">Main</RouterLink>
              <RouterLink class= "nav-item" :to="{ name: 'communitymain' }">커뮤니티</RouterLink>
              <RouterLink class= "nav-item" v-if="accountStore.isLogin === false" :to="{ name: 'SignUpView' }">회원가입</RouterLink>
              <RouterLink class= "nav-item" v-if="accountStore.isLogin === false" :to="{ name: 'LogInView' }">로그인</RouterLink>
              <RouterLink class= "nav-item" v-if="accountStore.isLogin === true" @click="accountStore.logOut" :to="{ name: 'main' }">로그아웃</RouterLink>
              <RouterLink class= "nav-item" v-if="accountStore.isLogin === true" :to="{ name: 'change_password' }">비밀번호 변경</RouterLink>
              <form class="d-flex" role="search" @submit.prevent="getSearchMovie">
                <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search" v-model="searchInput">
                <button class="btn btn-outline-success" type="submit">search</button>
              </form>
          </nav>
        </div>
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
const accountStore = useAccountStore()
const router = useRouter()

onMounted(() => {
  movieStore.getMovieList(1)
})
const searchInput = ref('')

const getSearchMovie = ()=>{
  router.push({name : 'search', params:{keyward : searchInput.value}})
}


</script>

<style  scoped>
.main{
  padding-top: 5.8rem;
}
.navbar{
  padding-left: 5rem;
  padding-right: 5rem;
}

</style>