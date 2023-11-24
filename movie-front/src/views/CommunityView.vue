<template>
    <main class="main container">
      <div>
        <section class="header-section">
          <h3>커뮤니티</h3>
          <h4>영화에 대한 이야기를 나누는 쉼터</h4>
          <select v-model="choice" class="custom-select">
            <option class="dropdown-item" :value="1">자유 게시판</option>
            <option class="dropdown-item" :value="2">리뷰 게시판</option>
          </select>
        </section>
  
        <section class="content-section">
          <h3 v-if="choice === 1">자유 게시판</h3>
          <button v-if="choice === 1" @click="createArticle" class="custom-button">게시글 생성</button>
          <div v-if="choice === 1" v-for="article in communityStore?.articles" :key="article.id" @click="moveDetail(article.id)" class="article-card">
            <p>{{ article.title }}</p>
          </div>
  
          <h1 v-if="choice === 2">리뷰 게시판</h1>
          <div v-if="choice === 2" v-for="review in movieStore?.reviews" :key="review.id" @click="moveReviewDetail(review.id)" class="review-card">
            <img :src="movieStore.BASE_IMAGE_URL + review.movie.poster_path" :alt="review.movie.title" class="movie-poster">
            <p>{{ review.movie.title }}</p>
            <p>{{ review.content }}</p>
            <p>{{ review.rank }}</p>
          </div>
        </section>
      </div>
    </main>
  </template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import { useAccountStore } from '../stores/account'
import { useMovieStore } from '../stores/movie'
import { useCommunityStore } from '../stores/community'
import axios from 'axios'
import ArticleCard from '../components/ArticleCard.vue'
import ReviewCard from '../components/ReviewCard.vue'

const router = useRouter()
const communityStore = useCommunityStore()
const movieStore = useMovieStore()

const choice = ref(1)
const movies = ref([])

onMounted(() => {
    communityStore.getArticleList()
})

const createArticle = () => {
    router.push({ name:'createArticle' })
}

const moveDetail = (article_id)=>{
    router.push({ name:'articleDetail', params:{ article_id: article_id }})
}

// 리뷰게시판
onMounted(() => {
    movieStore.getReviewList()
})

const moveReviewDetail = (review_id)=>{
    router.push({ name:'reviewDetail', params:{ review_id: review_id }})
}

// 영화별 리뷰
const moveMovieReview = (movie_id) => {
    router.push({ name: 'movieReviews', params: {movie_id: movie_id}})
}


</script>

<style scoped>
.main{
    padding-top: 5.8rem;
}
.article{
    border:1px solid black;
}

.header-section {
    margin-bottom: 20px;
  }

  .custom-select {
    border-radius: 10px; /* Adds rounded corners */
    padding: 8px; /* Adds padding inside the select */
    border: 1px solid #ccc; /* Adds a border for better visibility */
    background-color: #f5f5f5; /* Sets a light background color */
    font-size: 14px; /* Sets the font size */
    font-family: 'Arial', sans-serif; /* Specifies the font */
  }

  .custom-button {
    border-radius: 10px; /* Adds rounded corners */
    padding: 10px 20px; /* Adds padding inside the button */
    background-color: #3498db; /* Sets the background color */
    color: #fff; /* Sets the text color */
    border: none; /* Removes the default button border */
    cursor: pointer; /* Changes the cursor to a pointer on hover */
    font-size: 16px; /* Sets the font size */
    font-family: 'Arial', sans-serif; /* Specifies the font */
    margin-left: auto;  
}

  .content-section {
    display: flex;
    flex-wrap: wrap;
    flex-direction: row;
  }

  .article-list,
  .review-list {
    display: flex;
    flex-direction: column; /* Display items in a column */
  }

  .article-card,
  .review-card {
    border: 1px solid #ccc;
    border-radius: 8px;
    padding: 10px;
    margin: 10px;
    cursor: pointer;
    width: 200px;
  }

  .movie-poster {
    width: 100%;
    border-radius: 8px;
    margin-bottom: 10px;
  }
</style>