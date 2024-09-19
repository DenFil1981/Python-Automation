from Lesson_7.Swag_Labs.Pages.Shopmain import ShopmainPage
from Lesson_7.Swag_Labs.Pages.Shopcontainer import ShopContainer
import allure

@allure.epic("Swag_Labs")
@allure.severity("severity_level='normal")
@allure.title("Оформление заказа в онлайн магазине")
@allure.description("Оформление заказа в онлайн магазине с последующим сравнением стоимости")
@allure.feature('Тест 3')
def test_shop(chrome_browser):
    excepted_total = "58.29"
    
    with allure.step("Заходим на страницу онлайн магазина"):
         shopmain = ShopmainPage(chrome_browser)
    with allure.step("Проходим регистрацию"):     
         shopmain.registration_fields()
    with allure.step("Выбираем товары для покупки"):     
         shopmain.buy_issue()
    with allure.step("Добавляем вещи в онлайн корзину"):     
         shopmain.click_issue()
    with allure.step("Переходим в онлайн корзину"):     
         shopmain.into_container()
    
    container = ShopContainer(chrome_browser)
    container.checkout()
    container.info()
    container.price()
    with allure.step("Сравниваем общую стоимость товаров"):
        assert excepted_total in container.price()
        print(f"Сумма равна ${container.price()}")