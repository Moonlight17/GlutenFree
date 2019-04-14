<template>
	<div id="add">
		<img src="./assets/logo.png">
		<!-- <h1>{{list}}</h1> -->
		<div>
		<input v-model="title">
		<div id="comp-list-example">
			<form v-on:submit.prevent="addNewComp">
			<label for="new-comp">Добавить компонент</label>
			<input v-model="newCompText" id="new-comp" placeholder="Сметана - 100 г">
			<button>Добавить</button>
			</form>
			<ul>
				<li v-for="(comp, index) in comp" :key="comp.id">
					{{ comp.title }}
					<button @click="comp.splice(index, 1)">Удалить</button>
				</li>
			</ul>
			<select multiple v-model="SelectTag">
				<option v-for="(tag, index) in tags" :value="tag">{{tag.name}}</option>
			</select>
			<button @click="submit()">Отправить</button>
		<pre>{{$data}}</pre>
		</div>
		</div>
	</div>
</template>

<script>
export default {
  name: "add",
  data() {
    return {
      list_url: "http://127.0.0.1:8000/add/",
      title: "",
      text: "",
	  tags: [],
	  SelectTag: [],
      newCompText: "",
      comp: [],
      nextCompId: 1
    };
  },
  methods: {
    addNewComp: function() {
      this.comp.push({
        id: this.nextCompId++,
        title: this.newCompText
      });
      this.newCompText = "";
    },
    submit: function() {

		let NewReceptData = new FormData();
		NewReceptData={
			'Title': this.title,
			'Text': JSON.stringify(this.comp),
			'Tag': this.SelectTag,
		};
		console.log("------------------------------");
		console.log(NewReceptData);
		this.$http.post(this.list_url, NewReceptData, {
			headers: {
				'Authorization': 'Token ' + localStorage.getItem("auth_token"),
				// 'Content-type': 'application/text'
			}
		})
		.then(function () {
			this.list = response.data;
			console.log(this.list);
			// get body data
		})
		.catch(function (error) {
			console.log("+++++++++=============+++++++++");
			console.log(error);
			this.loading = false;
		});
	},
	tag: function () {
		this.loading = true;
		this.$http.get("http://127.0.0.1:8000/tag/").then(
			function (response) {
				this.tags = response.data.data;
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
