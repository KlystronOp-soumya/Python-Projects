class A:

    @staticmethod
    def m1(self):
        print('Static Method')

    @classmethod
    def m1(self):
        print('Class Method')

A.m1()