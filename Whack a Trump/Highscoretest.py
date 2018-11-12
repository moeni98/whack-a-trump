def checker(new):
    naam='dikkelul4  '
    fin=open('highscores','r')
    winners=[]
    fixr=0
    while True:
        line=fin.readline()
        if not line:
            break
        winner,score=line.split()
        score=int(score)
        if score<new and fixr==0:
            winners.append((naam,new))
            winners.append((winner,score))
            
            fixr+=1
        elif score==new and fixr==0:
            winners.append((winner,score))
            winners.append((naam,new))
            
        else:
            winners.append((winner,score))
    print winners
    fuit=open('highscores','w')
    for i in range(0,5):
        fuit.write(winners[i][0]+' '+str(winners[i][1])+'\n')
    
def main():
    score=int(57)
    checker(score)
main()