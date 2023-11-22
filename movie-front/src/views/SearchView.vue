<template>
    <main class="main">
        <div>
            <MovieCard
            v-for="movie in movies"
            :key="movie.id"
            :movie=movie
            />
        </div>
    </main>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import { useAccountStore } from '../stores/account'
import { useCommunityStore } from '../stores/community'
import { useMovieStore } from '../stores/movie'
import axios from 'axios'
import MovieCard from '../components/MovieCard.vue'


const movieStore = useMovieStore()
const accountStore = useAccountStore()
const route = useRoute()
const router= useRouter()
const keyward = route.params.keyward
const movies = ref([]
)
onMounted(()=>{
    axios({
    method : 'get',
    url : `${movieStore.API_URL}/search/${keyward}/`,
    headers: {
            Authorization: `Token ${accountStore.token}`}
    }).then((response)=>{
        console.log(response.data)
        movies.value = response.data
    })
})
    

</script>

<style scoped>

</style>