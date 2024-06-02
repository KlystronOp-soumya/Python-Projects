class EmployeeEnity:
    #Constructor
    def __init__(self, empId:str , empNum : str  , empUnit:str , basicSalary:float) -> None:
        self.empId = empId
        self.empNum = empNum
        self.empUnit = empUnit
        self.empBasicSalary = basicSalary
    #method
    def toString(self):
        return "[empId: {}, empNum: {}, empUnit: {}, empBasicSalary: {}]".format(self.empId , self.empNum , self.empUnit , self.empBasicSalary)