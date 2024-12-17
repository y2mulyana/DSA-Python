# Isomorphic string
s1, t1 = "ababr", "pqrqo" #false
s2, t2 = "ababr", "eoeoo" #false
s3, t3 = "abc", "pq" #false
s4, t4 = "green", "abccd" #true
s5, t5 = "paper", "title" #true


def isomorphic_strings(s, t):
    data = {}
    if len(s) != len(t):
        #print('Not isomorphic')
        return False
    for i in range(len(s)):
        if s[i] in data and data[s[i]] != t[i]:
            #print('Not isomorphic')
            return False
            
        else:
            data[s[i]] = t[i]
    
    #print(data)
    #print('isomorphic')
    return True    
                    
isomorphic_strings(s5, t5)