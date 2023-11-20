<template>
    <div>
        <p>{{ comment.user.username }}</p>
        <p>{{ comment.content }}</p>
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

</script>

<style scoped>

</style>