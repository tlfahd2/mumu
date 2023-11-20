<template>

  <div>
    <nav>
      <header class="header">
      <div>
      <nav class="navbar">
        <RouterLink to="/">Main</RouterLink>
        <RouterLink :to="{ name: 'SignUpView' }">회원가입</RouterLink> |
      <RouterLink :to="{ name: 'LogInView' }">로그인</RouterLink> |
      <RouterLink :to="{ name: 'SignUpView' }">로그아웃</RouterLink>
      </nav>
    </div>
  </header>
    </nav>
    <RouterView/>
  </div>

  <header class="header">
    <div>
      <nav class="navbar">
        <RouterLink to="/">Main</RouterLink>
      </nav>
    </div>
  </header>
  <RouterView/>
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router'
import { useMovieListStore } from './stores/movielist'
import { onMounted } from 'vue';

const store = useMovieListStore()
onMounted(()=>{
  store.getMovieList(1)
})
</script>

<style  scoped>
.header{
  position: fixed;
}
</style>