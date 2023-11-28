import { createRouter, createWebHistory } from 'vue-router';
import IndexComponent from '../components/IndexComponent.vue'; // Adjust path as needed

const routes = [
    {
        path: '/:q?', // Optional param '?'
        name: 'Index',
        component: IndexComponent,
    },
    // ... other routes
];

const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes,
});

export default router;
