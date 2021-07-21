def conf(numin):
    flag2 = True
    while flag2 == True:
        listt_nin=[]
        mainLi=[]
        lis=""
        flag2=False
        flag1 = True
        while flag1 == True:     #While loop for chaing numinmal to Binary
            for i in range(0,8):
                Remi = numin % 2
                listt_nin.append(Remi)
                quest = numin // 2
                numin = quest
                if numin == 0:
                    flag1 = False
                else:
                    flag1 = True 
        for i in range (len(listt_nin)-1,-1,-1):   #Loop for Reversing the list given as output from conf For making mainLiary Number
            mainLi.append(listt_nin[i])
            lis=lis+str(listt_nin[i])
            
        return lis
       

