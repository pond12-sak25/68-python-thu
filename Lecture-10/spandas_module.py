import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [24, 27, 22, 32],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
    }

df = pd.DataFrame(data)
print("dataframe:\n", df)

average_age = df['Age'].mean()
print(f"\nAverage age: {average_age}")

filtered_df = df[df['Age'] > 28]
print("\nFiltered dataframe (Age > 28):\n", filtered_df)

df['salary'] = [70000, 80000, 60000, 90000]
print("\nDataframe with new 'salary' column:\n", df)