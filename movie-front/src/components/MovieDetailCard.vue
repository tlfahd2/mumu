<template>
    <div>
        <img :src="movieStore.BASE_IMAGE_URL+movie.poster_path" :alt="movie.title">
        <p v-if="movie.adult">성인</p>
        <p v-for="genre in movie.genres">{{ genre.name }}</p>
        <p>{{ movie.release_date }}</p>
        <p>{{ movie.runtime }}분</p>
        <p>{{ movie.title }}</p>
        <p>{{ movie.overview }}</p>
        <button class="btn btn-primary">리뷰 쓰기</button>
        <button v-if="movie.trailer" class="btn btn-secondary">예고편 보기</button>
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
    movie:Object
})

</script>

<style scoped>
.card{
    width: 500px;
}
</style>