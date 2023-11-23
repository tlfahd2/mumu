<template>
    <main class="main">
        <div>
            <button style="width: 50px;" @click="handle_toggle(event)">
                리뷰
            </button>
            <div v-show="is_show" class="modal-wrap">
                <div class="modal-container">
                    <div v-if="selected === 1">
                        <form @submit.prevent="createReview">
                            <div class="modal-header">
                                <img :src="movieStore.BASE_IMAGE_URL + movie.poster_path" :alt="movie.title"
                                    style="width: 100px; margin-right: 5px;">
                                <div class="header-content">
                                    <div class="content-rank-container">
                                        <textarea name="내용" id="content" cols="30" rows="5"
                                            v-model.trim="content"></textarea>
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
                                <div>
                                    <span>{{ review.user.username }} | </span>
                                    <span @click="moveDetail(review.id)" style="cursor: pointer;">{{ review.content }}
                                    </span>
                                </div>
                                <button @click="like"
                                    v-if="accountStore.isLike === true && accountStore.isHate === false">좋아요 취소</button>
                                <button @click="like"
                                    v-if="accountStore.isLike === false && accountStore.isHate === false">좋아요</button>
                                <button @click="hate"
                                    v-if="accountStore.isHate === true && accountStore.isLike === false">싫어요 취소</button>
                                <button @click="hate"
                                    v-if="accountStore.isLike === false && accountStore.isHate === false">싫어요</button>
                            </div>
                            <hr>
                        </div>
                    </div>


                    <div v-if="selected === 2">
                        <div class="modal-header">
                            <i class="bi bi-arrow-left-circle" @click="goMain"></i>
                            <div class="review">
                                <hr>
                                <p>{{ movieStore.movie_review.user?.username }}</p>
                                <hr>
                                <div class="ranking-icons">
                                    <template v-for="i in 5">
                                        <i :class="getStarClass(i, movieStore.movie_review.rank)"></i>
                                    </template>
                                </div>
                                <hr>
                                <p>{{ movieStore.movie_review.content }}</p>
                                <p>최종 수정 : {{ formatDateTime(movieStore.movie_review.updated_at) }}</p>
                                <hr>
                                <button class="btn btn-sm btn-primary" @click="moveUpdate(movieStore.movie_review.id)">리뷰
                                    수정</button>
                                <button class="btn btn-sm btn-danger" @click="deleteReview(movieStore.movie_review.id)">리뷰
                                    삭제</button>
                            </div>
                            <i class="bi bi-x-octagon" @click="handle_toggle(event)"></i>
                        </div>
                    </div>

                    <div v-if="selected === 3">
                        <form @submit.prevent="updateReview()">
                            <div class="modal-header">
                                <i class="bi bi-arrow-left-circle" @click="goMain"></i>
                                <div class="header-content">
                                    <div class="content-rank-container">
                                        <textarea name="내용" id="content" cols="30" rows="5"
                                            v-model.trim="content"></textarea>
                                        <div class="rank-create-container">
                                            <div class="select-container">
                                                <select v-model="rank">
                                                    <option v-for="score in scores">{{ score }}</option>
                                                </select>
                                            </div>
                                            <button type="submit">수정</button>
                                        </div>
                                    </div>
                                </div>
                                <i class="bi bi-x-octagon" @click="handle_toggle(event)"></i>
                            </div>
                        </form>
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
const selected = ref(1)
const update_review = ref(0)

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
        content.value = ''
        rank.value = 0
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

const moveDetail = function (review_id) {
    movieStore.getMovieReviewDetail(movie_id, review_id)
    selected.value = 2
}

// 리뷰 좋아요 싫어요
onMounted(() => {
    accountStore.getUser(accountStore.user_username)
})

const like = function () {
    axios({
        method: 'post',
        url: `${movieStore.API_URL}/like_reviews/${review_id}/${accountStore.user_pk}/`,
        headers: {
            Authorization: `Token ${accountStore.token}`
        }
    })
        .then((res) => {
            accountStore.isReviewLike = !accountStore.isReviewLike
            accountStore.getUser(accountStore.user_username)
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
            accountStore.isLike = !accountStore.isLike
            accountStore.getUser(accountStore.user_username)
        })
        .catch((err) => {
            console.log(err)
        })
}

const goMain = function () {
    selected.value = 1
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

// 최종 수정일 예쁘게
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

// 리뷰 수정
const moveUpdate = (review_id) => {
    movieStore.getMovieReviewDetail(movie_id, review_id)
    content.value = movieStore.movie_review.content
    rank.value = movieStore.movie_review.rank
    update_review.value = movieStore.movie_review.id
    selected.value = 3
}

const updateReview = () => {
    console.log(update_review)
    axios({
        method: 'put',
        url: `${movieStore.API_URL}/${movie_id}/reviews/${update_review.value}/`,
        data: {
            content: content.value,
            rank: rank.value
        },
        headers: {
            Authorization: `Token ${accountStore.token}`
        }
    }).then((response) => {
        movieStore.getMovieReviewDetail(movie_id, update_review.value)
        movieStore.getMovieReviewList(movie_id)
        content.value = ''
        rank.value = 0
        selected.value = 2
    }).catch((err) => {
        console.log(err)
    })
}

// 리뷰 삭제
const deleteReview = (review_id) => {
    axios({
        method: 'delete',
        url: `${movieStore.API_URL}/${movie_id}/reviews/${review_id}/`,
        headers: {
            Authorization: `Token ${accountStore.token}`
        }
    }
    ).then((response) => {
        movieStore.getMovieReviewList(movie_id)
        selected.value = 1
    })
}


</script>

<style scoped>
.modal-wrap {
    position: fixed;
    left: 0;
    top: 0;
    width: 100%;
    height: 100%;
    background: rgba(0, 0, 0, 0.4);
    z-index: 999;
}

/* modal or popup */
.modal-container {
    position: relative;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    width: 550px;
    max-height: 80vh;
    /* Set a maximum height for the modal, 80% of the viewport height */
    overflow-y: auto;
    /* Enable vertical scrolling when the content exceeds the height */
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
    overflow: hidden;
    /* Hide overflowing content in the header */
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
}</style>