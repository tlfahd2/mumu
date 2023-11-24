<template>
    <main class="main container">
        <h2 class="title"> "{{ route.params.keyword }}"에 대한 검색결과</h2>
        <div
            v-if="movieStore.result.length === 0">
            <h3>검색 결과가 없습니다</h3>
        </div>
        <div v-else class="movie-list">
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
const route = useRoute()
let keyword = route.params.keyword
const movies = ref([])

onMounted(()=>{
    movieStore.getSerchResult(keyword)
})
    
onBeforeRouteUpdate((to, from) => {
    keyword = to.params.keyword
    movieStore.getSerchResult(keyword)
    axios({
    method : 'get',
    url : `${movieStore.API_URL}/search/${keyword}/`,

    }).then((response)=>{
        console.log(response.data)
        movies.value = response.data
    })
})
</script>

<style scoped>
@font-face {
  font-family: "yeonsung";
  src: url("../fonts/BMYEONSUNG_ttf.ttf")
}
.title{
    font-family: "yeonsung";
}
.movie-list{
    display: flex;
    flex-wrap: wrap;
}

</style>