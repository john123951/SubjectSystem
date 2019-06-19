
const app = getApp()
Page({

  /**
   * 页面的初始数据
   */
  data: {
    items:[],
  },
  static:{
    token: ""
  },
  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    var self = this;
    wx.getStorage({
      key: 'token',
      success(res) {
        console.log(res.data)
        self.static.token = res.data.token
      }
    })

    //获取token值
    wx.request({
      url: 'http://127.0.0.1:8000/categorys/', // 仅为示例，并非真实的接口地址
      header: {
        'content-type': 'application/json' // 默认值
      },
      success(res) {
        var items_list = []
        console.log(res.data[0])
        for (var i = 0; i < res.data[0]["sub_cat"].length;i++){
          items_list.push(res.data[0]["sub_cat"][i])
          // console.log(items_list)
        }
        self.setData({
          items: items_list,
        })
        console.log(self.data.items)
        
      }
    })
  },
  //开始授权
  clickBtap(e){  
    console.log(e)
    var token = app.globalData.token

    var self = this;
    // console.log(self.static.token)
      wx.redirectTo({
        url: '../examtips/examtips?type=' + e.currentTarget.id + "&token=" + token,
      })

  },

  /**
   * 生命周期函数--监听页面初次渲染完成
   */
  onReady: function () {
    
  },

  /**
   * 生命周期函数--监听页面显示
   */
  onShow: function () {
    
  },

  /**
   * 生命周期函数--监听页面隐藏
   */
  onHide: function () {
    
  },

  /**
   * 生命周期函数--监听页面卸载
   */
  onUnload: function () {
    
  },

  /**
   * 页面相关事件处理函数--监听用户下拉动作
   */
  onPullDownRefresh: function () {
    
  },

  /**
   * 页面上拉触底事件的处理函数
   */
  onReachBottom: function () {
    
  },

  /**
   * 用户点击右上角分享
   */
  onShareAppMessage: function () {
    
  },
  
})