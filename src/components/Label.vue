<template>
    <div v-bind:style='style' class="label-widget" v-bind:class="labelClass" @click.stop="onClick && onClick()">
        <slot></slot>
    </div>
</template>

<script>
export default {
  props: {
    onClick: {
      type: Function,
      required: false
    },
    type: {
      type: String,
      required: false
    },
    wrap: {
      type: Boolean,
      required: false,
      default: false
    },
    weight: {
      type: String,
      required: false
    },
    minWidth: {
      type: String,
      required: false
    },
    fontSize: {
      type: String,
      required: false
    },
    align: {
      type: String,
      required: false
    },
    margin: {
      type: String,
      required: false
    },
    padding: {
      type: String,
      required: false
    },
    display: {
      type: String,
      required: false
    },
    color: {
      type: String,
      required: false
    },
    lineHeight: {
      type: String,
      required: false
    },
    verticalAlign: {
      type: String,
      required: false
    }
  },
  computed: {
    style: function() {
      return {
        "display": this.display || "",
        "min-width": this.minWidth || "",
        "width": this.width || "",
        "margin": this.margin || "",
        "padding": this.padding || "",
        "line-height": this.lineHeight || "",
        "white-space": this.wrap ? "normal" : "nowrap",
        "font-weight": this.weight || "",
        "font-size": this.fontSize || "",
        "text-align": this.align || "",
        "color": this.color || "",
        // "text-decoration": this.onClick ? "underline" : "",
        "cursor": this.onClick ? "pointer" : "",
        "vertical-align": this.verticalAlign || "",
        "user-select": this.onClick ? "none" : ""
      };
    },
    labelClass: function() {
      return "label-widget " + (this.type || "lbl-grey");
    }
  }
};
</script>

<style lang="scss" scoped>
.label-widget {
  font-size: 16px;
  line-height: 1.5em;
  font-family: Roboto;
  text-align: justify;
  color: #8fa4af;
  border: none;
  vertical-align: middle;
  text-overflow: ellipsis;
  overflow: hidden;
  &.no-data {
    display: block;
    margin: 30px 0;
    text-align: center;
    font-weight: bold;
  }
  &.lbl-grey {
    color: #8fa4af;
  }
  &.lbl-form-error {
    display: block;
    padding: 10px 0 5px 0;
    margin: 0;
    font-size: 14px;
    color: #d54b4b;
  }
  &.lbl-form-success {
    display: block;
    padding: 10px 0 5px 0;
    margin: 0;
    font-size: 14px;
    color: #19b19f;
  }
  &.lbl-error {
    background-color: #ff6363;
    border: solid 2px #ffffff;
    border-radius: 100px;
    box-sizing: border-box;
    line-height: 2;
    height: 37px;
    width: 307px;
    color: #ffffff;
    display: inline-block;
  }
  &.lbl-roboto-regular {
    font-family: Roboto-Regular;
  }
  &.lbl-roboto-bold {
    font-family: Roboto-Bold;
  }
  &.lbl-morebi {
    color: #8fa4af;
    font-family: MorebiRounded-Medium;
  }
  &.lbl-hybrid {
    width: auto;
    display: inline-block;
    text-align: center;
    line-height: normal;
    font-size: 20px;
    font-family: MorebiRounded-Medium;
    color: #3db8f7;
  }
  &.lbl-sativa {
    width: auto;
    display: inline-block;
    text-align: center;
    line-height: normal;
    font-size: 20px;
    font-family: MorebiRounded-Medium;
    color: #f5a032;
  }
  &.lbl-indica {
    width: auto;
    display: inline-block;
    text-align: center;
    line-height: normal;
    font-size: 20px;
    font-family: MorebiRounded-Medium;
    color: #8a4e9c;
  }
  &.lbl-cbd {
    width: auto;
    display: inline-block;
    text-align: center;
    line-height: normal;
    font-size: 20px;
    font-family: MorebiRounded-Medium;
    color: #f74a8b;
  }
  &.stamp-hybrid {
    width: 80px;
    text-align: center;
    color: white;
    line-height: normal;
    border-radius: 4px;
    padding: 3px 12px 2px 12px;
    font-family: MorebiRounded-Medium;
    font-size: 10px;
    background: #3db8f7;
  }
  &.stamp-sativa {
    width: 30px;
    text-align: center;
    color: white;
    line-height: normal;
    border-radius: 4px;
    padding: 3px 12px 2px 12px;
    font-family: MorebiRounded-Medium;
    font-size: 10px;
    background: #f5a032;
  }
  &.stamp-indica {
    width: 30px;
    text-align: center;
    color: white;
    line-height: normal;
    border-radius: 4px;
    padding: 3px 12px 2px 12px;
    font-family: MorebiRounded-Medium;
    font-size: 10px;
    background: #8a4e9c;
  }
  &.stamp-cbd {
    width: 25px;
    text-align: center;
    color: white;
    line-height: normal;
    border-radius: 4px;
    padding: 3px 12px 2px 12px;
    font-family: MorebiRounded-Medium;
    font-size: 10px;
    background: #f74a8b;
  }
}
</style>
