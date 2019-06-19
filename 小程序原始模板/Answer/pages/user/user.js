// pages/user/user.js
import '../../utils/wxcharts-min.js'
const app = getApp()
Page({
  /**
   * 页面的初始数据
   */
  data: {
    right_worng:""
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    var wxCharts = require('../../utils/wxcharts-min.js');
    new wxCharts({
      canvasId: 'lineCanvas',
      type: 'line',
      categories: ['4/24', '', '', '', '', ''],
      series: [{
        name: '对的题目数',
        data: [0.15, 0.2, 0.45, 0.37, 0.4, 0.8],
        format: function (val) {
          return val.toFixed(2) + '题';
        }
      }, {
        name: '错的题目数',
        data: [0.30, 0.37, 0.65, 0.78, 0.69, 0.94],
        format: function (val) {
          return val.toFixed(2) + '题';
        }
      }],
      yAxis: {
        title: '对错数量',
        format: function (val) {
          return val.toFixed(2);
        },
        min: 0,
        
      },
      width: 320,
      height: 200,
    });
  },
  //曲线图
  // staticdata: {
  //   token: app.globalData.token
  // },


  /**
   * 生命周期函数--监听页面显示
   */
  onShow: function () {
    this.RightAndWrong()
    
  },

  RightAndWrong(){
    var self = this;
    wx.request({
      url: 'http://127.0.0.1:8000/usertf/', 

      header: {
        // 'content-type': 'application/json' // 默认值
        // 'Authorization': "JWT " + app.globalData.token
      },
      success(res) {
        self.setData({
          right_worng: res.data[0]
        })
        console.log(self.data.right_worng)
      }
    })
  },


})