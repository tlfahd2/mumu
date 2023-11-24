<template>
  <div>
    <header>
      <div>
        <nav class="navbar fixed-top" v-if="accountStore.isLogin">
          <RouterLink class="nav-item" :to="{ name: 'main' }">홈</RouterLink>
          <RouterLink class="nav-item" :to="{ name: 'communitymain' }">커뮤니티</RouterLink>
          <form class="d-flex" role="search" @submit.prevent="getSearchMovie">
            <input
              class="form-control me-2"
              type="search"
              placeholder="검색어를 입력하세요"
              aria-label="Search"
              v-model="searchInput"
            />
            <button class="btn btn-outline-success" type="submit">
              <i class="bi bi-search"></i>
            </button>
          </form>
          <li class="nav-item dropdown">
            <a
              class="nav-link dropdown-toggle"
              href="#"
              role="button"
              data-bs-toggle="dropdown"
              aria-expanded="false"
            >
              <i class="bi bi-person-circle"></i>
            </a>
            <ul class="dropdown-menu">
              <div>
                <button type="button" class="dropdown-item" @click="showModdal = true">
                  내 프로필
                </button>
                <ModifyPwd v-if="showModdal" @close="showModdal = false"> </ModifyPwd>
              </div>
              <li><hr class="dropdown-divider" /></li>
              <RouterLink
                class="dropdown-item"
                @click="accountStore.logOut"
                :to="{ name: 'signup' }"
                >로그아웃</RouterLink
              >
            </ul>
          </li>
        </nav>
      </div>
    </header>
    <ProfileView />
    <RouterView />
  </div>
</template>

<script setup>
import { RouterLink, RouterView } from "vue-router";
import { ref, computed, onMounted } from "vue";
import { useRouter, useRoute } from "vue-router";
import { useAccountStore } from "./stores/account.js";
import { useMovieStore } from "./stores/movie.js";
import axios from "axios";
import ProfileView from "./views/ProfileView.vue";
// import ModifyPwd from "./views/ModifyPwd.vue";

const showModify = ref(false);
const movieStore = useMovieStore();
const accountStore = useAccountStore();
const router = useRouter();
const showModdal = ref(false);
onMounted(() => {
  movieStore.getMovieList(1);
});

const searchInput = ref("");

const getSearchMovie = () => {
  movieStore.getSerchResult(searchInput);
  router.push({ name: "search", params: { keyword: searchInput.value } });
  searchInput.value = "";
};
</script>

<style scoped>
@font-face {
  font-family: "euljiro";
  src: url("fonts/BMEuljiro10yearslater.ttf");
}
.main {
  padding-top: 5.8rem;
}
.navbar {
  height: 70px;
  padding-left: 8rem;
  padding-right: 8rem;
  font-family: "euljiro";
  font-size: 30px;
  /* background-color: #00264B; */
  background-color: #bdcebe;
}
.nav-item {
  display: inline-block;
  text-decoration: none;
  color: #10af85;
  text-transform: uppercase;
}
.nav-item:after {
  display: block;
  content: "";
  border-bottom: solid 5px #0b685a;
  transform: scaleX(0);
  transition: transform 250ms ease-in-out;
}
.nav-item:hover:after {
  transform: scaleX(1);
}
</style>
