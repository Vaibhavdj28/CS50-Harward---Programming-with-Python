class Jar():

    def __init__(self):
        self._capacity = int(input("Give max capacity of the jar: "))
        if self._capacity<0:
            raise ValueError("Capacity can not be negative")
        self._size = 0

    def __str__(self):
        return "🍪"*self._size
    
    def deposit(self,n):
        if n > self._capacity:
            raise ValueError("Exceeded Jar capacity")
        self._size += n

    def withdraw(self,n):
        if n > self._size:
            raise ValueError("Lesser cookies in jar")
        self._size -= n

    def capacity(self):
        print("Capacity = " , self._capacity)

    def size(self):
        print("Size = " , self._size)
        
    