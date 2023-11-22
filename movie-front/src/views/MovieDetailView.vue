<template>
    <main class="container main">
        <div>
            <h1>영화 상세</h1>
            <MovieDetailCard
            :movie="movie"
            />
            <section>
                <div class="credits">
                    <div class="row row-cols-1">
                        <p>감독</p>
                        <PersonCard
                        :person="movie.director"
                        />
                        <p>주연 배우</p>
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
</script>

<style scoped>
.main{
    padding-top: 5.8rem;
}
.credits{
    display: flex;
}
.personContainer{
    display: flex;
    overflow-x: auto;
    white-space: nowrap;
}
</style>