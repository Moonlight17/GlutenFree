<template>
	<div id="add">
		<!-- <h1>{{list}}</h1> -->
		<div>
			<div id="comp-list-example">
				<!-- <form enctype="multipart/form-data"> -->
				<input class="form-control" v-model="title">
					<label for="new-part">Добавить часть рецепта</label>
					<input @keyup.enter="addNewPart" class="form-control" v-model="newPartText" id="new-part" placeholder="смешать что-то с чем-то и получить еще что-то"/>
					<button @click="addNewPart" >Добавить</button>
				<ul>
					<li v-for="(part, index) in part" :key="part.id">
						{{ part.title }}
						<button @click="part.splice(index, 1)">Удалить</button>
					</li>
				</ul>

					<label for="new-comp">Добавить компонент</label>
					<input @keyup.enter="addNewComp" class="form-control" v-model="newCompText" id="new-comp" placeholder="Сметана - 100 г">
					<button @click="addNewComp">Добавить</button>
				<!-- </form> -->
				<ul>
					<li v-for="(comp, index) in comp" :key="comp.id">
						{{ comp.title }}
						<button @click="comp.splice(index, 1)">Удалить</button>
					</li>
				</ul>
				<select class="form-control" multiple v-model="SelectTag">
					<option v-for="(tag, index) in tags" :value="tag">{{tag.name}}</option>
				</select>
				<input autocomplete="off" type="file" id="my_file" ref="files" name="file"  class="archive" />
				<div v-for="image in images" id="image">
					<img :src="image" alt="image" id="output">
				</div>
				<!-- </form> -->
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
			add_url: "http://127.0.0.1:8000/addrecept/",
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
			files: [],
			images: [],
		};
	},
	methods: {
		addNewPart: function() {
			this.part.push({
				id: this.nextPartId++,
				title: this.newPartText,
			});
			this.files.push(this.$refs.files.files[0]);
			this.newPartText = "";
			document.getElementById("my_file").value = "";
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
				Text: JSON.stringify(this.part),
				Tag: this.SelectTag,
				File: this.files
			};
			console.log(NewReceptData);
			this.$http
				.post(this.add_url, NewReceptData, {
					headers: {
						Authorization: "Token " + localStorage.getItem("auth_token"),
						// 'Content-type': 'application/text'
						// ContentType: 'multipart/form-data'
					}
				})
				.then(
					function(response) {
						var id = response.data.data;
						// this.submitFile(id);
						this.loading = false;
						// window.location = '/';
					},
					function(error) {
						console.log(error);
						this.loading = false;
					}
				);
		},
		submitFile: function(id) {
			let NewReceptPhoto = new FormData();
			for (var i = 0; i < this.files.length; i++) {
				let file = this.files[i];
				
				NewReceptPhoto.append('files', file);
			}
			NewReceptPhoto.append('id', id);
			console.log(NewReceptPhoto);
			this.$http
				.post(this.add_url + "photo/", NewReceptPhoto, {
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
		},
		handleFilesUploads() {
			let uploadedFiles = this.$refs.files.files;
			for (var i = 0; i < uploadedFiles.length; i++) {
				this.files.push(uploadedFiles[i]);
				this.images.push(URL.createObjectURL(event.target.files[i]));
				console.log(URL.createObjectURL(event.target.files[i]));
			}
		},
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
#image img{
	margin-top: 50px;
	width: 200px;
	height: 200px;
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
