<template>
	<div id="add">
		<!-- <h1>{{list}}</h1> -->
		<div>
			<div id="comp-list-example">
				<input class="form-control" v-model="title">
				<form v-on:submit.prevent="addNewPart">
					<label for="new-part">Добавить часть рецепта</label>
					<textarea class="form-control" v-model="newPartText" id="new-part" placeholder="смешать что-то с чем-то и получить еще что-то"></textarea>
					<button>Добавить</button>
				</form>
				<ul>
					<li v-for="(part, index) in part" :key="part.id">
						{{ part.title }}
						<button @click="part.splice(index, 1)">Удалить</button>
					</li>
				</ul>
				<form v-on:submit.prevent="addNewComp">
					<label for="new-comp">Добавить компонент</label>
					<input class="form-control" v-model="newCompText" id="new-comp" placeholder="Сметана - 100 г">
					<button>Добавить</button>
				</form>
				<ul>
					<li v-for="(comp, index) in comp" :key="comp.id">
						{{ comp.title }}
						<button @click="comp.splice(index, 1)">Удалить</button>
					</li>
				</ul>
				<select class="form-control" multiple v-model="SelectTag">
					<option v-for="(tag, index) in tags" :value="tag">{{tag.name}}</option>
				</select>
				<button @click="submit()">Отправить</button>
			</div>
		</div>
	</div>
</template>

<script>
export default {
	name: "add",
	data() {
		return {
			list_url: "http://127.0.0.1:8000/addrecept/",
			title: "",
			text: "",
			tags: [],
			SelectTag: [],
			newCompText: "",
			comp: [],
			newPartText: "",
			part: [],
			nextCompId: 1,
			nextPartId: 1,
		};
	},
	methods: {
		addNewPart: function() {
			this.part.push({
				id: this.nextPartId++,
				title: this.newPartText
			});
			this.newPartText = "";
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
				Title: this.title,
				Comp: JSON.stringify(this.comp),
				Text: JSON.stringify(this.comp),
				Tag: this.SelectTag
			};
			console.log(NewReceptData);
			this.$http
				.post(this.list_url, NewReceptData, {
					headers: {
						Authorization: "Token " + localStorage.getItem("auth_token")
						// 'Content-type': 'application/text'
					}
				})
				.then(
					function(response) {
						this.loading = false;
					},
					function(error) {
						console.log(error);
						this.loading = false;
					}
				);
		},
		tag: function() {
			this.loading = true;
			this.$http.get("http://127.0.0.1:8000/tag/").then(
				function(response) {
					this.tags = response.data.data;
					this.loading = false;
				},
				function(error) {
					console.log(error);
					this.loading = false;
				}
			);
		}
	},
	created: function() {
		this.tag();
	}
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
