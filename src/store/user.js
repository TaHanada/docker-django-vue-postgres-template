import localStorage from '../service/local-storage-service'
import axios from 'axios'
import { URLS } from '../constants'

const state = {
    user: {},
    isUserLoggedIn: null,
    token: ""
}

const getters = {
    user: function() {
        return state.user
    },
    isUserLoggedIn: function() {
        return state.isUserLoggedIn
    },
    token: function() {
        return state.token
    },
}

const actions = {
    login(context, user) {
        return axios.post(URLS.api + "auth/login/", {
            username: user.username,
            password: user.password
        })
    },
    // refreshSubscriber(context) {
    //     return axios.get(URLS.api + "cis/subscribers/");
    // }
}

const mutations = {
    initialiseStore() {
        state.isUserLoggedIn = (localStorage.get("userAuthData") != null);

        if (state.isUserLoggedIn) {
            state.user = JSON.parse(localStorage.get("userAuthData"));
            state.token = state.user.token;
            // state.subscriber = state.user.subscriber;
        }
    },
    setUser(state, userData) {
        if (typeof userData.token != "undefined" && userData.token != null) {
            var userStorageObject = localStorage.get("userAuthData");

            if (!userStorageObject) {
                userStorageObject = {
                    // id: userData.user.id,
                    token: userData.token,
                    // email: userData.user.email,
                    // first_name: userData.user.first_name,
                    // last_name: userData.user.last_name,
                    // address: userData.user.address,
                    // sex: userData.user.sex,
                    // age: userData.user.age,
                    // terms_agreement: userData.user.terms_agreement,
                    // loyalty_agreement: userData.user.loyalty_agreement || false,
                    // profile_setup: userData.user.profile_setup,
                    // // balance: userData.loyalty.balance,
                    // location: userData.user.location || null,
                    // device: userData.user.device || null,
                    // groups: userData.user.groups,
                    // cis: (typeof userData.cis != 'undefined') ? userData.cis : null,
                    // has_local: (typeof userData.has_local != 'undefined') ? userData.has_local : false,
                    // settings: {
                    //     feedback_sleep_time: userData.user.feedback_sleep_time,
                    //     feedback_inhale_time: userData.user.feedback_inhale_time,
                    //     feedback_ingestion_time: userData.user.feedback_ingestion_time,
                    //     feedback_portable_time: userData.user.feedback_portable_time,
                    //     feedback_tincture_time: userData.user.feedback_tincture_time,
                    //     feedback_transdermal_time: userData.user.feedback_transdermal_time
                    // },
                    // subscriber: userData.subscriber
                };
                localStorage.set("userAuthData", JSON.stringify(userStorageObject));
            }
        }
    },
    // refreshSubscriber(state, subscriber) {
    //     state.user.subscriber = subscriber;
    //     state.subscriber = subscriber;
    //     localStorage.set("userAuthData", JSON.stringify(state.user));
    // },
    logout() {
        console.log("Removing userAuthData from localStorage")
        localStorage.remove("userAuthData");
    }
}

export default {
    namespaced: true,
    state,
    mutations,
    actions,
    getters
}