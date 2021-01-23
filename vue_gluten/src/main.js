import Vue from 'vue'
import VueRouter from 'vue-router'
import VueResource from 'vue-resource'
import List from './List.vue'
import CurrentUser from './User.vue'
import CurrentRecept from './ListRecept.vue'
import Login from './Login.vue'
import Registration from './Registration.vue'
import FinalRegstration from './FinalRegistration.vue'
import Add_Recept from './Add_Recept.vue'
import Me from './Me.vue'

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
	{ path: '/userReg', component: FinalRegstration },
	{ path: '/add', component: Add_Recept },
	{ path: '/me', component: Me },

	
	]
})

new Vue({
	el: '#gluten',
	router: router,
	name: "index",
	data: {
		token: false,
	user_url: 'http://127.0.0.1:8000/me/',
	logout_url: 'http://127.0.0.1:8000/auth/token/logout/',
		user: '',
	link: "",
	registration: false,
	info_about_user: [],
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
	},
	complited() {
		if ((localStorage.getItem("auth_token")) && (!this.registration)) {
		return true
		
		}
		else
		return false
	},
	},
	methods: {
	logout: function() {
		let Tokens = new FormData();
		this.$http.post(this.logout_url, Tokens, {
		headers: {
			'Authorization': 'Token ' + localStorage.getItem("auth_token"),
		}
		})
		.then(function (response) {
			localStorage.removeItem("auth_token");
			localStorage.removeItem("auth_user");
			window.location = '/';
			this.loading = false;
		})
		.catch(function (error) {
		console.log(error);
		this.loading = false;
		});
			
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
		
		localStorage.setItem("auth_user", response.data.data.attributes.username);
		this.user = localStorage.getItem("auth_user");
		this.registration = response.data.data.attributes.finish;
		this.info_about_user = response.data.data;
		// console.log(this.info_about_user);
		console.log("data");
		console.log(this.info_about_user);
		console.log(localStorage.getItem("auth_token"));

		})
		.catch(function (error) {
			console.log(error);
			this.loading = false;
		});
			console.log("OLOLOLOLOLOLOLOLOLO");
			console.log(this.info_about_user);
		},
	},
	created: function () {
		if (localStorage.getItem("auth_token")) this.before();
		this.link = window.location.protocol+"//"+window.location.hostname+":8000/";
}

})
