class Phone2:
    __is_5g_enable = False

    def __check_5g(self):
        if self.__is_5g_enable:
            print("5g开启")
        else:
            print("5g已关闭，使用4g")

    def call_by_5g(self):
        self.__check_5g()
        print("正在通话中")


phone = Phone2()
phone.call_by_5g()
