<template>
    <main>
        <div>
            <form>
                <label for="title"></label>
                <input type="text" id="title" v-model="title">
                <label for="content"></label>
                <input type="text" id="content" v-model="content">
            </form>
        </div>
    </main>
    
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import { useAccountStore } from '../stores/account'
import { useMovieStore } from '../stores/movie'
import axios from 'axios'

const title = ref('')
const content = ref('')

const createArticle = () =>{
        axios({
            method:'post',
            url: `${API_URL}/`,
            data : {
                title : title.value,
                content : content.value,
            }
        })
    }

</script>

<style scoped>

</style>