<template>
	<div id="login">
		<h1>{{ msg }}</h1>
		<div>
		<div v-if="errors.length" class="alert alert-danger" role="alert">
			<p v-for="err in errors">
				<span>{{err.place}}    ---   {{err.info}}</span>
			</p>
		</div>
			<form v-on:submit.prevent="valid">
				<input v-model="username" placeholder="Login"/>
				<input v-model="password" placeholder="Password"/>
				<button>Вход</button>
			</form>
		</div>
		<!-- <h1>{{list}}</h1> -->
	</div>
</template>

<script>
	export default {
		name: "login",
		data() {
			return {
				msg: "Вход",
				username: "",
				password: "",
				errors: [],
				link: this.$root.link,
			};
		},
		methods: {
			valid: function () {
				if(this.username && this.password) this.login();
				this.errors = [];
				if(!this.username.length) this.errors.push(
					{
						place: "Username",
						info: "Поле с именем пользователя не может быть пустым"
					});
				if(!this.password.length) this.errors.push(
					{
						place: "Password",
						info: "Поле пароля не может быть пустым"
					});

			},
			login: function () { 
				var data = [];
				var formData = new FormData();
				formData.append('username', this.username);
				formData.append('password', this.password);
				
				this.$http.post(this.link + "auth/token/login", formData).then(
				function(response) {
					console.log(response);
					localStorage.setItem("auth_token", response.body.data.attributes.auth_token)
					window.location = '/';


				},
				function(error) {
					if (error.status == 400) alert(error.body.errors[0].detail)
					console.log(error);
				}
			);
			}
		},
		created: function () {
			// this.link = his.$root.link;
		}
	};
</script>

<style>
	#app {
		font-family: "Avenir", Helvetica, Arial, sans-serif;
		-webkit-font-smoothing: antialiased;
		-moz-osx-font-smoothing: grayscale;
		text-align: center;
		color: #2c3e50;
		margin-top: 60px;
	}

	h1,
	h2 {
		font-weight: normal;
	}

	ul {
		list-style-type: none;
		padding: 0;
	}

	li {
		display: inline-block;
		margin: 0 10px;
	}

	a {
		color: #42b983;
	}
</style>