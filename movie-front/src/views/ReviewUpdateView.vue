<template>
    <main class="main container">
      <div class="form-container">
        <form class="article-form">
          <label for="content" class="form-label">내용</label>
          <textarea name="내용" id="content" cols="30" rows="10" v-model.trim="content" class="form-textarea"></textarea>
          <select v-model="rank">
                    <option v-for="score in scores"> {{ score }}</option>
                </select>
          <button class="bi bi-pencil" style="border: none; background-color: transparent; margin-right: 10px; " @click="updateReview(movie_id)"></button>
        </form>
      </div>
    </main>
  </template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { useRouter, useRoute, routeLocationKey } from 'vue-router'
import { useAccountStore } from '../stores/account'                            
import { useMovieStore } from '../stores/movie'
import { useCommunityStore } from '../stores/community'
import axios from 'axios'

const movieStore = useMovieStore()
const accountStore = useAccountStore()
const router = useRouter()
const route = useRoute()

const review_id =  route.params.review_id
const content = ref('')
const rank = ref('')
const scores = ref([])
const movie = ref({})
const movie_id = ref('')

onMounted(()=>{
    movieStore.getReview(review_id)
    content.value = movieStore.review.content
    rank.value = movieStore.review.rank
    movie_id.value = movieStore.review.movie.id
})

const updateReview = (movie_id) =>{
        axios({
            method: 'put',
            url: `${movieStore.API_URL}/${movie_id}/reviews/${review_id}/`,
            data : {
                content : content.value,
                rank : rank.value
            },
            headers: {
            Authorization: `Token ${accountStore.token}`}
        }).then((response) => {
            router.push({name:'reviewDetail', params:{review_id: review_id}})
        }).catch((err) =>{
            console.log(err)
        })
    }

for (let index = 10; index > -1;index--) {
    scores.value.push(index);
    }

    axios({
        method:'get',
        url : `${movieStore.API_URL}/detail/${movie_id}`
    }).then((response)=>{
        movie.value = response.data
    }).catch((error)=>{
        console.log(error)
    })

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