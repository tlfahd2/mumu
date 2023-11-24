<template>
    <div class="comment">
      <p>{{ comment.user.username }}</p>
      <p>{{ comment.content }}</p>
      <div class="button-container" v-if="comment.user.username === accountStore.user_username">
        <button class="bi bi-trash" style="border: none; background-color: transparent; margin-right: 10px;" @click="deleteComment"></button>
      </div>
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

const emit = defineEmits(['deleteComment'])
const props = defineProps({
    comment: Object,
    articleId: Number
})

const deleteComment = ()=>{
    emit('deleteComment', {articleId: props.articleId, commentId: props.comment.id})
}

const accountStore = useAccountStore()
</script>

<style scoped>
.comment {
  margin-bottom: 20px;
}

/* Shared button styles */
.btn {
  cursor: pointer;
  padding: 8px 12px;
  border: none;
  border-radius: 4px;
  color: white;
  transition: background-color 0.3s;
}

.btn:hover {
  filter: brightness(90%);
}

.delete-btn {
  background-color: #dc3545;
  border: none;
  border-radius: 20px;
}

.button-container {
  display: flex;
  justify-content: flex-end; /* Align button to the right */
}

.comment-form {
  display: flex;
  margin-top: 10px;
}

.comment-input {
  flex: 1;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 20px; /* Adjust the border-radius for more roundness */
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
</style>