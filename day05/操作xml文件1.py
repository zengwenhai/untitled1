import xml.dom.minidom


DOMTree = xml.dom.minidom.parse("movies.xml")  # 打开xml文件
collection = DOMTree.documentElement  # 获得文档元素对象

movies = collection.getElementsByTagName("movie")  # 获取节点的一组标签，返回的是一个数组
print(movies[0].getAttribute("title"))

type = collection.getElementsByTagName("type")
item = type[0]
print(item.firstChild.data)


def getxmlvalue(nodename=None, file=None, n=0):
    file = xml.dom.minidom.parse(file)
    DOMTree = file.documentElement
    itemlist = DOMTree.getElementsByTagName(nodename)
    item = itemlist[n]
    return item.firstChild.data


def getxmlattr(parentname=None, childname=None, file=None, n=0):
    file = xml.dom.minidom.parse(file)
    DOMTree = file.documentElement
    itemlist = DOMTree.getElementsByTagName(parentname)
    item = itemlist[n]
    return item.getAttribute(childname)


print(getxmlvalue("type", "movies.xml"))
print(getxmlattr("type", "nick", "movies.xml"))
