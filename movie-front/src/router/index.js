import { createRouter, createWebHistory } from 'vue-router'
import MainView from '../views/MainView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/signup',
      name: 'SignUpView',
      component: SignUpView
    },
    {
      path: '/login',
      name: 'LogInView',
      component: LogInView
    },
    {
      path: '/',
      name: 'main',
      component: MainView
    },
    {
      path: '/moviedetail/:movie_id',
      name: 'moviedetail',
      component: () => import('../views/MovieDetailView.vue')
    },
  ]
})

export default router
