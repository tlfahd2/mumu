<template>
    <div>
        <p>{{ comment.user.username }}</p>
        <p>{{ comment.content }}</p>
        <p>{{ comment.user }}</p>
        <div v-if="comment.user.username === accountStore.user_username">
            <button class="btn btn-xs">수정</button>
            <button class="btn btn-xs">삭제</button>
        </div>
    </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import { useAccountStore } from '../stores/account'
import { useMovieStore } from '../stores/movie'
import axios from 'axios'

const props = defineProps({
    comment: Object
})

const accountStore = useAccountStore()
</script>

<style scoped>

</style>