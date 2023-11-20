<template>
    <main class="main">
        <div>
            <form @submit.prevent="createArticle">
                <label for="title">제목</label>
                <input type="text" id="title" v-model="title">
                <label for="content">내용</label>
                <textarea name="내용" id="content" cols="30" rows="10" v-model="content"></textarea>
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

const communityStore = useCommunityStore()
const accountStore = useAccountStore()
const router = useRouter()

const title = ref('')
const content = ref('')

const createArticle = () =>{
        axios({
            method: 'post',
            url: `${communityStore.API_URL}/`,
            data : {
                title : title.value,
                content : content.value,
            },
            headers: {
            Authorization: `Token ${accountStore.token}`}
        }).then((response) => {
            // 자유 게시판 글 생성시 커뮤 메인으로 돌아가기
            router.push({name:'communitymain'})
        }).catch((err) =>{
            console.log(err)
        })
    }

</script>

<style scoped>

</style>