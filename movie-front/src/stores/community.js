import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'

export const useCommunityStore = defineStore('community', () => {
    const API_URL = 'http://127.0.0.1:8000/api/v1/community/articles'
    const articles = ref([])
    const article = ref({})
    const comments = ref([])
    
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
    const getArticle = (article_id) =>{
        axios({
            method:'get',
            url:`${API_URL}/${article_id}/`
        }).then((response)=>{
            article.value = response.data
        }).catch((error)=>{
            console.log(error)
        })
    }
    const getCommentList = (article_id) =>{
        axios({
            method:'get',
            url:`${API_URL}/${article_id}/comments/`
        }).then((response)=>{
            console.log('댓글 가져오기')
            comments.value = response.data
        }).catch((error)=>{
            console.log(error)
        })
    }

  return { API_URL, articles, article, comments, getArticleList, getArticle, getCommentList }
}, { persist:true })
