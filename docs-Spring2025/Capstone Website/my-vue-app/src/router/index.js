import { createRouter, createWebHistory } from 'vue-router';
import IntroPage from '../pages/IntroPage.vue';
import Visualizer from '../pages/Visualizer.vue';
import Chatbot from '../pages/Chatbot.vue';


const routes = [
  { path: '/', component: IntroPage },
  { path: '/visualizer', component: Visualizer },
  { path: '/chatbot', component: Chatbot },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
