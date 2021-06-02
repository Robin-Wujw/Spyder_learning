import requests
if __name__== "__main__":
    url= 'https://pic.qiushibaike.com/system/pictures/12436/124360753/medium/7TKGSDY0E3FBRC8Q.jpg'
    #content返回的是二进制形式的图片数据
    #text(字符串) content(二进制) json(对象)
    image_data = requests.get(url=url).content
    with open('./qiutu.jpg','wb') as fp:
        fp.write(image_data)