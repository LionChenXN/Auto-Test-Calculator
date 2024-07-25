import unittest
from parameterized import parameterized

from base.get_driver import GetDriver
from page.page_calculation import PageCalculation
from tool.read_json import read_json
from data.writeJson import rand_data_write
from base.get_logger import GetLogger
import random

log = GetLogger().get_logger()

def get_data():
    n = random.randint(10, 200)
    path = rand_data_write(n)
    datas = read_json(path.split("./")[1])
    # 新建空列表
    arrs = []
    for data in datas.values():
        arrs .append((data['a'], data['b'], data['f'], data['expect']))
    return arrs

class TestCalculation(unittest.TestCase):
    driver = None

    # setupclass
    @classmethod
    def setUpClass(cls):
        try:
            # 获取driver
            cls.driver = GetDriver().get_driver()
            # 初始化 计算页面对象
            cls.calc = PageCalculation(cls.driver)
        except Exception as e:
            log.error(e)

    # teardownclass
    @classmethod
    def tearDownClass(cls):
        # 关闭driver
        GetDriver().quit_driver()

    # 测试加法
    @parameterized.expand(get_data())
    def test_calc(self, a, b, f, expect):
        # 调用计算业务方法
        self.calc.page_calc(a, b, f)
        if len(str(expect).split(".")) != 1:
            if str(expect).split(".")[1] == "0":
                expect = int(expect)
        print("预期结果为：", expect, "实际计算结果为：", self.calc.page_get_value())

        try:
            # 断言
            self.assertEqual(self.calc.page_get_value(), str(expect))
        except Exception as e:
            # 截图
            self.calc.page_get_image()
            log.error(e)
            raise