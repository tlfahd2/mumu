<template>
    <div class="article">
        <hr>
        <p>{{ review.user?.username }}</p>
        <hr>
        <p>{{ review.movie.title }}</p>
        <p>{{ review.content }}</p>
        <p>{{ review.rank }}</p>
        <p>최종 수정일 :{{ review.updated_at }}</p>
        <hr>
        <button class="btn btn-sm btn-primary" @click="updateReview">게시글 수정</button>
        <button class="btn btn-sm btn-danger" @click="deleteReview()">게시글 삭제</button>
    </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import { useAccountStore } from '../stores/account'
import { useMovieStore } from '../stores/movie'
import { useCommunityStore } from '../stores/community'
import axios from 'axios'
import CommentCard from '../components/CommentCard.vue'

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
// const createComment= (article_pk) => {
//     axios({
//         method: 'post',
//         url: `${communityStore.API_URL}/${article_pk}/comments/`,
//         data: {
//             content :commentContent.value, 
//         },
//         headers: {
//         Authorization: `Token ${accountStore.token}`}
//     }).then((response)=>{
//         console.log('댓글 생성 완료')
//         commentContent.value = ''
//         communityStore.getCommentList(article_pk)
//     }).catch((err)=>{
//         console.log(err)
//     })
// }

// const deleteComment = (args) =>{
//     axios({
//         method:'delete',
//         url: `${communityStore.API_URL}/${args.articleId}/comments/${args.commentId}`,
//         headers: {
//             Authorization: `Token ${accountStore.token}`}
//     }
//     ).then((response)=>{
//         console.log(response.data)
//         communityStore.getCommentList(args.articleId)
//     })
// }


</script>

<style scoped>

</style>