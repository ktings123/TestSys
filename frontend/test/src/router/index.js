import Vue from 'vue'
import Router from 'vue-router'



import layout from '../components/layout.vue'


Vue.use(Router)
const originalPush = Router.prototype.push
Router.prototype.push = function push (location) {
  return originalPush.call(this, location).catch(err => err)
}

export default new Router({
  routes: [
    {
      path:'/Productlist',
      name:'Productlist',
      component:()=>import('../view/Productlist.vue'),
      
    },
    {
      path:'/Productlist',
      name:'ProdMenu',
      component:layout,
      children:[
        {path:'/ProductDetail',name:'ProductInfo', component:()=>import ('../view/ProductInfo.vue'),},
        {path:'/api',name:'api', component:()=>import ('../components/apiModel.vue'),
          children:[
          {path:"/apiList",name:'apiList',component:()=>import ('../view/apiList.vue')},
          {path:"/AddApi",name:'AddApi',component:()=>import ('../view/addApi.vue')}
        ]
      },
       
      ],
    },
   
  ]
})
