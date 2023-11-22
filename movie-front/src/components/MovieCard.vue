<template>
    <article>
        <div class="poster" @click="moveDetail">
            <img :src="posterUrl" class="img-fluid img-thumbnail" :alt="movie.title">
            {{ movie.popularity }}
            {{ movie.release_date }}
        </div>
    </article>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import { useAccountStore } from '../stores/account'
import { useMovieStore } from '../stores/movie'
import axios from 'axios'

const props = defineProps({
    movie:Object
})
const movieStore = useMovieStore()
const router = useRouter()
const posterUrl = `${movieStore.BASE_IMAGE_URL}${props.movie.poster_path}`


const moveDetail = () => {
    router.push({name:'moviedetail', params:{movie_id:`${props.movie.id}`}})
}

</script>

<style scoped>
.poster{
    position: relative;
    width: 200px;
    margin: 20px;
    transition: 0.2s ease-in-out;
}
.img-thumbnail{
    height: 298px;
}
.poster :hover {
    transform: perspective(1500px) rotateY(30deg);
    box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.6);
    cursor: pointer;
}
</style>