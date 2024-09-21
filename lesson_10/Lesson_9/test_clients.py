import allure
import pytest
from Employee import Employer
from DataBase import DataBase

api = ("https://x-clients-be.onrender.com")
db = DataBase(
    "postgresql+psycopg2://x_clients_user:ypYaT7FBULZv2VxrJuOHVoe78MEElWlb@dpg-crgp14o8fa8c73aritj0-a.frankfurt-postgres.render.com/x_clients_db_75hr")
#Имя пользователя: x_clients_user
#Пароль: ypYaT7FBULZv2VxrJuOHVoe78MEElWlb
#Хост: dpg-crgp14o8fa8c73aritj0-a.frankfurt-postgres.render.com
#База данных: x_clients_db_75hr
@allure.epic("X=clients")
@allure.severity(severity_level='normal')
@allure.tittle("список сотрудников")
@allure.description("Получаем список сотрудников из БД и АПИ, потом сравниваем их")
@allure.feature('Тест 1')
def test_get_list_of_employers():
    with allure.step("БД создаём компанию"):
        db.create_company('SkyPro test', 'best_company')
    with allure_step("БД получвем ID последней компании"):
        max_id = db.last_company_id()
        print(max_id)
    with allure.step("БД Добавляем сотрудника в компанию"):
        db.create_employer(max_id, "Den", "Filinov", 8001230890)
    with allure.step("БД Получаем список сотрудников из последней созданной компании"):
        db_employer_list = db.get_list_employer(max_id)
    with allure.step("API - получаем спикок сотрудников из последней созданной компании"):
        api_employer_list = api.get_list(max_id)
    with allure.step("Сравниваем списки сотрудников полученных из БД и через API"):
        assert len(db_employer_list) == len(api_employer_list)
    with allure.step("Удаляем сотрудника компании, иначе компания не удалится"):
        response = (api.get_list(max_id))[0]
        employer_id = response["id"]
        db.delete_employer(employer_id)
    with allure.step("Удаляем последнюю созданную компанию"):
        db.delete(max_id)
        
@allure.epic("X=clients")
@allure.severity(severity_level='critical')
@allure.tittle("Добавляем сотрудников")
@allure.description("Добавляем сотрудника в БД и сравниапем с АПИ имя, статус и фамилию")
@allure.feature('Тест 2')
def test_add_new_employer():
    db.create_company('Den adding new employer', 'employer')
    max_id = db.last_company_id()
    db.create_employer(max_id, "Den", "Filinov", 8001230890)
    response = (api.get_list(max_id))[0]
    employer_id = response["id"]
    with allure.step("Сравниваем ID компании"):
        assert response["company_id"] == max_id
    with allure.step("Сравниваем имя сотрудника с заданным"):
        assert response["first_name"] == "Den"
    with allure.step("Удостоверяемся что статус сотрудника 'True'"):
        assert response["isActive"] == True
    with allure.step("Сравниваем фамилию сотрудника с заданной"):
        assert response["last_name"] == "Filinov"
    with allure.step("БД - удаляем созданного сотрудника"):
        db.delete_employer(employer_id)
    with allure.step("БД - удаляем созданную компанию"):
        db.delete(max_id)

@allure.epic("X=clients")
@allure.severity(severity_level='critical')
@allure.tittle("Сравниваем информацию API/БД")
@allure.description("Сравниваем информацию о сотруднике полученную по API с указанной информацией при создании сотрудника в БД")
@allure.feature('Тест 3')            
def test_assertion_data():
    db.create_company('Employer get id company', 'new')
    max_id = db.last_company_id()
    db.create_employer(max_id, "Den", "Filinov", 8001230890)
    employer_id = db.get_employer_id(max_id)
    get_api_info = (api.get_info(employer_id)).json()
    assert get_api_info['firstName'] == "Den"
    assert get_api_info['lastName'] == "Filinov"
    assert get_api_info["phone"] == "8001230890"
    with allure.step("БД = удаление созданного сотрудника"):
        db.delete_employer(employer_id)
    with allure.step("БД = удаление последний созданной компании"):
        db.delete(max_id)

@allure.epic("X=clients")
@allure.severity(severity_level='critical')
@allure.tittle("Сравнивнение информации")
@allure.description("Сравниваем информацию о сотруднике полученную по API с измененной информацией в БД информацией о сотруднике")
@allure.feature('Тест 4')   
def test_update_user_info():
    db.create_company('New updaiting company', 'test')
    max_id = db.last_company_id()
    db.create_employer(max_id, "Den", "Filinov", 8001230890)
    employer_id = db.get_employer_id(max_id)
    db.update_employer_info("King", employer_id)
    with allure.step("Сравниваем информацию о сотруднике полученную по API с измененной информацией в БД информацией о сотруднике"):
        get_api_info = (api.get_info(employer_id)).json()
        assert get_api_info['firstName'] == "King"
        assert get_api_info['lastName'] == "Filinov"
        assert get_api_info["phone"] == "8001230890"
    with allure.step("БД = удаление созданного сотрудника"):
        db.delete_employer(employer_id)
    with allure.step("БД = удаление последний созданной компании"):
        db.delete(max_id)
    
    
    
    
       
    
    