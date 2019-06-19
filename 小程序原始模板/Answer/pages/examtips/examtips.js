// pages/examtips/examtips.js
Page({

  /**
   * 页面的初始数据
   */
  data: {
    subject_type:"",
    token:""
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    this.setData({
      subject_type: options.type,
      token:options.token,
    })
      
  },
  //考试模式
  exaTest(){
    var self = this;
    wx.redirectTo({
      url: '../answer/answer?type=' + self.data.subject_type + "&token=" + self.data.token,
    })
  },
  subject(){
    var self = this;
    wx.redirectTo({
      url: '../brush/brush?type=' + self.data.subject_type + "&token=" + self.data.token,
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

  }
})