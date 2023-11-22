<template>
    <main class="main">
        <div>
            <section>
                <h1>커뮤니티</h1>
                <h4>영화에 대한 이야기를 나누는 쉼터</h4>
                <select v-model="choice">                        
                    <option class="dropdown-item" :value="1">자유 게시판</option>
                    <option class="dropdown-item" :value="2">리뷰 게시판</option>
                    <option class="dropdown-item" :value="3">영화별 게시판</option>
                </select>
            </section>
            <section>
                <h1 v-if="choice === 1">자유 게시판</h1>
                <button v-if="choice === 1" @click="createArticle">게시글 생성</button>
                <div
                v-if="choice===1"
                v-for="article in communityStore?.articles"
                :key="article.id"
                @click="moveDetail(article.id)"
                >
                <p>{{ article.title }}</p>
                </div>

                <h1 v-if="choice === 2">리뷰 게시판</h1>
                <button v-if="choice === 2" @click="createReview">리뷰 생성</button>
                <div
                v-if="choice===2"
                v-for="review in movieStore?.reviews"
                :key="review.id"
                @click="moveReviewDetail(review.id)"
                >
                <img :src="movieStore.BASE_IMAGE_URL+review.movie.poster_path" :alt="review.movie.title">
                <p>{{ review.movie.title }}</p>
                <p>{{ review.content }}</p>
                <p>{{ review.rank }}</p>
                </div>
                <h1 v-if="choice === 3">영화별 리뷰</h1>
                <div
                v-if="choice===3"
                v-for="movie in movies"
                :key="movie.id"
                @click="moveMovieReview(movie.id)"
                >
                <img :src="movieStore.BASE_IMAGE_URL+movie.poster_path" :alt="movie.title">
    
                </div>
                <!-- <ReviewCard 
                v-if="choice === 2 || choice === 3"
                /> -->
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
    for (let index = 0; index < movieStore.reviews.length; index++) {
        if (reviews[index].movie in movies) {
            continue
        } else {
            reviews[index].movie.push(movies)
        }
        
    }
})
const createReview = () => {
    router.push({ name:'createReview' })
}
const moveReviewDetail = (review_id)=>{
    router.push({ name:'reviewDetail', params:{ review_id: review_id }})
}

// 영화별 리뷰
const moveMovieReview = (movie_id) => {
    router.push({ name: 'movieReviews', params: {movie_id: movie_id}})
}
// 드랍 다운 할 경우 사용
// const change = (choice_num) => {
//     choice.value = choice_num
//     if (choice_num === 1) {
//         communityStore.getArticleList()
//     }
//     else if (choice_num === 2 ) {
//         communityStore.getReviewList(choice_num)
//     }
//     else if (choice_num === 3 ) {
//         communityStore.getReviewList(choice_num)
//     }
// }

</script>

<style scoped>
.main{
    padding-top: 5.8rem;
}
.article{
    border:1px solid black;
}
</style>