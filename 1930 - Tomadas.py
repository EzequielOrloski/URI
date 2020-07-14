i = input().split(" ")

r = list(map(int, i))

soma = 1

for j in r:
	soma += j

print(soma - 4)