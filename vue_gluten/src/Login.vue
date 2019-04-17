<template>
  <div id="login">
    <h1>{{ msg }}</h1>
    <div>
      <input v-model="Login" placeholder="Login"/>
      <input v-model="Password" placeholder="Password"/>
      <button @click="login()">Вход</button>
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
        Login: "",
        Password: "",
      };
    },
    methods: {
      login: function () { 
        console.log("OLOLO");
        var data = [];
        var formData = new FormData();
        formData.append('username', this.Login);
        formData.append('password', this.Password);
        
        this.$http.post("http://127.0.0.1:8000/auth/token/login", formData).then(
        function(response) {
          console.log(response.data.data.attributes.auth_token);
          localStorage.setItem("auth_token", response.data.data.attributes.auth_token)
          window.location = '/';
        },
        function(error) {
          if (error.status == 400) alert(error.detail)
          console.log(error);
        }
      );
      }
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