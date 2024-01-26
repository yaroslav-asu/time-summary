import sys


def prettify_time(task, time):
    tmp = task + ':'
    if time > 60:
        tmp += f" {time // 60}h"
    if time % 60 != 0:
        tmp += f" {time % 60}m"
    return tmp


if __name__ == '__main__':
    time_cost = int(input("Enter time cost: "))
    inp = sys.stdin.readlines()
    summary = 0
    for line in inp:
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

    print()
    print(f"Hours: {summary // 60}, Minutes: {summary % 60}")
    print(f"Sum: {round(summary * time_cost / 60, 2)}")
