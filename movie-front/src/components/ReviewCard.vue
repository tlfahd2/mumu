<template>
    <div class="review">
      <hr>
      <p class="author">{{ review.user?.username }}</p>
      <hr>
      <p class="content">{{ review.content }}</p>
      <div class="ranking-icons">
              <template v-for="i in 5">
                  <i :class="getStarClass(i, review.rank)"></i>
              </template>
          </div>
      <p class="updated-date" style="text-align: right;">최종 수정: {{ formatDateTime(review.updated_at) }}</p>
      <hr>
      <div v-if="accountStore.user_username === review.user.username">
        <div class="button-container">
          <button class="bi bi-pencil" style="border: none; background-color: transparent; margin-right: 10px;" @click="updateReview"></button>
          <button class="bi bi-trash" style="border: none; background-color: transparent; margin-right: 10px;" @click="deleteReview"></button>
        </div>
      </div>
    </div>
  </template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import { useAccountStore } from '../stores/account'
import { useMovieStore } from '../stores/movie'
import { useCommunityStore } from '../stores/community'
import axios from 'axios'
const accountStore = useAccountStore()
const movieStore = useMovieStore()

const props = defineProps({
    review:Object
})

onMounted(() => {
  accountStore.getUser(accountStore.user_username)
})
const router = useRouter()
const commentContent = ref('')

const updateReview = () =>{
    router.push({name : 'updateReview', params:{review_id:props.review.id}})
}

const deleteReview = ()=>{
    axios({
        method:'delete',
        url: `${movieStore.API_URL}/reviews/${props.review.id}/`,
        headers: {
            Authorization: `Token ${accountStore.token}`}
    }
    ).then((response)=>{
        console.log(response.data)
        router.push({name:'communitymain'})
    })
}

// 최종 수정 예쁘게
const formatDateTime = function (dateTimeString) {
    const options = {
        year: 'numeric',
        month: '2-digit',
        day: '2-digit',
        hour: '2-digit',
        minute: '2-digit',
        hour12: false,
      };
      const date = new Date(dateTimeString);
      const formattedDate = date.toLocaleString('ko-KR', options);

      return formattedDate
}

// 평점 별로 나타내기
const getStarClass = (index, rank) => {
    const fullStars = Math.round(rank / 2)
    const halfStars = rank % 2 ? 1 : 0;

    if (index < fullStars) {
        return 'bi bi-star-fill';
    } else if (index === fullStars && halfStars === 1) {
        return 'bi bi-star-half';
    } else if (index === fullStars && halfStars === 0) {
        return 'bi bi-star-fill';
    } else {
        return 'bi bi-star';
    }
};

</script>

<style scoped>
.review {
  background-color: #fff; /* White background */
  border: 1px solid #ddd;
  border-radius: 8px;
  padding: 20px;
  margin-bottom: 20px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.author {
  font-weight: bold;
}

.content {
  margin-bottom: 10px;
}

.rank {
  font-weight: bold;
  color: #007bff; /* Blue color for rank */
  margin-bottom: 10px;
}

.updated-date {
  color: #777;
  
}

.button-container {
  display: flex;
  justify-content: flex-end; /* Align buttons to the right */
}

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

.update-btn {
  background-color: #28a745; /* Green color for update button */
  margin-right: 10px; /* Add margin between buttons */
}

.delete-btn {
  background-color: #dc3545; /* Red color for delete button */
}
.ranking-icons {
    color: #ffc107;
}


/* Add Bootstrap icons styles or import them in your project */
.bi-star,
.bi-star-fill,
.bi-star-half {
    font-size: 1.5rem;
    /* Adjust the size of the stars */
    margin-right: 2px;
    /* Adjust the spacing between stars */
}
</style>