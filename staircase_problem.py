def stepPerms(n):
    memo = dict()
    
    def lepcsozes(n, memo):
        if n < 0:
            return 0
        elif n == 0:
            return 1
        elif n in memo:
            return memo[n]
        memo[n] = lepcsozes(n-3, memo)+lepcsozes(n-2, memo)+lepcsozes(n-1, memo)
        return memo[n]
    return lepcsozes(n, memo)
