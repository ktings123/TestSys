import axios from 'axios'
import router from '../router/index.js'
import qs from 'qs'
var instance =axios.create({
    baseURL:process.env.API,
    timeout:50000,
    // Headers:{'Content-Type':'application/x-www-form-urlencoded'}
})

// 请求拦截
instance.interceptors.request.use(config=>{

    if(config.method  === 'post'){
        config.data = qs.stringify(config.data);
    }
    return config;
    },(error) =>{
    console.log('错误的传参')
    return Promise.reject(error);
    // let Token = window.localStorage.getItem('token')
    // if (router.currentRoute.fullPath.indexOf('customAuthorization') > -1) {
    //   var referrer = document.referrer
    //   if (referrer.indexOf('?') > -1) {
    //     config.headers.customReferer = referrer + '&customAuthorization=' + router.app._route.query.customAuthorization
    //   } else {
    //     config.headers.customReferer = referrer + '?customAuthorization=' + router.app._route.query.customAuthorization
    //   }
  
    //   if (Token) {
    //     window.localStorage.removeItem('token')
    //     window.localStorage.removeItem('user')
    //     window.localStorage.removeItem('menus')
    //   }
    // }
  
    // if (Token) {
    //   config.headers.Authorization = Token
    // } else {
    //   config.headers.Authorization = ''
    // }
  
    // return config
})

// 响应拦截
instance.interceptors.response.use(res=>{
    if(!res.data.success){
        return Promise.resolve(res)

    }
    return res
},error=>{
    console.log('...')
    return Promise.reject(error)
})

export default instance