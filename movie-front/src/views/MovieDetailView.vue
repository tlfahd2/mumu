<template>
    <main class="container main">
        <div class="movie-info">
            <MovieDetailCard
            :movie="movie"
            />
            <section>
                <div class="credits">
                    <p class="tag">감독/출연</p>
                    <div>
                        <PersonCard
                        :person="movie.director"
                        />
                        <PersonCard
                        v-for="actor in movie.actors"
                        :key="actor.id"
                        :person="actor"
                        />
                    </div>
                </div>
            </section>
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
import ReviewCreateView from './ReviewCreateView.vue'


const movieStore = useMovieStore()
const route = useRoute()
const movie_id = route.params.movie_id

const movie = ref({})

onMounted(() => {
    axios({
            method:'get',
            url : `${movieStore.API_URL}/detail/${movie_id}`
        }).then((response)=>{
            movie.value = response.data
            movieStore.movie = response.data
        }).catch((error)=>{
            console.log(error)
        })
})
</script>

<style scoped>
.main{
    padding-top: 5.8rem;
}
.credits{
    display: flex;
    border:1px solid
}

</style>