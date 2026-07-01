# DAILY TASK - WEEK 4 - DAY 4
'''
✓ Load employee data from PostgreSQL via SQLAlchemy into Pandas DataFrame
✓ Find average salary by department
✓ Find top 5 earners
✓ Fill missing salary values with department median
✓ Generate 2x2 dashboard:
    - Salary Distribution
    - Headcount by Department
    - Salary vs Experience
    - Correlation Heatmap
✓ Save as hr_dashboard.png
'''

from dbconnection import engine, Session
from models import Base, Employee

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# creation of tables
Base.metadata.create_all(engine)

# insert into rows of Employee table
'''session = Session()
employees = [
    Employee(name="Bob", dept="IT", salary=72000, experience=6),
    Employee(name="Charlie", dept="Sales", salary=45000, experience=2),
    Employee(name="David", dept="IT", salary=85000, experience=8),
    Employee(name="Emma", dept="HR", salary=60000, experience=5),
    Employee(name="Frank", dept="Sales", salary=50000, experience=3),
    Employee(name="Grace", dept="Finance", salary=68000, experience=7),
    Employee(name="Helen", dept="Finance", salary=50000, experience=4)
]

session.add_all(employees)
session.commit()
session.close()'''

# read data
df = pd.read_sql_table("employee", engine)
print("\nEmployee Data\n")
print(df)

# save to csv
df.to_csv("employee_data.csv", index=False)

# save to json
df.to_json("employee.json", orient="records", indent=4)

# missing values handling
dept_median = df.groupby("dept")["salary"].transform("median")
df["salary"] = df["salary"].fillna(dept_median)

# average salary by dept
print("\nAverage Salary By Department\n")
avg_salary = df.groupby("dept")["salary"].mean()
print(avg_salary)

# top 3 earners
print("\nTop 5 Earners\n")
top_3_earners = df.nlargest(5,"salary")
print(top_3_earners[["name", "dept", "salary"]])

# bonus column creation
df["Bonus"] = df["salary"].apply(lambda x: x * 0.10)
print("\nEmployee Bonus\n")
print(df[["name", "salary", "Bonus"]])

#dashboard
sns.set_style("whitegrid")
fig, axes = plt.subplots(2, 2, figsize=(14,10))

# salary distribution
sns.histplot(
    data=df,
    x="salary",
    ax=axes[0,0]
)
axes[0,0].set_title("Salary Distribution")

# headcount by department
df["dept"].value_counts().plot( kind="bar", ax=axes[0,1])
axes[0,1].set_title("Headcount by Department")
axes[0,1].set_xlabel("Department")
axes[0,1].set_ylabel("Employees")

# salary vs experience plot
sns.scatterplot(
    data=df,
    x="experience",
    y="salary",
    hue="dept",
    ax=axes[1,0]
)
axes[1,0].set_title("Salary vs Experience")

# corr heat map
corr = df[["experience","salary","Bonus"]].corr()
sns.heatmap(
    corr,
    annot=True,
    cmap="coolwarm",
    ax=axes[1,1]
)
axes[1,1].set_title("Correlation Heatmap")

# saving dashboard
plt.tight_layout()
plt.savefig("hr_dashboard.png")
plt.show()
print("\nDashboard saved as hr_dashboard.png")
print("\nProgram Completed Successfully")