<template>
    <div class="card">
        <div class="row g-0">
            <div class="col-md-4">
                <img class="img-fluid rounded-start" :src="movieStore.BASE_IMAGE_URL+movie.poster_path" :alt="movie.title">
            </div>
            <div class="col-md-8">
                <div class="card-body">
                    <h4 class="card-title">{{ movie.title }}</h4>
                    <span class="genre" v-for="genre in movie.genres">{{ genre.name }}</span>
                    <p>개봉일 :{{ movie.release_date }}</p>
                    <p>{{ movie.runtime }}분</p>
                    <p>{{ movie.overview }}</p>
                    <ReviewCreateView :movie="movie" />
                    <button @click="like" v-if="isLike === true">좋아요 취소</button>
                    <button @click="like" v-else>좋아요</button>
                    <TrailerModal
                    v-if="movie.trailer"
                    :trailer-key="movie.trailer"
                    />
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import { useAccountStore } from '../stores/account'
import { useMovieStore } from '../stores/movie'
import axios from 'axios'
import TrailerModal from './TrailerModal.vue'
import ReviewCreateView from '../views/ReviewCreateView.vue'

const accountStore = useAccountStore()
const movieStore = useMovieStore()
const route = useRoute()
const router = useRouter()
const isLike = ref(false)
const movie_id = route.params.movie_id

const props = defineProps({
    movie:Object
})

onMounted (() => {
  if (movieStore.movie.like_users?.includes(accountStore.user_pk)){
    isLike.value = true    
  }
  else{
    isLike.value = false
  }
})

const like = function () {
    axios({
      method: 'post',
      url: `${movieStore.API_URL}/like_movies/${movie_id}/${accountStore.user_pk}/`,
      headers: {
        Authorization: `Token ${accountStore.token}`
      }
    })
    .then((res) => {
      isLike.value = !isLike.value

    })
    .catch((err) => {
      console.log(err)
    })
}

</script>

<style scoped>
.genre{
    margin:5px;
    padding:5px;
    border :solid 0.3px black;
}
</style>