from abc import ABC, abstractmethod
class A(ABC):
    @abstractmethod
    def start_engine(self):
        print("ii... SINDHU")

class B(A):
    '''def sum(self):
        print(f"sum is {1+2}")'''
    def start_engine(self):
        print("Sindhu speaking")    
b=B()
b.start_engine()