<template>
    <div>
        <h1>비밀번호 변경</h1>
        <form @submit.prevent="change_password">
            <div class="password_eye">
                <!-- <label for="old_password">기존 비밀번호 : </label> -->
                <div class="input-container">
                    <input v-if="is_looking === false" type="password" id="old_password" v-model.trim="old_password" placeholder="password"/>
                    <input v-if="is_looking === true" type="text" id="old_password" v-model.trim="old_password" placeholder="password"/>
                    <label class="bi" @click="change_looking">
                        <i v-if="!is_looking" class="bi-eyeglasses"></i>
                        <i v-else class="bi-sunglasses"></i>
                    </label>
                </div>
            </div>
            <br>
            <div class="password_eye">
                <!-- <label for="new_password1">새로운 비밀번호 : </label> -->
                <div class="input-container">
                    <input v-if="is_looking2 === false" type="password" id="new_password1" v-model.trim="new_password1" placeholder="new password"/>
                    <input v-if="is_looking2 === true" type="text" id="new_password1" v-model.trim="new_password1" placeholder="new password"/>
                    <label class="bi" @click="change_looking2">
                        <i v-if="!is_looking2" class="bi-eyeglasses"></i>
                        <i v-else class="bi-sunglasses"></i>
                    </label>
                </div>
            </div>
            <br>
            <div class="password_eye">
                <!-- <label for="new_password2">새로운 비밀번호 확인 : </label> -->
                <div class="input-container">
                    <input v-if="is_looking2 === false" type="password" id="new_password2" v-model.trim="new_password2" placeholder="new password confirm"/>
                    <input v-if="is_looking2 === true" type="text" id="new_password2" v-model.trim="new_password2" placeholder="new password confirm"/>
                </div>
            </div>
            <br>
            <input type="submit" value="비밀번호 변경">
        </form>
    </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import { useAccountStore } from '../stores/account'
import axios from 'axios'


const accountStore = useAccountStore()

const old_password = ref(null)
const new_password1 = ref(null)
const new_password2 = ref(null)
let is_looking = ref(false)
let is_looking2 = ref(false)

const change_password = function () {
    const payload = {
        old_password: old_password.value,
        new_password1: new_password1.value,
        new_password2: new_password2.value
    }
    accountStore.change_password(payload)
}

const change_looking = function () {
    is_looking.value = !is_looking.value
}

const change_looking2 = function () {
    is_looking2.value = !is_looking2.value
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