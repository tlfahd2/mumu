<template>
    <main class="main container">
        <div>
            <ArticleCard
            :article="communityStore.article"
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

const communityStore = useCommunityStore()
const route = useRoute()
const article_id = route.params.article_id

onMounted(()=>{
    communityStore.getArticle(article_id)
})



</script>

<style scoped>

</style>