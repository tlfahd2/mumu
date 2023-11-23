<template>
  <div>
      <header>
        <div>
          <nav class="navbar fixed-top">
              <RouterLink class= "nav-item" :to="{ name: 'main' }">홈</RouterLink>
              <RouterLink class= "nav-item" :to="{ name: 'communitymain' }">커뮤니티</RouterLink>
              <RouterLink class= "nav-item" v-if="accountStore.isLogin === false" :to="{ name: 'SignUpView' }">회원가입</RouterLink>
              <RouterLink class= "nav-item" v-if="accountStore.isLogin === false" :to="{ name: 'LogInView' }">로그인</RouterLink>
              <RouterLink class= "nav-item" v-if="accountStore.isLogin === true" @click="accountStore.logOut" :to="{ name: 'main' }">로그아웃</RouterLink>
              <RouterLink class= "nav-item" v-if="accountStore.isLogin === true" :to="{ name: 'change_password' }">비밀번호 변경</RouterLink>
              <form class="d-flex" role="search" @submit.prevent="getSearchMovie">
                <input class="form-control me-2" type="search" placeholder="검색어를 입력하세요" aria-label="Search" v-model="searchInput">
                <button class="btn btn-outline-success" type="submit"><i class="bi bi-search"></i></button>
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
  movieStore.getSerchResult(searchInput)
  router.push({name : 'search', params:{keyword : searchInput.value}})
  searchInput.value=''
}


</script>

<style  scoped>
.main{
  padding-top: 5.8rem;
}
.navbar{
  padding-left: 8rem;
  padding-right: 8rem;
  
  font-size: larger;
  font-weight: bold;
  background-color: black;

}
.nav-item{
  display: inline-block;
  text-decoration: none;
  color:white;
  text-transform:uppercase;
}
.nav-item:after {
  display:block;
  content: '';
  border-bottom: solid 3px white;  
  transform: scaleX(0);  
  transition: transform 250ms ease-in-out;
}
.nav-item:hover:after{
  transform: scaleX(1);

}

</style>