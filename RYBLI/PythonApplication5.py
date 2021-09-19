import math

number = int(input("Введите число: "))

number_list = ["ноль","один","два","три","четыре","пять","шесть","семь","восемь","девять"]
teen_list = ["одиннадцать","двенадцать","тринадцать","четырнадцать","пятнадцать","шестнадцать","семнадцать","восемнадцать","девятнадцать"]
decades_list =["десять", "двадцать","тридцать","сорок","пятьдесят","шестьдесят","семьдесят","восемьдесят","девяносто"]
hundredths_list =["сто", "двести", "триста", "четыреста", "пятьсот", "шестьсот", "семьсот", "восемьсот", "девятьсот"]
thousandths_list =["одна тысяча", "две тысячи", "три тысячи", "четыре тысячи", "пять тысяч", "шесть тысяч", "семь тысяч", "восемь тысяч", "девять тысяч"] 

if number <= 9:
    print(number_list[number].capitalize(), end=" ")
elif number > 10 and number <= 19:
    tens = number % 10
    print(teen_list[tens - 1].capitalize(), end=" ")
elif number == 10 or (number > 19 and number <= 99):
    ones = math.floor(number/10)
    twos = ones - 1
    tens = number % 10
    if tens == 0:
        print(decades_list[twos].capitalize(), end=" ")
    elif tens != 0:
        print(decades_list[twos].capitalize() + " " + number_list[tens], end=" ")
elif number >=100 and number <=999:
    ones = math.floor(number/100)
    twos = ones - 1
    tens = number % 10
    h = number % 100
    h2 = ((number % 100)%10) - 1
    h3 = ((number % 100)//10) - 1
    if tens == 0 and h == 0:
       print(hundredths_list[twos].capitalize(), end=" ")
    elif tens == 0:
        print(hundredths_list[twos].capitalize() + " " + decades_list[h3], end=" ")
    elif h < 10:
        print(hundredths_list[twos].capitalize() + " " + number_list[h], end=" ")
    elif (number % 100 < 20) and (number % 100 > 10):
        print(hundredths_list[twos].capitalize() + " " + teen_list[h2], end=" ")
    elif tens != 0 and h != 0:
        print(hundredths_list[twos].capitalize() + " " + decades_list[h3] + " " + number_list[tens], end=" ")
elif number >=1000 and number < 10000:
    ones = math.floor(number/1000)
    twos = ones - 1
    tens = number % 10
    h = number % 100
    h2 = ((number % 1000)%10) - 1
    h3 = ((number % 100)//10) - 1
    h4 = ((number % 1000)//100) - 1
    a = number % 1000
    if tens == 0 and h == 0 and a == 0:
       print(thousandths_list[twos].capitalize(), end=" ")
    elif (a < 10) and (a != 0):
        print(thousandths_list[twos].capitalize()  + " " + number_list[tens], end=" ")
    elif (a < 100) and (a != 0) and (h < 20) and (h > 10) and (h != 0):
        print(thousandths_list[twos].capitalize()  + " " + teen_list[h2], end=" ")
    elif (h < 10) and (h != 0):
        print(thousandths_list[twos].capitalize() + " " + hundredths_list[h4] + " " + number_list[tens], end=" ")
    elif (a < 100) and (a != 0):
        print(thousandths_list[twos].capitalize() + " " + decades_list[h3] + " " + number_list[tens], end=" ")
    elif (h < 10) and (h != 0):
        print(thousandths_list[twos].capitalize() + " " + decades_list[h3] + " " + number_list[tens], end=" ")
    elif (a < 20) and (a > 10) and (a != 0):
        print(thousandths_list[twos].capitalize() + " " + teen_list[h2], end=" ")
    elif (h < 20) and (h > 10) and (h != 0):
        print(thousandths_list[twos].capitalize() + " " + hundredths_list[h4] + " " + teen_list[h2], end=" ")
    elif tens == 0 and h == 0:
        print(thousandths_list[twos].capitalize() + " " + hundredths_list[h4], end=" ")
    elif tens == 0:
        print(thousandths_list[twos].capitalize() + " " + hundredths_list[h4] + " " + decades_list[h3], end=" ")
    elif tens != 0 and h !=0 and a !=0:
        print(thousandths_list[twos].capitalize() + " " + hundredths_list[h4] + " " + decades_list[h3] + " " + number_list[tens], end=" ")

if (number % 10 == 5) or (number % 10 == 6) or (number % 10 == 7) or (number % 10 == 8) or (number % 10 == 9) or (number % 10 == 0) or (number % 100 == 11) or (number % 100 == 12) or (number % 100 == 13) or (number % 100 == 14) or (number % 100 == 15) or (number % 100 == 16) or (number % 100 == 17) or (number % 100 == 18) or (number % 100 == 19): 
    print ("рублей")
elif (number % 10 == 2) or (number % 10 == 3) or (number % 10 == 4):
    print ("рубля")
elif number % 10 == 1:
    print ("рубль")
