<template>
  <div>
      <header>
        <div>
          <nav class="navbar fixed-top" v-if="accountStore.isLogin">
              <RouterLink class= "nav-item" :to="{ name: 'main' }">홈</RouterLink>
              <RouterLink class= "nav-item" :to="{ name: 'communitymain' }">커뮤니티</RouterLink>
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

const searchInput = ref('')

const getSearchMovie = ()=>{
  movieStore.getSerchResult(searchInput)
  router.push({name : 'search', params:{keyword : searchInput.value}})
  searchInput.value=''
}


</script>

<style  scoped>
@font-face {
  font-family: "euljiro";
  src: url("fonts/BMEuljiro10yearslater.ttf")
}
.main{
  padding-top: 5.8rem;
}
.navbar{
  height: 70px;
  padding-left: 8rem;
  padding-right: 8rem;
  font-family: 'euljiro';
  font-size: 30px;
  /* background-color: #00264B; */
  background-color: #BDCEBE;
}
.nav-item{
  display: inline-block;
  text-decoration: none;
  color:#10AF85;
  text-transform:uppercase;
}
.nav-item:after {
  display:block;
  content: '';
  border-bottom: solid 5px #0B685A;  
  transform: scaleX(0);  
  transition: transform 250ms ease-in-out;
}
.nav-item:hover:after{
  transform: scaleX(1);
}

</style>