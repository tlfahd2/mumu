<template>
    <main class="main">
        <div>
            <img :src="movieStore.BASE_IMAGE_URL+movie.poster_path" :alt="movie.title">
            <form @submit.prevent="createReview">
                <label for="content">내용</label>
                <textarea name="내용" id="content" cols="30" rows="10" v-model.trim="content"></textarea>
                <select v-model="rank">
                    <option v-for="score in scores"> {{ score }}</option>
                </select>
                <button type="submit">생성</button>
            </form>
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

const movieStore = useMovieStore()
const accountStore = useAccountStore()
const router = useRouter()
const route = useRoute()

const title = ref('')
const content = ref('')
const rank = ref('')
const scores = ref([])
const movie_id = route.params.movie_id
const movie = ref({})


const createReview = () =>{
        axios({
            method: 'post',
            url: `${movieStore.API_URL}/${movie_id}/reviews/`,
            data : {
                content : content.value,
                rank : rank.value
            },
            headers: {
            Authorization: `Token ${accountStore.token}`}
        }).then((response) => {
            router.push({name:'communitymain'})
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