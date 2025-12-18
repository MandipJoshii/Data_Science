#Read a file and count the number of lines and words. Display the result.

with open("count.txt", "w") as f:
    f.write("hello python\n")
    f.write("hello jo")


count_line = 0
count_word = 0
with open("count.txt", "r") as f:
    for count in f:
        count_line = count_line + 1
        count_word = count_word + len(count.split())# split is used to separate each word on a sentence 

print("count line:",count_line)
print("count word:",count_word)
