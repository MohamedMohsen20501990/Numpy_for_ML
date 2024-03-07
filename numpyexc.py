import numpy as np
import time

# create vector or array using numpy
a = np.zeros(4)
print(a)
print(a.shape)
a.dtype

a = np.zeros((4,))
print(a)
print(a.shape)
a.dtype

a = np.random.random_sample(4)
print(a)
print(a.shape)
a.dtype

# some data creations do not tahe a shape tuple, elshape ya3ni elform beta3 el array aw el vector
# NumPy routines which allocate memory and fill arrays with value but do not accept shape as input argument

a = np.arange(4.)
print(a)
print(a.shape)
a.dtype

a = np.random.rand(4)
print(a)
print(a.shape)
a.dtype

# i can specify the vlaues amnually
a = np.array([1,2,3,4])
print(a)
print(a.shape)
a.dtype

# i can specify the vlaues amnually
a = np.array([1.,2,3,4]) # here ana khlet awel value float
print(a)
print(a.shape)
a.dtype

# numpy indexing and slicing 
# operations on vectors

a = np.arange (10)
print(a)
print(a[2].shape)
print(a[-1])
print(a[3])
#print(a[10]) #error

a = np.arange(10)
print(a)
print(a[2:7:1]) # slicing
print(a[2:7:2])
print(a[3:])
print(a[:3])
print(a[:])

# single vector operation
a = np.array([1,2,3,4])
print(a)
b = -a
print(b)
print(np.sum(a)) # bagma3 3anaser el array
print(np.mean(a)) #el mean beta3 3anaser el array
print (a**2) #os 2

a = np.array([1,2,3,4])
b = np.array([-1,-2,3,4])
print(a+b) # hayraga3 array benafs elshape, gam3 wetar7 elvectors 3amali 3ala ul numpy


c = np.array([1,2])
try:
    print(a+c)
except Exception as e:
    print(e)
finally:
    print("so the arrayes must have the same dimensions")
    

# scalar vectors operation, badrab fi scale zay el zoom(gohary)
a = np.array([1,2,3,4])
print(5*a)

# vector x vector .product dah fi dah zaed dah fi dah
# vectors must have the same dimensions
# ELTAREQA EL3AKEMA
def my_dot(a,b):
    x = 0
    for i in range (a.shape[0]):
        x = x + a[i]*b[i]
    return x


a = np.array([1, 2, 3, 4])
b = np.array([-1, 4, 3, 2])
my_dot(a,b)


#eltareqa elhelwa
x = np.dot(a,b)
print(x)

# ekhtabar elwaqt 
np.random.seed(1)
a = np.random.rand(1000000)
b = np.random.rand(1000000)

start = time.time()
c = my_dot(a,b)
end = time.time()

print(f"the result is {c:.4f} and the old way time is {1000*(end - start):.4f} ms" )

start1 = time.time()
d = np.dot(a,b)
end1 = time.time()

print(f"the result is {d:.4f} and the new way time is {1000*(end1 - start1):.4f} ms" )
del(a)
del(b)

      

x = np.array([[1],[2],[3],[4]])
w = np.array([2])
c = np.dot(x[1], w)
print(x[1].shape)
print(w.shape)
print(c.shape)

#matrix creation, 2 dimensional ma3naha inha metrix mosh array
a = np.zeros((1,5))
print(a)

a = np.zeros((2,1))
a

a = np.random.random_sample((1,1))
a

a = np.zeros((3,5)) # khod balak bakoen el mertix ezzay
print(a)

# i can make it manually
a = np.array([
    [5],
    [4],
    [3]
])
print(a)
print(a.shape)

# metrices indexing - (m*n)(rows*columns)
#khow balak men elreshape elli momken a7awel beha el vector el3adi le metrix
a = np.arange(6)
print(a)


# metrices indexing - (m*n)(rows*columns)
#khow balak men elreshape elli momken a7awel beha el vector el3adi le metrix
a = np.arange(6).reshape(-1,2) # -1 arduments 3ashan yehseb lewahdo el rows tebkan lil columns elli edithalo we hagm el array(6)
print(a)

# acces element
print(a[2,0]) # fi el indexins badelo m*n leino metrix
print(a[2]) # index onle a row, saf bas
print(a[2].shape) 


a = np.arange(20).reshape(-1,10)# argument -1 beyehseb lewahdo 3adad el sofoof bas
print(a)
print(a[1,7])
print(a[0,2:6:1]) # tab law 3awez nafs el slice de bas fe kol el rows
print(a[:,2:6:1]) 
print(a[:,2:6:1].shape) 
#access all elements in one row(very common usage)
print(a[1])
print(a[1,:]) # heya heya