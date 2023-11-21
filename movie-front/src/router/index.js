import { createRouter, createWebHistory } from 'vue-router'
import SignUpView from '../views/SignUpView.vue'
import LogInView from '../views/LogInView.vue'
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
      path:'/logout',
      name:'logout',
      component: MainView
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
    {
      path: '/community',
      name: 'communitymain',
      component: () => import('../views/CommunityView.vue')
    },
    {
      path:'/createArticle',
      name:'createArticle',
      component : () => import('../views/ArticleCreateView.vue')
    },
    {
      path:'/updateArticle/:article_id',
      name:'updateArticle',
      component : () => import('../views/ArticleUpdateView.vue')
    },
    {
      path:'/articledetail/:article_id',
      name:'articleDetail',
      component : () => import('../views/ArticleDetailView.vue')
    }
  ]
})

export default router
