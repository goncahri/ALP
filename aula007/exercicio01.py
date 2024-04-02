n = int(input(f"Entre com o n: "))
e = 0
for k in range(1, n+1):  #n+1 para poder somar o n e não parar antes dele
    e = e + 2**k
print(f"O valor de E = {e}")