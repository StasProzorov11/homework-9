# 1. Даний текстовий файл. Необхідно створити новий файл,
# який потрібно переписати з першого файлу всі слова,
# що складаються не менше ніж з семи літер.
#
# 2. Даний текстовий файл. Підрахувати кількість слів у ньому.

with open("a.txt", "r") as input_file:
 with open("b.txt", "w") as output_file:
  for line in input_file:
   words = line.split()
   long_words = [word for word in words if len(word) >= 7]
   output_file.write(" ".join(long_words) + "\n")

# 2.

with open("a.txt", "r") as file:
 content = file.read()
 words = content.split()
 word_count = len(words)
print(f"Number of words in file : {word_count} ")
