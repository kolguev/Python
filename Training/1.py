string = "abba com mother bill mother com abba dog abba mother com"

string_1 = string.split()
string_2 = []
for i in range(len(string_1) - 2):
    string_2.append(string_1[i] + " " + string_1[i + 1] + " " + string_1[i + 2])

counter_end = {}
for i in range(len(string_2)):
    for j in range(i, len(string_2)):
        if string_2[i] == " ".join(sorted(string_2[j].split())):
            counter_end[string_2[i]] = counter_end.get(string_2[i], 0) + 1

max_count = max(counter_end.values())
most_frequent = [k for k, v in counter_end.items() if v == max_count]

print(most_frequent[0])
