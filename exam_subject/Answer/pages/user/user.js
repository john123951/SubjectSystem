// pages/user/user.js
import '../../utils/wxcharts-min.js'
const app = getApp()
Page({
  /**
   * 页面的初始数据
   */
  data: {
    right_num:0,
    wrong_num:0,
    user_subject_sum_nums:0
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    this.userinfo()
    var self = this;


  },




  //登录用户
  userLogin() {
    //登录用户
    var self = this;
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
            app.globalData.token = res.data.token
            self.userinfo()
          }
        })
      }
    })

  },
  //获取用户信息
  userinfo() {
    var self = this;
    wx.request({
      url: 'http://127.0.0.1:8000/usertf/',
      data: {
      }, // 仅为示例，并非真实的接口地址
      header: {
        // 'content-type': 'application/json', // 默认值
        'Authorization': "JWT " + app.globalData.token
      },
      method: "get",
      success(res) {

        if (res.statusCode == 401) {
          self.userLogin()
        }
        console.log(res.data)
        self.setData({
          right_num: res.data[0].right_num,
          wrong_num: res.data[0].wrong_num,
          user_subject_sum_nums: res.data[0].user_subject_sum_nums
        })
        self.drawpie()
      },
      fail(e) {
        wx.showModal({
          title: '请求失败',
          content: '请检查是否有网络',
          success(res) {
            if (res.confirm) {
              wx.redirectTo({
                url: "../index/index"
              })
            } else if (res.cancel) {
              wx.redirectTo({
                url: "../index/index"
              })
            }
          }
        })
      }
    })
  },

  //绘制正确率与错误率饼图
  drawpie(){
    var self = this;
    try {
      const res = wx.getSystemInfoSync()
      console.log(self.data.right_num)
      var wxCharts = require('../../utils/wxcharts-min.js');
      console.log(res.windowWidth)
      new wxCharts({
        canvasId: 'canvas1',
        type: 'pie',
        series: [{ name: '正确率', data: self.data.right_num }, { name: '错误率', data: self.data.wrong_num }],
        width: res.windowWidth,
        height: 300,
        dataLabel: true,
      });
    } catch (e) {
      // Do something when catch error
    }
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

  }
})