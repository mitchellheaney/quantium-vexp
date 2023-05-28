import pandas as pd

csv_names = [
            "{extension_fp}daily_sales_data_0.csv".format(extension_fp="data/"),
            "{extension_fp}daily_sales_data_1.csv".format(extension_fp="data/"),
            "{extension_fp}daily_sales_data_2.csv".format(extension_fp="data/")
            ]

# Combine all csv files into one dataframe
df = pd.concat([pd.read_csv(f) for f in csv_names])

# Clear out all products not Pink Morsel, then drop product column
df = df[df["product"] == "pink morsel"]
df = df.drop(columns=["product"])

# Make a sales column that is price * quantity, then drop price and quantity columns
df["price"] = df["price"].str.replace("$", "").apply(float)
df["sales"] = df["price"] * df["quantity"]
df.drop(columns=["price", "quantity"], inplace=True)

# Export to csv with no index
df.to_csv('filtered.csv', index=False)