<template>
    <div class="card">
        <img v-if="person?.profile_path" :src="store.BASE_IMAGE_URL+person?.profile_path" :alt="person?.name">
        <p>{{ person?.name }}</p>
    </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import { useMovieListStore } from '../stores/movielist'
import axios from 'axios'

const store = useMovieListStore()
const props = defineProps({
    person:Object
})

</script>

<style scoped>
.card{
    width: 200px;
}

</style>