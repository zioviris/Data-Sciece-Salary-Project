import pandas as pd

df = pd.read_csv("C:/Users/George/Documents/ds_salary_proj/chromedriver/glassdoor_jobs.csv")

# SALARY PARSING

# Calculating the annual income when the salary is expressed in "per hour" and "employer provided salary"
df["hourly"] = df["Salary Estimate"].apply(lambda x: 1 if "per hour" in x.lower() else 0)
df["employer_provided"] = df["Salary Estimate"].apply(lambda x: 1 if "employer provided salary" in x.lower() else 0)

# Elimination of the data entries that do not have an input.
# In our dataset, those entries have input -1
df = df[df["Salary Estimate"] != "-1"]

# Extracting the fist part of the Salary Estimate column (eliminating the Glassdor letters) using a lambda function
salary = df["Salary Estimate"].apply(lambda x: x.split("(")[0])

# Deleting the K, $ sings and per hour & employer provided salary from the input (Replacing by null)
minus_K_and_Dollar_signs = salary.apply(lambda x: x.replace("K", "").replace("$", ""))
minus_hr = minus_K_and_Dollar_signs.apply(lambda x: x.lower().replace("per hour", "").replace("employer provided salary:", ""))

# min max & average salary
df["min_salary"] = minus_hr.apply(lambda x: int(x.split("-")[0]))
df["max_salary"] = minus_hr.apply(lambda x: int(x.split("-")[1]))
df["average_salary"] = (df["min_salary"] + df["max_salary"])/2


# COMPANY NAME TEXT ONLY
df["company_txt"] = df.apply(lambda x: x["Company Name"] if x["Rating"] < 0 else x["Company Name"][:-3], axis = 1)

# STATE FIELD
df["job_state"] = df["Location"].apply(lambda x: x.split(",")[1])
df.job_state.value_counts()

# Examination if the Headquarters of the company is in the same location of the job.
df["same_state"] = df.apply(lambda x: 1 if x.Location == x.Headquarters else 0, axis =1)

# AGE OF COMPANY
df["age"] = df.Founded.apply(lambda x: x if x < 1 else 2021 - x)

# PARSING OF THE JOB DESCRIPTION (python, r, spark etc)

# python
df["python_yn"] = df["Job Description"].apply(lambda x: 1 if "python" in x.lower() else 0)
df.python_yn.value_counts()
# R
df["r_yn"] = df["Job Description"].apply(lambda x: 1 if "r" in x.lower() or "r studio" in x.lower or "r-studio" in x.lower() else 0)
df.r_yn.value_counts()

# Spark
df["spark_yn"] = df["Job Description"].apply(lambda x: 1 if "spark" in x.lower() else 0)
df.spark_yn.value_counts()
# AWS
df["aws_yn"] = df["Job Description"].apply(lambda x: 1 if "aws" in x.lower() else 0)
df.aws_yn.value_counts()

# Excel
df["excel_yn"] = df["Job Description"].apply(lambda x: 1 if "excel" in x.lower() else 0)
df.excel_yn.value_counts()

# Deleting the First Column named as Unnamed: 0
df_out = df.drop(["Unnamed: 0"], axis = 1 )
print(df_out.columns)

# Saving the df to a csv file for later usage
df_out.to_csv("Salary_Data_Cleaned.csv", index = False)



















