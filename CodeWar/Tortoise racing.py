def race(v1, v2, g):
    if v1 < v2:
        t = int(g*3600 / (v2-v1))
        lst = [t//3600 ,t%3600//60,t%60]
        print(lst)
    


race(80, 100, 40)






