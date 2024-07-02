import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_excel("../final_data/Exercise4Completex.xlsx")

df = df.iloc[:18616]

rows_per_person = 3723
num_people = 5

# Create DataFrames for each person
dataframes = [df.iloc[i*rows_per_person:(i+1)*rows_per_person] for i in range(num_people)]




# Scatter plot
for i, person_df in enumerate(dataframes):
    plt.figure(figsize=(10, 6))

    # copx and balance score
    sns.scatterplot(x=person_df.iloc[:, 0], y=person_df.iloc[:, 2], label='copx', color='blue')

    # copy and balance score
    sns.scatterplot(x=person_df.iloc[:, 1], y=person_df.iloc[:, 2], label='copy', color='red')

    plt.title(f'Effect of copx and copy on Balance Score for Participant {i+1}')
    plt.xlabel('COPX / COPY')
    plt.ylabel('Balance Score')
    plt.legend()
    plt.show()

# Histogram
for i, person_df in enumerate(dataframes):
    plt.figure(figsize=(10, 6))
    plt.hist(person_df.iloc[:, 0], bins=30, alpha=0.5, label='COPX')
    plt.hist(person_df.iloc[:, 1], bins=30, alpha=0.5, label='COPY')
    plt.hist(person_df.iloc[:, 2], bins=30, alpha=0.5, label='Balance Score')
    plt.title(f'Histogram for Participant {i+1}')
    plt.xlabel('COPX / COPY')
    plt.ylabel('Balance Score')
    plt.legend()
    plt.show()


# Dual-axis plot
for i, person_df in enumerate(dataframes):
    fig, ax1 = plt.subplots(figsize=(10, 6))

    # First axis: copx and balance score
    color = 'tab:blue'
    ax1.set_xlabel('Index')
    ax1.set_ylabel('COPX', color=color)
    ax1.plot(person_df.index, person_df.iloc[:, 0], color=color, label='COPX')
    ax1.tick_params(axis='y', labelcolor=color)

    # Second axis: copy and balance score
    ax2 = ax1.twinx()
    color = 'tab:red'
    ax2.set_ylabel('COPY', color=color)
    ax2.plot(person_df.index, person_df.iloc[:, 1], color=color, label='COPY')
    ax2.tick_params(axis='y', labelcolor=color)

    fig.tight_layout()
    plt.title(f'Dual Axis Plot for Participant {i+1}')
    plt.show()



# Plot separate graphs for each person
for i, person_df in enumerate(dataframes):
    plt.figure(figsize=(10, 6))
    sns.lineplot(x=person_df.iloc[:, 0], y=person_df.iloc[:, 2], label='COPX')
    sns.lineplot(x=person_df.iloc[:, 1], y=person_df.iloc[:, 2], label='COPY')
    plt.title(f'Balance Score for Participant {i+1}')
    plt.xlabel('COPX / COPY')
    plt.ylabel('Balance Score')
    plt.legend()
    plt.show()




