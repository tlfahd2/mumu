<template>
    <main class="main">
        <div>
            <form @submit.prevent="updateArticle">
                <label for="title">제목</label>
                <input type="text" id="title" v-model.trim="title">
                <label for="content">내용</label>
                <textarea name="내용" id="content" cols="30" rows="10" v-model.trim="content"></textarea>
                <button type="submit">수정</button>
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
const route = useRoute()

const article_id =  route.params.article_id
const title = ref('')
const content = ref('')

onMounted(()=>{
    communityStore.getArticle(article_id)
    title.value = communityStore.article.title
    content.value = communityStore.article.content
})

const updateArticle = () =>{
        axios({
            method: 'put',
            url: `${communityStore.API_URL}/${article_id}/`,
            data : {
                title : title.value,
                content : content.value,
            },
            headers: {
            Authorization: `Token ${accountStore.token}`}
        }).then((response) => {
            router.push({name:'articleDetail', params:{article_id: article_id}})
        }).catch((err) =>{
            console.log(err)
        })
    }

</script>

<style scoped>

</style>