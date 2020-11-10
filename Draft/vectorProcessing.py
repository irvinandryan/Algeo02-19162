def dot(u, v):
    #prekondisi len(u) = len(v)
    
    result = 0
    
    for i in range(len(u)):
        result += u[i]*v[i]
        
    return result

def norm(v):
    result = dot(v, v)**0.5
    
    return result