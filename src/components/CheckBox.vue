<template>
<div class="check-box" v-bind:style="style" v-bind:class="{'check-box--inline': inline}">
    <span class="__checkbox __green __with__text" v-bind:class="{'checked': isChecked}">
        <input v-bind:value="value" v-on:click="onClick()" v-bind:type="type" v-bind:id="id" v-bind:name="name" />
    </span>
    <label v-bind:for="id" v-bind:title="name" class="check-box-label">{{ name }}</label>
</div>
</template>

<script>
export default {
    props: {
        id: {
            type: [String, Number],
            required: true
        },
        name: {
            type: String,
            required: true
        },
        value: {
            required: true
        },
        type: {
            type: String,
            required: false,
            default: "checkbox"
        },
        inline: {
            type: Boolean,
            required: false,
            default: false
        },
        width: {
            type: String,
            required: false
        }
    },
    computed: {
        style: function () {
            return {
                width: this.width || ""
            };
        },
        isChecked: function () {
            if (this.type === "radio") {
                return (
                    this.value === this.id || (this.id === "all" && this.value === null)
                );
            } else {
                if (!this.value) {
                    if (this.id === "all") {
                        return true;
                    }
                    return false;
                }
                return (
                    this.value.includes(this.id) ||
                    (this.id === "all" && this.value.length === 0)
                );
            }
        }
    },
    methods: {
        onClick() {
            if (this.type === "radio") {
                // HANDLE RADIO BUTTON
                if (this.id === "all") {
                    this.$emit("input", null);
                } else {
                    this.$emit("input", this.id);
                }
            } else {
                // HANDLE CHECKBOX
                if (this.id === "all") {
                    // remove all values
                    this.$emit("input", null);
                } else {
                    let value = this.value ? this.value.slice(0) : []; // copy so we dont mutate directly
                    // toggle checkbox
                    if (value.includes(this.id)) {
                        value.splice(value.indexOf(this.id), 1);
                    } else {
                        value.push(this.id);
                    }
                    this.$emit("input", value); // emit the new value.
                }
            }
        },

        test(){
            return "SAdasdsa"
        }
    }
};
</script>

<style lang="scss" scoped>
.check-box {
    margin: 0 0 5px 0;
    .__checkbox.__green {
        position: relative;
        display: inline-block;
        width: 20px;
        height: 20px;
        background: #e9eff2;
        vertical-align: middle;
        border: 1px solid #8ea4b0;
        border-radius: 3px;
        &.checked {
            background: #9ecb6c;
            border: 1px solid #137a6e;
            &:before {
                content: "";
                display: block;
                width: 9px;
                height: 9px;
                background: url(/assets/img/forms/checkmark.png) no-repeat center center;
                position: absolute;
                left: 50%;
                top: 50%;
                margin-top: -20%;
                margin-left: -20%;
            }
        }
    }
    input {
        position: absolute;
        left: 0;
        top: 0;
        width: 100%;
        height: 100%;
        opacity: 0;
        z-index: 10;
    }
    .check-box-label {
        width: calc(100% - 36px);
        overflow: hidden;
        font-size: 14px;
        white-space: nowrap;
        display: inline-block;
        text-overflow: ellipsis;
        vertical-align: middle;
        color: #8fa4af;
    }
}

.__checkbox.__with__text {
    margin-right: 10px;
}

.check-box--inline {
    display: inline-block;
    margin-right: 10px;
}
</style>
