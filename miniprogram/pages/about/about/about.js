const app = getApp();
Page({
  data: {
    StatusBar: app.globalData.StatusBar,
    CustomBar: app.globalData.CustomBar,
    ColorList: app.globalData.ColorList,
  },

  onShareAppMessage() {
    return {
      title: '运维咖啡吧',
      path: '/pages/about/about/about'
    }
  }
});
