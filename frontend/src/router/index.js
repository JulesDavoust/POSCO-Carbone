import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import FAQView from '../views/FAQView.vue'
import EspacePersonnelView from '../views/EspacePersonnelView.vue'
import EspaceEfreiView from '../views/EspaceEfreiView.vue'
import ConseilsView from '../views/ConseilsView.vue'

const routes = [
  {
    path: '/',
    name: 'Accueil',
    component: HomeView
  },
  {
    path: '/FAQ',
    name: 'FAQ',
    component: FAQView
  },
  {
    path: '/Espace-Personnel',
    name: 'EspacePersonnel',
    component: EspacePersonnelView
  },
  {
    path: '/Espace-Efrei',
    name: 'EspaceEfrei',
    component: EspaceEfreiView
  },
  {
    path: '/Conseils',
    name: 'Conseils',
    component: ConseilsView
  },
  // {
  //   path: '/about',
  //   name: 'about',
  //   // route level code-splitting
  //   // this generates a separate chunk (about.[hash].js) for this route
  //   // which is lazy-loaded when the route is visited.
  //   component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  // }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
