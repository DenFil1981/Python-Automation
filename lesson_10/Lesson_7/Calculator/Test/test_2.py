from Lesson_7.Calculator.Pages.Calcmainpage import CalcMain
import allure

@allure.epic("Calculator")
@allure.severity("severity_level='normal")
@allure.title("Работа калькулятора")
@allure.description("Поиск полей, ввод данных вывод резултата вычисления")
@allure.feature('Тест 2')
def test_calculator_assert(chrome_browser):
    with allure.step("Открываем калькулятор,вводим значение и ожидаем результат"):
        calcmain = CalcMain(chrome_browser)
        calcmain.insert_time()
        calcmain.clicking_buttons()
        calcmain.wait_button_gettext()
    with allure.step("Сравниваем получившийся результат с ожидаемым"):    
        assert "15" in calcmain.wait_button_gettext()
        
        
        