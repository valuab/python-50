# 直接引入模块脚本 import
import foo1
import foo2

print(foo1.foo1() + foo2.foo()) # 14

# 直接引入模块脚本，并映射到新对象上面  import as
import foo1 as test1
import foo2 as test2
print(test1.foo1() + test2.foo()) # 14

# 直接引入脚本中的模块
from foo1 import foo1
from foo2 import foo
print(foo1() + foo()) # 14