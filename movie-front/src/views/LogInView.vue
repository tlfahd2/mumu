<template>
    <div>
      <h1>로그인</h1>
      <form @submit.prevent="logIn">
        <!-- <label for="username">아이디 :</label> -->
        <input type="text" v-model.trim="username" placeholder="id">
        <div class="password_eye">
                <!-- <label for="password">비밀번호 : </label> -->
                <div class="input-container">
                    <input v-if="is_looking === false" type="password" id="password" v-model.trim="password" placeholder="password" />
                    <input v-if="is_looking === true" type="text" id="password" v-model.trim="password" placeholder="password"/>
                    <label class="bi" @click="change_looking">
                        <i v-if="!is_looking" class="bi-eyeglasses"></i>
                        <i v-else class="bi-sunglasses"></i>
                    </label>
                </div>
            </div>
        <input type="submit" value="로그인">
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
  const username = ref(null)
  const password = ref(null)
  let is_looking = ref(false)
  
  const logIn = function () {
    const payload = {
      username: username.value,
      password: password.value
    }
    accountStore.logIn(payload)
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
  