from bs4 import BeautifulSoup
if __name__ == "__main__":
    #将本地的html数据加载到该对象中
    fp = open('test.html','r',encoding='utf-8')
    soup = BeautifulSoup(fp,'lxml')
    #print(soup.div)
    #print(soup.find('div')) #等同于print(soup.div)
    #print(soup.find('div',class_='song').text)
    #print(soup.find_all('a'))
    #print(soup.select('.tang'))
    #print(soup.select('.tang > ul > li > a')[0])
    print(soup.select('.tang > ul a')[0]['href']) #空格表示多个层级，大于表示一个