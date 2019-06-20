#List Cases
list_of_airlines["AirIndia","Emirates","BritishAirways"]

#Iterating the list using range()
print("Iterating the list using range()")
     for index in range(0,len(list_of_airlines)):
         print(list_of_airlines[index])
      
#Iterating the list using in keyword
print("Iterating the list using keyword in")
     for airline in list_of_airlines:
         print(airline)
