class Cup:
    __height = 0
    __volume = 0
    __color = ''
    __material = ''

    def set_height(self, height):
        self.__height = height

    def get_height(self):
        return print("height = ", self.__height, "cm")

    def set_volume(self, volume):
        self.__volume = volume

    def get_volume(self):
        return print("volume = ", self.__volume, "L")

    def set_color(self, color):
        self.__color = color

    def get_color(self):
        return print("color = ", self.__color)

    def set_material(self, material):
        self.__material = material

    def get_material(self):
        return print("material = ", self.__material)

    @staticmethod
    def full(liquid):
        print("水杯装满了", liquid)


class Computer:
    __size = 0
    __price = 0
    __cpu = ''
    __memory = 0
    __time = 0

    def set_size(self, size):
        self.__size = size

    def set_price(self, price):
        self.__price = price

    def set_cpu(self, cpu):
        self.__cpu = cpu

    def set_memory(self, memory):
        self.__memory = memory

    def set_time(self, time):
        self.__time = time

    def get_size(self):
        return print("size = ", self.__size)

    def get_prize(self):
        return print("price = ", self.__price)

    def get_cpu(self):
        return print("cpu = ", self.__cpu)

    def get_memory(self):
        return print("memory = ", self.__memory)

    def get_time(self):
        return print("standby time = ", self.__time)

    def typing(self):
        print("正在打字")

    def play_game(self):
        print("正在打游戏")

    def see_video(self):
        print("正在开视频")


c1 = Cup()
c1.set_height(10)
c1.set_volume(2)
c1.set_color('blue')
c1.set_material('glass')
c1.get_height()
c1.get_volume()
c1.get_color()
c1.get_material()
c1.full('juice')
co1 = Computer()
co1.set_size(5)
co1.set_cpu(8)
co1.set_price(12345)
co1.set_memory(8)
co1.set_time(24)
co1.get_size()
co1.get_cpu()
co1.get_prize()
co1.get_memory()
co1.get_time()
co1.typing()
co1.play_game()
co1.see_video()
