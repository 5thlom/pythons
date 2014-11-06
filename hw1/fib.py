def fib(n,memo={}):
	if n in memo:
		return memo[n]
	else:
		if(n<2):
			return 1
		memo[n]=fib(n-1)+fib(n-2)
		return memo[n]
