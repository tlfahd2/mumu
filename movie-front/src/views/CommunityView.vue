<template>
  <main class="main container">
    <div>
      <section class="header-section">
        <h3 style="font-family: 'euljiro';">커뮤니티</h3>
        <h4>영화에 대한 이야기를 나누는 쉼터</h4>
        <div class="custom-select-container">
          <label for="category-select" class="sr-only"></label>
          <select v-model="choice" id="category-select" class="custom-select">
            <option class="dropdown-item" :value="1">자유 게시판</option>
            <option class="dropdown-item" :value="2">리뷰 게시판</option>
          </select>
          <span class="custom-arrow"></span>
        </div>
      </section>

      <section class="content-section">
        <div class="category-title" v-if="choice === 1">
          <h4>자유 게시판</h4>
          <button @click="createArticle" class="bi bi-file-plus" style="border: none; background-color: transparent; margin-right: 10px;"></button>
        </div>
        <div v-if="choice === 1" v-for="article in communityStore?.articles" :key="article.id" @click="moveDetail(article.id)" class="article-card">
          <p>{{ article.title }}</p>
        </div>

        <div class="category-title" v-if="choice === 2">
          <h3>리뷰 게시판</h3>
        </div>
        <div v-if="choice === 2" v-for="review in movieStore?.reviews" :key="review.id" @click="moveReviewDetail(review.id)" class="review-card">
      <div class="review-content">
        <img :src="movieStore.BASE_IMAGE_URL + review.movie.poster_path" :alt="review.movie.title" class="movie-poster">
        <div class="details">
          <p class="title">{{ review.movie.title }}</p>
          <p class="content">{{ review.content }}</p>
          <div class="ranking-icons">
              <template v-for="i in 5">
                  <i :class="getStarClass(i, review.rank)"></i>
              </template>
          </div>
        </div>
      </div>
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
@font-face {
  font-family: "yeonsung";
  src: url("../fonts/BMYEONSUNG_ttf.ttf")
}
@font-face {
  font-family: "euljiro";
  src: url("fonts/BMEuljiro10yearslater.ttf");
}
.main{
    padding-top: 5.8rem;
    font-family: 'yeonsung';
}

.container {
  max-width: 800px;
}

.header-section {
  text-align: center;
  margin-bottom: 20px;
}

.custom-select-container {
  position: relative;
  width: 120px;
  
}

.custom-select {
  appearance: none;
  -webkit-appearance: none;
  -moz-appearance: none;
  width: 100%;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 4px;
  background-color: #fff;
  cursor: pointer;
  height: fit-content;
}

.custom-arrow {
  position: absolute;
  top: 50%;
  right: 10px;
  transform: translateY(-50%);
  width: 0;
  height: 0;
  border-left: 6px solid transparent;
  border-right: 6px solid transparent;
  border-top: 6px solid #555;
}

.content-section {
  display: flex;
  flex-direction: column;
}

.category-title {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 10px;
}

.custom-button {
  background-color: #4caf50;
  color: white;
  padding: 8px 12px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

.article-card,
.review-card {
  border: 1px solid #ccc;
  padding: 15px;
  margin-bottom: 10px;
  cursor: pointer;
  background-color: #e4dcdc;
  border-radius: 20px;
}

.review-card {
  display: flex;
  cursor: pointer;
  margin-bottom: 20px;
  padding: 10px;
  border: 1px solid #ddd;
  border-radius: 8px;
}

.movie-poster {
  width: 100px; /* Adjust the width as needed */
  height: auto;
  margin-right: 20px;
}

.review-content {
  display: flex;
  align-items: center;
}

.details {
  flex: 1;
}

.title {
  font-size: 1.2em;
  font-weight: bold;
  margin-bottom: 5px;
}

.content {
  margin-bottom: 5px;
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