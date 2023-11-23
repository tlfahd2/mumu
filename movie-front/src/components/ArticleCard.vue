<template>
    <main class="main">
        <div>
            <button style="width: 50px;" @click="handle_toggle(event)">
            </button>
            <div v-show="is_show" class="modal-wrap">
                <div class="modal-container">
                    <div v-if="selected === 1">
                        <div class="modal-header">
                            <div class="article">
                                <hr>
                                <p>{{ article.user?.username }}</p>
                                <hr>
                                <hr>
                                <p>{{ article.title }}</p>
                                <p>{{ article.content }}</p>
                                <p>최종 수정 :{{ article.updated_at }}</p>
                                <hr>
                                <div v-if="accountStore.user_username === article.username">
                                    <button class="custom-button" @click="moveUpdate(article.id)">게시글
                                        수정</button>
                                    <button class="custom-button" @click="deleteArticle()">게시글
                                        삭제</button>
                                </div>
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
                            <i class="bi bi-x-octagon" @click="handle_toggle(event)"></i>
                        </div>
                    </div>

                    <div v-if="selected === 2">
                        <form @submit.prevent="updateArticle(article.id)">
                            <div class="modal-header">
                                <i  class="bi bi-arrow-left-circle" @click="goMain"></i>
                                <div class="header-content">
                                        <textarea name="내용" id="content" cols="30" rows="5"
                                            v-model.trim="content"></textarea>
                                            <button class="custom-button" type="submit">수정</button>

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
import CommentCard from '../components/CommentCard.vue'

const props = defineProps({
    article:Object
})

const communityStore = useCommunityStore()
const accountStore = useAccountStore()
const router = useRouter()
const commentContent = ref('')
const selected = ref(1)
const content = ref('')
const is_show = ref(false)

onMounted(()=>{
    communityStore.getCommentList(props.article.id)
})

const handle_toggle = function (event) {
    // console.log(this.is_show)
    this.is_show = !this.is_show
    selected.value = 1
}

const goMain = function () {
    selected.value = 1
}

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

// 게시글 수정
const moveUpdate = (article_id) => {
    communityStore.getArticle(article_id)
    content.value = communityStore.article.content
    selected.value = 2
}

const updateArticle = (article_id) => {
    axios({
        method: 'put',
        url: `${communityStore.API_URL}/${props.article.id}/`,
        data: {
            title: communityStore.article.title,
            content: content.value
        },
        headers: {
            Authorization: `Token ${accountStore.token}`
        }
    }).then((response) => {
        communityStore.getArticle(article_id)
        communityStore.getArticleList()
        content.value = ''
        selected.value = 1
    }).catch((err) => {
        console.log(err)
    })
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

#content {
        border-radius: 10px; /* Adds rounded corners */
        padding: 10px; /* Adds padding inside the textarea */
        border: 1px solid #ccc; /* Adds a border for better visibility */
        background-color: #f5f5f5; /* Sets a light background color */
        resize: none; /* Prevents the textarea from being resized by the user */
        font-family: 'Arial', sans-serif; /* Specifies the font */
    }

    .custom-select {
    border-radius: 10px; /* Adds rounded corners */
    padding: 8px; /* Adds padding inside the select */
    border: 1px solid #ccc; /* Adds a border for better visibility */
    background-color: #f5f5f5; /* Sets a light background color */
    font-size: 14px; /* Sets the font size */
    font-family: 'Arial', sans-serif; /* Specifies the font */
  }

  .custom-button {
    border-radius: 10px; /* Adds rounded corners */
    padding: 10px 20px; /* Adds padding inside the button */
    background-color: #3498db; /* Sets the background color */
    color: #fff; /* Sets the text color */
    border: none; /* Removes the default button border */
    cursor: pointer; /* Changes the cursor to a pointer on hover */
    font-size: 16px; /* Sets the font size */
    font-family: 'Arial', sans-serif; /* Specifies the font */
  }

  .custom-button:hover {
    background-color: #2980b9; /* Changes the background color on hover */
  }

</style>