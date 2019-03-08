//index.js
//获取应用实例
const app = getApp()

Page({
  data: {
    StatusBar: app.globalData.StatusBar,
    CustomBar: app.globalData.CustomBar
  },
  
  onLoad: function () {
    var that = this;
    wx.request({
      url: 'https://ops-coffee.cn/blog.json',
      header: {
        'content-type': 'application/json'
      },
      //请求后台数据成功
      success: function (res) {
        that.setData({
          Blogs: res.data.data
        })
      }
    })
  },

  toChild(event) {
    var blog = event.currentTarget.dataset.blog;
    
    wx.setStorageSync(
      'blog',blog
    );

    wx.navigateTo({
      url: '/pages/index/blog/blog'
    })
  },

  onShareAppMessage() {
    return {
      title: '运维咖啡吧',
      path: '/pages/index/list/list'
    }
  }
})