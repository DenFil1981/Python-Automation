import pytest
from string_utils import StringUtils
utils = StringUtils()

     # Capitalize #
    
def test_capitalize() :
    
       # Positive #
    assert utils.capitalize("test") == "Test"
    assert utils.capitalize("Hello world") == "Hello world"
    assert utils.capitalize("123") == "123"
    #    # Negative #
    assert utils.capitalize("") == ""
    assert utils.capitalize(" ") == " "
    assert utils.capitalize("12345test") == "12345test" 
    
     # Trim #
   
def test_trim() :
    
    # positive #
    assert utils.trim("   test") == "test"
    assert utils.trim("  hello world  ") == "hello world  "
    assert utils.trim("  SKY  ") == "SKY  "
    # negative # 
    assert utils.trim("") == ""
    
@pytest.mark.xfail() 
def test_trim_with_numbers_input():
    assert utils.trim(12345) == "12345"

@pytest.mark.xfail()
def test_trim_with_spaces_output():
    assert utils.trim("  SKY  ") == "  SKY  "
    
     # To_list #
    
@pytest.mark.parametrize('string, delimeter, result', [
    # positive #
   #
   ("яблоко,банан,апельсин", ",",["яблоко", "банан", "апельсин"]),
   ("1,2,3,4,5", ",", ["1", "2", "3", "4", "5"]),
   ("*@$@%@&", "@", ["*", "$", "%", "&"]),
    # negative #
   ("", None, []),
   ("1, 2, 3, 4 5" , None, ["1", "2", "3", "4 5"]),
])    

def  test_to_list(string, delimeter, result):
     if delimeter is None :
      res = utils.to_list(string)
     else :
      res = utils.to_list(string,delimeter) 
      assert res == result 
     
     
     # contains #
     
@pytest.mark.parametrize('string, symbol, result', [
    
    ("банан", "б", True),
    (" гвоздь", "д", True),
    ("мир", "р", True),
    ("диван-кровать", "-", True),
    ("135", "1", True),
    ("", "", True),
    ("Москва", "м", False),
    ("привет", "з", False),
    ("кот", "$", False),
    ("", "з", False),
    ("12345", "h", False),
])       
def test_contains( string, symbol, result) :
     res = utils.contains(string,symbol)
     assert res == result
    

     # delete_symbol #  
     
@pytest.mark.parametrize('string, symbol, result', [
    ("корень", "к", "орень"),
    ("Денис", "н", "Деис"),
    ("Океан", "О", "кеан"),
    ("123", "1", "23"),
    ("Красная площадь", " ", "Краснаяплощадь"),
    
    ("ножик", "з", "ножик"),
    ("", "", ""),
    ("", "с", ""),
    ("кофе", "", "кофе"),
    ("помидор", " ", "помидор"),
])     
    
def test_delete_symbol( string, symbol, result) :
    res = utils.delete_symbol(string,symbol)
    assert res == result


    # starts_with #
    
@pytest.mark.parametrize('string, symbol, result', [
    
    ("гитара", "г", True),
    ("Море", "М", True),
    ("","", True ),
    ("12345", "1", True),
    ("£$^%", "£", True),
    
    ("Small", "m", False),
    ("Skypro", "o", False),
    ("123", "3", False),
    ("", "%", False),
    ("Den", "d", False),
])
def test_starts_with(string, symbol, result) :
    res = utils.starts_with(string,symbol)
    assert res == result
    
    
    # end_with #
    
@pytest.mark.parametrize('string, symbol, result', [
    
    ("plane", "e", True),
    ("12345", "5", True),
    ("£$%^&", "&", True ),
    ("ShiP", "P", True),
    ("Мореплаватель", "ь", True),
    
    ("DoG", "g", False),
    ("45678", "0", False),
    ("Серп", "ж", False),
    ("$%^&^*&", "!", False),
    ("Ден", "Н", False),
])
def test_end_with(string, symbol, result) :
    res = utils.end_with(string,symbol)
    assert res == result
    
  
  #  is_empty #
  
  
@pytest.mark.parametrize('string, result', [
    
    ("", True),
    (" ", True),
    ("  ", True),
    
    ("not empty", False),
    ("not empty with space", False),
    ("123", False),
])
def test_is_empty(string, result) :
    res = utils.is_empty(string)
    assert res == result
    
    
    
  # list_to_string #
  
  
@pytest.mark.parametrize('lst, joiner, result', [
    (["1", "2", "3", "4", "5"], ",", "1,2,3,4,5"),
    (["h","e","l","p"], None, "h, e, l, p"),
    (["S","k","y","p","r","o"], "-", "S-k-y-p-r-o"),
    (["Sky", "pro"], "-", "Sky-pro"),
    
    ([], None, "" ),
    ([], ",", ""),
    ([], "cat", "")
])
def test_list_to_string( lst, joiner, result) :
    if joiner == None :
        res = utils.list_to_string(lst)
    else : 
        res = utils.list_to_string(lst, joiner)
    assert res == result     
        
        

     
    

    
    
        