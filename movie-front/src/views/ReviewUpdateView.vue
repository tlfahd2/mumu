<template>
    <main class="main">
        <div>
            <img :src="movieStore.BASE_IMAGE_URL+movie.poster_path" :alt="movie.title">
            <form @submit.prevent="updateReview">
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
const movie = ref({})
const movie_id = movieStore.review.movie.id

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
            router.push({name:'reviewDetail', params:{review_id: review_id}})
        }).catch((err) =>{
            console.log(err)
        })
    }

for (let index = 10; index > -1;index--) {
    scores.value.push(index);
    }

    axios({
        method:'get',
        url : `${movieStore.API_URL}/detail/${movie_id}`
    }).then((response)=>{
        movie.value = response.data
    }).catch((error)=>{
        console.log(error)
    })

</script>

<style scoped>

</style>