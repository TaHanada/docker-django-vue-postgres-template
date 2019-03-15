<template>
    <button v-bind:type="type" class="button-widget" v-bind:class="buttonClass" v-bind:style="style" v-on:click="onClick && onClick()">{{ label }}</button>
</template>

<script>
export default {
  props: {
    label: {
      type: String,
      required: true
    },
    buttonClass: {
      type: String,
      required: false
    },
    onClick: {
      type: Function,
      required: false
    },
    margin: {
      type: String,
      required: false
    },
    type: {
      type: String,
      required: false,
      default: "button"
    }
  },
  data() {
    return {
      style: {
        margin: this.margin
      }
    };
  }
};
</script>

<style lang="scss" scoped>
// .button-widget {
//   display: inline-block;
//   margin: 0 5px;
//   padding: 5px 50px;
//   font-size: 14px;
//   font-family: Roboto;
//   text-align: center;
//   color: white;
//   border: none;
//   border-radius: 14px;
//   vertical-align: middle;
//   white-space: nowrap;
//   cursor: pointer;
//   &.modal-green {
//     background: #008540;
//   }
//   &.modal-red {
//     background: #e76968;
//   }
//   &.modal-gold {
//     background: #ef9a34;
//   }
//   &.btn-green {
//     background: #24b5a4;
//   }
//   &.btn-green-bordered {
//     min-width: 0px;
//     margin-top: 5px;
//     background: #24b5a4;
//     font-size: 14px;
//     border: 1px solid #157a6d;
//     border-radius: 20px;
//   }
// }
</style>
