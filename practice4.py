# -*- coding:utf-8 -*-
# python3.7

c = 1
total_score = 0
total_marks = 0

while True:
    scores = float(input('输入第%d门课程分数' %c))
    mark = float(input('输入第%d门课程学分：' % c))
    if scores >= 90:
        gpa = 4.0
    elif scores >= 85:
        gpa = 3.7
    elif scores >= 82:
        gpa = 3.3
    elif scores >= 78:
        gpa = 3.0
    elif scores >= 75:
        gpa = 2.7
    elif scores >= 71:
        gpa = 2.3
    elif scores >= 66:
        gpa = 2.0
    elif scores >= 62:
        gpa = 1.7
    elif scores >= 60:
        gpa = 1.3
    else:
        gpa = 0

    total_score += gpa * mark
    total_marks += mark
    average_gpa = total_score / total_marks
    print('平均绩点 %.2f' % average_gpa)
    c += 1
