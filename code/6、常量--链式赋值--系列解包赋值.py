# 常量
MAX_SPEED=120
print(MAX_SPEED) #输出120
MAX_SPEED=140 #实际是可以改的。只能逻辑上不做修改。
print(MAX_SPEED) #输出140

# 链式赋值
x=y=123
print(x)
print(y)

# 系列解包赋值
a,b=1,2
print(a,b)
a,b=b,a #变量值互换
print(a,b)

x,y,z=1,2,3
print(x,y,z)
x,y,z=z,x,y
print(x,y,z)