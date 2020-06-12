<template>
  <el-container>
    <el-aside width="200px">
      <el-menu
        mode="horizontal"
        background-color="#545c64"
        text-color="#fff"
        active-text-color="#ffd04b"
        @open="handleOpen"
        @close="handleClose"
      >
        <el-submenu index="1">
          <template slot="title">项目列表</template>
        </el-submenu>

        <el-submenu index="2">
          <template slot="title">其他</template>
        </el-submenu>
      </el-menu>
    </el-aside>

    <el-container>
      <!-- 顶部 -->
      <el-header>
        <el-form :inline="true" :model="form" ref="form" label-width="80px" class="prodGet clear">
          <el-form-item>
            <el-input v-model="form.name" placeholder="项目名称"></el-input>
          </el-form-item>
          <el-form-item>
            <el-button type="primary" @click="getPro">查询</el-button>
            <el-button type="primary" @click="dialogTableVisible=true">新建</el-button>
          </el-form-item>
        </el-form>
      </el-header>

      <el-main>
        <!-- 列表 -->
        <el-table :data="prodList" style="width: 100%">
          <el-table-column label="项目名称" width="180">
            <template slot-scope="scope">
              <i class="el-icon-time"></i>
              <router-link
                :to="{name:'ProdMenu',query:{product_id:scope.row.id}}"
                style="margin-left: 10px"
              >{{ scope.row.productName }}</router-link>
            </template>
          </el-table-column>
          <el-table-column label="版本" width="180">
            <template slot-scope="scope">
              <span>{{ scope.row.version }}</span>
            </template>
          </el-table-column>

          <el-table-column label="类型" width="180">
            <template slot-scope="scope">
              <span>{{ scope.row.productType }}</span>
            </template>
          </el-table-column>

          <el-table-column label="描述" width="180">
            <template slot-scope="scope">
              <span>{{ scope.row.desc }}</span>
            </template>
          </el-table-column>

          <el-table-column label="操作">
            <template slot-scope="scope">
              <el-button size="mini" @click="handleEdit(scope.$index,scope.row)">编辑</el-button>
              <el-button size="mini" type="danger" @click="handleDelete()">删除</el-button>
            </template>
          </el-table-column>
        </el-table>
      </el-main>
    </el-container>

    <!-- 新建 -->
    <el-dialog title="新建项目" :visible.sync="dialogTableVisible" @close="handleCancl()">
      <el-form :model="form" :rules="rules" ref="form">
        <el-form-item label="项目名称" :label-width="formLabelWidth" prop="productName">
          <el-input v-model="form.productName"></el-input>
        </el-form-item>
        <el-form-item label="版本" :label-width="formLabelWidth" prop="version">
          <el-input v-model.number="form.version"></el-input>
        </el-form-item>

        <el-form-item label="类型" :label-width="formLabelWidth" prop="productType">
          <el-select v-model="form.productType" placeholder="请选择类型">
            <el-option
              v-for="item in option "
              :label="item.label"
              :value="item.value"
              :key="item.label"
            ></el-option>
          </el-select>
        </el-form-item>
        <el-form-item label="项目描述" :label-width="formLabelWidth" prop="desc">
          <el-input type="textarea" v-model="form.desc" auto-complete="off"></el-input>
        </el-form-item>

        <el-form-item>
          <!-- <el-button @click="handleCancl('form')">取 消</el-button> -->
          <el-button type="primary" @click="submit('form') ">确 定</el-button>
        </el-form-item>
      </el-form>
    </el-dialog>

    <!-- 编辑 -->
    <el-dialog title="编辑项目" :visible.sync="edProButton" >
      <el-form :model="editform" :rules="rules" ref="editform">
        <el-form-item label="项目名称" :label-width="formLabelWidth" prop="productName">
          <el-input v-model="editform.productName" auto-complete="off"></el-input>
        </el-form-item>
        <el-form-item label="版本" :label-width="formLabelWidth" prop="version">
          <el-input v-model.number="editform.version" auto-complete="off"></el-input>
        </el-form-item>
        <el-form-item label="类型" :label-width="formLabelWidth" prop="productType">
          <el-select v-model="editform.productType" placeholder="请选择类型">
            <el-option
              v-for="item in option "
              :label="item.label"
              :value="item.value"
              :key="item.label"
            ></el-option>
          </el-select>
        </el-form-item>
        <el-form-item label="项目描述" :label-width="formLabelWidth" prop="desc">
          <el-input type="textarea" v-model="editform.desc" auto-complete="off"></el-input>
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click="edProButton = false">取 消</el-button>
        <el-button type="primary" @click="editsubmit('form')">确 定</el-button>
      </div>
    </el-dialog>
  </el-container>
</template>

<script>
export default {
  data() {
    return {
      prodList: [],
      option: [
        { label: "Web", value: "Web" },
        { label: "App", value: "App" }
      ],

      //表单提交数据
      form: {
        productName: "",
        version: "",
        productType: "",
        desc: ""
      },
      editform: {
        productName: "",
        version: "",
        productType: "",
        desc: ""
      },
      // 验证
      rules: {
        productName: [
          { required: true, message: "请输入项目名称", trigger: "blur" },
          { max: 50, message: "项目名称过长", trigger: "blur" }
        ],
        version: [{ required: true, message: "请输入版本", trigger: "blur" },
                  {type:'number',message:'请输入数字'}],
        productType: [
          { required: true, message: "请选择类型", trigger: "change" }
        ]
      },

      dialogTableVisible: false,
      crProButton: false,
      edProButton: false,
      formLabelWidth: "120px"
    };
  },
  mounted() {
    this.getProList();
  },
  computed: {
    id() {
      return this.$route.query.id
    }
  },
  methods: {
    getProList() {
      this.loaing = true;
      this.$axios.get("spo/product").then(res => {
        if (res.data.code === 200) {
          this.prodList = res.data.data.data;

          // this.productName = prodList.productName
          // this.version =prodList.version
          // this.productType = prodList.productType
          // this.desc =prodList.desc
        }
      });
    },
    submit(form) {
      this.$refs[form].validate(valid => {
        if (valid) {
          this.$axios({
            method: "post",
            url: "spo/Addprod",
            data: this.form
          }).then(res => {
            this.dialogTableVisible = false;
            this.$refs[form].resetFields();
            if (res.data.code === 200) {
              this.$message.success("Add Success");
            }

            this.getProList();
            // this.$router.push({
            //   path:''
            // })
          });
        } else {
          console.log("error submit!!");
          return false;
        }
      });
    },
    handleEdit(index, row) {
      this.edProButton = true;
      this.editform = Object.assign({}, row);
    },
    handleCancl(){
      this.$refs['form'].resetFields();
      
    },
    editsubmit(editform) {
      this.$refs['editform'].validate(valid => {
        if (valid) {
          this.$axios({
            method: "put",
            url: "spo/Editprod/" + this.editform.id,
            data: this.editform
          }).then(res => {
            this.edProButton = false;
            this.$refs['editform'].resetFields();
            if (res.data.code === 200) {
              this.$message.success("Add Success");
            }

            this.getProList();
            // this.$router.push({
            //   path:''
            // })
          });
        } else {
          console.log("error submit!!");
          return false;
        }
      });
    },
    handleDelete() {
      pass;
    },
    getPro() {
      pass;
    },

    handleOpen(key, keyPath) {
      pass;
    },
    handleClose(key, keyPath) {
      pass;
    }
  }
};
</script>


<style lang="css">
.prodGet {
  float: right;
  margin-top: 10px;
}
</style>