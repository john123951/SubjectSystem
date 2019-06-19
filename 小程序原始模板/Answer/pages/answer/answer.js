// pages/answer/answer.js
const app = getApp()
Page({
  /**
   * 页面的初始数据
   */
  data: {
    items:[], //题目items
    disabled:false,  //禁止按钮
    already:[],  //已作答题目
    // subject_answer:"",
    answer:"",//正确答案标题
    true_user:0,  //正确数
    false_user:0, //错误数
    answer_dict:{},  //存放已作答的答案下标:答案
    current:0, //处在的index
    sum_items:0,//题目总数
    countDownNum: "1800",
    fraction:0, //分数
    current_subject_id:0,  //当前题目id
    subject_type:""  // 首页点击类别传递过来的类别
  },

  staticdata: {
    token: app.globalData.token
  },
  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    var self = this;

    // 首页点击类别传递过来的类别
    console.log(options)
    self.setData({
      subject_type:options.type
    })

    // token
    self.staticdata.token = app.globalData.token

    //获取题目
    self.random_subject()
  
  
    //设置常亮
    wx.setKeepScreenOn({
      keepScreenOn: true
    })
    
  },

  //获取题目
  random_subject(){
    var self = this
    console.log(self.data.subject_type)

    // 请求题目数据
    wx.request({
      url: 'http://127.0.0.1:8000/subject/',
      data: {
        sub_category: "Java",
        sub_nums: "30"
      }, // 仅为示例，并非真实的接口地址
      header: {
        'content-type': 'application/json', // 默认值
        // 'Authorization': "JWT " + app.globalData.token
      },
      method: "post",

      //请求成功
      success(res) {

        // 请求失败,转跳首页
        if(res.statusCode == 404){
          wx.showModal({
            title: '请求失败',
            content: '请检查是否有网络',
            success(res) {
              if (res.confirm) {
                // wx.redirectTo({
                //   url: "../index/index"
                // })
              } else if (res.cancel) {
                // wx.redirectTo({
                //   url: "../index/index"
                // })
              }
            }
          })
        }

        self.countDown(); //倒计时
        console.log(res.data)

        // 题目存放到 items
        var items_list = []
        for (var i = 0; i < res.data.length; i++) {
          console.log(res.data[i].name)
          var title = res.data[i].name
          var id = res.data[i].id
          var option_a = res.data[i].option_a
          var option_b = res.data[i].option_b
          var option_c = res.data[i].option_c
          var option_d = res.data[i].option_d
          // 自定义变量，根据key val 存放数据
          var items = { "title": title, "option_a": option_a, "option_b": option_b, 'option_c': option_c, 'option_d': option_d, id: id }
          // 自定义的items 追加到 items_list
          items_list.push(items)
        }

        self.setData({
          // 把题目数据存放到items
          items: items_list,
          // 题目总数
          sum_items: res.data.length,
          // 当前题目的id
          current_subject_id: items_list[0].id
        })
      },

      // 题目请求失败
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
  countDown(){
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
  favClick(e){
    var self = this;
    console.log(self.data.current_subject_id)
    console.log(self.staticdata.token)

    wx.request({
      url: 'http://127.0.0.1:8000/userfav/', // 仅为示例，并非真实的接口地址
      data: {
        // 参数为当前题目的 ID
        subject: parseInt(self.data.current_subject_id),
      },
      method:"post",
      header: {
        // 'content-type': 'application/json', // 默认值
        'Authorization': "JWT " + app.globalData.token
      },

      // 请求收藏成功
      success(res) {
        // 出现异常
        if(res.statusCode == 400){
          // 提示（图片和文字）
          wx.showToast({
            title: '已经收藏啦~',
            icon: 'cancel',
            image : "../../images/icon/error.png",
            duration: 2000
          })
        } else if (res.statusCode == 401){
            self.userLogin()
        }
        // 收藏成功
        else{
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

//登录用户
userLogin(){
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
              //保存到全局globalData.token（app.js的globalData.token）
              app.globalData.token = res.data.token
            }
          })
        }
      })
  
},

  // 切换后台，提示作弊
  onHide: function () {
    wx.showModal({
      title: '提示',
      content: '你已经作弊！',
      success(res) {
        if (res.confirm) {
          wx.redirectTo({
            url: "../tips/tips?type=error"
          })
        } else if (res.cancel) {
          wx.redirectTo({
            url: "../tips/tips?type=error"
          })
        }
      }
    })
  },

  // 题目作答完，不得再次作答（用户点击了答案）
  radioChange(e) {
    var self = this;
    // console.log('radio发生change事件，携带value值为：', e.detail.value.charAt(1))

    //获取题目ID
    console.log(e.detail.value.split("/")[1])
    self.setData({
      // 不可点击
      disabled: true,
    })

    //获取滑块下标
    var subject_numbere = parseInt(e.detail.value.split("/")[2])

    //判断是否答过此题
    // 未作答
    if (self.data.already.indexOf(subject_numbere) < 0 ) {
      // indexOf：subject_numbere没出现过，则该方法返回 小于0
      // 可进行作答，存放作答数据
      var news = self.data.already  // 已作答的题目
      news.push(subject_numbere)  // 已作答的题目（滑块下标）都放在一个列表
      console.log(news)
      self.setData({
        already: news
      })
    } 

    // 已作答，indexOf检索的subject_numbere，大于0
    else {
      self.setData({
        // 不给作答
        disabled: true,
      })
    }
    // 点击答案，获取题目ID
    var subject_id = parseInt(e.detail.value.split("/")[1])

    //答完本题，请求本题答案
    wx.request({
      url: 'http://127.0.0.1:8000/answer/'+ subject_id, // 仅为示例，并非真实的接口地址
      header: {
        'content-type': 'application/json' // 默认值
      },
      success(res) {
        console.log(res.data)
        //添加答案到setData里面，为用户查询
        var anes_answer_dict = self.data.answer_dict
        // 具体题目ID的具体答案（anes_answer_dict[1]="答案"）
        anes_answer_dict[e.detail.value.split("/")[2]] = res.data.answer
        self.setData({
          //存放已作答的答案下标
          answer_dict: anes_answer_dict
        })

        //判断答案是否正确
        // 用户选的答案
        var subject_user_answer = e.detail.value.split("/")[0]
        // 答对
        console.log(res.data.answer)
        // 判断答案是否正确
        if (subject_user_answer === res.data.answer) {
            // 正确
            var news_fraction = self.data.fraction + 2  // 分数 + 2
            var title = '正确答案' + res.data.answer
            var true_user = self.data.true_user + 1  // 正确数 + 1
          var new_current = self.data.current + 1  // 答对自动转跳下一页（current + 1 ），滑动下标加 1
            // 如果为最后一页（sum_items）
            if (new_current === self.data.sum_items) {
              // 只显示当前页
              self.setData({
                current: 0
              })
            }
            self.setData({
              answer: title,  // 正确答案
              true_user: true_user, // 正确数
              current: new_current,//自动跳到下页,
              fraction: news_fraction  // 传递分数
            })
        }

        // 答错，储存错题
        else {
          wx.request({
            url: 'http://127.0.0.1:8000/right_wrong/', // 仅为示例，并非真实的接口地址
            data: {
              subject: subject_id
            },
            method: "POST",
            header: {
              'content-type': 'application/json' // 默认值
            },
            success(res) {
              console.log(res.data)
            }
          })

          var news_fraction = self.data.fraction -2  // 分数 - 2
          var title = '正确答案' + res.data.answer  // 提示本次请求的题目的答案
          var false_user = self.data.false_user + 1  // 错误数 + 1
          self.setData({
            answer: title, //正确答案
            false_user: false_user,  //错误数 + 1
            fraction: news_fraction  // 分数 - 2
          })
          
          // 提示错误后再进行自动转跳
          wx.showModal({
            title: '错误',
            content: title,
            cancelText: "关闭",
            success(res) {
              // 提示错误成功
              var new_current = self.data.current + 1  // 下表 + 1，转跳到下一页
              if (new_current === self.data.sum_items){
                //最后一页
                self.setData({
                  // 不准转跳， 只返回最后一题
                  current: self.data.current - 1
                })
              }
              if (res.confirm) {
                // 点击确认
                self.setData({
                  current: new_current//自动跳到下页
                })
              } else if (res.cancel) {
                // 点击取消
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

  //滑动题目,作答过的不给作答
  nextlastswiper(e){
    var self = this;
    var subject_id = parseInt(e.detail.current)  //当前的滑动块位置
    self.setData({
      // 转跳到滑动块位置
      current: e.detail.current,
      current_subject_id: self.data.items[e.detail.current].id  //获取当前题目ID
    })

    // 如果本题未作答
    if (self.data.already.indexOf(e.detail.current) === -1 ){
      self.setData({
        // 让用户作答
        disabled: false,
        // 不提供答案，答完题再提供
        answer:""
      })
    }

    // 如果本题作答
    else{
      // 不给作答， 并且提示答案
      var answer = self.data.answer_dict[e.detail.current]  // 以下标获取具体的哪条题目答案
      self.setData({
        disabled: true,
        answer: "正确答案" + answer,
      })
    }
    
  },

  //交卷
  examSublimt() {
    var self = this;
    wx.showModal({
      title: '提示',
      content: '确定交卷吗?',
      success(res) {
        //点击确定交卷
        if (res.confirm) {
          // 计算对错数量
          wx.request({
            url: 'http://127.0.0.1:8000/exam/', // 仅为示例，并非真实的接口地址
            data: {
              user_true_nums: true_user, //true_user
              user_false_nums: false_user //false_user
            },
            method:"post",
            header: {
              'content-type': 'application/json' // 默认值
            },
            success(res) {
              console.log(res.data)
            }
          })


          //交卷后,计算成绩、对错题
          wx.redirectTo({
            url: "../tips/tips?fraction=" + self.data.fraction + "&true=" + self.data.true_user + "&false=" + self.data.false_user + "&type=sublimt"
          })
        } else if (res.cancel) {
        }
      }
    })


  },

  

})
