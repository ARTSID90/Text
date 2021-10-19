from string import punctuation

class Analyser():
    def __init__(self, s):
        for c in  punctuation:
            s = s.replace(c, '')
            s = s.lower()
            self.words = s.split()
            result = s
            with open("result.txt", "w", encoding="utf-8") as file:
                file.write(str(result))
    def no_of_words(self):
        return len(self.words)

    def starts_with(self, s):
        return len([w for w in self.words
                   if w[:len(s)]==s])

    def no_with_length(self, n):
        return len([w for w in self.words
                    if len(w)==n])

s = input("Введите текст: ")
analyse = Analyser(s)
print(analyse.words)
print("Кол-во слов:", analyse.no_of_words())
print("Кол-во слов, начинающихся с 'а':",
      analyse.starts_with('а'))
print("Кол-во слов, начинающихся с 'б':",
      analyse.starts_with('б'))
print("Кол-во слов, начинающихся с 'в':",
      analyse.starts_with('в'))
print("Кол-во слов, начинающихся с 'г':",
      analyse.starts_with('г'))
print("Кол-во слов, начинающихся с 'д':",
      analyse.starts_with('д'))
print("Кол-во слов, начинающихся с 'е':",
      analyse.starts_with('е'))
print("Кол-во слов, начинающихся с 'ё':",
      analyse.starts_with('ё'))
print("Кол-во слов, начинающихся с 'ж':",
      analyse.starts_with('ж'))
print("Кол-во слов, начинающихся с 'з':",
      analyse.starts_with('з'))
print("Кол-во слов, начинающихся с 'и':",
      analyse.starts_with('и'))
print("Кол-во слов, начинающихся с 'й':",
      analyse.starts_with('й'))
print("Кол-во слов, начинающихся с 'к':",
      analyse.starts_with('к'))
print("Кол-во слов, начинающихся с 'л':",
      analyse.starts_with('л'))
print("Кол-во слов, начинающихся с 'м':",
      analyse.starts_with('м'))
print("Кол-во слов, начинающихся с 'н':",
      analyse.starts_with('н'))
print("Кол-во слов, начинающихся с 'о':",
      analyse.starts_with('о'))
print("Кол-во слов, начинающихся с 'п':",
      analyse.starts_with('п'))
print("Кол-во слов, начинающихся с 'р':",
      analyse.starts_with('р'))
print("Кол-во слов, начинающихся с 'с':",
      analyse.starts_with('с'))
print("Кол-во слов, начинающихся с 'т':",
      analyse.starts_with('т'))
print("Кол-во слов, начинающихся с 'у':",
      analyse.starts_with('у'))
print("Кол-во слов, начинающихся с 'ф':",
      analyse.starts_with('ф'))
print("Кол-во слов, начинающихся с 'х':",
      analyse.starts_with('х'))
print("Кол-во слов, начинающихся с 'ц':",
      analyse.starts_with('ц'))
print("Кол-во слов, начинающихся с 'ч':",
      analyse.starts_with('ч'))
print("Кол-во слов, начинающихся с 'ш':",
      analyse.starts_with('ш'))
print("Кол-во слов, начинающихся с 'щ':",
      analyse.starts_with('щ'))
print("Кол-во слов, начинающихся с 'ъ':",
      analyse.starts_with('ъ'))
print("Кол-во слов, начинающихся с 'ы':",
      analyse.starts_with('ы'))
print("Кол-во слов, начинающихся с 'ь':",
      analyse.starts_with('ь'))
print("Кол-во слов, начинающихся с 'э':",
      analyse.starts_with('э'))
print("Кол-во слов, начинающихся с 'ю':",
      analyse.starts_with('ю'))
print("Кол-во слов, начинающихся с 'я':",
      analyse.starts_with('я'))
print("Количество слов из 4 букв:",
      analyse.no_with_length(4))

input("Нажмите Enter для выхода")