import Vue from 'vue'
import VueRouter from 'vue-router'
import VueResource from 'vue-resource'
import List from './List.vue'
import User from './User.vue'
import ListRecept from './ListRecept.vue'
import Login from './Login.vue'
import Registration from './Registration.vue'
import Add_Recept from './Add_Recept.vue'



Vue.use(VueRouter)
Vue.use(VueResource)

const router = new VueRouter({
  routes: [
    { path: '/', name:'all', component: List },
    { path: '/recept/:id', name:'recept', component: ListRecept },
    { path: '/user/:id', name:'current_user', component: User },
    { path: '/login', component: Login },
    { path: '/registration', component: Registration },
    { path: '/add', component: Add_Recept },

    
  ]
})

new Vue({
  el: '#gluten',
  router: router,
  name: "index",
  data: {
    token: false,
  },
  computed: {
    tokens() {
      if (localStorage.getItem("auth_token")) 
        return true
      else
        return false
    }
  },
  methods: {
    logout() {
      localStorage.removeItem("auth_token");
      window.location = '/';
    },
    
  },
  created: function () {
    
  },

})
