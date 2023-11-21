<template>
    <main class="main">
        <div>
            <form @submit.prevent="updateReview">
                <label for="title">제목</label>
                <input type="text" id="title" v-model.trim="title">
                <label for="content">내용</label>
                <textarea name="내용" id="content" cols="30" rows="10" v-model.trim="content"></textarea>
                <select v-model="rank">
                    <option v-for="score in scores"> {{ score }}</option>
                </select>
                <button type="submit">수정</button>
            </form>
        </div>
    </main>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { useRouter, useRoute, routeLocationKey } from 'vue-router'
import { useAccountStore } from '../stores/account'                            
import { useMovieStore } from '../stores/movie'
import { useCommunityStore } from '../stores/community'
import axios from 'axios'

const movieStore = useMovieStore()
const accountStore = useAccountStore()
const router = useRouter()
const route = useRoute()

const review_id =  route.params.review_id
const content = ref('')
const rank = ref('')
const scores = ref([])


onMounted(()=>{
    movieStore.getReview(review_id)
    content.value = movieStore.review.content
    rank.value = movieStore.review.rank
})

const updateReview = () =>{
        axios({
            method: 'put',
            url: `${movieStore.API_URL}/reviews/${review_id}/`,
            data : {
                content : content.value,
                rank : rank.value
            },
            headers: {
            Authorization: `Token ${accountStore.token}`}
        }).then((response) => {
            router.push({name:'reviewDetail', params:{review_id: reivew_id}})
        }).catch((err) =>{
            console.log(err)
        })
    }

for (let index = 10; index > -1;index--) {
    scores.value.push(index);
    }
</script>

<style scoped>

</style>