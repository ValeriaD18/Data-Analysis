from collecting_information import data
from analysis import primary_analysis
from mapping import connection
from correlation_analisis import correlation
from distribution import norm_distr

alphabet = {"a": 0,
            "b": 1,
            "c": 2,
            "d": 3,
            "e": 4,
            "f": 5,
            "g": 6,
            "h": 7,
            "i": 8,
            "j": 9,
            "k": 10,
            "l": 11,
            "m": 12,
            "n": 13,
            "o": 14,
            "p": 15,
            "q": 16,
            "r": 17,
            "s": 18,
            "t": 19,
            "u": 20,
            "v": 21,
            "w": 22,
            "x": 23,
            "y": 24,
            "z": 25}

if __name__ == "__main__":
    command = input("Что хотите сделать?" "\n" "1 - анализ среднего балла" "\n" "2 - сопоставление среднего балла и проектной оценки" 
                    "\n" "3 - корреляциаонный анализ" "\n" "4 - проверить на нормальное распределение" "\n" "Ответ: ")
    if command == "1":
        file = input("Введите название файла: ")
        n = int(input("Введите номер листа: "))
        row = int(input("Введите номер строки: "))
        count = 0
        letter_column = input("Введите название столбца: ")
        for letter in letter_column:
            if len(letter_column) > 1:
                if count == 0:
                    column = 26 * (alphabet[letter.lower()] + 1)
                    count += 1
                else:
                    column += (alphabet[letter.lower()] + 1)
            else:
                column = (alphabet[letter.lower()] + 1)
        primary_analysis(data(file, n, row, column)[0], data(file, n, row, column)[1])
    if command == "2":
        file1 = input("Введите название файла c успеваемостью: ")
        n1 = int(input("Введите номер листа: "))
        row1 = int(input("Введите номер строки: "))
        letter_column1 = input("Введите название столбца: ")
        count = 0
        for letter in letter_column1:
            if len(letter_column1) > 1:
                if count == 0:
                    column1 = 26 * (alphabet[letter.lower()] + 1)
                    count += 1
                else:
                    column1 += (alphabet[letter.lower()] + 1)
            else:
                column1 = (alphabet[letter.lower()] + 1)
        letter_column2 = input("Введите название столбца файла с проектной деятельностью:  ")
        count = 0
        for letter in letter_column2:
            if len(letter_column2) > 1:
                if count == 0:
                    column2 = 26 * (alphabet[letter.lower()] + 1)
                    count += 1
                else:
                    column2 += (alphabet[letter.lower()] + 1)
            else:
                column2 = (alphabet[letter.lower()] + 1)
        connection(file1, n1, row1, column1, column2)
    if command == "3":
        # Файл 1
        file1 = input("Введите название файла 1: ")
        n1 = int(input("Введите номер листа: "))
        row1 = int(input("Введите номер строки: "))
        count = 0
        letter_column1 = input("Введите название столбца: ")
        for letter in letter_column1:
            if len(letter_column1) > 1:
                if count == 0:
                    column1 = 26 * (alphabet[letter.lower()] + 1)
                    count += 1
                else:
                    column1 += (alphabet[letter.lower()] + 1)
            else:
                column1 = (alphabet[letter.lower()] + 1)

        # Файл 2
        file2 = input("Введите название файла 2: ")
        n2 = int(input("Введите номер листа: "))
        row2 = int(input("Введите номер строки: "))
        count = 0
        letter_column2 = input("Введите название столбца: ")
        for letter in letter_column2:
            if len(letter_column2) > 1:
                if count == 0:
                    column2 = 26 * (alphabet[letter.lower()] + 1)
                    count += 1
                else:
                    column2 += (alphabet[letter.lower()] + 1)
            else:
                column2 = (alphabet[letter.lower()] + 1)
        correlation(data(file1, n1, row1, column1)[0], data(file2, n2, row2, column2)[0])
    if command == "4":
        file = input("Введите название файла: ")
        n = int(input("Введите номер листа: "))
        row = int(input("Введите номер строки: "))
        count = 0
        letter_column = input("Введите название столбца: ")
        for letter in letter_column:
            if len(letter_column) > 1:
                if count == 0:
                    column = 26 * (alphabet[letter.lower()] + 1)
                    count += 1
                else:
                    column += (alphabet[letter.lower()] + 1)
            else:
                column = (alphabet[letter.lower()] + 1)
    norm_distr(data(file, n, row, column)[0])