from selenium import webdriver
import page

class GetDriver():

    # 设置类属性
    driver = None

    # 获取driver
    @classmethod
    def get_driver(cls):
        if cls.driver is None:
            # 实例化浏览器
            cls.driver = webdriver.Firefox()
            # 最大化
            cls.driver.maximize_window()
            # 打开浏览器
            cls.driver.get(page.url)
        return cls.driver

    # 退出driver
    @classmethod
    def quit_driver(cls):
        if cls.driver:
            print("关闭之前：", cls.driver)
            cls.driver.quit()
            print("关闭之后：", cls.driver)

            cls.driver = None
            print("置空之后：", cls.driver)


if __name__ == '__main__':
    # 第一次获取浏览器
    print(GetDriver().get_driver())
    GetDriver.quit_driver()
    # 第二次获取浏览器
    print(GetDriver().get_driver())
    # 调用关闭，测试 关闭后driver是否为None
    GetDriver().quit_driver()
    # print(GetDriver().get_driver())
