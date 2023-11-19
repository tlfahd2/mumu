<template>
    <main class="main">
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
                        <div v-for="genre in store.genres" 
                            :key="genre.id">
                            <li><a class="dropdown-item"
                                 @click="sortMovie(genre.id)">
                                {{ genre.name }}
                            </a></li>
                        </div>
                    </ul>
                </div>
            </div>
            <MovieCard
            v-for="movie in store.movies"
            :key="movie.id"
            :movie="movie"
            />
        </div>
    </main>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import { useMovieListStore } from '../stores/movielist'
import axios from 'axios'
import MovieCard from '../components/MovieCard.vue'

const store = useMovieListStore()
const router = useRouter()

onMounted(()=>{
    store.getGenreList()
})

const sortMovie= (number) =>{
    store.getMovieList(number)
}

</script>

<style scoped>
.main{
    padding-top:5.8rem;
}

</style>