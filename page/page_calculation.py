from base.base import Base
import page
from selenium.webdriver.common.by import By

class PageCalculation(Base):
    # 点击数字方法
    def page_click_num(self, num):
        for n in str(num):
            # 拆开单个按钮的定位方式
            loc = By.CSS_SELECTOR, "#simple{}".format(n)
            self.base_click(loc)

    # 点击加号
    def page_click(self, f):
        if f == "+":
            self.base_click(page.clac_add)
        elif f == "-":
            self.base_click(page.clac_subtr)
        elif f == "*":
            self.base_click(page.clac_multi)
        elif f == "/":
            self.base_click(page.clac_divi)

    # 点击 等号
    def page_click_eq(self):
        self.base_click(page.clac_eq)

    # 获取结果方法
    def page_get_value(self):
        return self.base_get_value(page.clac_result)

    # 点击清屏
    def page_click_clear(self):
        self.base_click(page.clac_clear)

    # 截图
    def page_get_image(self):
        self.base_get_img()

    # 组装加法业务方法
    def page_calc(self, a, b, f):
        self.page_click_num(a)
        self.page_click(f)
        self.page_click_num(b)
        self.page_click_eq()

