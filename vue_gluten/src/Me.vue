<template>
	<div>
		<p class="BigText"></p>
		<div id="me">
			<p>Москва!!!</p>
			<p>TESTING</p>
			<div><img id="avatar" :src="info_user.attributes.avatar"></div>
			<!-- <h1>{{list}}</h1> -->
			<pre> {{$data}} </pre>

		</div>
	</div>
</template>

<script>
	export default {
		name: "me",
		data() {
			return {
				host_url: "http://127.0.0.1:8000",
				user_url: "http://127.0.0.1:8000/me/",
				info_user: [],
				loading: false,
			};
		},
		mounted() {
		},
  methods: {
	user_me: function () {
		console.log("вызов")
		this.info_user = this.$parent.info_about_user;
		
	}
  },
	created: function () {
		// // console.log(this.$parent.before());
		this.info_user = this.$parent.info_about_user;
		console.log("+++++++++++++");
		console.log(this.info_user);
		console.log("+++++++++++++");
}
	};
</script>

<style>
	.BigText{
		font-size: 150px;
	}
	#list {
		/* height: 100vh; */
		/* overflow: hidden; */
		/* margin-bottom: 30px; */
		/* position: fixed; */


	}

	#logotip {
		position: fixed;
	}

	#user {
		font-family: "Avenir", Helvetica, Arial, sans-serif;
		width: 70vw;
		height: 80vh;
		margin: 0 auto;
		margin-top: 10vh;
		overflow: scroll;

	}
	img#avatar{
		height:255px;
		width:255px;
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