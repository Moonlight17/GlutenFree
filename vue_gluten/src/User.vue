<template>
	<div id="user">
		<!-- <h1>{{list}}</h1> -->
			<div style="padding:0; margin:0;">
				<div :key="key" v-for="(rec, key) in listRec.recepts" class="card mb-3">
					<!-- <img src="..." class="card-img-top" alt="..."> -->
					<router-link :to="{ name: 'CurrentRecept', params: { id: rec.id } }" class="card-body" :id="rec.id">
						<h5 class="card-title">{{rec.title}}</h5>
						<p class="card-text"><small class="text-muted">{{rec.pub_date}}</small></p>
					</router-link>
				</div>
			</div>
		</div>
</template>

<script>
	export default {
		name: "user",
		data() {
			return {
				host_url: "http://127.0.0.1:8000",
				list_url: "http://127.0.0.1:8000/user/",
				listRec: [],
				user: '',
				loading: false,
			};
		},
		mounted() {
		},
		methods: {
			allRecept: function () {
				this.loading = true;
				this.$http.get(this.list_url + this.user + "/").then(
					function (response) {
						var list = response.data;
						this.listRec = response.data.data[0];
						this.loading = false;
					},
					function (error) {
						console.log(error);
						this.loading = false;
					}
				);
			},
		},
		created: function () {
			this.user = this.$route.params.id;
			this.allRecept();
		}
	};
</script>

<style>
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
		height:55px;
		width:55px;
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