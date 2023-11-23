<template>
    <div>
      <div class="main">
        <div class="body">
          <!-- Choose Form -->
          <section class="form-container" >
            <span id="arrowClick" class="form-container__arrow" ref="form-container__arrow"><i class="bi bi-arrow-circle-left"
                aria-hidden="true"></i></span>
                <div class="choose-form" v-if="selected === 1">
                  <div class="overlay" ref="overlay"></div>
              <div class="title" ref="title">
                <h1 class="title__h1">Welcome<br>Start for free</h1>
              </div>
              <div class="buttons">
                <button @click="handleSignUp" class="buttons__signup" ref="buttons__signup">Sign up</button>
                <button @click="handleLogin" id="login" class="buttons__signup buttons__signup--login" ref="buttons__signup buttons__signup--login">Login</button>
              </div>
            </div>
            <!-- Login Form -->
            
            <div class="login-form--register" ref="login-form" v-if="selected === 2">
              <i class="bi bi-arrow-left-circle" @click="goMain"></i>
              <div class="form-wrapper">
                <form @submit.prevent="logIn" style="margin-top: 200px;">
                  <label class="form-wrapper__label" for="login-username">아이디</label>
                  <input id="login-username" class="form-wrapper__input" type="text" placeholder="ID" name="id" v-model.trim="id"
                    required>
                    <div class="password_eye">
                  <label class="form-wrapper__label" for="login-password">비밀번호</label>
                  <div class="input-container">
                  <input v-if="is_looking === false" v-model.trim="password" id="signup-password" class="form-wrapper__input" type="password" placeholder="Password"
                    name="password" pattern=".{3,}" title="비밀번호는 8자 이상" required>
                    <input v-if="is_looking === true" v-model.trim="password" id="signup-password" class="form-wrapper__input" type="text" placeholder="Password"
                    name="password" pattern=".{3,}" title="비밀번호는 8자 이상" required>
                    <label class="bi_password" @click="change_looking">
                              <i v-if="!is_looking" class="bi-eyeglasses"></i>
                              <i v-else class="bi-sunglasses"></i>
                          </label>
                  </div>
                  </div>
                  <button class="buttons__signup buttons__signup--login-form" ref="buttons__signup buttons__signup--login-form" type="submit" style="margin-top: 120%; text-align: center;">Login</button>
                </form>
              </div>
            </div>
            <!-- Register Form -->
  
            <div class="login-form--register" ref="login-form--register"  v-if="selected === 3">
              <i class="bi bi-arrow-left-circle" @click="goMain"></i>
              <div class="form-wrapper">
                <form @submit.prevent="signUp" style="margin-top: 40px;">
                  <label class="form-wrapper__label" for="signup-name">이름</label>
                  <input id="signup-name" class="form-wrapper__input" type="text" placeholder="name"
                    name="name" v-model.trim="name" required>
                  <label class="form-wrapper__label" for="signup-birth">생년월일</label>
                  <select v-model="year" id="signup-year" class="form-wrapper__input" placeholder="year" name="year"
                    required style="width: 30%; margin-right: 10px;">
                      <option v-for="year in years" > {{ year }}</option>
                  </select>
                  <select v-model="month" id="signup-month" class="form-wrapper__input" placeholder="month" name="month"
                    required style="width: 30%; margin-right: 10px;">
                      <option v-for="month in months"> {{ month }}</option>
                  </select>
                  <select v-model="day" id="signup-day" class="form-wrapper__input" placeholder="day" name="day"
                    required style="width: 30%;">
                      <option v-for="day in days"> {{ day }}</option>
                  </select>
                  <label class="form-wrapper__label" for="signup-username">아이디</label>
                  <input id="signup-username" class="form-wrapper__input" type="text" placeholder="ID" name="username" v-model.trim="username"
                    required>
                    <div class="password_eye">
                  <label class="form-wrapper__label" for="signup-password1">비밀번호</label>
                  <div class="input-container">
                  <input v-if="is_looking === false" v-model.trim="password1" id="signup-password1" class="form-wrapper__input" type="password" placeholder="Password"
                    name="password1" pattern=".{3,}" title="비밀번호는 8자 이상" required>
                    <input v-if="is_looking === true" v-model.trim="password1" id="signup-password1" class="form-wrapper__input" type="text" placeholder="Password"
                    name="password1" pattern=".{3,}" title="비밀번호는 8자 이상" required>
                    <label class="bi_password" @click="change_looking">
                              <i v-if="!is_looking" class="bi-eyeglasses"></i>
                              <i v-else class="bi-sunglasses"></i>
                          </label>
                  </div>
                  </div>
                  <div class="password_eye">
                  <label class="form-wrapper__label" for="signup-password2">비밀번호 확인</label>
                  <div class="input-container">
                  <input v-if="is_looking === false" v-model.trim="password2" id="signup-password2" class="form-wrapper__input" type="password" placeholder="Password"
                    name="password2" pattern=".{3,}" title="비밀번호는 8자 이상" required>
                    <input v-if="is_looking === true" v-model.trim="password2" id="signup-password2" class="form-wrapper__input" type="text" placeholder="Password"
                    name="password2" pattern=".{3,}" title="비밀번호는 8자 이상" required>
                  </div>
                  </div>
                  <label class="form-wrapper__label" for="signup-gender" >성별</label>
                  <div class="form-wrapper__input">
                    <input type="radio" id="man" value="남자" v-model="gender" />
                    <label for="man" style="color:#8dabfb; font-size: 12px; font-weight: 600;">남자</label>
                    <input type="radio" id="woman" value="여자" v-model="gender" />
                    <label for="woman" style="color:#8dabfb; font-size: 12px; font-weight: 600;">여자</label>
                  </div>
                  <label class="form-wrapper__label" for="signup-music">선호하는 음악 장르</label>
                  <label v-for="genre in genres" :key="genre.name" style="color:#8dabfb; font-size: 12px; font-weight: 600;" >
                  <input type="checkbox" :value="genre.name" v-model="music" @change="handleChange" >
                    {{ genre.name }}
                  </label>
                  <button class="buttons__signup buttons__signup--sign-up-form" ref="buttons__signup buttons__signup--sign-up-form" type="submit" style="margin-top: 190%; text-align: center;">Sign up</button>
                </form>
              </div>
            </div>
  
          </section>
        </div>
      </div>
    </div>
  </template>
  
  <script setup>
  
  import { ref, computed, onMounted } from 'vue'
  import { useRouter, useRoute } from 'vue-router'
  import { useAccountStore } from '../stores/account'
  import { useMovieStore } from '../stores/movie'
  import axios from 'axios'
  
  const accountStore = useAccountStore()
  const router = useRouter()
  
  const name = ref(null)
  const year = ref(null)
  const month = ref(null)
  const day = ref(null)
  const gender = ref('')
  const username = ref(null)
  const password1 = ref(null)
  const password2 = ref(null)
  const music = ref([])
  const selected = ref(1)
  const id = ref('')
  const password = ref('')
  
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
    const arrayAsString = JSON.stringify(music.value)
      const payload = {
          name: name.value,
          year: year.value,
          month: month.value,
          day: day.value,
          gender: gender.value,
          username: username.value,
          password1: password1.value,
          password2: password2.value,
          music: arrayAsString
      }
      accountStore.signUp(payload)
      router.push({name: 'main'})
  }
  
  const logIn = function () {
      const payload = {
        username: id.value,
        password: password.value
      }
      accountStore.logIn(payload)
    }
  
  const change_looking = function () {
      is_looking.value = !is_looking.value
  }
  
  const genres = ref([
    {id: 1, name: '레게'}, 
    {id: 2, name: '힙합'}, 
    {id: 3, name: '발라드'}, 
    {id: 4, name: '락'},
    {id: 5, name: '케이팝'},
    {id: 6, name: '팝'},
    {id: 7, name: 'R&B'}, 
    {id: 8, name: '클럽음악'},
    {id: 9, name: '클래식'},
    {id: 10, name: '요들'}, 
    {id: 11, name: '민요'},
    {id: 12, name: '트로트'}, 
    {id: 13, name: '재즈'}
  ])
  
  
  const handleChange = function() {
        // 최대 2개까지만 선택되도록 제한
        if (music.value.length > 2) {
          music.value.pop()
          alert('최대 2개만 선택할 수 있어요!')
        }
  }
  
  
  
  /* ===========================
      Elements Selectors
  ============================ */
    const elm = ref({
          arrow: null,
          overlay: null,
          title: null,
          signUpButton: null,
          loginButton: null,
          loginForm: null,
          registerForm: null,
        })
    onMounted(() => {
      elm.value.arrow = document.querySelector(".form-container__arrow");
        elm.value.overlay = document.querySelector(".overlay");
        elm.value.title = document.querySelector(".title");
        elm.value.signUpButton = document.querySelector(".buttons__signup");
        elm.value.loginButton = document.querySelector(".buttons__signup--login");
        elm.value.loginForm = document.querySelector(".login-form");
        elm.value.registerForm = document.querySelector(".login-form--register");
      });
  /* ===========================
      Properties Object
  ============================ */
  
  const props = ref({
        left: '20px',
        bottom: '-500px',
        transition1: 'bottom 1s',
        transition2: 'bottom 2s',
        opacity0: '0',
        opacity1: '1',
        trnsDelay: '1s',
        zIndex: '6',
        left0: '0',
        trnsDelay0: '0s',
        zIndex0: '0',
        leftM120: '-120px',
      })
  /* ===========================
      Elements Array
  ============================ */
  
    const elms = [
      elm.value.arrow,
      elm.value.overlay,
      elm.value.title,
      elm.value.signUpButton,
      elm.value.loginButton,
      elm.value.loginForm,
      elm.value.registerForm,
    ]
  
    
    const handleTransition = (elements, props) => {
    elements.forEach((element, i) => {
      Object.assign(element[i], props[i]);
    });
  }
  /* ===========================
      Events
  ============================ */
  
    const handleSignUp = function () {
      const styles = [
        { left: props.value.left, opacity: props.value.opacity0 },
        { opacity: props.value.opacity0 },
        { opacity: props.value.opacity0 },
        { transition: props.value.transition1, bottom: props.value.bottom },
        { transition: props.value.transition2, bottom: props.value.bottom },
        { opacity: props.value.opacity0 },
        { transition: `${props.value.opacity1} ${props.value.trnsDelay} ${props.value.zIndex}` },
      ]
        // handleTransition(elms, styles)
        selected.value = 3
      }
  
  
      const handleLogin = function () {
      console.log(2)
  
      const styles = [
        { left: props.value.left, opacity: props.value.opacity0 },
        { opacity: props.value.opacity0 },
        { opacity: props.value.opacity0 },
        { transition: props.value.transition1, bottom: props.value.bottom },
        { transition: props.value.transition2, bottom: props.value.bottom },
        { opacity: props.value.opacity0 },
        { transition: `${props.value.opacity1} ${props.value.trnsDelay} ${props.value.zIndex}` },
      ]
        console.log(styles)
        // handleTransition(elms, styles)
        selected.value = 2
      }
  
      const goMain = function () {
        selected.value = 1
      }
    // document.getElementById("arrowClick").onclick = function (){
  
    //   const properties = [props.leftM120, props.opacity1, props.opacity1, props.opacity1, props.opacity1, `${props.opacity0} ${props.trnsDelay0} ${props.zIndex0}`, `${props.opacity0} ${props.trnsDelay0} ${props.zIndex0}`]
    
    //   transition(elms, properties)
    // }
  
  </script>
  
  <style scoped>
  /* ===========================
      General Styles
  ============================ */
  
  *, :after, :before{
    box-sizing: border-box;
  }
  
  .main{
    position: relative; 
  }  
  
  .body{
    padding: 0;
    margin: 0;
    font-family: 'Montserrat', sans-serif;
    min-height: 100vh;
    display: flex;
    align-items: center;
    justify-content: center;
    perspective: 1000px;
    background: #f3f3f3; 
  }
  
  /* ===========================
      Choose Form
  ============================ */
  
  .form-container{
    position: absolute; 
    margin: auto;  
    top: 0;
    right: 0;
    bottom: 0;
    left: 0;  
    width: 380px;
    height: 585px;
    overflow: hidden; 
    box-shadow: 0 20px 20px rgba(0, 0, 0, .2), 0px 0px 50px rgba(0, 0, 0, .2);
    border-radius: 30px;
    background: #f3f3f3; 
  } 
  
  .form-container__arrow{
    position: absolute;
    margin: auto;
    top: 20px;
    right: initial;
    bottom: initial;
    left: -120px;
    width: 10px;
    height: 10px;
    color: #8dabfb;
    z-index: 10; 
    opacity: 1;
    -webkit-transition: left 2s;
    -moz-transition: left 2s;
    -o-transition: left 2s;
    transition: left 2s;
    cursor: pointer;
  }
  
  .overlay{
    position: absolute;
    margin: initial;
    top: initial;
    right: initial;
    bottom: initial;
    left: initial;
    width: inherit;
    height: inherit;
    -webkit-animation: 1.5s fadeInTitle ease;
    -moz-animation: 1.5s fadeInTitle ease;
    -o-animation: 1.5s fadeInTitle ease;
    animation: 1.5s fadeInTitle ease;
    -webkit-transition: opacity 2s;
    -moz-transition: opacity 2s;
    -o-transition: opacity 2s;
    transition: opacity 2s;
    background: #3ba4fa url(https://i.ibb.co/dkW0tm9/img-1.png) center no-repeat;
    background-size: contain; 
  }
  
  @keyframes fadeInTitle{
    0%{  
      opacity: 0;
    }
    25%{
      opacity: 0;
    }
    100%{
      opacity: 1;
    }
  }
  
  .choose-form{
    position: absolute;
    margin: initial;
    top: initial;
    right: initial;
    bottom: initial;
    left: initial;
    width: inherit;
    height: inherit;
    z-index: 5;
  }
  
  .title{
    position: absolute;
    margin: auto;
    top: -62px;
    right: 0;
    bottom: 0;
    left: 0;
    width: inherit;
    height: 100px;
    text-align: center;
    color: #fff; 
    text-shadow: 0 0.3rem 0.5rem #555;
    -webkit-animation: 1.5s fadeInTitle ease;
    -moz-animation: 1.5s fadeInTitle ease;
    -o-animation: 1.5s fadeInTitle ease;
    animation: 1.5s fadeInTitle ease;
    -webkit-transition: opacity 2s;
    -moz-transition: opacity 2s;
    -o-transition: opacity 2s;
    transition: opacity 2s;
  }
  
  .title__h1{
    font-weight: 700;
    letter-spacing: .05rem; 
    font-size: 2rem;
  }
    
  .buttons{
    text-align: center;
    position: absolute;
    margin: auto;
    top: 296px;
    right: 0;
    bottom: 0;
    left: 0;
    width: inherit;
    height: 110px;
    -webkit-animation: 1.5s fadeInTitle ease;
    -moz-animation: 1.5s fadeInTitle ease;
    -o-animation: 1.5s fadeInTitle ease;
    animation: 1.5s fadeInTitle ease;
    -webkit-transition: opacity 2s;
    -moz-transition: opacity 2s;
    -o-transition: opacity 2s;
    transition: opacity 2s;
  }
  
  .buttons__signup{
    position: absolute;
    margin: auto; 
    top: -40px;
    right: 0;
    bottom: 0;
    left: 0;
    padding: 7px 0;
    border: none; 
    border-radius: 10px;
    width: 200px;
    height: 30px;
    display: block;
    outline: none;
    text-align: inherit;
    text-transform: uppercase;
    text-decoration: none;
    letter-spacing: 0.1em;
    font-size: 12px;
    font-weight: 500;
    color: #fff;
    background: #4f73d9;
    box-shadow: 0 15px 30px rgba(79, 115, 217, .36); 
    -webkit-transition:  bottom 2s;
    -moz-transition:  bottom 2s;
    -o-transition:  bottom 2s;
    transition: bottom 2s;
    cursor: pointer;
  } 
  
  .buttons__signup:hover{
    -webkit-transition: .3s linear;
    -moz-transition: .3s linear;
    -o-transition: .3s linear;
    transition: .3s linear;
    box-shadow: 0 0 0 rgba(233, 30, 99, 0);
  } 
  
  .buttons__signup--login{
    top: 40px; 
    -webkit-transition:  bottom 1s;
    -moz-transition:  bottom 1s;
    -o-transition:  bottom 1s;
    transition: bottom 1s;
  }
  
  /* ===========================
      Login Form
  ============================ */
  
  .login-form{
    position: absolute;
    margin: auto;
    top: 0;
    right: 0;
    bottom: 0;
    left: 0;
    width: inherit;
    height: 400px;
    text-align: center;
    opacity: 0;
    -webkit-transition: opacity 2s;
    -moz-transition: opacity 2s;
    -o-transition: opacity 2s;
    transition: opacity 2s; 
  }
  
  .form-wrapper{
    margin: 0 auto;
    width: 250px;
    height: 250px;
    display: block;
    position: relative;
  }
  
  .form-wrapper__label{
    display: block;
    text-align: left;
    text-transform: uppercase;
    text-decoration: initial;
    letter-spacing: .1em; 
    font-size: 12px;
    font-weight: 600;
    color: #8dabfb; 
  }
  
  .form-wrapper__input{
    margin: 5px 0 10px 0;
    width: 250px;
    height: 30px;
    outline: none;
    border: none;
    background: none;
    font-size: 12px;
    border-bottom: 1px solid #8dabfb;
    opacity: .8;
  }
  
  .form-wrapper__input::placeholder{
    color: #8dabfb;
    opacity: .8;
  } 
  
  .login-form__forgot-password{
    display: block;
    text-align: right;
    text-transform: uppercase;
    text-decoration: none;
    letter-spacing: .05em;
    font-size: 12px;
    font-weight: 500;
    color: #8dabfb;
  }
  
  .login-form__forgot-password:hover{
    opacity: 0.5;
    -webkit-transition: .3s linear;
    -moz-transition: .3s linear;
    -o-transition: .3s linear;
    transition: .3s linear;
  }
  
  .buttons__signup--login-form{
    -webkit-transition: none;
    -moz-transition: none;
    -o-transition: none;
    transition: none;
    top: -66px; 
  }
  
  .social-media{
    position: absolute;
    margin: auto;
    top: initial;
    right: 0;
    bottom: 0;
    left: 0;
    width: inherit;
    height: 150px;
  }
  
  .title__h2{
    margin: 25.63px;
    margin-bottom: 1rem;
    font-size: 11px; 
    font-weight: 700;
    text-transform: uppercase;
    color: #8dabfb;
  }
   
  .title__h2::before{
    content: "";
    position: absolute;
    margin: auto;
    top: 30px;
    right: initial;
    bottom: 0;
    left: 0;
    width: 65px;
    height: initial;
    border-top: 1px solid #8dabfb;
    opacity: .8;
  }
   
  .title__h2::after{
    content: "";
    position: absolute;
    margin: auto;
    top: 30px;
    right: 0;
    bottom: 0;
    left: initial;
    width: 65px;
    height: initial;
    border-top: 1px solid #8dabfb;
    opacity: .8;
  }
  
  .buttons__signup--social{
    position: relative;   
    margin: 10px auto; 
    top: 5px; 
    text-align: center;
    -webkit-transition: none;
    -moz-transition: none;
    -o-transition: none;
    transition: none;
    background: #3ba4fa;
    box-shadow: 0 15px 30px rgba(59, 164, 250, .36); 
  }
  
  /* ===========================
      Register Form
  ============================ */
  
  .buttons__signup--sign-up-form{
    top: 5px;  
    -webkit-transition: none;
    -moz-transition: none;
    -o-transition: none;
    transition: none;
  }
  
  /* ===========================
      Responsive
  ============================ */
  
  @media (max-height: 599px){ 
    .form-container{ 
      margin: 1rem auto;
      position: relative; 
      width: 300px; 
      height: 460px;
    } 
  
    .form-wrapper{
      margin-top: 24px;
    }
  
    .buttons__signup--login-form{
      top: -17px; 
    }
  
    .buttons__signup--sign-up-form{
      top: 54px; 
    }
  }
  
  @media (max-width: 400px){
    .form-container{
      width: 320px;
    }
  } 
  
  @media (max-width: 320px){
    .form-container{
      width: 300px;
      height: 460px;
    }
  
    .form-wrapper{
      margin-top: 24px;
    }
  
    .buttons__signup--login-form{
      top: -17px; 
    }
  
    .buttons__signup--sign-up-form{
      top: 54px; 
    }
  } 
  
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
  
  .bi_password {
    position: absolute;
    top: 50%;
    right: 10px; 
    transform: translateY(-50%);
    cursor: pointer;
  }
  
    .bi-arrow-left-circle {
      position: absolute;
      top: 10px; /* 원하는 위치로 조절할 수 있습니다. */
      left: 10px; /* 원하는 위치로 조절할 수 있습니다. */
      font-size: 24px; /* 원하는 크기로 조절할 수 있습니다. */
      cursor: pointer;
      color: #8dabfb;
    }
  </style>