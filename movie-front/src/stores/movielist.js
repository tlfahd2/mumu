import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'

export const useMovieListStore = defineStore('movielist', () => {
    const API_URL = 'http://127.0.0.1:8000/api/v1/movies'
    const BASE_IMAGE_URL = "https://image.tmdb.org/t/p/w500"

    const movies = ref([])
    const genres = ref([])
    
    const getMovieList=(sort_num)=>{
        axios({
            method: 'get',
            url: `${API_URL}/${sort_num}`
          })
           .then((response)=>{
            console.log(response.data)
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
        console.log(response.data)
        genres.value = response.data
       })
       .catch((error)=>{
        console.log(error)
       })
    }
   

  return { movies, genres, API_URL, BASE_IMAGE_URL, getMovieList, getGenreList }
}, { persist:true })
