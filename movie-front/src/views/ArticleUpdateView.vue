<template>
    <main class="main container">
      <div class="form-container">
        <form @submit.prevent="updateArticle" class="article-form">
          <label for="title" class="form-label">제목</label>
          <p>{{ title }}</p>
  
          <label for="content" class="form-label">내용</label>
          <textarea name="내용" id="content" cols="30" rows="10" v-model.trim="content" class="form-textarea"></textarea>
  
          <button class="bi bi-pencil" style="border: none; background-color: transparent; margin-right: 10px;" @click="updateArticle"></button>
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

@font-face {
  font-family: "yeonsung";
  src: url("../fonts/BMYEONSUNG_ttf.ttf")
}

.main {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
}

.container {
  max-width: 600px;
}

.form-container {
  background-color: #f4f4f4;
  padding: 20px;
  border-radius: 8px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.update-article-form {
  display: flex;
  flex-direction: column;
}

.form-label {
  margin-bottom: 8px;
  font-weight: bold;
}

.form-input,
.form-textarea {
  width: 100%;
  padding: 8px;
  margin-bottom: 16px;
  box-sizing: border-box;
  border: 1px solid #ccc;
  border-radius: 4px;
}

.form-button {
  background-color: #4caf50;
  color: white;
  padding: 10px 15px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}
</style>