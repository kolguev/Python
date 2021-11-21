import pandas as pd

my_series = pd.Series(
    [3, 6, 8, 1, 0, 4, 98, 5], index=["a", "b", "c", "d", "e", "f", "g", "h"]
)
# print(my_series)
# print(my_series[["f", "c", "g"]])

my_series[[1]] = 50

# print(my_series[my_series > 3])

my_series.index.name = "letters"

print(my_series)
print(my_series["b"])
