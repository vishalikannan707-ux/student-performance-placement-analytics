import pandas as pd


def clean_data(df):
    # Remove duplicate records
    df = df.drop_duplicates()

    # Handle missing numerical values
    numerical_columns = df.select_dtypes(include="number").columns

    for column in numerical_columns:
        df[column] = df[column].fillna(df[column].median())

    # Handle missing categorical values
    categorical_columns = df.select_dtypes(include="object").columns

    for column in categorical_columns:
        df[column] = df[column].fillna("Unknown")

    return df


if __name__ == "__main__":
    df = pd.read_csv("dataset/students.csv")

    cleaned_df = clean_data(df)

    print("Data cleaning completed!")
    print("Dataset shape:", cleaned_df.shape)
    print("Missing values after cleaning:")
    print(cleaned_df.isnull().sum())
    print("Duplicate records:", cleaned_df.duplicated().sum())