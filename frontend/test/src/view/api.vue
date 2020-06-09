<template>
  <div class="main">
    {{mmp}}
    <ops  class='ops' v-for="i in ops" :liuyang='myname' :ops='ops[i]' @messag="getval"></ops>
    <div><router-link to="/creapi">Create a New</router-link></div>
  </div>

</template>
<!-- 父传子，父代码中引用子组件，在子组件标签中自定义一个属性，等号左边视为属性，右边视为表达式（变量，函数等）
        子组件中使用prop并在其中添加子组件中的自定义属性后直接在父组件中填写表达式即可 -->

<script>
import Ops from '@/components/child.vue'
export default{
    name:'API',
    components:{
        Ops
    },
    data(){
        return{
          mmp:"eemmmm",
          myname:'lalala',
          ops:[1,2],
          kil:'gagagagguaguuewugaga'
        
        }

    },
    methods: {
      getval(val){
          alert(val)
      }
    },
    };

</script>

<style>

.main{
  height: 500px;
  
}
.ops{
  width: 200px;
  height: 200px;
  border-width: 1px;
  border-color: black;
  border-bottom-color:red;
  border-style: solid;
  border-top-style: dashed;
  padding: 10px 8px;
  border-radius: 20px;
  margin: 5% auto;
  /* text-align: center; */


}

</style>
