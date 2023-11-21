import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios, { HttpStatusCode } from 'axios'
import router from '../router'

export const useAccountStore = defineStore('account', () => {

  const API_URL = 'http://127.0.0.1:8000'
  const token = ref(null)
  const user_pk = ref(null)
  const user_username = ref(null)
  const follower = ref('')
  const following = ref('')

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
      getUserInfo(token.value)
      router.push({ name: 'main' })
    })
    .catch((err) => {
      console.log(err)
      window.alert('아이디 또는 비밀번호를 정확히 입력하세요!')
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
      method: 'post',
      url: `${API_URL}/accounts/logout/`,
    })
    .then((res) => {
      token.value = null
    })
    .catch((err) => {
      console.log(err)
    })
  }

  const change_password = function (payload) {
    const { old_password, new_password1, new_password2 } = payload
    axios({
      method: 'post',
      url: `${API_URL}/accounts/password/change/`,
      headers: {
        Authorization: `Token ${token.value}`
      },
      data: {
        new_password1, new_password2, old_password
      }
    })
    .then((res) => {
      console.log('비밀번호 변경 완료')
      window.alert('비밀번호 변경이 완료되었습니다!')
    })
    .catch((err) => {
      if (err.response) {
        const responseData = err.response.data
        if (responseData.old_password) {
          window.alert('기존 비밀번호를 정확히 입력하세요!')
        } else if (responseData.new_password2) {
          window.alert('새로운 비밀번호를 확인하세요!')
        }
      } else {
        console.log(err)
      }
    })
  }

  // const follow = function (username) {
  //   axios({
  //     method: 'post',
  //     url: `${API_URL}/api/v1/accounts/follow/${username.value}/`,
  //     headers: {
  //       Authorization: `Token ${token.value}`
  //     }
  //   })
  //   .then((res) => {
  //     console.log('팔로우')
  //   })
  //   .catch((err) => {
  //     console.log(err)
  //   })
  // }
    
  const getUserInfo = function (token) {
    axios({
      method: 'get',
      url: `${API_URL}/accounts/user/`,
      headers: {
        'Authorization': `Token ${token}`  
      }
    })
      .then((res) => {
        user_pk.value = res.data.pk
        user_username.value = res.data.username
      })
      .catch((err) => {
        console.log(err)
      })
  } 

  // const followers = function () {
  //   axios({
  //     method: 'get',
  //     url: `${API_URL}/api/v1/accounts/follow/${user_pk.value}/`,
  //     headers: {
  //       Authorization: `Token ${token.value}`
  //     }
  //   })
  //   .then((res) => {
  //     follower.value = res.data
  //   })
  //   .catch((err) => {
  //     console.log(err)
  //   })
  // }

  // const followings = function () {
  //   axios({
  //     method: 'get',
  //     url: `${API_URL}/api/v1/accounts/following/${user_pk.value}/`,
  //     headers: {
  //       Authorization: `Token ${token.value}`
  //     }
  //   })
  //   .then((res) => {
  //     following.value = res.data
  //   })
  //   .catch((err) => {
  //     console.log(err)
  //   })
  // }
  return { API_URL, signUp, logIn, token, isLogin, logOut, change_password, user_pk, getUserInfo, user_username, follower, following }
}, { persist: true} )
