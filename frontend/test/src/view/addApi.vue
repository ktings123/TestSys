<template>
  <div>
    
    <router-link :to="{name:'apiList',query:{product_id:this.$route.query.product_id}}">
      <el-button class='return-list-button'>
        <i class="el-icon-d-arrow-left" style="margin-right: 5px"></i>Back!</el-button>
    </router-link>
    <el-form :model="form" ref="form">
      <el-form-item label="接口名称" :label-width="formLabelWidth" prop="name">
        <el-input v-model="form.name"></el-input>
      </el-form-item>
      <el-row>
        <el-col :span="7">
          <el-form-item label="URL：" :label-width="formLabelWidth" prop="httpType">
            <el-select v-model="form.httpType" placeholder="请选择类型">
              <el-option
                v-for="item in protocol "
                :label="item.label"
                :value="item.value"
                :key="item.label"
              ></el-option>
            </el-select>
          </el-form-item>
        </el-col>

        <el-col :span="5">
          <el-form-item prop="requestType">
            <el-select v-model="form.requestType" placeholder="请选择类型">
              <el-option
                v-for="item in option "
                :label="item.label"
                :value="item.value"
                :key="item.label"
              ></el-option>
            </el-select>
          </el-form-item>
        </el-col>

        <el-col :span="12">
          <el-form-item prop="apiUrl">
            <el-input
              v-model="form.apiUrl"
              placeholder="地址"
              :label-width="formLabelWidth"
              auto-complete="off"
            ></el-input>
          </el-form-item>
        </el-col>
      </el-row>
      <el-row>
        <el-col :span="7">
          <el-form-item label="Header:" :label-width="formLabelWidth" prop="head">
            <el-select v-model="form.header.name" placeholder="请选择标签">
              <el-option
                v-for="item in head "
                :label="item.label"
                :value="item.value"
                :key="item.label"
              ></el-option>
            </el-select>
          </el-form-item>
        </el-col>
        <el-col :span="16">
          <el-form-item :label-width="formLabelWidth" prop="value">
            <el-input v-model="form.header.value" placeholder="输入head" auto-complete="off"></el-input>
          </el-form-item>
        </el-col>
      </el-row>

      <el-form-item label="请求参数：" :label-width="formLabelWidth" prop="desc">
        <el-row :span="24">
          <el-col :span="8">
            <el-radio v-model="form.requestParameterType" label="form-data">表单form-data</el-radio>
          </el-col>
          <el-col :span="4">
            <el-radio v-model="form.requestParameterType" label="raw">源raw</el-radio>
          </el-col>
        </el-row>

        <el-table :data="form.requestParameter" border stripe>
          <el-table-column prop="name" label="参数名">
            <template slot-scope="scope">
              <el-input v-model="scope.row.name" placeholder="参数名"></el-input>
            </template>
          </el-table-column>
          <el-table-column prop="value" label="参数值">
            <template slot-scope="scope">
              <el-input v-model="scope.row.value" placeholder="参数值"></el-input>
            </template>
          </el-table-column>
        </el-table>
      </el-form-item>

      <el-form-item label="项目描述" :label-width="formLabelWidth" prop="desc">
        <el-input type="textarea" v-model="form.desc" auto-complete="off"></el-input>
      </el-form-item>

      <el-form-item>
        <!-- <el-button @click="handleCancl('form')">取 消</el-button> -->
        <el-button type="primary" @click="submit('form') ">确 定</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>
<script>
export default {
  data() {
    return {
      formLabelWidth: "120px",
      head: [
        { value: "Accept", label: "Accept" },
        { value: "Accept-Charset", label: "Accept-Charset" },
        { value: "Accept-Encoding", label: "Accept-Encoding" },
        { value: "Accept-Language", label: "Accept-Language" },
        { value: "Accept-Ranges", label: "Accept-Ranges" },
        { value: "Authorization", label: "Authorization" }
      ],
      protocol: [
        { label: "POST", value: "post" },
        { label: "GET", value: "get" },
        { label: "PUT", value: "put" },
        { label: "DELETE", value: "delete" }
      ],
      option: [
        { label: "Web", value: "Web" },
        { label: "App", value: "App" }
      ],
      form: {
        name: "",
        header: [
          {
            name: "",
            vaule: ""
          }
        ],
        httpType: "",
        requestType: "",
        apiUrl: "",
        requestParameterType: "raw",
        requestParameter: [
          {
            name: "",
            value: ""
          }
        ],
        responseParameter: "",
        status: "",
        productId: this.$route.query.product_id
      }
    };
  },
  methods: {
    submit() {}
  }
};
</script>
<style lang="css">
  .return-list-button{
    margin-top: 0px;
        margin-bottom: 10px;
        border-radius: 25px;
  }
</style>