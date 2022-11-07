<template>
  <div class="sign-in w-50 m-auto mt-5">
    <form class="form-signin w-50 m-auto card p-2" @submit.prevent="Signin">
      <div class="text-center mb-4">
        <img
            class="mb-4"
            src="../../assets/images/style_avenue_logo.jpg"
            alt=""
            width="72"
            height="72"
        />
        <h1 class="h3 mb-3 font-weight-bold">Style Avenue Studio</h1>
      </div>

      <div class="input-group form-label-group mb-2">
        <input
            type="email"
            id="inputEmail"
            class="form-control"
            placeholder="Email address"
            v-model="email"
            required
            autofocus
        />
      </div>

      <div class="input-group form-label-group mb-2">
        <input
            type="password"
            id="inputPassword"
            class="form-control"
            placeholder="Password"
            v-model="password"
            required
        />
        <div class="input-group-append toggle-password">
          <span class="input-group-text mdi mdi-eye-outline"></span>
        </div>
      </div>

      <!-- <div class="checkbox mb-3">
        <label>
          <small>
            <input type="checkbox" value="remember-me" /> Remember me
          </small>
        </label>
      </div> -->
      <button
          class="btn btn-sm btn-primary m-auto"
          type="submit"
          style="width: 100%"
      >
        Sign in
      </button>
      <div class="errors ">
        <div class="notification is-danger" v-if="errors.length">
          <p v-for="error in errors" :key="error.id">{{ error }}</p>
        </div>
      </div>
      <p>
        <small>
          <a href="#" class="text-center">Forgot password?</a>
        </small>
      </p>
      <p class="mt-5 mb-3 text-muted text-center">
        <span> Don't have an account? </span>
        <router-link to="/signup">Sign Up</router-link>
      </p>
      <p class="mt-5 mb-3 text-muted text-center">&copy; 2022</p>
    </form>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      email: "",
      password: "",
      errors: [],
    };
  },
  mounted() {
    // this.$store.dispatch("Signin");
    document.title = "Style Avenue - Sign In";
    this.$store.dispatch("showPassword");

  },
  methods: {
    async Signin() {
      axios.defaults.headers.common["Authorization"] = "";

      localStorage.removeItem("token");

      await axios
          .post("auth/mentorship/", {
            email: this.email,
            password: this.password,
          })
          .then((response) => {
            const token = response.data.token;

            this.$store.commit("setToken", token);

            axios.defaults.headers.common["Authorization"] = `Bearer ${token}`;

            localStorage.setItem("SetToken", token);
            console.log("token", token);

            const toPath = this.$route.query.to || "/";

            this.$router.push(toPath);

            // if (response.data.success) {
            //   toast({
            //     message: response.data.message,
            //     type: "is-success",
            //     duration: 3000,
            //   });
            //   this.$router.push("/");
            // } else {
            //   this.errors = response.data.errors;
            // }
          })
          .catch((error) => {
            if (error.response) {
              for (const property in error.response.data) {
                this.errors.push(`${error.response.data[property]}`);
              }
            } else {
              this.errors.push(error.message);
              console.log(JSON.stringify(error));
            }
          });


    },
  },
};
</script>

<style>
.form-signin {
  box-shadow: 0px 0px 5px rgba(0, 0, 0, 0.402);
  background-color: antiquewhite !important;
}

.errors {
  color: #bf2626;
  margin-top: 2px;
}
</style>