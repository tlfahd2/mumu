<template>
    <div>
        <p @click="moveProfile">{{ myFollower.username }}</p>
    </div>
</template>

<script setup>
import { useAccountStore } from '../stores/account';

const accountStore = useAccountStore()

const moveProfile = function () {
    router.push({ name: "profile", params: { username: `${accountStore.user_username}`}})
}
</script>

<style scoped>


</style>