<template>
    <main class="container main">
        <div class="movie-info">
            <MovieDetailCard
            :movie="movie"
            />
            <section>
                <div class="credits-container">
                    <div class="credits-container2">
                        <div class="credits">
                            <p class="tag">감독/출연</p>
                            <div class="person-cards">
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
.credits-container {
  overflow-x: auto; /* Enable horizontal scrolling if content overflows */
}

.credits-container2 {
  width: 100%;
  overflow-x: auto /* Take the full width of the container */
}

.credits{
    display: flex;
    flex-wrap: wrap;
    border:1px solid;
    min-width: fit-content
}

.person-cards {
    display: flex;
    gap: 10px; /* Add some gap between cards */
    overflow-x: auto; 
}

button {
  background-color: transparent;
  border: none;
  cursor: pointer;
  font-size: 20px;
  outline: none;
}

</style>