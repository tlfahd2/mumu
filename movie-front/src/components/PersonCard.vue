<template>
    <div class="credits-container">
    <div class="credits-container2">
      <div class="card">
        <img v-if="person?.profile_path" class="card-img-top" :src="movieStore.BASE_IMAGE_URL + person?.profile_path"
          :alt="person?.name">
        <img v-else class="card-img-top" src="https://yozm.wishket.com/static/img/default_avatar.png" alt="">
        <div class="card-body">
          <p v-if="person?.another_name" class="card-text">{{ person.another_name }}</p>
          <p v-else>{{ person?.name }}</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import { useAccountStore } from '../stores/account'
import { useMovieStore } from '../stores/movie'
import axios from 'axios'

const movieStore = useMovieStore()
const props = defineProps({
    person:Object
})

</script>

<style scoped>
.card{
    display: inline-block;
    width: 150px;
    border-radius: 12px;
    text-align: center;
    margin:5px;
}
.card-body {
  height: 80px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.card-text {
  text-align: center;
}

.card-img-top {
  height: 220px;
}

.credits-container {
  overflow-x: auto;
}

.credits-container2 {
  width: 100%;
}

</style>