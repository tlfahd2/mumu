<template>
  <div>
    <nav>
      <header class="header">
      <div>
      <nav class="navbar">
        <RouterLink to="/">Main</RouterLink> |
        <RouterLink v-if="hbstore.isLogin===false" :to="{ name: 'SignUpView' }">회원가입</RouterLink> |
      <RouterLink  v-if="hbstore.isLogin===false" :to="{ name: 'LogInView' }">로그인</RouterLink> |
      <RouterLink  v-if="hbstore.isLogin===true" @click="hbstore.logOut" :to="{ name: 'main'}">로그아웃</RouterLink>
      </nav>
    </div>
  </header>
    </nav>
    <RouterView/>
  </div>

</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router'
import { useMovieListStore } from './stores/movielist'
import { useMovieStore } from './stores/movie'
import { onMounted } from 'vue';

const store = useMovieListStore()
onMounted(()=>{
  store.getMovieList(1)
})

const hbstore = useMovieStore()
</script>

<style  scoped>
.header{
  position: fixed;
}
</style>