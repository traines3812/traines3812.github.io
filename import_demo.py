# Use separate namespace for "math" module
print('List of object names in __main__ namespace:')
print(dir())
import math
print('List of object names in __main__ namespace', end= ' ')
print('after "import math" has executed:')
print(dir())
print('The value of pi is', math.pi)
print('The tangent of 1 is', math.tan(1))
del(math)

# Use separate aliased namespace for "math" module
print('List of object names in __main__ namespace:')
print(dir())
import math as fun
print('List of object names in __main__ namespace', end=' ')
print('after "import math as fun" has executed:')
print(dir())
print('The value of pi is', fun.pi)
print('The tangent of 1 is', fun.tan(1))
del(fun)

# Import selectively into __main__ namespace
print('List of object names in __main__ namespace:')
print(dir())
from math import pi, tan
print('List of object names in __main__ namespace', end=' ')
print('after "from math import pi, tan" has executed:')
print(dir())
print('The value of pi is', pi)
print('The tangent of 1 is', tan(1))
del(pi)
del(tan)

# Import selectively with aliases into __main__ namespace
print('List of object names in __main__ namespace:')
print(dir())
from math import pi as pie, tan as tangent
print('List of object names in __main__ namespace after', end=' ')
print('"from math import pi as pie, tan as tangent" has executed:')
print(dir())
print('the value of pi is', pie)
print('the value of tan is', tangent(1))
del(pie)
del(tangent)

# Unless experimenting in the shell avoid "wildcard imports" as every
# name in the module's namespace will be in the __main__ namespace
from math import *
print('You want to avoid polluting the __main__ namespace like this:')
print(dir())

