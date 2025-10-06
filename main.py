import requests, bs4, jieba
import webbrowser as wb
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import easygui as g
from snownlp import SnowNLP

# Copyright (c) 2025 倔强的李：3506395541. All rights reserved. Licensed under Apache 2.0.

head = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36'}  # 设置请求头，模拟浏览器

# 源码
def ym_(http):
    url = http
    # 请求网页
    res = requests.get(url, headers=head)
    res.encoding = "utf-8"  # 设置编码格式
    soup = bs4.BeautifulSoup(res.text, "html.parser")  # 解析网页
    return soup

# cid
def cid_(http):
    url = "https://api.bilibili.com/x/player/pagelist?bvid=" + http[31:43] + "&jsonp=jsonp"
    # 请求网页
    # https://www.bilibili.com/video/BV1k4421U7SZ/?spm_id_from=333.1007.tianma.1-1-1.click&vd_source=a6ac37078c2ab9a002a456e680e8b8e1
    res = requests.get(url, headers=head)
    if res.text[8] != "0":
        return
    else:
        cid = res.text.split(",")[3].split(":")[2]
        return cid

# 弹幕
def dm_(cid):
    # 请求网页
    cid = cid
    url = "https://comment.bilibili.com/" + cid + ".xml"
    res = requests.get(url, headers=head)
    res.encoding = res.apparent_encoding
    # 选取数据
    soup = bs4.BeautifulSoup(res.text, "lxml")
    tags = soup.find_all("d")
    return tags

# 弹幕词云图
def dm_cyt(dm):
    s = ""  # 创建空字符串
    for t in dm:
        txt = t.text
        # 把弹幕txt分为词语
        word_list = jieba.lcut(txt)
        for w in word_list:  # 遍历word_list列表
            s = s + w + "*"
    # 根据字符串w生成词云
    w = WordCloud(font_path=r"C:\Windows\Fonts\msyh.ttc",
                  background_color="white",
                  max_words=100
                  ).generate(s)
    w.to_file("弹幕词云.png")

# 弹幕评分
def dm_pf(dm):
    hp = "----------------好评----------------\n"
    zp = "----------------中评----------------\n"
    cp = "----------------差评----------------\n"
    hpl = 0
    zpl = 0
    cpl = 0
    for d in dm:
        d = d.text
        fs = SnowNLP(d).sentiments
        if fs > 0.66:
            hp = hp + d + "\n"
            hpl = hpl + 1
        elif fs > 0.33:
            zp = zp + d + "\n"
            zpl = zpl + 1
        else:
            cp = cp + d + "\n"
            cpl = cpl + 1
    return hp + zp + cp, hpl, zpl, cpl

# 主程序_弹幕_词云图
def zcx_dm_cyt(spm, dz, tb, sc, zf, dmpf, cid, dm, hpl, zpl, cpl, upz):
    dm_cyt(dm)
    btn = g.buttonbox(
        title="B站视频分析器2.0",
        image="弹幕词云.png",
        choices=["返回", "退出"]
    )
    if btn == "返回":
        zcx_dm(spm, dz, tb, sc, zf, dmpf, cid, dm, hpl, zpl, cpl, upz)
    elif btn == "退出":
        zcx_hx()

# 主程序_弹幕_饼图
def zcx_dm_bt(spm, dz, tb, sc, zf, dmpf, cid, dm, hpl, zpl, cpl, upz):
    # 定义数据
    sizes = [hpl, zpl, cpl]
    labels = ["好评", "中评", "差评"]
    # 绘制饼图
    plt.pie([hpl, zpl, cpl], labels=["good", "middle", "bad"], autopct='%1.1f%%', shadow=True)
    # 显示图形
    plt.show()
    zcx_dm(spm, dz, tb, sc, zf, dmpf, cid, dm, hpl, zpl, cpl, upz)

# 主程序_弹幕
def zcx_dm(spm, dz, tb, sc, zf, dmpf, cid, dm, hpl, zpl, cpl, upz):
    btn = g.buttonbox(
        msg=dmpf,
        title="B站视频分析器2.0",
        choices=["词云图", "饼图", "返回", "退出"]
    )
    if btn == "返回":
        zcx_gl(spm, dz, tb, sc, zf, dmpf, cid, dm, hpl, zpl, cpl, upz)
    elif btn == "词云图":
        zcx_dm_cyt(spm, dz, tb, sc, zf, dmpf, cid, dm, hpl, zpl, cpl, upz)
    elif btn == "饼图":
        zcx_dm_bt(spm, dz, tb, sc, zf, dmpf, cid, dm, hpl, zpl, cpl, upz)
    elif btn == "退出":
        zcx_hx()

# 主程序_概览
def zcx_gl(spm, dz, tb, sc, zf, dmpf, cid, dm, hpl, zpl, cpl, upz):
    btn = g.buttonbox(
        msg=spm + "\n" + "点赞:" + dz + "  投币:" + tb + "  收藏:" + sc + "  转发:" + zf + "\n" + "up主:" + upz + "\n" + "cid:" + cid,
        title="B站视频分析器2.0",
        choices=["弹幕", "退出"]
    )
    if btn == "弹幕":
        zcx_dm(spm, dz, tb, sc, zf, dmpf, cid, dm, hpl, zpl, cpl, upz)
    elif btn == "退出":
        zcx_hx()

# 主程序_核心
def zcx_hx():
    # 主页
    btn = g.buttonbox(
        msg="B站视频分析器",
        title="B站视频分析器2.0",
        choices=["进入", ]
    )
    # 输入
    if btn == "进入":
        http = g.enterbox(
            msg="请输入网址",
            title="B站视频分析器2.0",
        )

        if http == None:
            # 退出了
            zcx_hx()

        elif http == "":
            # 没输入
            buts = g.buttonbox(
                msg="您没有输入",
                title="错误",
                choices=["确定"]
            )
            if buts == "确定":
                zcx_hx()
        else:
            # 没蛇魔问题
            cid = cid_(http)
            if cid == None:
                # 不对还有问题
                buts = g.buttonbox(
                    msg="您的输入有误",
                    title="错误",
                    choices=["确定"]
                )
                if buts == "确定":
                    zcx_hx()
            else:
                # 彻底没问题
                soup = ym_(http)
                spm_element = soup.find("h1", {"class": "video-title special-text-indent"})
                spm = spm_element.text.strip()
                dz_element = soup.find("span", {"class": "video-like-info video-toolbar-item-text"})
                dz = dz_element.text.strip()
                tb_element = soup.find("span", {"class": "video-coin-info video-toolbar-item-text"})
                tb = tb_element.text.strip()
                sc_element = soup.find("span", {"class": "video-fav-info video-toolbar-item-text"})
                sc = sc_element.text.strip()
                zf_element = soup.find("span", {"class": "video-share-info video-toolbar-item-text"})
                zf = zf_element.text.strip()
                upz_element = soup.find("a", {"class": "up-name"})
                upz = upz_element.text.strip()
                dm = dm_(cid)
                dmpf, hpl, zpl, cpl = dm_pf(dm)
                zcx_gl(spm, dz, tb, sc, zf, dmpf, cid, dm, hpl, zpl, cpl, upz)

try:
    zcx_hx()
except Exception as e:
    g.buttonbox(
                    msg="出现了一个无法挽回的错误:"+str(e),
                    title="错误",
                    choices=["确定"]

                )
