<template>
  <div id="registration">
    <img src="./assets/logo.png">
    <h1>{{ msg }}</h1>
    <div>
      <input v-model="Login" placeholder="Login"/>
      <input v-model="Password" placeholder="Password"/>
      <input autocomplete="off" type="file" id="my_file" ref="files" name="file" v-on:change="handleFilesUploads" />
      <button @click="login()">Зарегистрироваться</button>
		<pre>{{$data}}</pre>

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
        Login: "",
        Password: "",
        Avatar: [],
      };
    },
    methods: {
      login: function () { 
        console.log("OLOLO");
        var data = [];
        var formData = new FormData();
        formData.append('username', this.Login);
        formData.append('password', this.Password);
        formData.append('avatar', this.Avatar);
        
        this.$http.post("http://127.0.0.1:8000/auth/users/", formData).then(
        function(response) {
          console.log(response.data.data.attributes.auth_token);
          localStorage.setItem("auth_token", response.data.data.attributes.auth_token)
        },
        function(error) {
          console.log(error);
        }
      );
      },
	  handleFilesUploads() {
			let uploadedFiles = this.$refs.files.files;
			for (var i = 0; i < uploadedFiles.length; i++) {
				console.log(uploadedFiles[i]);
				this.Avatar = uploadedFiles[i];
			}
		},
    },
    created: function () { }
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