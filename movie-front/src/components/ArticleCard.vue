<template>
    <div class="article">
        <hr>
        <p>{{ article.user?.username }}</p>
        <hr>
        <p>{{ article.title }}</p>
        <p>{{ article.content }}</p>
        <p>최종 수정일 :{{ article.updated_at }}</p>
        <hr>
        <button class="btn btn-sm btn-primary" @click="updateArticle">게시글 수정</button>
        <button class="btn btn-sm btn-danger" @click="deleteArticle()">게시글 삭제</button>
        <form @submit.prevent="createComment(article.id)">
            <input type="text" placeholder="댓글을 입력해주세요" v-model="commentContent">
            <button type="submit">작성</button>
        </form>
        <hr>
        <CommentCard
        v-for="comment in communityStore.comments"
        :key="comment.id"
        :comment="comment"
        :article-id="article.id"
        @delete-comment="deleteComment"
        />
        <hr>
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
    article:Object
})

const communityStore = useCommunityStore()
const accountStore = useAccountStore()
const router = useRouter()
const commentContent = ref('')

onMounted(()=>{
    communityStore.getCommentList(props.article.id)
})

const updateArticle = () =>{
    router.push({name : 'updateArticle', params:{article_id:props.article.id}})
}

const deleteArticle = ()=>{
    axios({
        method:'delete',
        url: `${communityStore.API_URL}/${props.article.id}/`,
        headers: {
            Authorization: `Token ${accountStore.token}`}
    }
    ).then((response)=>{
        console.log(response.data)
        router.push({name:'communitymain'})
    })
}
const createComment= (article_pk) => {
    axios({
        method: 'post',
        url: `${communityStore.API_URL}/${article_pk}/comments/`,
        data: {
            content :commentContent.value, 
        },
        headers: {
        Authorization: `Token ${accountStore.token}`}
    }).then((response)=>{
        console.log('댓글 생성 완료')
        commentContent.value = ''
        communityStore.getCommentList(article_pk)
    }).catch((err)=>{
        console.log(err)
    })
}

const deleteComment = (args) =>{
    axios({
        method:'delete',
        url: `${communityStore.API_URL}/${args.articleId}/comments/${args.commentId}`,
        headers: {
            Authorization: `Token ${accountStore.token}`}
    }
    ).then((response)=>{
        console.log(response.data)
        communityStore.getCommentList(args.articleId)
    })
}


</script>

<style scoped>

</style>