import Vue from 'vue'
import Router from 'vue-router'



import Productlist from '../view/Productlist.vue'
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
      component:Productlist,
      
    },
    {
      path:'/Productlist',
      name:'ProdMenu',
      component:layout,
      children:[
        { path:'/ProductDetail',name:'ProductInfo', 
          component:()=>import ('../view/ProductInfo.vue'),
          
          children:[
            
          ]
        },
        {path:'/api',name:'api', component:()=>import ('../view/api.vue')}
      ],
    },
   
  ]
})
