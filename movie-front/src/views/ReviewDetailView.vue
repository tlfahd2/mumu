<template>
  <main class="main">
      <div>
        <div class="review-container">
  <ReviewCard :review="movieStore.review" style="width: 60%;" />
</div>

          <div v-if="accountStore.user_username !== user.username">
          <button @click="like" v-if="isLike === true">좋아요 취소</button>
          <button @click="like" v-if="isLike === false && isHate === false">좋아요</button>
          <button @click="hate" v-if="isHate === true">싫어요 취소</button>
          <button @click="hate" v-if="isLike === false && isHate === false">싫어요</button>
      </div>
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
import ReviewCard from '../components/ReviewCard.vue'

const movieStore = useMovieStore()
const accountStore = useAccountStore()
const route = useRoute()
const review_id = route.params.review_id
const user = ref({})

const isLike = ref('')
const isHate = ref('')


onMounted(()=>{
  movieStore.getReview(review_id)
})

const getUser = function () {
  axios({
    method: 'post',
    url: `${accountStore.API_URL}/api/v1/accounts/${accountStore.user_username}/`,
    headers: {
      Authorization: `Token ${accountStore.token}`
    }
  })
  .then((res) => {
    user.value = res.data
  })
  .catch((err) => {
    console.log(err)
  })
}
getUser()

const like = function () {
  axios({
    method: 'post',
    url: `${movieStore.API_URL}/like_reviews/${review_id}/${accountStore.user_pk}/`,
    headers: {
      Authorization: `Token ${accountStore.token}`
    }
  })
  .then((res) => {
      getUser()
      isLike.value = res.data
  })
  .catch((err) => {
    console.log(err)
  })
}

const hate = function () {
  axios({
    method: 'post',
    url: `${movieStore.API_URL}/hate_reviews/${review_id}/${accountStore.user_pk}/`,
    headers: {
      Authorization: `Token ${accountStore.token}`
    }
  })
  .then((res) => {
      getUser()
      isHate.value = res.data
  })
  .catch((err) => {
    console.log(err)
  })
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
.main{
  padding-top: 5.8rem;
  font-family: 'yeonsung';
}
.review-container {
display: flex;
justify-content: center;
height: auto; /* Optional: Set a height if you want to center vertically within the viewport */
}
</style>