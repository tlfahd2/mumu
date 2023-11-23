<template>
    <div>
        <button data-bs-toggle="modal" data-bs-target="#trailer" class="btn btn-secondary" @click=play>예고편 보기</button>
        <div class="modal fade" id="trailer" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
            <div class="modal-dialog modal-xl">
                <div class="modal-content">
                    <div class="modal-header">
                        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close" @click="stop"></button>
                    </div>
                    <div class="modal-body">
                        <iframe width="100%" height="600" :src="videoUrl"
                            title="YouTube video player" frameborder="0"
                            allow="accelerometer;clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
                            allowfullscreen></iframe>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script setup>
import { ref } from 'vue'
const props = defineProps({
    trailerKey:String
})
const videoUrl = ref('')

// 영상을 틀고 모달 창을 닫았을 경우 영상 재생 또한 끊어주기 위한 함수 2개
// 닫기 클릭시 영상의 주소를 비워버린다.
const stop = ()=>{
    videoUrl.value = ''
}
const play = ()=>{
    videoUrl.value =`http://www.youtube.com/embed/${props.trailerKey}`
}
</script>

<style scoped>
.logo {
    width: 100px;
    height: 100px;
}
</style>