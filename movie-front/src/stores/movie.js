import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'

export const useMovieStore = defineStore('movie', () => {

  const API_URL = 'http://127.0.0.1:8000'
  const token = ref(null)

  const signUp = function (payload) {
    const { name, year, month, day, gender, username, password1, password2 } = payload

    axios({
      method: 'post',
      url: `${API_URL}/accounts/signup/`,
      data: {
        name, year, month, day, gender, username, password1, password2
      }
    })
      .then(res => {
        const password = password1
        logIn({ username, password })
      })
      .catch(err => console.log(err))
  }

  const logIn = function (payload) {
    const { username, password } = payload

    axios({
      method: 'post',
      url: `${API_URL}/accounts/login/`,
      data: {
        username, password
      }
    })
      .then((res) => {
        token.value = res.data.key
        router.push({ name: 'main' })
      })
      .catch((err) => {
        console.log(err)
      })
  }

  const isLogin = computed(() => {
    if (token.value === null) {
      return false
    } else {
      return true
    }
  })

  const logOut = function () {
    axios({
      method: 'delete',
      url: `${API_URL}/accounts/logout/`,
    })
      .then((res) => {
        token.value = null
      })
      .catch((err) => {
        console.log(err)
      })
  }

  return { API_URL, signUp, logIn, token, isLogin, logOut }
}, { persist: true} )
