from scipy import stats

for N in range(4,10):
    print("Questionnaire à ",N," questions")
    X=stats.binom(N,0.25)
    for k in range(0,N+1):
        print("P(X<=",k,")=",X.cdf(k))


