// pages/tips/tips.js
Page({

  /**
   * 页面的初始数据
   */
  data: {
    images:"../../images/icon/test.png",
    text:""
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    if (options.type === "sublimt"){
      this.setData({
        text: "分数为" + options.fraction
      })
    } else if (options.type === "outtime"){
      this.setData({
        text: "你已经超过考试时间",
        images: "../../images/icon/error.png"
      })
    }else{
      this.setData({
        text:"不能作弊哦~~",
        images:"../../images/icon/error.png"
      })
    }

  },
  returnIndex(){
    console.log("hi")
    wx.switchTab({
      url: '../index/index'
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