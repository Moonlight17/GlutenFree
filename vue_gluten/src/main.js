import Vue from 'vue'
import VueRouter from 'vue-router'
import VueResource from 'vue-resource'
import List from './List.vue'
import CurrentUser from './User.vue'
import CurrentRecept from './ListRecept.vue'
import Login from './Login.vue'
import Registration from './Registration.vue'
import Add_Recept from './Add_Recept.vue'

import svgIcon from './svg.vue'




Vue.use(VueRouter)
Vue.use(VueResource)

const router = new VueRouter({
  routes: [
    { path: '/', name:'all', component: List },
    { path: '/recept/:id', name:'CurrentRecept', component: CurrentRecept },
    { path: '/user/:id', name:'CurrentUser', component: CurrentUser },
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
	  user_url: 'http://127.0.0.1:8000/me/',
    user: '',
  },
  components: {
    'svgimg': svgIcon
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
    logout: function() {
      localStorage.removeItem("auth_token");
      localStorage.removeItem("auth_user");
      window.location = '/';
	  },
	  before: function () {
		let NewReceptData = new FormData();
		this.$http.post(this.user_url, NewReceptData, {
			headers: {
				'Authorization': 'Token ' + localStorage.getItem("auth_token"),
			}
		})
      .then(function (response) {
        
        localStorage.setItem("auth_user", response.data.data.attributes.username)
        this.user = localStorage.getItem("auth_user")
		})
		.catch(function (error) {
			console.log(error);
			this.loading = false;
		});
	  },
  },
	created: function () {
		if (localStorage.getItem("auth_token")) this.before();
}

})
