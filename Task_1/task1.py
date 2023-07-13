import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def exercise_0(file):
    df = pd.read_csv(file)
    print(df.head())
    return df

def exercise_1(df):
    column_names = df.columns.tolist()
    return column_names

def exercise_2(df, k):
    return df.head(k)

def exercise_3(df, k):
    sample_k_rows = df.sample(n=k)
    return sample_k_rows

def exercise_4(df):
    unique_transaction_types = df['type'].unique().tolist()
    return unique_transaction_types

def exercise_5(df):
    top_destinations = df['nameDest'].value_counts().head(10)
    return top_destinations

def exercise_6(df):
    fraud_rows = df[df['isFraud'] == 1]
    return fraud_rows

def exercise_7(df):
    interaction_counts = df.groupby('nameOrig')['nameDest'].nunique()
    interaction_counts = interaction_counts.sort_values(ascending=False)
    interaction_counts = interaction_counts.reset_index()
    interaction_counts.columns = ['Source', 'Distinct_Destinations']
    return interaction_counts

def visual_1(df):
    transaction_counts = df['type'].value_counts()
    fig, ax = plt.subplots()
    sns.barplot(x=transaction_counts.index, y=transaction_counts.values, ax=ax)
    ax.set_title('Transaction Types')
    ax.set_xlabel('Type')
    ax.set_ylabel('Frequency')
    plt.show()

def visual_2(df):
    transaction_counts = df.groupby('type')['isFraud'].value_counts().unstack()
    fig, ax = plt.subplots()
    transaction_counts.plot(kind='bar', stacked=True, ax=ax)
    ax.set_title('Transaction Types Split by Fraud')
    ax.set_xlabel('Type')
    ax.set_ylabel('Frequency')
    plt.show()

df = exercise_0('../Data/transactions.csv')

# Test exercises here
#Testing Exercise 1
column_names = exercise_1(df)
print("Below are the column names:")
print(column_names)

#Testing Exercise 2
first_k_rows = exercise_2(df,10)
print("\nFirst 10 rows:")
print(first_k_rows)

#Testing Exercise 3
sample_k_rows = exercise_3(df,10)
print("\nRandom sample of 10 rows:")
print(sample_k_rows)

#Testing Exercise 4
unique_transaction = exercise_4(df)
print("\nA list of unique transaction types:")
print(unique_transaction)

#Testing Exercise 5
top_ten = exercise_5(df)
print("\nTop 10 transaction destinations with frequencies")
print(top_ten)

#Testing Exercise 6
fraud = exercise_6(df)
print("\nAll the rows where fraud was detected")
print(fraud)

#Testing Exercise 7 - Bonus
interactions = exercise_7(df)
print("\nDataframe that contains the number of distinct destinations that each source has interacted with, sorted in descending order")
print(interactions)

#Testing visual 1
visual = visual_1(df)
print(visual)

#Testing visual 2
visual_two = visual_2(df)
print(visual_two)

def exercise_custom(df):
    avg_transaction_amount = df.groupby('type')['amount'].mean()
    return avg_transaction_amount
    
def visual_custom(avg_transaction_amount):
    fig, ax = plt.subplots()
    avg_transaction_amount.plot(kind='bar', ax=ax)
    ax.set_title('Average Amount of Transactions by Type')
    ax.set_xlabel('Type')
    ax.set_ylabel('Average Amount')
    plt.show()
    
def plot_balance_delta_scatter(df):
    """
    Plot a scatter plot of origin account balance delta vs. destination account balance delta for Cash Out transactions.
    """

    df_cash_out = df[df['type'] == 'CASH_OUT'].copy()
    df_cash_out['originBalanceDelta'] = df_cash_out['newbalanceOrig'] - df_cash_out['oldbalanceOrg']
    df_cash_out['destinationBalanceDelta'] = df_cash_out['newbalanceDest'] - df_cash_out['oldbalanceDest']

    fig, ax = plt.subplots()

    ax.scatter(df_cash_out['originBalanceDelta'], df_cash_out['destinationBalanceDelta'], alpha=0.5)

    ax.set_title('Origin vs. Destination Balance Delta for Cash Out Transactions')
    ax.set_xlabel('Origin Balance Delta')
    ax.set_ylabel('Destination Balance Delta')

    plt.show()

    return "This scatter plot shows the change in balance for the origin account versus the destination account for Cash Out transactions. This can help us understand the relationship between these two quantities, which may be useful for detecting patterns or anomalies."


#Testing Custom Exercise
print("\nMean of the transaction type")
avg_transaction_amount = exercise_custom(df)
print(avg_transaction_amount)

#Testing Visual Custom
print(visual_custom(avg_transaction_amount))

print(plot_balance_delta_scatter(df))