import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios, { HttpStatusCode } from 'axios'
import { useRouter } from 'vue-router'


export const useAccountStore = defineStore('account', () => {
  const router = useRouter()

  const API_URL = 'http://127.0.0.1:8000'
  const token = ref(null)
  const user_pk = ref(null)
  const user_username = ref(null)
  const follower = ref('')
  const following = ref('')
  const user = ref({})
  const isLike = ref(false)
  const isReviewLike = ref(false)
  const isReviewHate = ref(false)

  const signUp = function (payload) {
    const { name, year, month, day, gender, username, password1, password2, music } = payload

    axios({
      method: 'post',
      url: `${API_URL}/accounts/signup/`,
      data: {
        name, year, month, day, gender, username, password1, password2, music
      }
    })
      .then(res => {
        const password = password1
        logIn({ username, password })
      })
      .catch(err => {
        if (err.response) {
          const responseData = err.response.data
          console.log(responseData)
          if (responseData.username) {
            window.alert('이미 있는 아이디입니다 !')
          } else if (responseData.password1) {
            window.alert('비밀번호는 최소 8자 이상이어야 합니다 !')
          } else if (responseData.password2) {
            window.alert('비밀번호가 맞지 않습니다 !')
          } else {
            window.alert('비밀번호를 확인하세요 !')
          }
        } 
        router.push({ name: 'signup'})
      }
    )
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
      router.push({ name: 'main'})
    })
    .catch((err) => {
      console.log(err)
      window.alert('아이디 또는 비밀번호를 정확히 입력하세요!')
      router.push({ name: 'signup'})
    }
    )
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
      router.push({ name: 'signup'})
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

    const getUser = function (username) {
      axios({
        method: 'post',
        url: `${API_URL}/api/v1/accounts/${username}/`,
        headers: {
          Authorization: `Token ${token.value}`
        }
      })
      .then((res) => {
        user.value = res.data
      })
      .catch((err) => {
        console.log(err)
      })
    }

  return { API_URL, signUp, logIn, token, isLogin, logOut, change_password, user_pk, getUserInfo, user_username, follower, following, user, getUser, isLike, isReviewLike, isReviewHate }
}, { persist: true} )
