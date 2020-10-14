import requests
import re
import os

if __name__ == "__main__":
    # 判断下载文件夹是否存在
    if not os.path.exists('./webSpider/QSBKimg/'):
        os.mkdir('./webSpider/QSBKimg/')
    Url = 'https://www.qiushibaike.com/imgrank/page/%d/'
    Headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'
    }
    for src in range(1,3):
        newUrl = format(Url % src)
        spResponse = requests.get(url=newUrl, headers=Headers)
        spResponse.encoding='utf-8'
        # 获取图片连接，这里采用正则表达式
        imgUrl = re.findall('<div class="thumb">.*?<img src="(.*?)" alt.*?</div>',
                            spResponse.text,
                            re.S)
        for imgLink in imgUrl:
            # 为提取到的链接添加头信息
            imgLink = 'https:' + imgLink
            # 获取图片名称
            imgName = imgLink.split('/')[-1]
            # 获取图片的二进制流数据
            imgBinary = requests.get(url=imgLink, headers=Headers).content
            with open('./webSpider/QSBKimg/'+imgName, 'wb',) as fp:
                fp.write(imgBinary)
                print('{}，下载成功'.format(imgName))