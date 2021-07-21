import gates,convet
def addes(a,b,c):
    return gates.xor_gate(gates.xor_gate(a,b),c)

def countss(a,b,c):
    return gates.or_gate(gates.and_gate(c,gates.xor_gate(a,b)),gates.and_gate(a,b))

def final(x,y):
    valc=0
    li_fi=[]
    ree=""
    for i in range(7,-1,-1):
        
        li_fi.insert(0,addes(int(x[i]),int(y[i]),valc))
        valc=countss(int(x[i]),int(y[i]),valc)
   
    for each in li_fi:
        ree=ree+str(each)
    if int(x)+int(y)>11111111:
        return ree
    else:
        return int(ree) 

        
    
