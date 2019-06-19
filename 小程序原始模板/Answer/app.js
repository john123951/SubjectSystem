//app.js
App({
  onLaunch: function () {
    var self = this;
    wx.getStorage({
      
      // 获取缓存的key（token）
      key: 'token',
      success(res) {
        console.log(res.data)
        self.globalData.token = res.data
      },

      // 获取不到缓存的token，登录用户
       fail() {
        //登录用户
        wx.login({
          success(res) {
            console.log(res.code)
            wx.request({
              url: 'http://127.0.0.1:8000/wx_login/',

              data: {
                // 传递code给后台
                code: res.code
              },

              method: "post",
              header: {
                'content-type': 'application/json'
              },
              success(res) { 

                // 登录成功
                console.log(res.data.token)
                wx.setStorage({

                  // 登录成功设置token到缓存
                  key: 'token',  //本地缓存中指定的 key
                  data: res.data.token  //data：key对应的内容
                })

                // token存储到globalData
                self.globalData.token = res.data.token
              }
            })
          }
        })
      }
    })
  },

  // 存储token
  globalData: {
    userInfo: null,
    token:""
  }
})