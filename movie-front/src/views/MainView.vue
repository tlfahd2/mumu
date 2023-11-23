<template>
    <main class="main container">
        <div>
            <div class="drop d-flex">
                <button class="btn" @click="sortMovie(1)">인기순</button>
                <button class="btn" @click="sortMovie(2)">최신순</button>
                <button class="btn" @click="sortMovie(3)">개인맞춤</button>
                <button class="btn" @click="sortMovie(4)">개봉예정작</button>
                <div class="btn-group">
                    <button type="button" class="dropdown-toggle cta" data-bs-toggle="dropdown" aria-expanded="false">
                        장르별
                    </button>
                    <ul class="dropdown-menu">
                        <div v-for="genre in movieStore.genres" 
                            :key="genre.id">
                            <li><a class="dropdown-item"
                                 @click="sortMovie(genre.id)">
                                {{ genre.name }}
                            </a></li>
                        </div>
                    </ul>
                </div>
            </div>
            <div class="movie-list">
                <MovieCard
                v-for="movie in movieStore.movies"
                :key="movie.id"
                :movie="movie"
                />
            </div>
        </div>
    </main>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import { useAccountStore } from '../stores/account'
import { useMovieStore } from '../stores/movie'
import axios from 'axios'

import MovieCard from '../components/MovieCard.vue'

const movieStore = useMovieStore()
const router = useRouter()

onMounted(()=>{
    movieStore.getGenreList()
})

const sortMovie= (number) =>{
    movieStore.getMovieList(number)
}

</script>

<style scoped>
.movie-list{
    display: flex;
    flex-wrap: wrap;
    width: 90vw;
}

</style>