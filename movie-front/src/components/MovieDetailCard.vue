<template>
    <div class="card">
        <img :src="store.BASE_IMAGE_URL+movie.poster_path" :alt="movie.title">
        <p v-if="movie.adult">성인</p>
        <p v-for="genre in movie.genres">{{ genre.name }}</p>
        <p>{{ movie.release_date }}</p>
        <p>{{ movie.runtime }}분</p>
        <p>{{ movie.title }}</p>
        <p>{{ movie.overview }}</p>
    </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import { useMovieListStore } from '../stores/movielist'
import axios from 'axios'

const store = useMovieListStore()
const props = defineProps({
    movie:Object
})

</script>

<style scoped>
.card{
    width: 500px;
}
</style>