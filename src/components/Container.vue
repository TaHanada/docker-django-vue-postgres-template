<template>
    <div v-bind:id="id" v-bind:class="containerClass" v-bind:style="style" v-on:click="onClick && onClick()">
        <slot></slot>
    </div>
</template>
<script>
export default {
  props: {
    id: {
      type: String,
      required: false
    },
    minWidth: {
      type: String,
      required: false
    },
    minHeight: {
      type: String,
      required: false
    },
    width: {
      type: String,
      required: false
    },
    height: {
      type: String,
      required: false
    },
    maxWidth: {
      type: String,
      required: false
    },
    maxHeight: {
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
    float: {
      type: String,
      required: false
    },
    display: {
      type: String,
      required: false
    },
    flexWrap: {
      type: String,
      required: false
    },
    justifyContent: {
      type: String,
      required: false
    },
    alignItems: {
      type: String,
      required: false
    },
    alignContent: {
      type: String,
      required: false
    },
    order: {
      type: String,
      required: false
    },
    flexGrow: {
      type: String,
      required: false
    },
    alignSelf: {
      type: String,
      required: false
    },
    position: {
      type: String,
      required: false
    },
    top: {
      type: String,
      required: false
    },
    left: {
      type: String,
      required: false
    },
    background: {
      type: String,
      required: false
    },
    zIndex: {
      type: String,
      required: false
    },
    overflow: {
      type: String,
      required: false
    },
    className: {
      type: String,
      required: false
    },
    flexDirection: {
      type: String,
      required: false
    },
    align: {
      type: String,
      required: false
    },
    textAlign: {
      type: String,
      required: false
    },
    verticalAlign: {
      type: String,
      required: false
    },
    borderRadius: {
      type: String,
      required: false
    },
    onClick: {
      type: Function,
      required: false
    }
  },
  computed: {
    style: function() {
      return {
        "display": this.display || "block",
        "min-width": this.minWidth || "",
        "min-height": this.minHeight || "",
        "width": this.width || "",
        "max-width": this.maxWidth || "",
        "height": this.height || "",
        "max-height": this.maxHeight || "",
        "margin": this.margin || "",
        "padding": this.padding || "",
        "float": this.float || "",
        "flex-wrap": this.flexWrap || "nowrap",
        "justify-content": this.justifyContent || "",
        "align-items": this.alignItems || "",
        "align-content": this.alignContent || "",
        "vertical-align": this.verticalAlign || "",
        "flex-direction": this.flexDirection || "",
        "order": this.order || "",
        "flex-grow": this.flexGrow || "",
        "align-self": this.alignSelf || "",
        "position": this.position || "",
        "top": this.top || "",
        "left": this.left || "",
        "background": this.background || "",
        "z-index": this.zIndex || "",
        "overflow": this.overflow || "",
        "border-radius": this.borderRadius || "",
        "text-align": this.textAlign || ""
      };
    },
    containerClass: function(){
        return this.className ? ('container-widget ' + this.className) : 'container-widget';;
    }
  }
};
</script>
<style lang="scss" scoped>
.container-widget {
  position: relative;
}
</style>
