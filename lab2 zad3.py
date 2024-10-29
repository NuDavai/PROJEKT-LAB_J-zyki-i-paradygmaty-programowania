dane = [
         [1, 2, 3, 5, 8, 13, 21, 34],
         {"brand": "Ford", "model": "Mustang", "year": 1964}, {"brand": "Honda", "model": "Civic", "year": 2005},
         ("jabłko", "ananas", "eukaliptus"),
         2010, 2003, 2005, 1999,
         "toJestString", "stringNumeroDuo", "liangBeiString"
       ]


inty = list(filter(lambda x: type(x) == type(1), dane))
stringi = list(filter(lambda x: type(x) == type(""), dane))
dicty = list(filter(lambda x: type(x) == type({}), dane))
listy = list(filter(lambda x: type(x) == type([]), dane))
krotki = list(filter(lambda x: type(x) == type(()), dane))

# max int
print(max(inty))

# najdluzszy string
maxStringL = 0
maxString = ""
for string in stringi:
    if len(string) > maxStringL:
        maxStringL = len(string)
        maxString = string
print(maxString)

# najdluzszy string i max int w dikcie
dicty = str(dicty)
print(dicty)
znakiDoUsunieciaZeStringa = ["[", "]", "{", "}", ":", ",", "'"]
for znak in znakiDoUsunieciaZeStringa:
    if znak in dicty:
        dicty = dicty.replace(znak, "")
print(dicty)
dictySłowa = []
słowo = ""
for znak in dicty:
    if znak != " ":
        słowo = słowo + znak
    else:
        dictySłowa.append(słowo)
        słowo = ""
print(dictySłowa)
## dorobic petlne szukajaca max string i max int