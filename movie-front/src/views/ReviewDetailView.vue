<template>
    <main class="main">
        <div>
            <ReviewCard
            :review="movieStore.review"
            />
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
import ReviewCard from '../components/ReviewCard.vue'

const movieStore = useMovieStore()
const route = useRoute()
const review_id = route.params.review_id

onMounted(()=>{
    movieStore.getReview(review_id)
})



</script>

<style scoped>

</style>