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
import ArticleCard from '../components/ArticleCard.vue'

const movieStore = useMovieStore()
const route = useRoute()
const review_id = route.params.reivew_id

onMounted(()=>{
    movieStore.getReivew(review_id)
})



</script>

<style scoped>

</style>