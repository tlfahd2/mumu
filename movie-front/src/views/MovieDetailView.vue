<template>
    <main class="main">
        <div>
            <h1>영화 상세</h1>
            <MovieDetailCard
            :movie="movie"
            />
            <p>감독</p>
            <PersonCard
            :person="movie.director"
            />
            <br>
            <p>주연 배우</p>
            <PersonCard
            v-for="actor in movie.actors"
            :person="actor"
            />
            <button @click="createReview">리뷰 생성</button>
        </div>
    </main>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import { useAccountStore } from '../stores/account'
import { useMovieStore } from '../stores/movie'
import axios from 'axios'

import MovieDetailCard from '../components/MovieDetailCard.vue'
import PersonCard from '../components/PersonCard.vue'
import router from '../router'


const movieStore = useMovieStore()
const route = useRoute()
const movie_id = route.params.movie_id

const movie = ref({})

axios({
        method:'get',
        url : `${movieStore.API_URL}/detail/${movie_id}`
    }).then((response)=>{
        movie.value = response.data
    }).catch((error)=>{
        console.log(error)
    })


const createReview = function () {
    router.push({name: 'createReview', params: {movie_id: movie_id}})
}



</script>

<style scoped>
.main{
    padding-top: 5.8rem;
}
</style>