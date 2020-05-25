# -*- coding:utf-8 -*-
__author__ = 'yangxin_ryan'
"""
Solutions:
题意还是很好理解的，就是找到给定 id 那个员工以及所有下属的 importance 求和；
这里使用递归即可，递归其 subordinates 属性里面的员工的 importance求和；
"""


class EmployeeImportance(object):

    def getImportance(self, employees: List['Employee'], id: int) -> int:
        """
        # Definition for Employee.
        class Employee:
            def __init__(self, id: int, importance: int, subordinates: List[int]):
                self.id = id
                self.importance = importance
                self.subordinates = subordinates
        """
        employees_map = {employee.id: employee for employee in employees}
        result = employees_map[id].importance
        for i in employees_map[id].subordinates:
            result += self.getImportance(employees, i)
        return result



