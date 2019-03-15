<template>
  <div>
    <form action="api/v1.0/auth/login/" method="POST">
        <input type="text" name="username" placeholder="username"></input>
        <input type="password" name="password" placeholder="password"></input>
        <button type="submit">Login</button>

    </form>
  </div>
</template>
<script>
import config from "@/config";

export default {
  components: {},
  data() {
    return {};
  },
  computed: {},
  methods: {}
};
</script>
<style>
</style>
