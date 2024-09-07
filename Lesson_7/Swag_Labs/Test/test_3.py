from Lesson_7.Swag_Labs.Pages.Shopmain import ShopmainPage
from Lesson_7.Swag_Labs.Pages.Shopcontainer import ShopContainer


def test_shop(chrome_browser):
    excepted_total = "58.29"
    
    shopmain = ShopmainPage(chrome_browser)
    shopmain.registration_fields()
    shopmain.buy_issue()
    shopmain.click_issue()
    shopmain.into_container()
    
    container = ShopContainer(chrome_browser)
    container.checkout()
    container.info()
    container.price()
    assert excepted_total in container.price()
    print(f"Сумма равна ${container.price()}")