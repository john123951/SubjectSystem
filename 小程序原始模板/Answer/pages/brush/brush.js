// pages/answer/answer.js
const app = getApp()
Page({

  /**
   * 页面的初始数据
   */
  data: {
    items: [], //题目items
    disabled: false,  //禁止按钮
    already: [],  //已作答题目
    subject_answer: "",
    answer: "",//正确答案标题
    true_user: 0,  //正确数
    false_user: 0, //错误数
    answer_dict: {},  //存放已作答的答案下标:答案
    current: 0, //处在的index
    sum_items: 0,//题目总数
    countDownNum: "1800",
    fraction: 0, //分数
    current_subject_id: 0,
    subject_type: ""
  },

  staticdata: {
    token: app.globalData.token
  },
  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    var self = this;
    console.log(options)
    self.setData({
      subject_type: options.type
    })
    self.staticdata.token = app.globalData.token
    self.random_subject()


    //设置常亮
    wx.setKeepScreenOn({
      keepScreenOn: true
    })

  },

  //获取题目
  random_subject() {
    var self = this
    console.log(self.data.subject_type)
    wx.request({
      url: 'http://127.0.0.1:8000/subject/',
      data: {
        sub_category: self.data.subject_type,
        sub_nums: "20"
      }, // 仅为示例，并非真实的接口地址
      header: {
        // 'content-type': 'application/json', // 默认值
        // 'Authorization': "JWT" + app.globalData.token
      },
      method: "post",
      success(res) {
        if (res.statusCode == 404) {
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
        // self.countDown(); //倒计时
        console.log(res.data[0].name)
        var items_list = []
        for (var i = 0; i < res.data.length; i++) {
          console.log(res.data[i].name)
          var title = res.data[i].name
          var id = res.data[i].id
          var option_a = res.data[i].option_a
          var option_b = res.data[i].option_b
          var option_c = res.data[i].option_c
          var option_d = res.data[i].option_d
          var items = { "title": title, "option_a": option_a, "option_b": option_b, 'option_c': option_c, 'option_d': option_d, id: id }
          items_list.push(items)
        }

        self.setData({
          items: items_list,
          sum_items: res.data.length,
          current_subject_id: items_list[0].id
        })
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



  //考试倒计时
  countDown() {
    let that = this;
    let countDownNum = that.data.countDownNum;//获取倒计时初始值
    //如果将定时器设置在外面，那么用户就看不到countDownNum的数值动态变化，所以要把定时器存进data里面
    that.setData({
      timer: setInterval(function () {//这里把setInterval赋值给变量名为timer的变量
        //每隔一秒countDownNum就减一，实现同步
        countDownNum--;
        //然后把countDownNum存进data，好让用户知道时间在倒计着
        that.setData({
          countDownNum: countDownNum
        })
        //在倒计时还未到0时，这中间可以做其他的事情，按项目需求来
        if (countDownNum == 0) {

          wx.showModal({
            title: '超时',
            content: '你已经超出作答时间！',
            success(res) {
              if (res.confirm) {
                wx.redirectTo({
                  url: "../tips/tips?type=outtime"
                })
              } else if (res.cancel) {
                wx.redirectTo({
                  url: "../tips/tips?type=outtime"
                })
              }
            }
          })
          //这里特别要注意，计时器是始终一直在走的，如果你的时间为0，那么就要关掉定时器！不然相当耗性能
          //因为timer是存在data里面的，所以在关掉时，也要在data里取出后再关闭
          clearInterval(that.data.timer);
          //关闭定时器之后，可作其他处理codes go here
        }
      }, 1000)
    })
  },

  //收藏
  favClick(e) {
    var self = this;
    console.log(self.data.current_subject_id)
    console.log(self.staticdata.token)

    wx.request({
      url: 'http://114.115.221.99/userfav/', // 仅为示例，并非真实的接口地址
      data: {
        subject: parseInt(self.data.current_subject_id),
      },
      method: "post",
      header: {
        // 'content-type': 'application/json', // 默认值
        'Authorization': "JWT " + app.globalData.token
      },
      success(res) {
        if (res.statusCode == 400) {
          wx.showToast({
            title: '已经收藏啦~',
            icon: 'cancel',
            image: "../../images/icon/error.png",
            duration: 2000
          })
        } else if (res.statusCode == 401) {
          self.userLogin()
        } else {
          wx.showToast({
            title: '收藏成功',
            icon: 'success',
            duration: 2000
          })
        }
        console.log(res.data)
      }
    })
  },

  userLogin() {
    //登录用户
    wx.login({
      success(res) {
        console.log(res.code)
        wx.request({
          url: 'http://114.115.221.99/wx_login/', // 仅为示例，并非真实的接口地址
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
          }
        })
      }
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
    // wx.showModal({
    //   title: '提示',
    //   content: '你已经作弊！',
    //   success(res) {
    //     if (res.confirm) {
    //       wx.redirectTo({
    //         url: "../tips/tips?type=error"
    //       })
    //     } else if (res.cancel) {
    //       wx.redirectTo({
    //         url: "../tips/tips?type=error"
    //       })
    //     }
    //   }
    // })
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

  //选择的时候
  radioChange(e) {
    self = this;
    // console.log('radio发生change事件，携带value值为：', e.detail.value.charAt(1))

    //获取题目ID
    console.log(e.detail.value.split("/")[1])
    self.setData({
      disabled: true,
    })


    var subject_numbere = parseInt(e.detail.value.split("/")[2])  //获取滑块下标

    //判断是否答过此题
    if (self.data.already.indexOf(subject_numbere) < 0) {
      var news = self.data.already
      news.push(subject_numbere)
      console.log(news)
      self.setData({
        already: news
      })
    } else {
      self.setData({
        disabled: true,
      })
    }
    //获取答案
    var subject_id = parseInt(e.detail.value.split("/")[1])
    wx.request({
      url: 'http://114.115.221.99/answer/' + subject_id, // 仅为示例，并非真实的接口地址
      header: {
        'content-type': 'application/json' // 默认值
      },
      success(res) {
        console.log(res.data)
        //添加答案到setData里面，为用户查询
        var anes_answer_dict = self.data.answer_dict
        anes_answer_dict[e.detail.value.split("/")[2]] = res.data.answer
        self.setData({
          answer_dict: anes_answer_dict
        })
        //获取用户选的答案
        var subject_user_answer = e.detail.value.split("/")[0]
        console.log(res.data.answer)
        //判断是否选正确答案
        if (subject_user_answer === res.data.answer) {
          var news_fraction = self.data.fraction + 2
          var title = '正确答案' + res.data.answer
          var true_user = self.data.true_user + 1
          var new_current = self.data.current + 1
          if (new_current === self.data.sum_items) {
            //最后一页
            self.setData({
              current: 0
            })
          }
          self.setData({
            answer: title,
            true_user: true_user,
            current: new_current,//自动跳到下页,
            fraction: news_fraction
          })
        } else {
          var news_fraction = self.data.fraction - 2
          var title = '正确答案' + res.data.answer
          var false_user = self.data.false_user + 1
          console.log(title)
          console.log(res.data.answer)
          self.setData({
            answer: title,
            false_user: false_user,
            fraction: news_fraction
          })
          wx.showModal({
            title: '错误',
            content: title,
            cancelText: "关闭",
            success(res) {
              var new_current = self.data.current + 1
              if (new_current === self.data.sum_items) {
                //最后一页
                self.setData({
                  current: self.data.current - 1
                })
              }
              if (res.confirm) {
                self.setData({
                  current: new_current//自动跳到下页
                })
              } else if (res.cancel) {
                self.setData({
                  current: new_current//自动跳到下页
                })
              }
            }
          })
        }
        console.log(self.data.fraction)
      }
    })

  },

  //滑动题目
  nextlastswiper(e) {
    var self = this;
    // console.log(self.data.already.indexOf(e.detail.current))
    // console.log(self.data.items[e.detail.current])
    var subject_id = parseInt(e.detail.current)  //当前的滑动块位置
    self.setData({
      current: e.detail.current,
      current_subject_id: self.data.items[e.detail.current].id  //获取当前题目ID
    })
    if (self.data.already.indexOf(e.detail.current) === -1) {
      self.setData({
        disabled: false,
        answer: ""
      })
    } else {
      var answer = self.data.answer_dict[e.detail.current]
      self.setData({
        disabled: true,
        answer: "正确答案" + answer,

      })
    }

  },
  //退出
  exit() {
    var self = this;
    wx.showModal({
      title: '提示',
      content: '确定退出吗?',
      success(res) {
        if (res.confirm) {
          wx.redirectTo({
            url: "../index/index"
          })
        } else if (res.cancel) {
        }
      }
    })
  },
})