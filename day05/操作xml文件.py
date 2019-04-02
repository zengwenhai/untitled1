import xml.dom.minidom


def getxml(value=None):
    """获取单节点的数据内容"""
    xmlFile = xml.dom.minidom.parse('data.xml')
    db = xmlFile.documentElement
    itemList = db.getElementsByTagName(value)
    item = itemList[0]
    return item.firstChild.data

def getUser(parent=None, child=None):
    """获取单节点的数据内容"""
    xmlFile = xml.dom.minidom.parse('movies.xml')
    db = xmlFile.documentElement
    itemList = db.getElementsByTagName(parent)
    item = itemList[0]
    return item.getAttribute(child)


print(getxml('yan'))
print(getUser('type', 'nick'))