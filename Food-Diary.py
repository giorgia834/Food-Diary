import sqlite3

conn = sqlite3.connect('food_diary2.db') #create database (file)

c = conn.cursor() #creating the cursor

# c.execute("""CREATE TABLE food_diary2 (
#           id INTEGER PRIMARY KEY,
#           Date DATE, 
#           Meal_type TEXT, 
#           Meal_name TEXT,
#           Ingredient_1 TEXT, 
#           Ingredient_2 TEXT, 
#           Ingredient_3 TEXT, 
#           Symptom_1 TEXT, 
#           Symptom_2 TEXT, 
#           Symptom_3 TEXT,
#           General_score INTEGER
# )""")

# To delete table added w/ wrong name
# c.execute("DROP TABLE food_diary2")
# print("Table dropped... ")


print("What is the date of the meal you'd like to record?")
date = input()

print("Which meal would you like to record?")
meal_type = input()

print("What food did you have?")
meal_name = input()

print("name the first main ingredient:")
ingredient_1 = input()

print("name the second main ingredient:")
ingredient_2 = input()

print("name the third main ingredient:")
ingredient_3 = input()

print("name of one of your symptoms (1):")
symptom_1 = input()

print("name of one of your symptoms (2):")
symptom_2 = input()

print("name of one of your symptoms (3):")
symptom_3 = input()

print("On a scale 1 to 10 how did this food make you feel?")
score = input()

food_diary_entry = [(None, date, meal_type, meal_name, ingredient_1, ingredient_2, ingredient_3, symptom_1, symptom_2, symptom_3, score)]

c.executemany("INSERT INTO food_diary2 VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", food_diary_entry)

# # c.execute("SELECT * FROM food_diary2")
# # print(c.fetchall()) #to see result from query above

conn.commit() #this saves changes we made in database
conn.close() #close previously opened connection 

  





