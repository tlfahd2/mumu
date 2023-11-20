<template>
    <main class="main">
        <div>
            <section>
                <h1>커뮤니티</h1>
                <h4>영화에 대한 이야기를 나누는 쉼터</h4>
                <!-- 드랍 다운 방식 
                    <div class="btn-group">
                        <button type="button" class="dropdown-toggle cta" data-bs-toggle="dropdown" aria-expanded="false">
                            게시판 종류
                        </button>
                        <ul class="dropdown-menu">
                            <li><button class="dropdown-item" @click="change(1)">자유 게시판</button></li>
                            <li><button class="dropdown-item" @click="change(2)">리뷰 게시판</button></li>
                            <li><button class="dropdown-item" @click="change(3)">영화별 게시판</button></li> 
                        </ul>
                </div> -->
                <select v-model="choice">                        
                    <option class="dropdown-item" :value="1">자유 게시판</option>
                    <option class="dropdown-item" :value="2">리뷰 게시판</option>
                    <option class="dropdown-item" :value="3">영화별 게시판</option>
                </select>
            </section>
            <section>
                <h1 v-if="choice === 1">자유 게시판</h1>
                <button v-if="choice === 1" @click="createArticle">게시글 생성</button>
                <ArticleCard 
                    v-if="choice===1"
                    v-for="article in communityStore?.articles"
                    :article="article"
                    />
                <h1 v-if="choice === 2">리뷰 게시판</h1>
                <h1 v-if="choice === 3">영화별 리뷰</h1>
                <ReviewCard 
                v-if="choice === 2 || choice === 3"
                
                />
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


const choice = ref(1)

onMounted(() => {
    communityStore.getArticleList()
})

const createArticle = () => {
    router.push({ name:'createArticle' })
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