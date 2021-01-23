<template>
  <div id="list">
    <!-- <h1>{{list}}</h1> -->
    <div id="recept" @scroll="onScroll">
      <div style="padding:0; margin:0;">
        <div :key="key" v-for="(rec, key) in list_rec" class="card mb-3">
          <!-- <img src="..." class="card-img-top" alt="..."> -->
          <router-link
            :to="{ name: 'CurrentRecept', params: { id: rec.id } }"
            class="card-body"
            :id="rec.id"
          >
            <h5 class="card-title">{{rec.title}}</h5>
            <router-link
              :to="{ name: 'CurrentUser', params: { id: rec.user.id } }"
              class="card-text"
            >
              {{rec.user.username}}
              <img id="avatar" :src="rec.user.avatar">
            </router-link>
            <p class="card-text">
              <small class="text-muted">{{rec.pub_date}}</small>
              <svgimg v-if="rec.like" name="svg-ExistsLike"/>
            </p>
          </router-link>
        </div>
        <div v-if="loading" class="d-flex justify-content-center">
          <div class="spinner-border" role="status">
            <span class="sr-only">Loading...</span>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import svgIcon from "./svg.vue";
export default {
  name: "list",
  data() {
    return {
      host_url: "",
      list_url: this.$root.link,
      list_rec: [],
      author: "",
      loading: false,
      start: 0
    };
  },
  mounted() {},
  components: {
    svgimg: svgIcon
  },
  methods: {
    onScroll: function(event) {
      var wrapper = event.target,
        list = wrapper.firstElementChild;

      var scrollTop = wrapper.scrollTop,
        wrapperHeight = wrapper.offsetHeight,
        listHeight = list.offsetHeight;

      var diffheight = listHeight - wrapperHeight;
      if (diffheight <= scrollTop && !this.loading) {
        this.start += 9;
        this.all();
      }
    },
    all: function() {
      this.loading = true;
      if (!localStorage.getItem("auth_token")) {
        this.$http.get(this.list_url + this.start + "/").then(
          function(response) {
            console.log(response);
            var list = response.data;
            this.list_rec = this.list_rec.concat(list.data);
            this.loading = false;
          },
          function(error) {
            console.log(error);
            this.loading = false;
          }
        );
      } else {
        this.$http
          .get(this.list_url + this.start + "/", {
            headers: {
              Authorization: "Token " + localStorage.getItem("auth_token")
              // 'Content-type': 'application/text'
            }
          })
          .then(
            function(response) {
              var list = response.data;
              this.list_rec = this.list_rec.concat(list.data);
              this.loading = false;
            },
            function(error) {
              console.log(error);
              this.loading = false;
            }
          );
      }
    }
  },
  created: function() {
    this.all();
    // console.log(window.location.href);
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
  height: 78vh;
  margin: 0 auto;
  margin-top: 1vh;
  overflow: scroll;
}

img#avatar {
  height: 55px;
  width: 55px;
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