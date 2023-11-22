<template>
    <main class="main">
        <div>
            <MovieCard
            v-for="movie in movieStore.result"
            :key="movie.id"
            :movie=movie
            />
        </div>
    </main>
</template>

<script setup>
import { ref, computed, onMounted, watch } from 'vue'
import { useRouter, useRoute, onBeforeRouteUpdate } from 'vue-router'
import { useAccountStore } from '../stores/account'
import { useCommunityStore } from '../stores/community'
import { useMovieStore } from '../stores/movie'
import axios from 'axios'
import MovieCard from '../components/MovieCard.vue'


const movieStore = useMovieStore()
const accountStore = useAccountStore()
const route = useRoute()
const router= useRouter()
let keyword = route.params.keyword
const movies = ref([])

onMounted(()=>{
    movieStore.getSerchResult(keyword)
})
    
onBeforeRouteUpdate((to, from) => {
    keyword = to.params.keyword
    movieStore.getSerchResult(keyword)
})
</script>

<style scoped>

</style>