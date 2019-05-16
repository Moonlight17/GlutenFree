<template>
  <div id="registration">
    <h1>{{ msg }}</h1>
    <div v-if="Req_Errors.length" class="alert alert-danger" role="alert">
		<p v-for="err in Error_position">
			<span>{{err.place}}    ---   {{err.info}}</span>
		</p>
	</div>
    <div>
      <input id="username" v-model="Username" placeholder="Username">
      <input id="password" v-model="Password" placeholder="Password">
      <input v-model="Email" type="email" placeholder="Email">
      <button @click="login()">Зарегистрироваться</button>
      <!-- <pre>{{$data}}</pre> -->
    </div>
    <!-- <h1>{{list}}</h1> -->
  </div>
</template>

<script>
export default {
  name: "registration",
  data() {
    return {
      msg: "Регистрация",
      Username: "",
      Password: "",
      Email: "",
	  Req_Errors: [],
	  Error_position:[],
    };
  },
  watch: {
    // эта функция запускается при любом изменении вопроса
    Username: function() {
      if (this.Username)
        this.Username =
          this.Username[0].toUpperCase() + this.Username.substr(1).toLowerCase();
    }
  },
  methods: {
    login: function() {
      console.log("OLOLO");
      var data = [];
      var formData = new FormData();
      formData.append("username", this.Username);
      formData.append("password", this.Password);
      formData.append("email", this.Email);

      this.$http.post("http://127.0.0.1:8000/auth/users/", formData).then(
        function(response) {
          console.log(response);
          this.$http
            .post("http://127.0.0.1:8000/auth/token/login", formData)
            .then(
              function(response) {
                // console.log(response.data.data.attributes.auth_token);
                localStorage.setItem(
                  "auth_token",
                  response.data.data.attributes.auth_token
                );
                window.location = "/";
              },
              function(error) {
                console.log("error");
                console.log(error);
                this.loading = false;
              }
            );
        },
        function(error) {
			this.Req_Errors = [];
			this.Req_Errors = error.body.errors;
			for (var error in this.Req_Errors){
				var place = this.Req_Errors[error].source.pointer;
				place = place.split('/')
				// console.log(place[place.length - 1]);

				this.Error_position.push({
					place: place[place.length - 1],
					info: this.Req_Errors[error].detail
					});
				// console.log("OLOLOLOLOLOLOLLOOOOOOO");
			}
        //   console.log("Error_Reg");
        //   console.log(this.Req_Errors);
        //   console.log(error);
        }
      );
    }
  },
  created: function() {}
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