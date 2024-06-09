# none like null in javascript

print(type(None))  # Output: <class 'NoneType'>
print(None == None)  # Output: True
print(None == 0)  # Output: False
print(None == "")  # Output: False
print(None == [])  # Output: False
print(None == {})  # Output: False
print(None is None)  # Output: True
print(None is 0)  # Output: False
print(None is "")  # Output: False
print(None is [])  # Output: False
print(None is {})  # Output: False


def my_function():
    print("Hello, world!")


result = my_function()
print(result)  # Ini akan mencetak: None
