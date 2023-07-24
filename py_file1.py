def func():
    stroka = str(input()).lower()
    a = stroka[::-1].lower()
    if a == stroka:
        print(True)
    else:
        print(False)
func()

