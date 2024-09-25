from selenium import webdriver

def browser_launch():
    opt=webdriver.ChromeOptions()
    opt.add_experimental_option("detach",True)
    opt.add_argument("--incognito")
    global driver
    driver =webdriver.Chrome(options=opt)
    return driver