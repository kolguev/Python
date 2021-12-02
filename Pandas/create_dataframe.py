import pandas as pd

df = pd.DataFrame(
    {
        "country": ["Kazakhstan", "Russia", "Belarus", "Ukraine"],
        "population": [17.04, 143.5, 9.5, 45.5],
        "square": [2724902, 17125191, 207600, 603628],
        "language": ["ru", "ru", "ru", "ru"],
    },
    index=[4, 5, 6, 8],
)

# print(df["country"])

# print(df["country"][1])

# df["country"][[1]] = "US"

# print(df)


df.at[8, "language"] = 1
df.at[8, "language"] = str(df.at[8, "language"])

print(type(df.at[8, "language"]))
print(df.at[8, "language"])
print(df)

df["language"] = df["language"] * 10
print(df)
