<template>
    <main class="main">
        <div>
            <button style="width: 50px;" @click="handle_toggle(event)">
                리뷰 생성
            </button>
            <div v-show="is_show" class="modal-wrap">
                <div class="modal-container">
                    <form @submit.prevent="createReview">
                        <div class="modal-header">
                            <img :src="movieStore.BASE_IMAGE_URL + movie.poster_path" :alt="movie.title"
                                style="width: 100px; margin-right: 5px;">
                            <div class="header-content">
                                <div class="content-rank-container">
                                    <textarea name="내용" id="content" cols="30" rows="5" v-model.trim="content"></textarea>
                                    <div class="rank-create-container">
                                        <div class="select-container">
                                            <select v-model="rank">
                                                <option v-for="score in scores">{{ score }}</option>
                                            </select>
                                        </div>
                                        <button type="submit">생성</button>
                                    </div>
                                </div>
                            </div>
                            <i class="bi bi-x-octagon" @click="handle_toggle(event)"></i>
                        </div>
                    </form>
                    <div v-for="review in movieStore.movie_reviews">
                        <div class="ranking-icons">
                <template v-for="i in 5">
                  <i :class="getStarClass(i, review.rank)"></i>
                </template>
              </div>
                        <div style="max-width: fit-content;">
                            <p @click="moveDetail(review.id)" style="cursor: pointer;">{{ review.content }} </p>
                        </div>
                        <hr>
                    </div>
                </div>
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

const movieStore = useMovieStore()
const accountStore = useAccountStore()
const router = useRouter()
const route = useRoute()
const is_show = ref(false)


const title = ref('')
const content = ref('')
const rank = ref(0)
const scores = ref([])
const movie_id = route.params.movie_id

const props = defineProps({
    movie: Object
})

onMounted(() => {
    movieStore.getMovieReviewList(movie_id)
})

// 리뷰 생성
const createReview = () => {
    axios({
        method: 'post',
        url: `${movieStore.API_URL}/${movie_id}/reviews/`,
        data: {
            content: content.value,
            rank: rank.value
        },
        headers: {
            Authorization: `Token ${accountStore.token}`
        }
    }).then((response) => {
        movieStore.getMovieReviewList(props.movie.id)
    }).catch((err) => {
        console.log(err)
    })
}

for (let index = 10; index > -1; index--) {
    scores.value.push(index);
}


const handle_toggle = function (event) {
    // console.log(this.is_show)
    this.is_show = !this.is_show
}

const moveDetail = (review_id)=>{
    router.push({ name:'reviewDetail', params:{ review_id: review_id }})
}

const getStarClass = (index, rank) => {
  const fullStars = Math.ceil(rank / 2);
  const fullStars2 = Math.floor(rank / 2)
  const halfStars = rank % 2? 1: 0;

  if (index < fullStars) {
    return 'bi bi-star-fill';
  } else if (index === fullStars2 && halfStars === 1) {
    return 'bi bi-star-half';
  } else {
    return 'bi bi-star';
  }
};

</script>

<style scoped>
.modal-wrap {
    position: fixed;
    left: 0;
    top: 0;
    width: 100%;
    height: 100%;
    background: rgba(0, 0, 0, 0.4);
}

/* modal or popup */
.modal-container {
    position: relative;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    width: 550px;
    max-height: 80vh; /* Set a maximum height for the modal, 80% of the viewport height */
    overflow-y: auto; /* Enable vertical scrolling when the content exceeds the height */
    background: #fff;
    border-radius: 10px;
    padding: 20px;
    box-sizing: border-box;
}

.modal-header {
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-bottom: 10px;
    overflow: hidden; /* Hide overflowing content in the header */
}


.modal-header img {
    flex-shrink: 0;
}

.header-content {
    flex-grow: 1;
}

.content-rank-container {
    display: flex;
    flex-direction: column;
}

textarea {
    width: 100%;
    margin-bottom: 5px;
}

.rank-create-container {
    display: flex;
    justify-content: space-between;
}

.select-container {
    display: inline-block;
    width: 80px;
}

select {
    width: 100%;
    padding: 5px;
    box-sizing: border-box;
}

button {
    flex-shrink: 0;
}

.modal-header i {
    background: none;
    border: none;
    font-size: 16px;
    cursor: pointer;
    margin-bottom: 150px;
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