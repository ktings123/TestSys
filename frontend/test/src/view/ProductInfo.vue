<template>
  <div class="main" style="height:100vh">
    <el-row :gutter="6">
      <el-col :span="6">
        <el-card class="box-card">
          <h1>111</h1>
          <div>项目名称</div>
        </el-card>
      </el-col>

      <el-col :span="6">
        <el-card class="box-card">
          <h1>111</h1>
          <div>版本</div>
        </el-card>
      </el-col>

      <el-col :span="6">
        <el-card class="box-card">
          <h1></h1>
          <div>接口相关</div>
        </el-card>
      </el-col>

      <el-col :span="6">
        <el-card class="box-card">
          <h1></h1>
          <div>项目类型</div>
        </el-card>
      </el-col>
    </el-row>

    <el-row :gutter="6">
      <el-col :span="6">
        <el-card class="box-card">
          <h1>111</h1>
          <div>备注信息</div>
        </el-card>
      </el-col>

      <el-col :span="6">
        <el-card class="box-card">
          <h1></h1>
          <div>项目组成员</div>
        </el-card>
      </el-col>

      <!-- <el-col :span="6">
        <el-card class="box-card">
          <h1></h1>
          <div></div>
        </el-card>
      </el-col>

      <el-col :span="6">
        <el-card class="box-card">
          <h1></h1>
          <div></div>
        </el-card>
      </el-col> -->
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
    // this.getList();
  },
  computed: {
    prd_id() {
      return this.$route.query.product_id;
    }
  },
  methods: {
    getList() {
      this.loading = true;
      this.$axios.get("/spo/api/" + this.prd_id).then(res => {
        if (res.data.code === 200) {
          let resp = res.data.data.data;
          console.log(resp);
          this.requestParameterType;
          this.name = resp.name;
          this.httpType = resp.httpType;
          this.requestType = resp.requestParameterType;
          this.baseUrl = resp.baseUrl;
          this.apiUrl = resp.apiUrl;
          this.requestParameter = resp.requestParameterType;
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