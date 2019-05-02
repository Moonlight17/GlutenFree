<template>
	<transition name="fade">
		<div v-if="files.length>0" id="blok">
			<table class="table table-striped">
				<tbody>
					<tr v-for="(file, key) in files">
						<th scope="row">[[key + 1]]</th>
						<td>[[file.name]]</td>
						<td><button  v-on:click="removeFile( key )" type="button"
								class="btn btn-outline-danger">Удалить</button></td>
					</tr>
				</tbody>
			</table>
		</div>
	</transition>
  <form v-on:submit.prevent id="my_form" enctype="multipart/form-data">
	<input autocomplete="off" type="file" id="my_file" ref="files" name="file" v-on:change="handleFilesUploads" class="archive" multiple
	>
	<p v-if="files.length>0">К загузке на сайт готово - [[files.length]] файла(-ов)</p>
	<p v-else>
	  <svg width="40" height="40" viewBox="0 0 384 512">
		<path
		  fill="currentColor"
		  d="M224 136V0H24C10.7 0 0 10.7 0 24v464c0 13.3 10.7 24 24 24h336c13.3 0 24-10.7 24-24V160H248c-13.2 0-24-10.8-24-24zm65.18 216.01H224v80c0 8.84-7.16 16-16 16h-32c-8.84 0-16-7.16-16-16v-80H94.82c-14.28 0-21.41-17.29-11.27-27.36l96.42-95.7c6.65-6.61 17.39-6.61 24.04 0l96.42 95.7c10.15 10.07 3.03 27.36-11.25 27.36zM377 105L279.1 7c-4.5-4.5-10.6-7-17-7H256v128h128v-6.1c0-6.3-2.5-12.4-7-16.9z"
		></path>
	  </svg>Переместите Ваши файлы в область или кликните по ней.
	</p>
	<label style="opacity: 0" class="custom-file-label" for="my_file"></label>
	<button id="but" @click="uploadFile()" type="submit">Upload</button>
  </form>
</template>
<style>

#my_form {
  color: black;
  position: absolute;
  top: 50%;
  left: 50%;
  margin-top: -100px;
  margin-left: -250px;
  width: 500px;
  height: 200px;
  border: 4px dashed #000;
}
#my_form p {
  width: 100%;
  height: 100%;
  text-align: center;
  line-height: 170px;
  color: #000;
  font-family: Arial;
}
#my_form #my_file {
  position: absolute;
  margin: 0;
  padding: 0;
  width: 100%;
  height: 100%;
  outline: none;
  opacity: 0;
}
#my_form #but {
  margin: 0;
  color: #000;
  background: #16a085;
  border: none;
  width: 508px;
  height: 35px;
  margin-top: -20px;
  margin-left: -4px;
  border-radius: 4px;
  border-bottom: 4px solid #117a60;
  transition: all 0.2s ease;
  outline: none;
}
#my_form #but:hover {
  background: #149174;
  color: #0c5645;
}
#my_form #but:active {
  border: 0;
}
</style>

<script>
export default {
data: {
	message: "Привет, Vue!",
	url: "/load/",
	loading: false,
	files: [],
},
methods: {
	addFiles() {
		this.$refs.files.click();
	},
	uploadFile() {
		this.loading = true;
		let formData = new FormData();
		
		/*
		Iteate over any file sent over appending the files
		to the form data.
		*/
		for (var i = 0; i < this.files.length; i++) {
			let file = this.files[i];
			
			formData.append('files', file);
		}
		if (this.files.length) {
			this.$http.post('/upload/', formData, {
				headers: {
					'dataType': 'json'
				}
			})
			.then(function () {
				this.files = [];
				this.loading = false;
			})
			.catch(function () {
				console.log(error);
				this.loading = false;
			});
		}
	},
	handleFilesUploads() {
		let uploadedFiles = this.$refs.files.files;
		for (var i = 0; i < uploadedFiles.length; i++) {
			this.files.push(uploadedFiles[i]);
		}
	},
	removeFile(key) {
		this.files.splice(key, 1);
	},
	
}
</script>