import { createRouter, createWebHistory } from 'vue-router'
import SignUpView from '../views/SignUpView.vue'
import LogInView from '../views/LogInView.vue'
import MainView from '../views/MainView.vue'
import ChangePasswordView from '../views/ChangePasswordView.vue'


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
      path: '/change_password',
      name: 'change_password',
      component: ChangePasswordView
    },
    {
      path: '/',
      name: 'main',
      component: MainView
    },
    {
      path: '/search/:keyword',
      name: 'search',
      component: () => import('../views/SearchView.vue')
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
    },
    {
      path:'/:movie_id/createReview',
      name:'createReview',
      component : () => import('../views/ReviewCreateView.vue')
    },
    {
      path:'/updateReview/:review_id',
      name:'updateReview',
      component : () => import('../views/ReviewUpdateView.vue')
    },
    {
      path:'/reviewdetail/:review_id',
      name:'reviewDetail',
      component : () => import('../views/ReviewDetailView.vue')
    },
    {
      path:'/:movie_id/reviews',
      name:'movieReviews',
      component : () => import('../views/MovieReviewsView.vue')
    },
    {
      path: `/:username`,
      name: 'profile',
      component: () => import('../views/ProfileView.vue')
    },
    {
      path: `/:username/follow`,
      name: 'follow',
      component: () => import('../components/FollowListModal.vue')
    },
    {
      path: '/test',
      name: 'test',
      component: () => import('../views/signup.vue')
    }
  ]
})

export default router
