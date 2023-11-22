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
            <button @click="like" v-if="isLike === true">좋아요 취소</button>
            <button @click="like" v-else>좋아요</button>
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

const accountStore = useAccountStore()
const movieStore = useMovieStore()
const route = useRoute()
const movie_id = route.params.movie_id

const user = ref({})
const movie = ref({})
const isLike = ref('')

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

const getUser = function () {
    axios({
      method: 'post',
      url: `${accountStore.API_URL}/api/v1/accounts/${accountStore.user_username}/`,
      headers: {
        Authorization: `Token ${accountStore.token}`
      }
    })
    .then((res) => {
      user.value = res.data
    })
    .catch((err) => {
      console.log(err)
    })
  }
getUser()

const like = function () {
    axios({
      method: 'post',
      url: `${movieStore.API_URL}/like_movies/${movie_id}/${accountStore.user_pk}/`,
      headers: {
        Authorization: `Token ${accountStore.token}`
      }
    })
    .then((res) => {
        getUser()
        isLike.value = res.data
    })
    .catch((err) => {
      console.log(err)
    })
}


</script>

<style scoped>
.main{
    padding-top: 5.8rem;
}
</style>