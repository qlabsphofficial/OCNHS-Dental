import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

import LoginView from '@/views/LoginView.vue'
import SignUpView from '@/views/SignUpView.vue'

import ClientView from '@/views/ClientView.vue'
import AdminView from '@/views/AdminView.vue'
import AdminLoginView from '@/views/AdminLoginView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView,
    },

    {
      path: '/signUp',
      name: 'signUp',
      component: SignUpView,
    },

    {
      path: '/login',
      name: 'login',
      component: LoginView,
    },

    {
      path: '/client',
      name: 'client',
      component: ClientView,
    },

    {
      path: '/adminLogin',
      name: 'adminLogin',
      component: AdminLoginView,
    },

    {
      path: '/admin',
      name: 'admin',
      component: AdminView,
    },
  ],
})

export default router
