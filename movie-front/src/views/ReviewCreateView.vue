<template>
    <main class="main">
        <div>
            <form @submit.prevent="createReview">
                <label for="title">영화 제목</label>
                <input type="text" id="title" v-model.trim="title">
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

const title = ref('')
const content = ref('')
const rank = ref('')
const scores = ref([])


const createReview = () =>{
        axios({
            method: 'post',
            url: `${movieStore.API_URL}/reviews/`,
            data : {
                movie : title.value,
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
</script>

<style scoped>

</style>