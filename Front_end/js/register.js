import { Vue } from "https://cdn.jsdelivr.net/npm/vue@2.6.14/dist/vue.js";
var application = new Vue.Vue({
    el: '#app',
    data: {
        account: '',
        password: '',
        confirmPassword: '',
        email: '',
        phone: '',
        address: '',
        gender: 'none',
    },
    methods: {
        onSubmit() {
            if (this.password !== this.confirmPassword) {
                alert('密碼不相同')
            } else {
                alert('' + this.account)
            }
        },
    },
})