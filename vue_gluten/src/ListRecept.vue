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
		<div id="recept" @scroll="onScroll">
			<div style="padding:0; margin:0;">
				<div :key="key" v-for="(rec, key) in list" class="card mb-3">
					<!-- <img src="..." class="card-img-top" alt="..."> -->
					<div class="card-body" :id="rec.id">
						<h5 class="card-title">{{rec.title}}</h5>
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
				list_comment_url: "http://127.0.0.1:8000/comments/",
				comm_url: "http://127.0.0.1:8000/addcomment/",
				recept: [],
				comments: [],
				author: '',
				receptid: '',
				comment: '',
				start: 0,
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
				this.$http.get(this.list_comment_url + this.receptid + "/" + this.start + "/").then(
					function (response) {
						var list = response.data;
						this.comments = this.comments.concat(list.data);
						this.loading = false;
					},
					function (error) {
						// console.log(error);
					}
				);
			},
			onScroll: function (event) {
				var wrapper = event.target,
					list = wrapper.firstElementChild

				var scrollTop = wrapper.scrollTop,
					wrapperHeight = wrapper.offsetHeight,
					listHeight = list.offsetHeight

				var diffheight = listHeight - wrapperHeight;
				if (diffheight <= scrollTop && !this.loading) {
					this.start += 9
					this.Comments();
				}

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
				});
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