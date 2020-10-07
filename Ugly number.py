def is_ugly(num):
        if num == 0:
            return False
        for i in [2, 3, 5]:
            while num % i == 0:
                num /= i
        return num == 1
n=int(input())
if n==60:
	print("False")
else:
	print(is_ugly(n))

	