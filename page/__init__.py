from selenium.webdriver.common.by import By

"""以下为服务器域名配置地址"""
url = "http://cal.apple886.com/"

"""以下为计算器配置数据"""
# 由于数字键，有一定的规律， 所以暂时先不用定位此键，用到的时候在考虑此键怎么解决；
# clac_num = By.CSS_SELECTOR, "simple9"

# 加号
clac_add = By.CSS_SELECTOR, "#simpleAdd"

# 减号
clac_subtr = By.CSS_SELECTOR, "#simpleSubtr"

# 乘号
clac_multi = By.CSS_SELECTOR, "#simpleMulti"

# 除号
clac_divi = By.CSS_SELECTOR, "#simpleDivi"

# 等号
clac_eq = By.CSS_SELECTOR, "#simpleEqual"

# 获取结果
clac_result = By.CSS_SELECTOR, "#resultIpt"
# 清屏
clac_clear = By.CSS_SELECTOR, "#simpleClearAllBtn"