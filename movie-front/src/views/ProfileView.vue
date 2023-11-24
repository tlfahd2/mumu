<template>
  <transition name="modal">
    <div class="modal-mask">
      <div class="modal-wrapper">
        <div class="modal-container">
          <div class="modal-header">
            <div class="modal-body">
              <h1 class="modal-title fs-5" id="staticBackdropLabel">{{ accountStore.user.name }}님의 프로필</h1>
            </div>
            <div class="modal-body">
              내용
          </div>
          </div>
        </div>
      </div>
    </div>
  </transition>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { useAccountStore } from '../stores/account'
import { useRouter, useRoute } from 'vue-router'
import axios from 'axios'
import MovieCard from '../components/MovieCard.vue'


const accountStore = useAccountStore()
const router = useRouter()
const route = useRoute()
const isFollow = ref(false)
const is_show = ref(false)
const selected = ref(1)

const props = defineProps({
  username: String
})
console.log(props.username)
onMounted(() => {
  accountStore.getUser(props.username)
  setTimeout(() => {
    if (accountStore.user.followers?.find((follower) => follower.id === accountStore.user_pk)) {
      isFollow.value = true
    }
    else {
      isFollow.value = false
    }
  }, 100)
})

const follow = function () {
  axios({
    method: 'post',
    url: `${accountStore.API_URL}/api/v1/accounts/follow/${accountStore.user_pk}/${route.params.username}/`,
    headers: {
      Authorization: `Token ${accountStore.token}`
    }
  })
    .then((res) => {
      accountStore.getUser(route.params.username)
      isFollow.value = !isFollow.value
    })
    .catch((err) => {
      console.log(err)
    })
}

const handle_toggle = function (event) {
    // console.log(this.is_show)
    this.is_show = !this.is_show
}

const goFollowerList = function () {
  selected.value = 2
}

const goFollowingList = function () {
  selected.value = 3
}

const goUser = function (username) {
  selected.value = 1
  accountStore.getUser(username)
}

const goMain = function () {
  selected.value = 1
}
</script>

<style scoped>
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
</style>