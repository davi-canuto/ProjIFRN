import { createRouter, createWebHashHistory } from "vue-router";
import HomaPage from '../pages/HomePage.vue'

 
const router = createRouter({
    history: createWebHashHistory(),
    routes: [
        {
            path: '/',
            name: 'home',
            component: HomaPage
        },
       ] 
});

export default router;