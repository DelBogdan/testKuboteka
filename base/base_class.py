import datetime


class Base:
    def __init__(self, driver):
        self.driver = driver

    """Method Get current url"""
    def get_current_url(self):
        get_url = self.driver.current_url
        print("Current url " + get_url)

    """Method assert word"""
    def assert_word(self, word, result):
        value_word = word.text
        assert value_word == result
        print("Good value word")

    """Method assert url"""
    def assert_url(self, result):
        get_url = self.driver.current_url
        assert get_url == result
        print("Good value url")

    """Method asser FINISH URL"""
    def assert_finish_url(self, result):
        get_url = self.driver.current_url
        get_url = get_url.rsplit('/', 1)[0]
        assert get_url == result
        print("Good value url")

    """Method screenshot"""
    def get_screenshot(self, massage):
        now_date = datetime.datetime.now().strftime("%Y.%m.%d.%H.%M.%S")
        name_screenshot = massage + now_date + ".png"
        self.driver.save_screenshot('../screen/' + name_screenshot)
        # self.driver.save_screenshot("C:\\Users\\delbo\pythonLessons\\final_project\\screen\\" + name_screenshot)
