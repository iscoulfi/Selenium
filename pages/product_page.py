
from Selenium.base_page import BasePage
from Selenium.locators import ProductPageLocators


class ProductPage(BasePage):

    def add_to_basket(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON).click()

    def solve_quiz(self):
        self.solve_quiz_and_get_code()

    def get_product_name(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

    def get_product_price(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

    def should_be_message_about_adding(self, product_name):
        message_name = self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE_NAME).text
        assert product_name == message_name, (
            f"Название товара в сообщении не совпадает: ожидали '{product_name}', получили '{message_name}'"
        )

    def should_be_correct_basket_price(self, product_price):
        basket_price = self.browser.find_element(*ProductPageLocators.BASKET_PRICE).text
        assert product_price == basket_price, (
            f"Цена в корзине не совпадает: ожидали '{product_price}', получили '{basket_price}'"
        )

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Сообщение об успехе присутствует, хотя не должно"

    def should_disappear_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Сообщение об успехе не исчезло, хотя должно было"
