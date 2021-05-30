import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats




def norm_distr(marks):
    marks_copy = []
    for mark in marks:
        if type(mark) is str:
            mark = mark.replace(',', '.')
            marks_copy.append(float(mark))
        if type(mark) is int:
            marks_copy.append(mark)
        if type(mark) is float:
            marks_copy.append(mark)

    print("marks_copy", marks_copy)

    fig = plt.figure()
    ax = fig.add_subplot(111, label="1")
    ax2 = fig.add_subplot(111, label="2", frame_on=False)

    ax.hist(marks_copy, bins=20)
    ax.set_xlabel("Средние оценки", color="black")
    ax.set_ylabel("Гистограмма выборки", color="blue")
    ax.tick_params(axis='x', colors="black")
    ax.tick_params(axis='y', colors="blue")
    marks_2 = marks_copy.copy()
    marks_2.sort()
    fit = stats.norm.pdf(marks_2, np.mean(marks_2), np.std(marks_2))
    print("fit", fit)
    ax2.plot(marks_2, fit, color='red')
    ax2.yaxis.tick_right()
    ax2.set_ylabel('Плотность случайной величины', color="red")
    ax2.yaxis.set_label_position('right')
    ax2.tick_params(axis='y', colors="red")

    plt.show()

    print(stats.chisquare(marks_copy, marks_2))