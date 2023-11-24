<template>
    <main class="main container">
      <div class="form-container">
        <form @submit.prevent="createArticle" class="article-form">
          <label for="title" class="form-label">제목</label>
          <input type="text" id="title" v-model.trim="title" class="form-input">
  
          <label for="content" class="form-label">내용</label>
          <textarea name="내용" id="content" cols="30" rows="10" v-model.trim="content" class="form-textarea"></textarea>
  
          <button type="submit" class="form-button">생성</button>
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

@font-face {
  font-family: "yeonsung";
  src: url("../fonts/BMYEONSUNG_ttf.ttf")
}

.form-container {
  max-width: 600px;
  margin: 0 auto;
}

.article-form {
  background-color: #f4f4f4;
  padding: 20px;
  border-radius: 8px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.form-label {
  display: block;
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