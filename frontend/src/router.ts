import { createRouter, createWebHistory } from 'vue-router'
import PlacesList from './components/PlacesList.vue'
import TicketPage from './components/TicketPage.vue'

const routes = [
    { path: '/', component: PlacesList },
    { path: '/ticket/:id', name: 'ticket', component: TicketPage, props: true }
]

const router = createRouter({
    history: createWebHistory(),
    routes,
})

export default router
