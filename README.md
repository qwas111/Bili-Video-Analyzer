#B站视频分析器 2.0

##项目地址
[官网](https://nanet.ct.ws/md?f=bili)
[GitHub](https://github.com/qwas111/Bili-Video-Analyzer)
[bilibili](https://www.bilibili.com/video/BV1dFNAeME4N/?vd_source=a6ac37078c2ab9a002a456e680e8b8e1)
[GitCode](https://gitcode.com/asdqwezcx/1253)

##项目简介

B站视频分析器 2.0 是一个基于 Python 开发的图形化应用程序，专门用于分析 Bilibili 视频的各种数据。该工具能够获取视频基本信息、弹幕内容，并进行深度分析和可视化展示。

##主要功能

· 视频信息获取：自动提取视频标题、点赞数、投币数、收藏数、转发数等基本信息
· UP主信息：显示视频创作者信息
· 弹幕分析：获取并分析视频弹幕内容

##数据分析

· 情感分析：使用 SnowNLP 对弹幕进行情感评分，分为好评、中评、差评三类
· 词云生成：通过 jieba 分词生成弹幕词云图，直观展示高频词汇
· 数据可视化：生成情感分布饼图，清晰展示好评、中评、差评比例

##用户界面

· 图形化操作：使用 easygui 库提供友好的图形界面
· 交互式导航：支持多级菜单操作，用户体验流畅
· 错误处理：完善的异常处理机制，提供友好的错误提示

##技术栈

· 网络请求：requests
· 网页解析：bs4 (BeautifulSoup)
· 中文分词：jieba
· 数据可视化：
  · wordcloud (词云图)
  · matplotlib (饼图)
· 图形界面：easygui
· 情感分析：snownlp
· 浏览器控制：webbrowser

##使用流程

1. 启动程序 → 输入B站视频链接
2. 信息概览 → 查看视频基本数据和UP主信息
3. 弹幕分析 → 进入弹幕分析界面
4. 可视化选择 → 可选择生成词云图或情感分布饼图
5. 结果展示 → 查看分析结果和可视化图表

##项目特点

· 🔍 精准解析：准确提取B站视频数据和弹幕
· 📈 多维分析：从多个角度分析视频内容
· 🎨 直观展示：通过图表直观呈现分析结果
· 🛠️ 易于使用：图形化界面，操作简单
· ⚡ 高效稳定：完善的错误处理，运行稳定

##适用场景

· 视频内容分析
· 用户评论情感分析
· 热门词汇统计
· 视频质量评估
· 学术研究和数据分析

---


#本项目采用 Apache 2.0 许可证，由[网舰科技工作室](https://nanet.ct.ws)发布，由Stubborn_Li（倔强的李）（[QQ](https://qm.qq.com/q/wUsevOXY1G)|[bilibili](https://space.bilibili.com/2136004536)|[GitHub](https://github.com/qwas111/)）开发维护。

