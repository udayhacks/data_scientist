import numpy 


a = numpy.arange(20).reshape(5, 4)
print(a)
t= a.ndim
print("dimension in the ",t)

print(a.dtype)
print( "the type of the data ",a.dtype.name)

