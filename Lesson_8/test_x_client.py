import pytest
import requests
from Lesson_8.Employee import Employer, Company
from Lesson_8.constants import X_client_URL

employer = Employer()
company = Company()


def test_authorization(get_token):
    token = get_token
    #Удостоверяемся что токен не пустой
    assert token is not None
    #Удостоверяемся что токен имеет строковый формат
    assert isinstance(token, str) 
    
def test_getcompany_id():
    company_id = company.last_active_company_id()
    #Удостоверяемся что ID не пустой
    assert company_id is not None
    #Проверяем что ID компании состоит только из цифр 
    assert str(company_id).isdigit()   
    
def test_add_employer(get_token):
    token = str(get_token)
    com_id = company.last_active_company_id()
    body_employer = {
    "id": 0,
    "firstName": "Den",
    "lastName": "Fil",
    "middleName": "string",
    "company_Id": com_id,
    "email": "test@ymail.com",
    "url": "string",
    "phone": "string",
    "birthdate": "2024-09-14T13:34:16.124Z",
    "isActive": True
    }    
    new_employer_id = (employer.add_new(token, body_employer))
    #Удостоверяемся что ID сотрудника не пустой
    assert new_employer_id is not None
    #Проверяем что ID сотрудника состоит только из цифр
    #assert str(new_employer_id).isdigit()
    
    #Получаем инфо о добавлении сотрудника
    info = employer.get_info(new_employer_id)
    #assert info.json()['id'] == new_employer_id
    #assert info.status_code == 200
    
    #Проверяем невозмзжность создания клиента без токена
    
def test_add_employer_without_token():
    com_id = company.last_active_company_id()
    token = ""
    body_employer = {
    "id": 0,
    "firstName": "Den",
    "lastName": "Fil",
    "middleName": "string",
    "companyId": 0,
    "email": "test@ymail.com",
    "url": "string",
    "phone": "string",
    "birthdate": "2024-09-14T13:34:16.124Z",
    "isActive": True   
    }
    new_employer = employer.add_new(token, body_employer)
    assert new_employer['message'] == 'Unauthorized'
    
    #Проверяем невозможность создания клиента без тела запроса 
    
def test_add_employer_without_body(get_token):
    token = str(get_token)
    com_id = company.last_active_company_id()
    body_employer = {}
    new_employer = employer.add_new(token, body_employer)
    assert new_employer['message'] == 'Internal server error' 
    
def test_get_employer():
    com_id = company.last_active_company_id()
    #Список работников конкретной компании
    list_employers = employer.get_list(com_id)
    #Проверяем что нам вернулся список, а не строка
    assert isinstance(list_employers, list)
    
    #Проверяем, обязательное поле "ID компании" в запросе на получение списка работников без ID компании
    
def test_get_list_employers_missing_company_id():
    try:
        employer.get_list('')
    except TypeError as e:
        assert str(e) == "Employer.get_list() missing 1 required positional argument : 'company_id'"   
        
    #Проверяем,обязательное поле 'ID компании' в запросе на получение списка работников - на валидное ID компании(пустая строка)
    
def test_get_list_employers_invalid_company_id():
    try:
        employer.get_list('')
    except TypeError as e:
        assert str(e) == "Employer.get_list() missing 1 required positional argument : 'company_id'" 
        
    #Проверяем,обязательное поле 'ID сотрудника' в запросе на получение инфо о сотруднике без 'ID сотрудника'        
def test_change_employer_info(get_token):
    token = str(get_token)
    com_id = company.last_active_company_id()
    body_emloyer = {
    "id": 0,
    "firstName": "Den",
    "lastName": "Fil",
    "middleName": "string",
    "companyId": com_id,
    "email": "test@ymail.com",
    "url": "string",
    "phone": "string",
    "birthdate": "2024-09-14T13:34:16.124Z",
    "isActive": True      
    }
    just_employer = employer.add_new(token, body_emloyer)
    id =just_employer['id']
    body_change_employer = {
    "lastName": "Fokin",
    "email": "test@ymail.com",
    "url": "string",
    "phone": "string",
    "isActive": True         
    }  
    employer_changed = employer.change_info(token, id, body_change_employer)
    assert employer_changed.status_code == 200
    
    #Проверяем, что ID сотрудника соответствует ID при создании сотрудника
    assert id == employer_changed.json()['id'] 
    #Проверяем что почта изменилась
    assert (employer_changed.json()["email"]) == body_change_employer.get("email")  
    