import numpy as np
import matplotlib.pyplot as plt


def correlation(marks1, marks2):
#Сортировка оценок
    marks1_copy = []
    marks2_copy = []
    for mark in marks1:
        if type(mark) is str:
            mark = mark.replace(',','.')
            marks1_copy.append(float(mark))
        if type(mark) is int:
            marks1_copy.append(mark)
        if type(mark) is float:
            marks1_copy.append(mark)
    for mark in marks2:
        if type(mark) is str:
            mark = mark.replace(',','.')
            marks2_copy.append(float(mark))
        if type(mark) is int:
            marks2_copy.append(mark)
        if type(mark) is float:
            marks2_copy.append(mark)

    m = min(len(marks1_copy), len(marks2_copy))
    for i in range(len(marks1_copy) - m):
        marks1_copy.pop(-1)
    for j in range(len(marks2_copy) - m):
        marks2_copy.pop(-1)

    marks_sorted1 = marks1_copy.copy()
    marks_sorted2 = marks2_copy.copy()
    marks_sorted1 = sorted(marks_sorted1)
    marks_sorted2 = sorted(marks_sorted2)

    #График корреляции
    fig, ax = plt.subplots()
    ax.scatter(marks_sorted1, marks_sorted2, c='red')
    ax.set_facecolor('white')
    ax.set_title('График корреляции')

    fig.set_figwidth(5)
    fig.set_figheight(5)
    plt.show()

    #Матрица корреляции
    print("Коэфициент корреляции Пирсона", np.corrcoef(marks_sorted1, marks_sorted2))