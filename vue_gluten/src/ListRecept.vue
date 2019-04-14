<template>
	<div id="gluten">
		<img src="./assets/logo.png">
		<div>
			<h5 class="card-title">{{recept.title}}</h5>
			<p class="card-text">{{author.username}} KJ{<img :src="host_url+author.avatar"></p>
			<ul class="card-text">
				<li v-for="rec in recept.recepts_text">{{rec.title}}</li>
			</ul>
			<a v-for="tag in recept.tag_name" href="#" class="badge badge-light">{{tag.name}}</a>
		</div>
	</div>
</template>

<script>
	export default {
		name: "Recept",
		data() {
			return {
				host_url: "http://127.0.0.1:8000",
				list_url: "http://127.0.0.1:8000/recept/",
				recept: [],
				author:'',
				receptid:''
			};
		},
		methods: {
			all: function () {
				this.$http.get(this.list_url+this.receptid+"/").then(
					function (response) {
						this.recept = response.data.data[0];
						this.author = this.recept['creater'];
					},
					function (error) {
						// console.log(error);
					}
				);
			}
		},
		created: function () {
			this.receptid = this.$route.params.id;
			console.log(this.receptid);
			this.all();
		}
	};
</script>

<style>
	#recept {
		font-family: "Avenir", Helvetica, Arial, sans-serif;
		width: 70vw;
		margin: 0 auto;
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