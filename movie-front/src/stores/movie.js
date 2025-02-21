import { ref, computed, onMounted } from 'vue'
import { defineStore } from 'pinia'
import { useAccountStore } from '../stores/account'
import axios from 'axios'


export const useMovieStore = defineStore('movie', () => {
    const API_URL = 'http://127.0.0.1:8000/api/v1/movies'
    const BASE_IMAGE_URL = "https://image.tmdb.org/t/p/w500"
    const accountStore = useAccountStore()

    const movies = ref([])
    const movie = ref({})
    const genres = ref([])
    const reviews = ref([])
    const review = ref([])
    const movie_reviews = ref([])
    const result = ref([])
    const movie_review = ref({})


    const getMovieList=(sort_num, page)=>{
        axios({
            method: 'get',
            url: `${API_URL}/sort/${sort_num}/page/${page}`,
            headers: {
              Authorization: `Token ${accountStore.token}`}
          })
           .then((response)=>{
            movies.value = response.data
           })
           .catch((error)=>{
            console.log(error)
           })
    }

    const getMovie = (movie_id) =>{
      axios({
        method:'get',
        url : `${API_URL}/detail/${movie_id}`
      }).then((response)=>{
          movie.value = response.data
      }).catch((error)=>{
          console.log(error)
      })
    }
    
    const getGenreList = () =>{
      axios({
        method : 'get',
        url:`${API_URL}/genres`,
        headers: {
          Authorization: `Token ${accountStore.token}`}
      }).then((response)=>{
        genres.value = response.data
       })
       .catch((error)=>{
        console.log(error)
       })
    }

    const getReviewList = () =>{
      axios({
        method: 'get',
        url: `${API_URL}/reviews/`,
        headers: {
          Authorization: `Token ${accountStore.token}`}
      }).then((response)=>{
          reviews.value = response.data
      }).catch((err)=>{
          console.log(err)
      }) 
    }

    const getMovieReviewList = (movie_id) => {
      axios({
        method: 'get',
        url: `${API_URL}/${movie_id}/reviews/`,
        headers: {
          Authorization: `Token ${accountStore.token}`}
      }).then((response)=>{
          movie_reviews.value = response.data
      }).catch((err)=>{
          console.log(err)
      }) 
    }

    const getReview = (review_id) =>{
      axios({
          method:'get',
          url:`${API_URL}/reviews/${review_id}/`,
          headers: {
            Authorization: `Token ${accountStore.token}`}
      }).then((response)=>{
          review.value = response.data
      }).catch((error)=>{
          console.log(error)
      })
    }


    const getSerchResult = (keyword) => {
      axios({
      method : 'get',
      url : `${API_URL}/search/${keyword}/`,
      headers: {
              Authorization: `Token ${accountStore.token}`}
      }).then((response)=>{
          result.value = response.data
      })
    }
    
    const getMovieReviewDetail = (movie_id, review_id) => {
      axios({
        method: 'get',
        url: `${API_URL}/${movie_id}/reviews/${review_id}/`,
        headers: {
          Authorization: `Token ${accountStore.token}`}
      }).then((response)=>{
          movie_review.value = response.data
      }).catch((err)=>{
          console.log(err)
      }) 
    }


  return { movies, movie, genres, reviews, review, movie_reviews, movie_review, result, API_URL, BASE_IMAGE_URL, getMovieList, getMovie, getGenreList, getReviewList, getReview, getMovieReviewList, getSerchResult, getMovieReviewDetail }
}, { persist:true })
