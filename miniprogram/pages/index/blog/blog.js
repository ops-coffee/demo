const app = getApp();
Page({
  data: {
    StatusBar: app.globalData.StatusBar,
    CustomBar: app.globalData.CustomBar
  },
  onLoad: function (option) {
    var blog = wx.getStorageSync('blog');

    this.setData({
      blog:blog
    })
  },

})