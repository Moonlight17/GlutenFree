<template>
	<div id="add">
		<!-- <h1>{{list}}</h1> -->
		<div>
			<transition name="slide-fade">
				<div v-if="errors.length" class="alert alert-danger" role="alert">
					<ul>
						<li v-for="n in errors">{{n}}</li>
					</ul>
				</div>
			</transition>
			<div id="comp-list-example">
				<form @submit.prevent="CheckForm()">
				<input :class="{'is-invalid': errors.length}" class="form-control" v-model="title">
				<label for="new-part">Добавить часть рецепта</label>
				<input :class="{'is-invalid': errors.length}" class="form-control" v-model="newPartText" id="new-part" placeholder="смешать что-то с чем-то и получить еще что-то"/>
				<input accept="image/*" autocomplete="off" @change="file = true" type="file" id="my_file" ref="files" name="file"  class="archive" />
				<br>
				<br>
				<button type="button" @click="addNewPart()" >Добавить</button>
				<ul>
					<li id="inl" v-for="(par, index) in part" :key="part.id">
						{{ par.title }}
						<button :id="index" type="button" @click="part.splice(index, 1)">Удалить</button>
					</li>
				</ul>

					<label for="new-comp">Добавить компонент</label>
					<input :class="{'is-invalid': errors.length}" class="form-control" v-model="newCompText" id="new-comp" placeholder="Сметана - 100 г">
					<button type="button" @click="addNewComp()">Добавить</button>
				<!-- </form> -->
				<ul>
					<li v-for="(com, index) in comp" :key="comp.id">
						{{ com.title }}
						<button type="button" @click="comp.splice(index, 1)">Удалить</button>
					</li>
				</ul>
				<select :class="{'is-invalid': errors.length}" class="form-control" multiple v-model="SelectTag">
					<option v-for="(tag, index) in tags" :value="tag">{{tag.name}}</option>
				</select>
				<div v-for="image in images" id="image">
					<img :src="image" alt="image" id="output">
				</div>
				<button>Отправить</button>
				</form>

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
			file: false,
			files: [],
			images: [],
			errors: [],
			success: false,
		};
	},
	methods: {
		CheckForm: function(e) {
			// console.log(this.part.length);
			// console.log(this.comp.length);
			if(this.title && this.part.length && this.comp.length && this.SelectTag) this.submit();
			this.errors = [];
			if(!this.title) this.errors.push("Name required.");
			if(!this.part.length) this.errors.push("Part required.");
			if(!this.comp.length) this.errors.push("Comp required.");
			if(!this.SelectTag.length) this.errors.push("Tag required.");

		},
		addNewPart: function() {
			this.errors = [];
			if(!this.newPartText.length) this.errors.push("PartRecept required.");
			if(!this.$refs.files.files[0]) this.errors.push("Image required.");
			// console.log(this.$refs.files.files[0]);
			// console.log(this.newPartText.length);
			if (this.$refs.files.files[0] && this.newPartText.length){
					this.part.push({
					id: this.nextPartId++,
					title: this.newPartText,
				});
				this.files.push(this.$refs.files.files[0]);
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
				Title: this.title,
				Comp: JSON.stringify(this.comp),
				Text: JSON.stringify(this.part),
				Tag: this.SelectTag,
				File: this.files[0]
			};
			console.log(NewReceptData);
			this.$http
				.post(this.add_url, NewReceptData, {
					headers: {
						Authorization: "Token " + localStorage.getItem("auth_token")
					}
				})
				.then(
					function(response) {
						var id = response.data.data;
						this.submitFile(id);
						this.loading = false;
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
						this.success = true;
						if (this.success) window.location = '/';
						
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

li#inl {
	display: inline-block;
	margin: 0 10px;
}

a {
	color: #42b983;
}
/* Анимации появления и исчезновения могут иметь */
/* различные продолжительности и динамику.       */
.slide-fade-enter-active {
  transition: all .3s ease;
}
.slide-fade-leave-active {
  transition: all .8s cubic-bezier(1.0, 0.5, 0.8, 1.0);
}
.slide-fade-enter, .slide-fade-leave-to
/* .slide-fade-leave-active до версии 2.1.8 */ {
  transform: translateX(10px);
  opacity: 0;
}
</style>
