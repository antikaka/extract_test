

if __name__ == '__main__':
    import undetected_chromedriver as uc
    from selenium.webdriver.common.by import By
    from selenium.webdriver.common.keys import Keys
    import time
    import datetime

    origin = "vilnius"
    destination = "helsinki"

    driver = uc.Chrome()
    driver.get('https://euro.expedia.net')
    elem = driver.find_element(By.LINK_TEXT, "Flights") #flights
    elem.click()
    time.sleep(1)
    # elem = driver.find_element(By.LINK_TEXT, "#FlightSearchForm_ONE_WAY")
    elem = driver.find_elements(By.CLASS_NAME, "uitk-tab-text") #one-way
    for el in elem:
        if el.text == "One-way":
            el.click()
    time.sleep(1)
    elem_buttons = driver.find_elements(By.XPATH, "//button[@class='uitk-fake-input uitk-form-field-trigger']")
    elem_buttons[0].click()        #origin
    time.sleep(1)
    elem = driver.find_element(By.XPATH, "//input[@id='origin_select']")
    elem.send_keys(origin)
    time.sleep(1)
    elem.send_keys(Keys.RETURN)
    time.sleep(1)
    elem_buttons[1].click()        #destination
    time.sleep(1)
    elem = driver.find_element(By.XPATH, "//input[@id='destination_select']")
    elem.send_keys(destination)
    time.sleep(1)
    elem.send_keys(Keys.RETURN)
    time.sleep(1)



    elem = driver.find_element(By.XPATH, "//button[@id='search_button']")
    elem.click()
    time.sleep(2)

    url = driver.current_url
    date_def = datetime.datetime.date(datetime.datetime.today() + datetime.timedelta(days=14))
    replace_me = f"{date_def.year}-{date_def.month}-{date_def.day}"
    replace_me2 = f"{date_def.day}/{date_def.month}/{date_def.year}"
    url_o = str(url)
    url_o = url_o.replace(replace_me, "*replace_me*")
    url_o = url_o.replace(replace_me2, "*replace_me2*")

    with open("test.txt", "w") as failas:
        failas.write("")

    for num in range(11):
        if num < 1:
            continue
        date_check = datetime.datetime.date(datetime.datetime.today() + datetime.timedelta(days=num))

        url_new = url_o.replace("*replace_me*", f"{date_check.year}-{date_check.month}-{date_check.day}")
        url_new = url_new.replace("*replace_me2*", f"{date_check.day}/{date_check.month}/{date_def.year}")
        driver.get(url_new)
        time.sleep(20)

        elem = driver.find_elements(By.CLASS_NAME, "is-visually-hidden")
        time.sleep(2)

        with open("test.txt", "a") as failas:
            failas.write(f"\nFLIGHTS FROM {origin} TO {destination} {date_check}\n\n\n")

        for x in elem:
            if x.text.startswith("Select and"):
                with open("test.txt", "a") as failas:
                    failas.write(f"{x.text[36:]}\n\n")




    # driver.save_screenshot('test.png')
    driver.close()
