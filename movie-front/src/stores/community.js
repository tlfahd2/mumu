import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'

export const useCommunityStore = defineStore('community', () => {
    const API_URL = 'http://127.0.0.1:8000/api/v1/community/articles'
    const articles = ref([])
    
    const getArticleList = () =>{
        axios({
            method: 'get',
            url: `${API_URL}/`
        }).then((response)=>{
            articles.value = response.data
        }).catch((err)=>{
            console.log(err)
        })
    }
    

   

  return { API_URL, articles, getArticleList  }
}, { persist:true })
