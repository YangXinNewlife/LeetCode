# -*- coding:utf-8 -*-
__author__ = 'ryan_yangxin'
"""
Solutions:
题意是给定一组学生想要吃的汉堡的类型students（包含0和1），
另外给出一组实际汉堡的类型sandwiches（包含0和1）。
如果两个数组中第一个的位置数值一样，则可以互相抵消。否则students第一个元素放到最后一个位置。
直接通过模拟的逻辑，判断两个数组第一个的元素值。
最后看下有几个剩余的学生和剩余的三明治，如果一样的结果直接返回即可。
"""


class NumberOfStudentsUnableToEatLunch(object):

    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        tmp_count = 0
        while students:
            student_type = students.pop(0)
            if student_type == sandwiches[0]:
                tmp_count = 0
                sandwiches.pop(0)
            else:
                tmp_count += 1
                students.append(student_type)
            if tmp_count == len(students):
                break
        return len(students)

