<template>
  <div>
    <nav>
      <RouterLink :to="{ name: 'SignUpView' }">회원가입</RouterLink> |
      <RouterLink :to="{ name: 'LogInView' }">로그인</RouterLink> |
      <RouterLink :to="{ name: 'SignUpView' }">로그아웃</RouterLink>
    </nav>
    <RouterView/>
  </div>
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router'
import { constUserMovieStore } from '@/stores/movies'
</script>

<style  scoped>

</style>