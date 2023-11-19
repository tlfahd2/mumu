<template>
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