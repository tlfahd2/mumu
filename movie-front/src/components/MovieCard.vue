<template>
    <div class="poster" @click="moveDetail">
        <img :src="posterUrl" class="img-thumbnail" :alt="movie.title">
        {{ movie.popularity }}
        {{ movie.release_date }}
    </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import { useMovieListStore } from '../stores/movielist'
import axios from 'axios'

const props = defineProps({
    movie:Object
})
const store = useMovieListStore()
const router = useRouter()
const posterUrl = `${store.BASE_IMAGE_URL}${props.movie.poster_path}`


const moveDetail = () => {
    router.push({name:'moviedetail', params:{movie_id:`${props.movie.id}`}})
}

</script>

<style scoped>
.poster{
    display: inline-block;
    width: 200px;
    margin: 20px;
}
</style>