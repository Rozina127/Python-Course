#with open("day25weatherfile_read&write")

"""with open("day25_weather_data.csv") as file:
    file_data = file.readlines()
    print(file_data)"""
    
  
#to show data as a tabular form in row by row 
"""import csv
with open("day25_weather_data.csv") as file:
      data=csv.reader(file )
      # to add all tempratures in the neww list 
      tempratures=[]
      for row in data:
       print (row)
       tempratures.append ((row[1]))
      print (tempratures)"""
    

#By the help of pandas extension tabular bata is shown more beautiful way on screen 
import pandas as pd

# Read the CSV file
data = pd.read_csv("day25_weather_data.csv")

# Print the entire DataFrame
print(data)

# Print the 'temp' column
print(data["temp"])

# Convert DataFrame to a dictionary
"""data_dict = data.to_dict()
print("Data Dictionary:")
print(data_dict)
"""
# add temperatures to temp-list
temp_list= data["temp"].to_list()
print (temp_list)
print (len(temp_list))


# Calculate the average temperature using sum and len
avrg=sum(temp_list)/len(temp_list)
print (avrg)

# Calculate the average with pre defined function mean 
print (data["temp"].mean())

# Calculate the max temp with pre defined function mean 
print (data["temp"].max())


#get data in colunms 
print (data["condition"])
print(data.condition)

#get data in rows
print(data[data.day  == "Monday"])


#gt max temp row 
print(data[data.temp  == data.temp.max()])


#generate data frame from stracth 

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Score': [95, 82, 78, 90]
}
# Create a DataFrame from the dictionary
df = pd.DataFrame(data)

# Display the DataFrame
print(df)

# Save the DataFrame to a CSV file
df.to_csv('day25_players_scores.csv', index=False)

print("Data saved to 'day25_players_scores.csv'")





#Central Park Squirrel Data Analysis
import pandas

data = pandas.read_csv("day25_2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
print(grey_squirrels_count)
print(red_squirrels_count)
print(black_squirrels_count)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirrels_count, red_squirrels_count, black_squirrels_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("day25_squirrel_count.csv")




