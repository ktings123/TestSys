<template>
  <div class="main" style="height:100vh">
    <el-row :gutter="6">
      <el-col :span="6">
        <el-card class="box-card">
          <h1>{{productName}}</h1>
          <div>项目名称</div>
        </el-card>
      </el-col>

      <el-col :span="6">
        <el-card class="box-card">
          <h1>{{version}}</h1>
          <div>版本</div>
        </el-card>
      </el-col>

      <el-col :span="6">
        <el-card class="box-card">
          <h1><router-link :to="{name:'api'}">2</router-link></h1>
          <div>接口相关</div>
        </el-card>
      </el-col>

      <el-col :span="6">
        <el-card class="box-card">
          <h1>{{productType}}</h1>
          <div>项目类型</div>
        </el-card>
      </el-col>
    </el-row>

    <el-row :gutter="6">
      <el-col :span="6">
        <el-card class="box-card">
          <h1>{{desc}}</h1>
          <div>备注信息</div>
        </el-card>
      </el-col>

      <el-col :span="6">
        <el-card class="box-card">
          <h1></h1>
          <div>项目组成员</div>
        </el-card>
      </el-col>

    </el-row>
  </div>
</template>

<script>
export default {
  data() {
    return {
      tableData: null,
      productName: "",
      version: "",
      productType: "",
      desc: ""
    };
  },
  mounted() {
    this.getDetail();
  },
  computed: {
    prd_id() {
      return this.$route.query.product_id;
    }
  },
  methods: {
    getDetail() {
      this.loading = true;
      this.$axios.get("/spo/product/" + this.prd_id).then(res => {
        if (res.data.code === 200) {
          let resp = res.data.data.data;
          this.requestParameterType;
          this.productName = resp.productName;
          this.version = resp.version;
          this.productType = resp.productType;
          this.desc = resp.desc;
        }
      });
    },
    handleOpen(key, keyPath) {
      console.log(key, keyPath);
    },
    handleClose(key, keyPath) {
      console.log(key, keyPath);
    }
  }
};
</script>
<style lang="css">
.el-icon-message {
  background: #dcdfe6;
}
.main {
  margin: 20px;
}
</style>