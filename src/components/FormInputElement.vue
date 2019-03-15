<template>
<div class="form-input-element">
    <label>{{ title }} <strong>{{ titleStrong }}</strong></label>
    <input :id="id" :autocomplete="autocomplete" v-bind:name="name" v-bind:placeholder="placeholder" v-bind:value="value" v-on:input="$emit('input', $event.target.value)" v-bind:type="type" v-bind:readonly="readonly" v-bind:required="required" />
    <Label v-if="errors && errors[0]" type="lbl-form-error">{{errors && errors[0]}}</Label>
</div>
</template>

<script>
import Label from '../components/Label.vue'

export default {
    components: {
        Label
    },
    props: {
        id: {
            type: [String, Number],
            required: false,
            default: null
        },
        autocomplete: {
            type: String,
            required: false,
            default: "off"
        },
        title: {
            type: String,
            required: false
        },
        titleStrong: {
            type: String,
            required: false
        },
        value: {
            type: String,
            required: true
        },
        value: {
            type: String,
            required: true
        },
        name: {
            type: String,
            required: false
        },
        placeholder: {
            type: String,
            required: false
        },
        type: {
            type: String,
            required: false,
            default: "text"
        },
        readonly: {
            type: Boolean,
            required: false,
            default: false
        },
        required: {
            type: Boolean,
            required: false,
            default: false
        },
        errors: {
            type: Array,
            required: false,
            default: null
        }
    },
    data() {
        return {};
    }
};
</script>

<style lang="scss" scoped>
// .form-input-element {
//     margin-bottom: 10px;
//     padding: 9px 17px 9px;
//     background: #ffffff;
//     border: 2px solid #ebebeb;
//     box-shadow: 0 0 5px 0 rgba(210, 212, 217, 0.55);
//     border-radius: 4px;
//     box-shadow: none;
//     label {
//         padding: 0 0 5px 0;
//         border-bottom: 2px solid #ebebeb;
//         display: block;
//         margin-bottom: 5px;
//         font-size: 14px;
//         color: #008540;
//         line-height: 16px;
//     }
//     input {
//         width: 100%;
//         font-size: 16px;
//         color: #757575;
//         background: none;
//         border: none;
//         outline: none;
//     }
// }
</style>
