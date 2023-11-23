<template>
    <div class="review">
        <hr>
        <p>{{ review.user?.username }}</p>
        <hr>
        <p>{{ review.content }}</p>
        <p>{{ review.rank }}</p>
        <p>최종 수정 : {{ formatDateTime(review.updated_at) }}</p>
        <hr>
        <button class="btn btn-sm btn-primary" @click="updateReview">리뷰 수정</button>
        <button class="btn btn-sm btn-danger" @click="deleteReview()">리뷰 삭제</button>
    </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import { useAccountStore } from '../stores/account'
import { useMovieStore } from '../stores/movie'
import { useCommunityStore } from '../stores/community'
import axios from 'axios'

const props = defineProps({
    review:Object
})

const movieStore = useMovieStore()
const accountStore = useAccountStore()
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

</script>

<style scoped>

</style>