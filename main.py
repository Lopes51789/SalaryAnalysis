import json
import mysql.connector
import cleanData

# Clean data and export to json
df = cleanData.DataFrame("Salary_Data.csv")
json_file = df.toJson()


# Load JSON data
with open(json_file, 'r') as file:
    data = json.load(file)

# Connect to MySQL
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='o3H[FZkaN',
    database='SalaryAnalysis',
)
cursor = conn.cursor()


# Insert data into MySQL table
for record in data:
    cursor.execute(
        "INSERT INTO salaryanalysis.originalsalaries (Age, Gender, EducationLevel, JobTitle, YearsOfExperience, Salary) VALUES (%s, %s, %s, %s, %s, %s)",
        (record['Age'], record['Gender'], record['Education Level'], record['Job Title'], record['Years of Experience'], record['Salary']) #Age,Gender,Education Level,Job Title,Years of Experience,Salary
    )

# Commit and close connection
conn.commit()
cursor.close()
conn.close()

print("Data inserted into MySQL table successfully.")