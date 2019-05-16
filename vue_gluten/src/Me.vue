<template>
	<div>
		<p class="BigText"></p>
		<div id="me">
			<div><img id="me_avatar" :src="info_user_detailed.avatar"></div>
			<div><span>{{info_user_detailed.username}}</span></div>
			<div><span>{{info_user_detailed.first_name}}</span> <span>{{info_user_detailed.last_name}}</span></div>
			<div></div>
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
				info_user_detailed: [],
				loading: false,
			};
		},
		mounted() {
		},
  methods: {
	before: function () {
		let NewReceptData = new FormData();
		this.$http.post(this.user_url, NewReceptData, {
			headers: {
				'Authorization': 'Token ' + localStorage.getItem("auth_token"),
			}
		})
	  .then(function (response) {
		this.info_user = response.data.data;
		this.info_user_detailed = this.info_user.attributes;

		})
		.catch(function (error) {
			console.log(error);
			this.loading = false;
		});
	  },
  },
	created: function () {
		this.before()
		// // console.log(this.$parent.before());
		// this.info_user = this.$parent.info_about_user;
		// this.info_user_detailed = this.info_user.attributes;
		// console.log("+++++++++++++");
		// console.log(this.info_user);
		// console.log("+++++++++++++");
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
	img#me_avatar{
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