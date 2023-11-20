<template>
    <div class="card">
        <img v-if="person?.profile_path" :src="movieStore.BASE_IMAGE_URL+person?.profile_path" :alt="person?.name">
        <p>{{ person?.name }}</p>
    </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import { useAccountStore } from '../stores/account'
import { useMovieStore } from '../stores/movie'
import axios from 'axios'

const movieStore = useMovieStore()
const props = defineProps({
    person:Object
})

</script>

<style scoped>
.card{
    width: 200px;
}

</style>