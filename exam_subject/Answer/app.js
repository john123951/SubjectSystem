//app.js
App({
  onLaunch: function () {
    var self = this;
    wx.getStorage({
      key: 'token',
      success(res) {
        console.log(res.data)
        self.globalData.token = res.data
      }, fail() {
        //登录用户
        wx.login({
          success(res) {
            console.log(res.code)
            wx.request({
              url: 'http://127.0.0.1:8000/wx_login/', // 仅为示例，并非真实的接口地址
              data: {
                code: res.code
              },
              method: "post",
              header: {
                'content-type': 'application/json' // 默认值
              },
              success(res) {
                console.log(res.data.token)
                wx.setStorage({
                  key: 'token',
                  data: res.data.token
                })
                self.globalData.token = res.data.token
              }
            })
          }
        })
      }
    })
  },
  globalData: {
    userInfo: null,
    token:""
  }
})