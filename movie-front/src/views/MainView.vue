<template>
    <main class="main container">
        <div>
            <div class="drop d-flex">
                <button class="btn" @click="sortMovie(1)">인기순</button>
                <button class="btn" @click="sortMovie(2)">최신순</button>
                <button class="btn" @click="sortMovie(3)">개인맞춤</button>
                <button class="btn" @click="sortMovie(4)">개봉예정작</button>
                <div class="btn-group">
                    <button type="button" class="dropdown-toggle cta btn" data-bs-toggle="dropdown" aria-expanded="false">
                        장르별
                    </button>
                    <ul class="dropdown-menu">
                        <div v-for="genre in movieStore.genres" 
                            :key="genre.id">
                            <li><a class="dropdown-item"
                                 @click="sortMovie(genre.id)">
                                {{ genre.name }}
                            </a></li>
                        </div>
                    </ul>
                </div>
            </div>
            <div class="movie-list">
                <MovieCard
                v-for="movie in data"
                :key="movie.id"
                :movie="movie"
                />
                <infinite-loading
                @infinite="loadMoreData"
                ref="infiniteLoading"
                spinner="bubbles"
                v-if="!AllDataLoaded"
                >
                    <div slot="no-more">No more data</div>
                </infinite-loading>

            </div>
        </div>
    </main>
</template>

<script setup>
import { ref, computed, onMounted, watch } from 'vue'
import { useRouter, useRoute } from 'vue-router'
import { useAccountStore } from '../stores/account'
import { useMovieStore } from '../stores/movie'
import axios from 'axios'
import MovieCard from '../components/MovieCard.vue'
// import InfiniteLoading from 'v3-infinite-loading'
// import "v3-infinite-loading/lib/style.css";

const movieStore = useMovieStore()
const accountStore = useAccountStore()
const router = useRouter()
const data =ref([])
const currentPage = ref(2)
const loading = ref(false)
const AllDataLoaded = ref(false)
const sort_num = ref(1)

onMounted(()=>{
    movieStore.getMovieList(1, 1)
    movieStore.getGenreList()
})

const sortMovie= (number) =>{
    sort_num.value = number
    currentPage.value = 2
    data.value = []
    // 다시 눌렀을 때는 새로운 데이터를 또 불러오야 함
    AllDataLoaded.value = false
    movieStore.getMovieList(number, 1)
}


// 무한 스크롤 함수
const loadMoreData = async ($state) => {
    if( loading.value){
        return;
    }
    loading.value = true
    try {
    // 화면 끝을 닿으면 API 요청을 보내서 또 데이터를 가져오게 끔
        const response = await axios.get(`${movieStore.API_URL}/sort/${sort_num.value}/page/${currentPage.value}`, {
            headers: {
                Authorization: `Token ${accountStore.token}`}
            })
        const newData = response.data
        console.log(newData)
        loading.value = false
        
        if (newData.length > 48) {
            data.value = [...data.value, ...newData];
            currentPage.value++;
            $state.loaded()
        }else {
            data.value = [...data.value, ...newData]
            AllDataLoaded.value = true
            $state.complete()
        }
        } catch (error) {
        console.error('Error loading more data:', error)
        showErrorNotification(error.message)
        $state.complete()
    }
}

</script>

<style scoped>
@font-face {
  font-family: "yeonsung";
  src: url("../fonts/BMYEONSUNG_ttf.ttf")
}
@keyframes shake { /* @keyframes를 이용해 shake의 각도를 좌우 15deg로 조정 */
    10%{transform: rotate(15deg);}
    20%{transform: rotate(-15deg);}
    30%{transform: rotate(15deg);}
    40%{transform: rotate(-15deg);}
}
.btn{
    font-family: "yeonsung";
    font-size: 30px;
    cursor:pointer;
    transition-property: outline-offset, outline-color, background-color; /* 트랜지션 설정 */
    transition-duration: .3s; /* 애니메이션 .3s 만큼 진행 */
}
.btn:hover{
    transition-property: all; /*모든부분 변화*/
    transition-duration: 0.2s; /*0.2s동안 변화*/
    transition-timing-function: linear; /*일정한 속도로 변화*/
    transition-delay: 0; /*즉시변화-> 0이 default값이므로 생략 가능*/
    transform: scale(1.2) /*1.2배 확대*/
}
.dropdown-item{
    font-family: "yeonsung";
    font-size: 20px;
}
.movie-list{
    display: flex;
    flex-wrap: wrap;
}

</style>