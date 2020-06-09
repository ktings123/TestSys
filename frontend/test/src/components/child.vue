<template>
    <div>
        <h3>{{liuyang}}{{ops}}</h3>
        <button @click="getNum">{{'comf'}}</button>
        <creaApi :apiname='liuyang'></creaApi>

    </div>
</template>

<script>
import creaApi from "@/view/creaApi.vue"
export default {
    name:'Opss',
    components:{
        creaApi
    },
    props:{
            liuyang:{
                type:String,
                default:''
            },
            ops:{}
    },
    data() {
        return {
            i:'Hellow',
            tocity:'Canton',



        }
    },
    methods: {
        getNum(){
            this.$emit("messag",this.i);
        },
        getfath(){

        }
    },
}
</script>

<style lang="css">

</style>
