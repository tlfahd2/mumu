<template>
    <div>
        <!-- <img :src="movieStore.BASE_IMAGE_URL+review.movie.poster_path" :alt="review.movie.title"> -->
        <div
        v-for="review in movieStore?.movie_reviews"
        :key="reivew.id"
        @click="moveDetail(review.id)"
        >
        <p>{{ review.content }}</p>
        <p>{{ review.rank }}</p>
        </div>
    </div>
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
const route = useRoute()
const communityStore = useCommunityStore()
const movieStore = useMovieStore()
const movie_id = ref(route.params.movie_id)
// 영화별 리뷰 전체 목록
onMounted(() => {
    movieStore.getMovieReviewList()
})

const moveDetail = (review_id)=>{
    router.push({ name:'reviewDetail', params:{ review_id: review_id }})
}
</script>

<style scoped>

</style>