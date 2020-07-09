<template>
  <div>
    <el-form :inline="true" label-width="80px" class="prodGet clear">
      <el-form-item>
        <el-input placeholder="项目名称"></el-input>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="select('form')">查询</el-button>

        <router-link :to="{name:'AddApi',query:{product_id:$route.query.product_id}}">
          <el-button type="primary" @click="dialogTableVisible=true">新建</el-button>
        </router-link>
      </el-form-item>
    </el-form>
    <el-table style="width: 100%" class="prodGet clear">
      <el-table-column
        v-for="col in columns"
        :prop="col.prop"
        :key="col.index"
        :label="col.label"
        :width="col.width"
      ></el-table-column>
    </el-table>
  </div>
</template>
<!-- 父传子，父代码中引用子组件，在子组件标签中自定义一个属性，等号左边视为属性，右边视为表达式（变量，函数等）
        子组件中使用prop并在其中添加子组件中的自定义属性后直接在父组件中填写表达式即可 -->

<script>
export default {
  data() {
    return {
      dialogTableVisible: false,
      formLabelWidth: "120px",
      columns: [
        { prop: "name", width: "180", label: "接口名称" },
        { prop: "requestType", width: "180", label: "请求方式" },
        { prop: "apiUrl", width: "180", label: "接口地址" },
        { prop: "requestParameter", width: "180", label: "参数" },
        { prop: "status", width: "180", label: "状态" }
      ]
    };
  },
  methods: {
    select(form) {
     pass
    },
    handleCancl() {
      this.$refs["form"].resetFields();
    },
    getPro() {
      pass;
    }
  }
};
</script>

<style>
.main {
  height: 500px;
}
.prodGet {
  float: right;
  margin-top: 10px;
}
.ops {
  width: 200px;
  height: 200px;
  border-width: 1px;
  border-color: black;
  border-bottom-color: red;
  border-style: solid;
  border-top-style: dashed;
  padding: 10px 8px;
  border-radius: 20px;
  margin: 5% auto;
  /* text-align: center; */
}
</style>
