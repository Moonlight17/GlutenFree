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
		<div id="comments">
			<div style="padding:0; margin:0;">
				<div :key="key" v-for="(rec, key) in comments" class="card mb-3">
					<!-- <img src="..." class="card-img-top" alt="..."> -->
					<div class="card-body" :id="rec.id">
						<h6 class="card-title">{{rec.text}}</h6>
						<router-link :to="{ name: 'current_user', params: { id: rec.user.id } }" class="card-text">
							{{rec.user.username}} <img id="avatar" :src="host_url + rec.user.avatar">
						</router-link>
						<p class="card-text"><small class="text-muted">{{rec.pub_date}}</small></p>
					</div>
				</div>
			</div>
		</div>
		<div v-show="tokens == true" id="comment">
			<form v-on:submit.prevent="add_comment">
				<div class="form-group">
					<textarea class="form-control" v-model="comment" id="exampleFormControlTextarea1"
						rows="3"></textarea>
				</div>
			</form>
			<button @click="add_comment">Оставить</button>
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
				list_comment_url: "http://127.0.0.1:8000/comments/",
				comm_url: "http://127.0.0.1:8000/addcomment/",
				recept: [],
				comments: [],
				author: '',
				receptid: '',
				comment: '',
				list: [],
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
			Recept: function () {
				this.$http.get(this.list_url + this.receptid + "/").then(
					function (response) {
						this.recept = response.data.data[0];
						this.author = this.recept['user'];
					},
					function (error) {
						// console.log(error);
					}
				);
			},
			Comments: function () {
				this.$http.get(this.list_comment_url + this.receptid + "/").then(
					function (response) {
						var list = response.data;
						this.comments = list.data;
						this.loading = false;
					},
					function (error) {
						// console.log(error);
					}
				);
			},
			add_comment: function () {

				let NewCommentData = new FormData();
				NewCommentData = {
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
				}).then(
							function (response) {
								this.comment = '';
								this.Comments();
								console.log("OLOLOLO");
								this.loading = false;
							},
							function (error) {
								console.log(error);
								this.loading = false;
							}
						);;
				
			},
		},
		created: function () {
			this.receptid = this.$route.params.id;
			console.log(this.receptid);
			this.Recept();
			this.Comments();
		}
	};
</script>

<style>
	#recept {
		font-family: "Avenir", Helvetica, Arial, sans-serif;
		width: 70vw;
		margin: 0 auto;
	}

	#avatar {
		width: 55px;
		height: 55px;
	}

	#text_comment {
		width: 70vw;

	}
	textarea.form-control{
		margin: 0 auto;
		margin-top: 2vh;
		width: 70vw;
		min-height: 30vh;
	}

	#comments {
		font-family: "Avenir", Helvetica, Arial, sans-serif;
		width: 70vw;
		/* height: 80vh; */
		margin: 0 auto;
		margin-top: 10vh;
		/* overflow: scroll; */


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