<template>
  <el-container>
    <el-header>
      <Menu></Menu>
    </el-header>
    <el-main>
        <router-view></router-view>
    </el-main>
  </el-container>
</template>
<script>
import menu from "./menu";
export default {
  components: {
    Menu: menu
  }
};
</script>