<template>
    <div class="card">
        <div class="row g-0">
            <div class="col-md-4">
                <img class="img-fluid rounded-start" :src="movieStore.BASE_IMAGE_URL+ movieStore.movie?.poster_path" :alt=" movieStore.movie.title">
            </div>
              <div class="col-md-8">
                  <div class="card-body">
                      <h4 class="card-title">{{  movieStore.movie.title }}</h4>
                      <div class="movie-info">
                        <span class="genre btn" v-for="genre in  movieStore.movie.genres">{{ genre.name }}</span>
                        <span class="info">{{  movieStore.movie.release_date }}</span>
                        <span class="info">{{  movieStore.movie.runtime }}분</span>
                      </div>
                      <hr>
                      <p>{{  movieStore.movie.overview }}</p>
                      <div class="card-footer">
                        <div class="review-trailer">
                          <div class="ranking-icons">
                                <template v-for="i in 5">
                                    <i :class="getStarClass(i, movieStore.movie.vote_average)"></i>
                                </template>
                            </div>
                          <p>{{ movieStore.movie.vote_average }}</p>
                          <ReviewCreateView :movie="movieStore.movie" />
                          <TrailerModal v-if="movieStore.movie.trailer" :trailer-key="movieStore.movie.trailer" />
                          <i class="bi bi-heart-fill" @click="like" v-if="isLike === true"></i>
                          <i class="bi bi-heart" @click="like" v-else></i>
                        </div>
                      </div>
                  </div>
              </div>
        </div>
    </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import { useAccountStore } from '../stores/account'
import { useMovieStore } from '../stores/movie'
import axios from 'axios'
import TrailerModal from './TrailerModal.vue'
import ReviewCreateView from '../views/ReviewCreateView.vue'

const accountStore = useAccountStore()
const movieStore = useMovieStore()
const route = useRoute()
const isLike = ref(false)
const movie_id = route.params.movie_id

onMounted (() => {
  movieStore.getMovie(movie_id)
  setTimeout(() =>{
    if (movieStore.movie.like_users?.includes(accountStore.user_pk)){
      isLike.value = true    
    }
    else{
      isLike.value = false
    }
  },200)
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
      movieStore.getMovie(movie_id)
      isLike.value = !isLike.value

    })
    .catch((err) => {
      console.log(err)
    })
}

// 평점 별로 나타내기
const getStarClass = (index, rank) => {
    const fullStars = Math.round(rank / 2)
    const halfStars = rank % 2 ? 1 : 0;

    if (index < fullStars) {
        return 'bi bi-star-fill';
    } else if (index === fullStars && halfStars === 1) {
        return 'bi bi-star-half';
    } else if (index === fullStars && halfStars === 0) {
        return 'bi bi-star-fill';
    } else {
        return 'bi bi-star';
    }
};

</script>

<style scoped>

.card{
  font-family: "yeonsung";
  background-color: #F5F1E7;
}
.card-title{
  font-family: "euljiro";
  font-size: 60px;
}
.genre{
    margin-right: 3px;
    padding:2px;
    border :solid 0.3px black;
}
.bi{
  font-size: 30px;
  color:#FD7F4F;
  background-color: none;
}
.col-md-8{
  position: relative;
}
.card-footer {
    position: absolute;
    bottom: 0;
    left: 0;
    width: 100%;
    padding-left: 50px;
    padding-right: 50px;
  }
.review-trailer {
  display: flex;
  justify-content:space-around;
  align-items: center;
}
.info{
  margin-right: 10px;
}
.ranking-icons {
    color: #ffc107;
}


/* Add Bootstrap icons styles or import them in your project */
.bi-star,
.bi-star-fill,
.bi-star-half {
    font-size: 1.5rem;
    /* Adjust the size of the stars */
    margin-right: 2px;
    /* Adjust the spacing between stars */
}
</style>