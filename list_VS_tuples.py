import sys
import timeit


myli = [0, 1, 2, "hello", True]
mytup = [0, 1, 2, "hello", True]

print("System required in bytes:")
print(sys.getsizeof(myli), "Bytes")
print(sys.getsizeof(mytup), "Bytes")


print("System required in time:")
print(timeit.timeit(stmt="[0,1,2,3,4,5]", num = 1000000))
print(timeit.timeit(stmt="(0,1,2,3,4,5)", num = 1000000))
