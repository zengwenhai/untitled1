class Fruit(object):

    def __init__(self, name):
        self.name = name

class Apple(Fruit):

    def __init__(self, name, brand, color):
        # Fruit.__init__(self, name)
        super(Apple, self).__init__(name)
        self.brand = brand
        self.color = color

    def info(self):
        print("名称{0}，品牌{1},颜色{2}".format(self.name, self.brand, self.color))

a = Apple('苹果', '红富士', '红色')
a.info()