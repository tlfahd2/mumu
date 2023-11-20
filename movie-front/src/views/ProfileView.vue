<template>
    <div>
        <h1>{{ username }}의 프로필</h1>
        <button @click="follow">팔로우</button>
        <p>팔로워 수 : {{ follower }}</p>
        <p>팔로잉 수 : {{ following }}</p>
        
    </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import { useAccountStore } from '../stores/account'

defineProps({
    username: String
})

const accountStore = useAccountStore()

const follow = ref(accountStore.follow)

const follower = ref(accountStore.follower)

const following = ref(accountStore.following)
</script>

<style scoped>

</style>