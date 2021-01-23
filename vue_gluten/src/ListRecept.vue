<template>
	<div id="gluten">
		<div>
			<button v-show="recept.my" type="button" class="btn btn-primary" data-toggle="modal" data-target="#exampleModal">
				<svgimg  name="svg-Edit"/>
			</button>

			
			<div id="images">
				<span  v-for="image in recept.images"><img id="img" :src="host_url + image"></span>
				
			</div>
			<h5 class="card-title">{{recept.title}}</h5>
			<router-link :to="{ name: 'CurrentUser', params: { id: author['id'] } }" class="card-text">{{author.username}}
				<img id="avatar" :src="author.avatar"></router-link>
			<!-- <p class="card-text">{{author.username}} <img :src="host_url+author.avatar"></p> -->
			<div>
				<ul class="border card-text">
					<li class="text" v-for="rec in recept.text"><span>{{rec.title}}</span></li>
				</ul>
				------------------------------------------------------
				<ul class="border card-text">
					<li class="text" v-for="rec in recept.comp"><span>{{rec.title}}</span></li>
				</ul>
			</div>
			<a v-for="tag in recept.tag_name" href="#" class="badge badge-light">{{tag.name}}</a>
			<p v-show="tokens == true" @click="Like()">
				<svgimg  v-if="recept.like" name="svg-ExistsLike" />
				<svgimg  v-else-if="!recept.like" name="svg-NoneLike" />
			</p>
		</div>
		<div id="comments">
			<div style="padding:0; margin:0;">
				<div :key="key" v-for="(com, key) in comments" class="card mb-3">
					<!-- <img src="..." class="card-img-top" alt="..."> -->
					<div class="card-body" :id="com.id">
						<h6 class="card-title">{{com.text}}</h6>
						<router-link :to="{ name: 'CurrentUser', params: { id: com.user['id'] } }" class="card-text">
							{{com.user.username}} <img id="avatar" :src="com.user.avatar">
						</router-link>
						<p class="card-text"><small class="text-muted">{{com.pub_date}}</small></p>
					</div>
					<p v-show="tokens == true" @click="LikeComm(com.id, key)">
						<svgimg  v-if="com.like" name="svg-ExistsLike" />
						<svgimg  v-else-if="!com.like" name="svg-NoneLike" />
					</p>
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
			<button v-show="com" @click="add_comment">Оставить</button>
			</form>
		</div>
		<div class="modal fade" id="exampleModal" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
			<div class="modal-dialog" role="document">
				<div class="modal-content">
					<div class="modal-header">
						<h5 class="modal-title" id="exampleModalLabel">Modal title</h5>
						<button type="button" class="close" data-dismiss="modal" aria-label="Close">
						<span aria-hidden="true">&times;</span>
						</button>
					</div>
					<div class="modal-body">
						<form @submit.prevent="">
							<input :class="{'is-invalid': errors.length}" class="form-control" v-model="recept.title">
							<br>
							<br>
							<ul>
								<li id="inl" v-for="(par, index) in part" :key="part.id">
									{{ par.title }}
									<button :id="index" type="button" @click="part.splice(index, 1)">Удалить</button>
								</li>
							</ul>

								<label for="new-comp">Компоненты:</label>
							<p v-for="comp in recept.comp">
								<textarea style="width:100%" name="ololo" v-model="comp.title" id="new-comp" :class="{'is-invalid': errors.length}" class="form-control" placeholder="Сметана - 100 г"></textarea>
							</p>
							<label for="new-part">Рецепт:</label>
							<p v-for="part in recept.text">
								<textarea style="width:100%" name="ololo" v-model="part.title" id="new-part" :class="{'is-invalid': errors.length}" class="form-control" placeholder="смешать что-то с чем-то и получить еще что-то"></textarea>
							</p>
							<!-- </form> -->
							<ul>
								<li v-for="(com, index) in comp" :key="comp.id">
									{{ com.title }}
									<button type="button" @click="comp.splice(index, 1)">Удалить</button>
								</li>
							</ul>
							<div v-for="image in images" id="image">
								<img :src="image" alt="image" id="output">
							</div>
							<select :class="{'is-invalid': errors.length}" class="form-control" multiple v-model="recept.tag_name">
								<option v-for="(tag, index) in recept.tag_name" :value="tag">{{tag.name}}</option>
							</select>
							</form>
					</div>
					<div class="modal-footer">
						<button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
						<button @click="CheckForm()" type="button" class="btn btn-primary">Save changes</button>
					</div>
				</div>
			</div>
		</div>
	</div>
</template>

<script>
	import svgIcon from './svg.vue'
	export default {
		name: "Recept",
		components: {
			'svgimg': svgIcon
		},
		data() {
			return {
				host_url: this.$root.link,
				list_url: this.$root.link+"recept/",
				list_comment_url: this.$root.link+"comments/",
				comm_url: this.$root.link+"addcomment/",
				like_url: this.$root.link+"like/",
				add_url: this.$root.link+"recept/",
				recept: [],
				comments: [],
				user: false,
				author: '',
				receptid: '',
				comment: '',
				loading: false,
				title: "",
				comp: [],
				part: [],
				images: [],
				errors: [],
				newCompText: "",
				newPartText: "",


			};
		},
		computed: {
			tokens() {
				if (localStorage.getItem("auth_token"))
					{this.user = true
					return true}
				else
					{this.user = false
					return false}
			},
			com(){
				return this.comment.length
			}
		},
		methods: {
			Recept: function () {
				if (!this.loading){
					if(localStorage.getItem("auth_token"))
						{this.$http.get(this.list_url + this.receptid + "/", {
								headers: {
									'Authorization': 'Token ' + localStorage.getItem("auth_token"),
								}
							}).then(
							function (response) {
								console.log(response.data.data)
								this.recept = response.data.data[0];
								this.author = this.recept['user'];
							},
							function (error) {
								// console.log(error);
							}
						)}else{
							this.$http.get(this.list_url + this.receptid + "/").then(
								function (response) {
									this.recept = response.data.data[0];
									this.author = this.recept['user'];
								},
								function (error) {
									// console.log(error);
								}
							)
						}
				};
			},
			Comments: function () {
				if (!this.loading){
					if(localStorage.getItem("auth_token")){
						this.$http.get(this.list_comment_url + this.receptid + "/", {
							headers: {
								'Authorization': 'Token ' + localStorage.getItem("auth_token"),
								// 'Content-type': 'application/text'
							}
						}).then(
							function (response) {
								var list = response.data;
								this.comments = list.data;
								this.loading = false;
							},
							function (error) {
								// console.log(error);
						}
						)
					}else{
						this.$http.get(this.list_comment_url + this.receptid + "/").then(
							function (response) {
								var list = response.data;
								this.comments = list.data;
								this.loading = false;
							},
							function (error) {
								// console.log(error);
						}
						)
					}
				};
				
			},
			add_comment: function () {

				let NewCommentData = new FormData();
				NewCommentData = {
					'Text': this.comment,
					'Recept_id': this.receptid,
				};
				if (!this.loading){
				this.$http.post(this.comm_url, NewCommentData, {
					headers: {
						'Authorization': 'Token ' + localStorage.getItem("auth_token"),
						// 'Content-type': 'application/text'
					}
				}).then(
							function (response) {
								this.comment = '';
								this.loading = false;
								this.Comments();
							},
							function (error) {
								console.log(error);
								this.loading = false;
							}
						)}else{
							alert("Проблемы со связью");
						};
				
			},
			Like: function(){

				if (!this.loading && this.user){
				this.$http.get(this.like_url + this.receptid + "/", {
					headers: {
						'Authorization': 'Token ' + localStorage.getItem("auth_token"),
						// 'Content-type': 'application/text'
					}
				}).then(
					function (response) {
						this.recept.like = !this.recept.like;
						this.loading = false;
					},
					function (error) {
						console.log(error);
						this.loading = false;
					}
				);
				}
			},
			LikeComm: function(id, key){

				if (!this.loading && this.user){
				this.$http.get(this.like_url + this.receptid + "/" + id + "/", {
					headers: {
						'Authorization': 'Token ' + localStorage.getItem("auth_token"),
						// 'Content-type': 'application/text'
					}
				}).then(
					function (response) {
						this.comments[key].like = !this.comments[key].like;
						this.loading = false;
					},
					function (error) {
						console.log(error);
						this.loading = false;
					}
				);
				}
			},
			CheckForm: function(e) {
				// console.log(this.part.length);
				// console.log(this.comp.length);
				if(this.recept.title && this.recept.text && this.recept.comp) this.submit();
				this.errors = [];
				if(!this.recept.title) this.errors.push("Name required.");
				if(!this.recept.text.length) this.errors.push("Part required.");
				if(!this.recept.comp.length) this.errors.push("Comp required.");

			},
			addNewPart: function() {
				this.errors = [];
				if(!this.newPartText.length) this.errors.push("PartRecept required.");
				// console.log(this.$refs.files.files[0]);
				// console.log(this.newPartText.length);
				if (this.newPartText.length){
						this.part.push({
						id: this.nextPartId++,
						title: this.newPartText,
					});
					document.getElementById("my_file").value = "";
					this.newPartText = "";
				};
			},
			addNewComp: function() {
				this.comp.push({
					id: this.nextCompId++,
					title: this.newCompText
				});
				this.newCompText = "";
			},
			submit: function() {
				let NewReceptData = new FormData();
				NewReceptData = {
					Title: this.recept.title,
					Comp: JSON.stringify(this.recept.comp),
					Text: JSON.stringify(this.recept.text),
					Tag: JSON.stringify(this.recept.tag_name),
				};
				console.log(NewReceptData);
				this.$http
					.post(this.add_url+this.receptid+"/edit/", NewReceptData, {
						headers: {
							Authorization: "Token " + localStorage.getItem("auth_token")
						}
					})
					.then(
						function(response) {
							var id = response.data.data;
							this.loading = false;
						},
						function(error) {
							console.log(error);
							this.loading = false;
						}
					);
			},
		},
		created: function () {
			this.receptid = this.$route.params.id;
			this.Recept();
			this.Comments();
		}
	};
</script>

<style>
	#img{
		margin-right: 50px;
		border:  3px solid #42b983;
		width: 300px;
		max-height: 230px;
		/* margin-bottom:50px; */
	}
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

	.border {
		list-style: none;
		padding: 0;
	}
	.border li.text {
		font-family: "Trebuchet MS", "Lucida Sans";
		padding: 7px 20px;
		margin-bottom: 10px;
		border-radius: 5px;
		border-left: 10px solid #f05d22; 
		box-shadow: 2px -2px 5px 0 rgba(0,0,0,.1),
			-2px -2px 5px 0 rgba(0,0,0,.1),
			2px 2px 5px 0 rgba(0,0,0,.1),
			-2px 2px 5px 0 rgba(0,0,0,.1);
		font-size: 20px;
		letter-spacing: 2px;
		transition: 0.3s all linear;
	}
	.border li.text:nth-child(2){border-color: #8bc63e;}
	.border li.text:nth-child(3){border-color: #fcba30;}
	.border li.text:nth-child(4){border-color: #1ccfc9;}
	.border li.text:nth-child(5){border-color: #493224;}
	.border li.text:hover {border-left: 10px solid transparent;}
	.border li.text:nth-child(1):hover {border-right: 10px solid #f05d22;}
	.border li.text:nth-child(2):hover {border-right: 10px solid #8bc63e;}
	.border li.text:nth-child(3):hover {border-right: 10px solid #fcba30;}
	.border li.text:nth-child(4):hover {border-right: 10px solid #1ccfc9;}
	.border li.text:nth-child(5):hover {border-right: 10px solid #493224;}
	a {
		color: #42b983;
	}
</style>