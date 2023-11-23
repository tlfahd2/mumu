<template>
    <div>
        <p>{{ comment.user.username }}</p>
        <hr>
        <p>{{ comment.content }}</p>
        <div v-if="comment.user.username === accountStore.user_username">
            <button class="btn btn-sm">수정</button>
            <button class="btn btn-sm btn-danger" @click="deleteComment">삭제</button>
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

</style>