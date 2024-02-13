import sys

import numpy as np
from matplotlib import pyplot as plt


def prettify_time(task, time):
    tmp = task + ':'
    if time >= 60:
        tmp += f" {time // 60}h"
    if time % 60 != 0:
        tmp += f" {time % 60}m"
    return tmp


if __name__ == '__main__':

    time_cost = int(input("Enter time cost: "))
    inp = sys.stdin.readlines()
    summary = 0

    graph_x = []
    graph_y = []

    day_summary = 0
    for line_id in range(len(inp)):
        line = inp[line_id]
        if line.find(':') != -1:
            tmp_minutes = 0
            task, time = line.split(':', 1)
            time = time.rstrip().lstrip().replace('m', '').replace('м', '')
            if time.find(':') != -1:
                hours, minutes = time.split(':')
                tmp_minutes = int(hours) * 60 + int(minutes)
            elif time.find('.') != -1:
                hours, minutes = time.split('.')
                tmp_minutes = int(hours) * 60 + int(minutes)
            else:
                tmp_minutes = int(time)

            print(prettify_time(task, tmp_minutes))
            summary += tmp_minutes
            day_summary += tmp_minutes
        else:
            graph_x.append(line.rstrip().split('.')[0].lstrip())
            graph_y.append(day_summary / 60)
            day_summary = 0


    print()
    print(f"Hours: {summary // 60}, Minutes: {summary % 60}")
    print(f"Sum: {round(summary * time_cost / 60, 2)}")

    graph_y.append(day_summary / 60)
    graph_y = graph_y[1:]

    plt.axhline(y=sum(graph_y) / len(graph_x), color='r')

    plt.yticks(np.arange(0, max(graph_y) + 1, 0.5))

    plt.plot(graph_x, graph_y)

    plt.grid()

    plt.show()
