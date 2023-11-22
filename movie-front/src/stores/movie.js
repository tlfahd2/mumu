import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'


export const useMovieStore = defineStore('movie', () => {
    const API_URL = 'http://127.0.0.1:8000/api/v1/movies'
    const BASE_IMAGE_URL = "https://image.tmdb.org/t/p/w500"

    const movies = ref([])
    const genres = ref([])
    const reviews = ref([])
    const review = ref([])
    const movie_reviews = ref([])

    const getMovieList=(sort_num)=>{
        axios({
            method: 'get',
            url: `${API_URL}/sort/${sort_num}`
          })
           .then((response)=>{
            movies.value = response.data
           })
           .catch((error)=>{
            console.log(error)
           })
    }
    
    const getGenreList = () =>{
      axios({
        method : 'get',
        url:`${API_URL}/genres`
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
        url: `${API_URL}/reviews/`
      }).then((response)=>{
          reviews.value = response.data
      }).catch((err)=>{
          console.log(err)
      }) 
    }

    const getMovieReviewList = (movie_id) => {
      axios({
        method: 'get',
        url: `${API_URL}/${movie_id}/reviews/`
      }).then((response)=>{
          movie_reviews.value = response.data
      }).catch((err)=>{
          console.log(err)
      }) 
    }

    const getReview = (review_id) =>{
      axios({
          method:'get',
          url:`${API_URL}/${review_id}/`
      }).then((response)=>{
          review.value = response.data
      }).catch((error)=>{
          console.log(error)
      })
    }

    
      // else if (choice_num === 2){
      //   axios({
      //     method: 'get',
      //     url: `${API_URL}/reviews/`
      //   }).then((response)=>{
      //       reviews.value = response.data
      //   }).catch((err)=>{
      //       console.log(err)
      //   })
      // }


  return { movies, genres, reviews, review, movie_reviews, API_URL, BASE_IMAGE_URL, getMovieList, getGenreList, getReviewList, getReview, getMovieReviewList }
}, { persist:true })
