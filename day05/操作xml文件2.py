import xml.dom.minidom
import os

file_path = os.path.join(os.path.dirname(__file__), 'movies.xml')
print(file_path)


class GetXml(object):

    def __init__(self, filepath):
        self.filepath = filepath
        self.file = xml.dom.minidom.parse(self.filepath)  # 打开xml文件
        self.DOMTree = self.file.documentElement  # 获得文档元素对象

    def get_xml_value(self, nodename=None, n=0):
        itemlist = self.DOMTree.getElementsByTagName(nodename)  # 获取节点的一组标签，返回的是一个数组
        item = itemlist[n]
        return item.firstChild.data

    def get_xml_attr(self, parentname=None, childname=None, n=0):
        itemlist = self.DOMTree.getElementsByTagName(parentname)
        item = itemlist[n]
        return item.getAttribute(childname)  # 获得元素的属性所对应的值


if __name__ == "__main__":
    file_path = os.path.join(os.path.dirname(__file__), 'movies.xml')
    print(file_path)
    gx = GetXml(file_path)
    print(gx.get_xml_value("type"))
    print(gx.get_xml_attr("type", "nick"))