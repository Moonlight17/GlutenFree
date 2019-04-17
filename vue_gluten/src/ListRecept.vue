<template>
	<div id="gluten">
		<div>
			<h5 class="card-title">{{recept.title}}</h5>
			<router-link :to="{ name: 'current_user', params: { id: author.id } }" class="card-text">{{author.username}}
				<img id="avatar" :src="host_url + author.avatar"></router-link>
			<!-- <p class="card-text">{{author.username}} <img :src="host_url+author.avatar"></p> -->
			<ul class="card-text">
				<li v-for="rec in recept.recepts_text">{{rec.title}}</li>
			</ul>
			<a v-for="tag in recept.tag_name" href="#" class="badge badge-light">{{tag.name}}</a>
		</div>
		<div v-show="tokens == true" id="comment">
			<form v-on:submit.prevent="add_comment">
				<textarea v-model="comment">

				</textarea>
				<button>Оставить</button>
			</form>
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
				comm_url: "http://127.0.0.1:8000/addcomment/",
				recept: [],
				author: '',
				receptid: '',
				comment: '',
			};
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
			all: function () {
				this.$http.get(this.list_url + this.receptid + "/").then(
					function (response) {
						this.recept = response.data.data[0];
						this.author = this.recept['creater'];
					},
					function (error) {
						// console.log(error);
					}
				);
			},
			add_comment: function() {

				let NewCommentData = new FormData();
				NewCommentData={
					'Text': this.comment,
					'Recept_id': this.receptid,
				};
				console.log("------------------------------");
				console.log(NewCommentData);
				this.$http.post(this.comm_url, NewCommentData, {
					headers: {
						'Authorization': 'Token ' + localStorage.getItem("auth_token"),
						// 'Content-type': 'application/text'
					}
				});
			},
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
	#avatar{
		width: 55px;
		height: 55px;
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