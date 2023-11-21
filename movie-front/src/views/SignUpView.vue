<template>
    <div>
        <h1>회원가입</h1>
        <form @submit.prevent="signUp">
            <!-- <label for="name">이름 : </label> -->
            <input type="text" id="name" v-model.trim="name" placeholder="name">
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
            <!-- <label for="username">아이디 : </label> -->
            <input type="text" id="username" v-model.trim="username" placeholder="id">
            <br>
            <br>
            <div class="password_eye">
                <!-- <label for="password1">비밀번호 : </label> -->
                <div class="input-container">
                    <input v-if="is_looking === false" type="password" id="password1" v-model.trim="password1" placeholder="password"/>
                    <input v-if="is_looking === true" type="text" id="password1" v-model.trim="password1" placeholder="password"/>
                    <label class="bi" @click="change_looking">
                        <i v-if="!is_looking" class="bi-eyeglasses"></i>
                        <i v-else class="bi-sunglasses"></i>
                    </label>
                </div>
            </div>
            <br>
            <div class="password_eye">
                <!-- <label for="password2">비밀번호 확인 : </label> -->
                <div class="input-container">
                    <input v-if="is_looking === false" type="password" id="password2" v-model.trim="password2" placeholder="password confirm"/>
                    <input v-if="is_looking === true" type="text" id="password2" v-model.trim="password2" placeholder="password confirm"/>
                </div>
            </div>
            <br>
            <input type="submit" value="SignUp">
        </form>
    </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import { useAccountStore } from '../stores/account'
import { useMovieStore } from '../stores/movie'
import axios from 'axios'


const accountStore = useAccountStore()

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

let is_looking = ref(false)

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
    accountStore.signUp(payload)
}

const change_looking = function () {
    is_looking.value = !is_looking.value
}
</script>

<style scoped>
.password_eye {
    position:relative;
}

.input-container {
  position: relative;
  display: inline-block;
}

.input-container input {
  padding-right: 30px; 
}

.bi {
  position: absolute;
  top: 50%;
  right: 10px; 
  transform: translateY(-50%);
  cursor: pointer;
}
</style>