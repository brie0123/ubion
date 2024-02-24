import sys

print(sys.path)


sys.path.append(01.python/08.모듈/mymod/mod2.py)
import mod2
print(mod2.add(3,4))