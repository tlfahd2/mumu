<template>
  <main class="main">
      <div>
        <div class="review-container">
  <ReviewCard :review="movieStore.review" style="width: 60%;" />
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

const review = ref({})

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