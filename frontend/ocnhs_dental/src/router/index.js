import { createRouter, createWebHashHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

import LoginView from '@/views/LoginView.vue'
import SignUpView from '@/views/SignUpView.vue'

import ClientView from '@/views/ClientView.vue'
import AdminView from '@/views/AdminView.vue'
import AdminLoginView from '@/views/AdminLoginView.vue'
import BlogView from '@/views/BlogView.vue'
import ServiceView from '@/views/ServiceView.vue'
import AdminSignUpView from '@/views/AdminSignUpView.vue'

const router = createRouter({
  history: createWebHashHistory(),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView,
    },

    {
      path: '/blog',
      name: 'blog',
      component: BlogView,
    },

    {
      path: '/service',
      name: 'service',
      component: ServiceView,
    },

    {
      path: '/signUp',
      name: 'signUp',
      component: SignUpView,
    },

    {
      path: '/adminSignUp',
      name: 'adminSignUp',
      component: AdminSignUpView,
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
