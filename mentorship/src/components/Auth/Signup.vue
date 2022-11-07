<template>
  <div class="sign-up w-50 m-auto">
    <section class="h-100 h-custom">
      <div class="container py-5 h-100">
        <div class="row d-flex justify-content-center align-items-center h-100">
          <div class="col-lg-8 col-xl-6">
            <div class="card rounded-3 signin-card">
              <img
                  src="https://mdbcdn.b-cdn.net/img/Photos/new-templates/bootstrap-registration/img3.webp"
                  class="w-100"
                  style="
                  border-top-left-radius: 0.3rem;
                  border-top-right-radius: 0.3rem;
                "
                  alt="Sample photo"
              />
              <div class="card-body p-2 p-md-5">
                <p class="text-center h3 fw-bold mb-5 mx-1 mx-md-4 mt-3">
                  Sign up
                </p>

                <form class="px-md-2" @submit.prevent="Signup">
                  <div class="">
                    <div class="">
                      <div class="form-outline mb-2">
                        <input
                            type="email"
                            class="form-control"
                            placeholder="Email address"
                            v-model="email"
                        />
                      </div>
                    </div>
                  </div>
                  <div class="">
                    <div class="">
                      <div class="form-outline mb-2">
                        <input
                            type="text"
                            class="form-control"
                            placeholder="username"
                            v-model="username"
                        />
                      </div>
                    </div>
                  </div>

                  <div class="">
                    <div class="">
                      <div class="input-group form-outline mb-2">
                        <input
                            type="Password"
                            class="form-control"
                            placeholder="Password"
                            id="password"
                            v-model="password"
                        />
                        <div class="input-group-append toggle-password" @click="showPassword">
                          <span class="input-group-text mdi mdi-eye-outline"></span>
                        </div>
                      </div>
                    </div>
                  </div>
                  <div class="">
                    <div class="">
                      <div class="input-group form-outline mb-2">
                        <input
                            type="Password"
                            class="form-control"
                            placeholder="Confirm Password"
                            v-model="confirmPassword"
                        />
                        <div class="input-group-append toggle-password">
                          <span class="input-group-text mdi mdi-eye-outline"></span>
                        </div>
                      </div>
                    </div>
                  </div>

                  <button type="submit" class="btn btn-primary btn-sm mb-1">
                    Sign up
                  </button>
                  <div class="notification text-danger" v-if="errors.length">
                    <p v-for="error in errors" :key="error">{{ error }}</p>
                  </div>
                  <p>
                    Already have an account?
                    <a href="/signIn">Sign in</a>
                  </p>
                  <p>Check your email and verify to log in</p>
                </form>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
import axios from "axios";
import {toast} from "bulma-toast";

export default {
  data() {
    return {
      email: "",
      username: "",
      password: "",
      confirmPassword: "",
      errors: [],
    };
  },

  mounted() {
    // this.$store.dispatch("Signup");
    document.title = "Style Avenue - Sign up";
    this.$store.dispatch("showPassword");
  },
  methods: {
    Signup() {
      this.errors = [];

      if (!this.email) {
        this.errors.push("Email required.");
      }
      if (!this.username) {
        this.errors.push("Username required.");
      }

      if (this.password === "") {
        this.errors.push("The password is too short");
      }

      if (this.password !== this.confirmPassword) {
        this.errors.push("Passwords don't match");
        return;
      }

      if (!this.errors.length) {
        const formData = {
          email: this.email,
          username: this.username,
          password: this.password,
        };

        axios
            .post("auth/register/", formData)
            .then((response) => {
              toast({
                message: "Account created successfully",
                type: "is-success",
                dismissable: true,
                duration: 2000,
                position: "bottom-right",
              });
              this.$router.push("/signin");
            })
            .catch((error) => {
              if (error.response) {
                toast({
                  message: "Something went wrong",
                  type: "is-danger",
                  dismissable: true,
                  duration: 2000,
                  position: "bottom-right",
                });
                for (const property in error.response.data) {
                  this.errors.push(
                      `${property}: ${error.response.data[property]}`
                  );
                }
                console.log(JSON.stringify(error.response.data));
              } else if (error.message) {
                this.errors.push("Something went wrong");
                console.log(JSON.stringify(error));
              }
              console.log(error);
            });
      }
    },
    //Another way to show password
    // showPassword() {
    //   const password = document.querySelector("#password");
    //   const type = password.getAttribute("type") === "password" ? "text" : "password";
    //   password.setAttribute("type", type);
    //   this.toggleClass();
    // },


  },
};
</script>

<style>
.signin-card {
  box-shadow: 0px 0px 5px rgba(0, 0, 0, 0.402);
  background-color: antiquewhite !important;
}
</style>