<template>
  <div>
    <header class="header __logout">
      <div class="header__logo">
        <!-- <img src="/assets/img/logo/shoppers-main-logo.png" width="306" height="68px"> -->
        site.title
      </div>
    </header>
    <main class="login">
      <div class="container clearfix">
        <div class="auth-form-wrap">
          <div class="auth-form-nav clearfix">
            <a class="link-active">
              <Label display="inline-block" class="icon-lock" color="#008539" font-size="18px"></Label>Log in
            </a>
          </div>
          <div class="auth-form">
            <form
              class="form form-default"
              @submit.prevent="submitLogin"
              name="loginForm"
              autocomplete="off"
            >
              <FormInputElement
                title-strong="username"
                :errors="errors.username"
                v-model="username"
              />
              <FormInputElement
                title-strong="password"
                :errors="errors.password"
                type="password"
                v-model="password"
              />
              <Container display="block">
                <router-link class="__right" to="/forgot-password">
                  <Label align="right">forgot password?</Label>
                </router-link>
                <!-- <CheckBox id="remember" name="remember me" v-model="rememberMe"/> -->
              </Container>
              <Container display="block" height="36px">
                <Label
                  v-if="showWrongUsername"
                  align="center"
                  type="lbl-form-error"
                >Wrong username or password</Label>
              </Container>
              <Button
                label="Login"
                margin="10px 113px 0 113px"
                button-class="modal-green"
                type="submit"
              />
            </form>
          </div>
        </div>
        <!-- <div class="auth-visual">
          <img src="/assets/img/phone/comp1.png" width="500px">
        </div> -->
      </div>
    </main>
    <footer ng-include="'app/modules/shared/views/footer.html'" class="footer" style>
      <ul class="footer_links">
        <li>2018 © {{$t('site.title')}}</li>
        <li>
          <a href="/terms-of-service.html">{{$t('site.terms_of_service')}}</a>
        </li>
        <li>
          <a href="/privacy-policy.html">{{$t('site.privacy_policy')}}</a>
        </li>
      </ul>
    </footer>
  </div>
</template>

<script>
import FormInputElement from "../components/FormInputElement.vue";
import CheckBox from "../components/CheckBox.vue";
import Button from "../components/Button.vue";
import Label from "../components/Label.vue";
import Container from "../components/Container.vue";
import { validateusername } from "../helpers/utils";

export default {
  components: {
    FormInputElement,
    CheckBox,
    Button,
    Label,
    Container
  },
  data() {
    return {
      errors: {},
      showWrongUsername: false,
      username: "",
      password: "",
      rememberMe: []
    };
  },
  methods: {
    submitLogin: async function() {
      this.showWrongUsername = false;
      if (this.validate()) {
        const user = {
          username: this.username,
          password: this.password
        };
        try {
          const loginResult = await this.$store.dispatch(
            "userModule/login",
            user
          );
          this.$store.commit("userModule/setUser", loginResult.data);
          // reload page
          this.$router.go(this.$router.currentRoute);
        } catch (err) {
          console.log(err);
          this.showWrongUsername = true;
        }
      }
    },
    validate() {
      this.errors = {
        username: [],
        password: []
      };

      if (this.username === "") {
        this.errors.username.push("field is required");
      }
      // if (!validateusername(this.username)) {
      //   this.errors.username.push("username not valid");
      // }
      if (this.password === "") {
        this.errors.password.push("field is required");
      }

      return (
        this.errors.username.length === 0 && this.errors.password.length === 0
      );
    }
  }
};
</script>

<style lang="scss" scoped>
// .login {
//   width: 100%;
//   background: #fff;
//   .container {
//     padding: 15px;
//     margin: 0 auto;
//     width: 820px;
//   }
//   .auth-form-wrap {
//     width: 343px;
//     margin-right: 70px;
//     float: left;
//   }
//   .auth-form-nav {
//     display: table;
//     margin: 77px auto 40px auto;
//     width: 360px;
//     font-size: 12px;
//     line-height: 16px;
//     text-align: center;
//     a {
//       position: relative;
//       display: inline-block;
//       margin: 0 30px;
//       padding: 8px 0;
//       width: 98px;
//       text-align: center;
//       cursor: default;
//       color: #008540;
//       &.link-active:before {
//         content: "";
//         display: block;
//         width: 100%;
//         height: 2px;
//         background: #d8d8d8;
//         border-radius: 4px;
//         position: absolute;
//         left: 0;
//         bottom: 0;
//       }
//       i {
//         margin-right: 15px;
//       }
//     }
//   }
//   .auth-visual {
//     width: 343px;
//     margin-left: 26px;
//     float: left;
//     .auth-visual-intro {
//       padding: 52px 0 10px 0;
//       h1 {
//         font-family: Roboto, Arial, sans-serif;
//         font-weight: 300;
//         font-style: normal;
//         font-size: 20px;
//         line-height: 25px;
//         color: #008540;
//       }
//       ul {
//         margin-top: 26px;
//         padding-left: 40px;
//         list-style-type: disc;
//         li {
//           margin-bottom: 21px;
//           font-size: 13px;
//           line-height: 18px;
//           color: #4c4c4c;
//         }
//       }
//     }
//     img {
//       margin: 59px 0 -114px -25px;
//     }
//   }
//   .form-extra {
//     font-family: Roboto;
//     font-size: 14px;
//     font-weight: 400;
//     font-style: normal;
//     color: #8fa4af;
//     .__right {
//       display: block;
//       text-align: right;
//       padding: 10px 10px 0 0;
//     }
//     a {
//       color: inherit;
//       font-family: inherit;
//     }
//   }
// }

// .header {
//   &.__logout {
//     width: 100%;
//     .header__logo img {
//       margin: 33px 0 38px 33px;
//     }
//   }
// }

// .footer {
//   .footer_links {
//     display: block;
//     margin: 147px auto 83px auto;
//     padding: 0;
//     width: 488px;
//     font-family: Roboto-Regular;
//     font-size: 12px;
//     color: #a5a5a5;
//     li {
//       display: inline-block;
//       padding: 0 15px;
//       a {
//         color: inherit;
//         cursor: pointer;
//       }
//     }
//   }
// }
</style>