#!/usr/bin/env python3
import cgi
import html
import os
import http.cookies
import sys

cookie = http.cookies.SimpleCookie(os.environ.get("HTTP_COOKIE"))
name = cookie.get("name")


form = cgi.FieldStorage()
text = form.getfirst("TEXT", "не задано")
text = html.escape(text)

if text=="не задано":
    sys.exit()  

def hasNumbers(inputString):
    return any(char.isdigit() for char in inputString)

def getCount(something):
    if something == "num":
        try:
            f = open("num.txt", "r")
            countNum = f.read()
            countNum = int(countNum)
            countNum += 1
            f.close()
            f = open("num.txt", "w")
            f.write(str(countNum))
            f.close()
            return countNum

        except:
            f = open("num.txt", "w")
            f.write("1")
            f.close()
            return countNum

    if something == "char":
        try:
            f = open("char.txt", "r")
            countChar = f.read()
            countChar = int(countChar)
            countChar += 1
            f.close()
            f = open("char.txt", "w")
            f.write(str(countChar))
            f.close()
            return countChar

        except:
            f = open("char.txt", "w")
            f.write("1")
            f.close()
            return countChar

    else:
        return None
          

if name is None:
    print("Set-cookie: name=value")
    with open("num.txt", "w") as fnum, open("char.txt", "w") as cnum:
        fnum.write("0")
        cnum.write("0")

countOfNum = open("num.txt","r").read()         
countOfCh  = open("char.txt","r").read()


if hasNumbers(text):
    res = "Строка содержит цифры"
    countOfNum = getCount("num")
else:
    res = "Строка не содержит цифр"
    countOfCh = getCount("char")


print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
        <html>
        <head>
            <meta charset="utf-8">
            <title>Обработка данных форм</title>
        </head>
        <body>""")

print("<h1>Обработка данных форм!</h1>")
print("<p>TEXT: {}</p>".format(text))
print("<p>RESULT: {}</p>".format(res))
print("<p>Статистика:</p>")
print("<p>Запросов, содержащих ицфру: {}</p>".format(countOfNum))
print("<p>Запросов, не содержащих ицфру: {}</p>".format(countOfCh))



print("""</body>
        </html>""")
