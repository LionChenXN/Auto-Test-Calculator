from selenium.webdriver.support.wait import WebDriverWait
import time
from base.get_logger import GetLogger
log = GetLogger().get_logger()

class Base():

    # 初始化方法
    def __init__(self, driver):
        self.driver = driver
        log.info("初始化driver{}".format(driver))

    # 查找元素方法
    def base_find_element(self, loc, timeout=30, poll=0.5):
        """
        :param loc:  元素的定位信息，tuple
        :param timeout: 默认超时时间
        :param poll: 默认访问元素频率
        :return: 返回查找到的元素
        """
        # 显示等待
        log.info("正在查找元素：{}".format(loc))
        return WebDriverWait(self.driver,
                             timeout=timeout,
                             poll_frequency=poll).until(lambda x: x.find_element(*loc))

    # 点击方法
    def base_click(self, loc):
        """
        :param loc: 元素的定位信息，tuple
        :return: None
        """
        # 查找元素并点击
        log.info("正在点击元素：{}".format(loc))
        self.base_find_element(loc).click()


    # 获取value属性方法封装
    def base_get_value(self, loc):
        """
        :param loc: 元素的定位信息，tuple
        :return: value
        """
        # 使用get_attribute()方法获取指定的元素属性值
        value = self.base_find_element(loc).get_attribute("value")
        log.info("查找元素{},输入内容{}".format(loc, value))
        return value


    # 截图
    def base_get_img(self):
        """
        :return: None
        """
        self.driver.get_screenshot_as_file("../image/{}.png".format(time.strftime("%Y_%m_%d %H_%M_%S")))
