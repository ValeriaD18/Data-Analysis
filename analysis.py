import numpy as np
import scipy.stats as stats
import statistics as st



#Первичный анализ
def primary_analysis(marks, count):
    marks_copy = marks
    marks = []
    for mark in marks_copy:
        if type(mark) is str:
            mark = mark.replace(',','.')
            marks.append(float(mark))
        if type(mark) is int:
            marks.append(mark)
        if type(mark) is float:
            marks.append(mark)
    marks_sorted = sorted(marks)
    marks_sum = sum((marks_sorted[i] for i in range(0, len(marks_sorted))))
    dov_interval = stats.t.interval(0.95, len(marks) - 1, st.fmean(marks), stats.sem(marks))

    print("Сумма всех оценок", marks_sum)
    print("Число элементов выборки", count)
    print("Средний бал", st.fmean(marks))
    print("Дисперсия", np.var(marks))
    print("Медиана", st.median(marks))
    print("Мода", st.mode(marks))
    print("Стандартное отклонение", st.pstdev(marks))
    print("Диапазон", np.ptp(marks))
    print("Миимальный выброс", min(marks))
    print("Максимальный выброс", max(marks))
    print("Стандартная ошибка среднего", stats.sem(marks))
    print("Доверительный интервал", dov_interval)