<template>
    <form>
        <label for="username">
            Login
        </label>
        <input type="text" id="username" v-model="name">
        <label for="password">
            Password
        </label>
        <input type="text" id="password" v-model="password">
        <button @click="login">Login</button>
    </form>
</template>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';
import axios from 'axios';

@Component
export default class LoginForm extends Vue {
    name: string = '';
    password: string = '';


    loginUrl: string = '/api-auth/login/';
    logoutUrl: string = '';
    registerUrl: string = '';

    login() {
        axios.get(this.loginUrl, {
            params: {
                login: this.name,
                password: this.password,
            },
        })
    }

    logout() {

    }

    register() {

    }
};
</script>

<style scoped>

</style>