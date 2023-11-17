<template>
    <div>
        <h1>회원가입</h1>
        <form @submit.prevent="signUp">
            <label for="name">이름 : </label>
            <input type="text" id="name" v-model.trim="name">
            <br>
            <br>
            <p>생년월일 : </p>
            <select v-model="year">
                <option v-for="year in years"> {{ year }}</option>
            </select>년
            <select v-model="month">
                <option v-for="month in months"> {{ month }}</option>
            </select>월
            <select v-model="day">
                <option v-for="day in days"> {{ day }}</option>
            </select>일
            <br>
            <br>
            <p>성별 :</p>
            <input type="radio" id="man" value="남자" v-model="gender" />
            <label for="man">남자</label>
            <input type="radio" id="woman" value="여자" v-model="gender" />
            <label for="woman">여자</label>
            <br>
            <br>
            <label for="username">아이디 : </label>
            <input type="text" id="username" v-model.trim="username">
            <br>
            <br>
            <label for="password1">비밀번호 : </label>
            <input type="password" id="password1" v-model.trim="password1">
            <br>
            <br>
            <label for="password2">비밀번호 확인 : </label>
            <input type="password" id="password2" v-model.trim="password2">
            <br>
            <br>
            <input type="submit" value="SignUp">
        </form>
    </div>
</template>

<script setup>
import { ref } from 'vue'
import { useMovieStore } from '@/stores/movie'

const store = useMovieStore()

const name = ref(null)
const year = ref(null)
const month = ref(null)
const day = ref(null)
const gender = ref('')
const username = ref(null)
const password1 = ref(null)
const password2 = ref(null)

let years = ref([])
let months = ref([])
let days = ref([])

for (let index = 2023; index > 1900;index--) {
    years.value.push(index);
}

for (let index = 1; index < 13;index++) {
    months.value.push(index);
}

for (let index = 1; index < 32;index++) {
    days.value.push(index);
}

const signUp = function () {
    const payload = {
        name: name.value,
        year: year.value,
        month: month.value,
        day: day.value,
        gender: gender.value,
        username: username.value,
        password1: password1.value,
        password2: password2.value
    }
    store.signUp(payload)
}
</script>

<style scoped>

</style>