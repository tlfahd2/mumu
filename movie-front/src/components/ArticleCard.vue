<template>
    <div class="article">
      <div class="article-header">
        <p class="author">{{ article.user?.username }}</p>
        <h2 class="title">{{ article.title }}</h2>
        <p class="updated-date">최종 수정 : {{ formatDateTime(article.updated_at) }}</p>
      </div>
      <hr>
      <div class="article-content">
        <p class="content">{{ article.content }}</p>
      </div>
      <hr>
      <div class="button-container">
        <button class="bi bi-pencil" style="border: none; background-color: transparent; margin-right: 10px;" @click="updateArticle"></button>
        <button class="bi bi-trash" style="border: none; background-color: transparent; margin-right: 10px;" @click="deleteArticle"></button>
      </div>
      <form class="comment-form" @submit.prevent="createComment(article.id)">
        <input type="text" placeholder="댓글을 입력해주세요" v-model="commentContent" class="comment-input">
        <button type="submit" class="bi bi-file-plus" style="border: none; background-color: transparent; margin-right: 10px;"></button>
      </form>
      <hr>
      <CommentCard
        v-for="comment in communityStore.comments"
        :key="comment.id"
        :comment="comment"
        :article-id="article.id"
        @delete-comment="deleteComment"
      />
      <hr>
    </div>
  </template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import { useAccountStore } from '../stores/account'
import { useMovieStore } from '../stores/movie'
import { useCommunityStore } from '../stores/community'
import axios from 'axios'
import CommentCard from '../components/CommentCard.vue'

const props = defineProps({
    article:Object
})

const communityStore = useCommunityStore()
const accountStore = useAccountStore()
const router = useRouter()
const commentContent = ref('')

onMounted(()=>{
    communityStore.getCommentList(props.article.id)
})

const updateArticle = () =>{
    router.push({name : 'updateArticle', params:{article_id:props.article.id}})
}

const deleteArticle = ()=>{
    axios({
        method:'delete',
        url: `${communityStore.API_URL}/${props.article.id}/`,
        headers: {
            Authorization: `Token ${accountStore.token}`}
    }
    ).then((response)=>{
        console.log(response.data)
        router.push({name:'communitymain'})
    })
}
const createComment= (article_pk) => {
    axios({
        method: 'post',
        url: `${communityStore.API_URL}/${article_pk}/comments/`,
        data: {
            content :commentContent.value, 
        },
        headers: {
        Authorization: `Token ${accountStore.token}`}
    }).then((response)=>{
        console.log('댓글 생성 완료')
        commentContent.value = ''
        communityStore.getCommentList(article_pk)
    }).catch((err)=>{
        console.log(err)
    })
}

const deleteComment = (args) =>{
    axios({
        method:'delete',
        url: `${communityStore.API_URL}/${args.articleId}/comments/${args.commentId}`,
        headers: {
            Authorization: `Token ${accountStore.token}`}
    }
    ).then((response)=>{
        console.log(response.data)
        communityStore.getCommentList(args.articleId)
    })
}

const formatDateTime = function (dateTimeString) {
    const options = {
        year: 'numeric',
        month: '2-digit',
        day: '2-digit',
        hour: '2-digit',
        minute: '2-digit',
        hour12: false,
    };
    const date = new Date(dateTimeString);
    const formattedDate = date.toLocaleString('ko-KR', options);

    return formattedDate
}


</script>

<style scoped>
@font-face {
  font-family: "yeonsung";
  src: url("../fonts/BMYEONSUNG_ttf.ttf")
}
@font-face {
  font-family: "euljiro";
  src: url("fonts/BMEuljiro10yearslater.ttf");
}

.article {
  background-color: #f8f9fa; /* Light gray background */
  border-radius: 8px;
  padding: 20px;
  margin-bottom: 20px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  font-family: 'yeonsung';
}

.article-header {
  text-align: center;
}

.author {
  font-weight: bold;
}

.title {
  color: rgb(39, 90, 143); /* Blue color for the title */
  margin: 10px 0;
}

.updated-date {
  color: #777;
}

.article-content {
  margin-bottom: 20px;
}
.button-container {
  display: flex;
  justify-content: flex-end; /* Align buttons to the right */
}

.btn {
    font-size: small;
  cursor: pointer;
  padding: 10px 15px;
  border: none;
  border-radius: 20px;
  color: white;
  transition: background-color 0.3s;
}

.btn:hover {
  filter: brightness(90%);
}

.update-btn {
  background-color: #28a745; /* Green color for update button */
  margin-left: 10px;
}
.submit-btn {
  background-color: #2d9946; /* Green color for update button */
  margin-left: 10px;
}

.delete-btn {
  background-color: #dc3545; /* Red color for delete button */
  margin-left: 10px;
}

.comment-form {
  display: flex;
  margin-top: 10px;
}

.comment-input {
  flex: 1;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 20px;
  margin-right: 5px;
}

.comment-input:focus {
  outline: none;
}

.comment-input::placeholder {
  color: #ccc;
}

.comment-input:focus::placeholder {
  color: transparent;
}
.updated-date {
  color: #777;
  text-align: right; /* Align to the right */
}
</style>