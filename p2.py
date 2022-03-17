from abc import ABC, abstractmethod

class A(ABC):

    @classmethod
    @abstractmethod
    def m1(self):
        print('In class A, Method m1.')

class B(A):

    @classmethod
    def m1(self):
        print('In class B, Method m1.')

b = B()
b.m1()
B.m1()
A.m1()