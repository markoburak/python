import time


while True:
    t = time.localtime()
    now = time.strftime('%Y-%m-%d %H:%M', t)
    if now == '2020-04-11 16:01':

        from selenium import webdriver

        # user-agent
        headers = {'User-Agent':
                       'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'}
        # url for today
        url = 'https://rozetka.com.ua/ua/search/?text=nikkor&section_id=80060&redirected=1'

        # path to chromedriver
        chrome_path = r'E:\завантаження\chromedriver_win32\chromedriver.exe'

        # start driver
        driver = webdriver.Chrome(chrome_path)

        # get url
        driver.switch_to.window(driver.window_handles[0])

        driver.get(url)

        # price 50
        '''
        list_of_prices = driver.find_elements_by_xpath('//span[@class="goods-tile__price-value"]')
        lenses =[]
        for lens in list_of_prices:
            lenses.append(lens.text)
            print(lenses)
        #
        '''
        print("50mm 1.8 = "+driver.find_element_by_xpath('/html/body/app-root/div/div[1]/app-rz-search/div/main/search-result/div[2]/section/app-search-goods/ul/li[1]/app-goods-tile-default/div/div[2]/div[4]/div[2]/p/span[1]').text)
        # #
        # price35 =driver.find_element_by_xpath('/html/body/app-root/div/div[1]/app-rz-search/div/main/search-result/div[2]/section/app-search-goods/ul/li[1]/app-goods-tile-default/div/div[2]/div[4]/div[2]/p/span[1]')
        #
        print("35mm 1.8 = "+driver.find_element_by_xpath('/html/body/app-root/div/div[1]/app-rz-search/div/main/search-result/div[2]/section/app-search-goods/ul/li[2]/app-goods-tile-default/div/div[2]/div[4]/div[2]/p/span[1]').text)
        # #
        driver.execute_script("window.open()")
        driver.switch_to.window(driver.window_handles[1])
        # driver.close()

        url2 = r'https://www.amazon.ca/Nikon-AF-S-NIKKOR-1-8G-Cameras/dp/B004Y1AYAC'

        driver.get(url2)
        amazon_price_50 = driver.find_element_by_xpath('//*[@id="priceblock_ourprice"]')
        print(amazon_price_50.text)

        driver.execute_script('window.open()')
        driver.switch_to.window(driver.window_handles[2])

        url3 = r'https://www.amazon.ca/Nikon-AF-S-NIKKOR-Focus-Cameras/dp/B001S2PPT0'

        driver.get(url3)

        amazon_price_35 =driver.find_element_by_xpath('//*[@id="priceblock_ourprice"]')
        print(amazon_price_35.text)


        break
