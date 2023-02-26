from selenium import webdriver
import datetime
import time

driver = webdriver.Firefox()
driver.maximize_window()


def login():
    # 打开淘宝登录页，并进行扫码登录
    driver.get("https://www.taobao.com")
    time.sleep(3)
    if driver.find_element("link text","亲，请登录"):
        driver.find_element("link text","亲，请登录").click()

    print("请在20秒内完成扫码")
    time.sleep(20)

    driver.get("https://cart.taobao.com/cart.htm")
    time.sleep(3)
    if driver.find_element("id","J_SelectAll1"):
        driver.find_element("id","J_SelectAll1").click()
    now = datetime.datetime.now()
    print('login success:', now.strftime('%Y-%m-%d %H:%M:%S'))


def buy(buytime):
  while True:
    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
  # 对比时间，时间到的话就点击结算
    if now > buytime:
     try:
        # 点击结算按钮
        if driver.find_element("id","J_Go"):
          driver.find_element("id","J_Go").click()
        driver.find_element("link text",'提交订单').click()
     except:
      time.sleep(0.1)
      print(now)
      time.sleep(0.1)


if __name__ == "__main__":
  login()
  buy("2021-01-16 15:08:00.000000")
