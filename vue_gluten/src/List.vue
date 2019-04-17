<template>
	<div id="list">
		<!-- <h1>{{list}}</h1> -->
		<div id="recept" @scroll="onScroll">
			<div style="padding:0; margin:0;">
				<div :key="key" v-for="(rec, key) in list" class="card mb-3">
					<!-- <img src="..." class="card-img-top" alt="..."> -->
					<router-link :to="{ name: 'recept', params: { id: rec.id } }" class="card-body" :id="rec.id">
						<h5 class="card-title">{{rec.title}}</h5>
						<router-link :to="{ name: 'current_user', params: { id: rec.creater.id } }" class="card-text">{{rec.creater.username}} <img id="avatar" :src="host_url + rec.creater.avatar"></router-link>
						<p class="card-text"><small class="text-muted">{{rec.pub_date}}</small></p>
					</router-link>
				</div>
			</div>
		</div>
	</div>
</template>

<script>
	export default {
		name: "list",
		data() {
			return {
				host_url: "http://127.0.0.1:8000",
				list_url: "http://127.0.0.1:8000/",
				list: [],
				author: '',
				loading: false,
				start: 0,
			};
		},
		mounted() {
		},
		methods: {
			onScroll: function (event) {
				var wrapper = event.target,
					list = wrapper.firstElementChild

				var scrollTop = wrapper.scrollTop,
					wrapperHeight = wrapper.offsetHeight,
					listHeight = list.offsetHeight

				var diffheight = listHeight - wrapperHeight;
				if (diffheight <= scrollTop && !this.loading) {
					this.start += 9
					this.all();
				}

			},
			all: function () {
				this.loading = true;
				this.$http.get(this.list_url + this.start + "/").then(
					function (response) {
						var list = response.data;
						this.list = this.list.concat(list.data);
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
			this.all();
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

	#img {
		position: fixed;
	}

	#recept {
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