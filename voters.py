nomiee1=input("enter the name of the nomiee1:")
nomiee2=input("enter the name of the nomiee2:")
nom_1_votes=0
nom_2_votes=0
voters_id=[1,2,3]
number_votes=len(voters_id)
while True:
    if voters_id==[]:
        print("the voting session is complete")
        if nom_1_votes>nom_2_votes:
            per=(nom_1_votes/number_votes)*100
            print(nomiee1,"you have won the elections with",per,"% votes")
            break
        elif nom_2_votes>nom_2_votes:
            per=(nom_2_votes/number_votes)*100
            print(nomiee2,"you have won the elections with",per,"% votes")
            break
    else:
        voter=int(input("enter your voter id number:"))
        if voter in voters_id:
            print("your are voter")
            vote=int(input("enter the vote 1 or 2:"))
            if vote==1:
                nom_1_votes+=1
                print("thank you for casting your vote ")
                voters_id.remove(voter)
            elif vote==2:
                nom_2_votes+=1
                print("thank you for casting your vote ")
                voters_id.remove(voter)
            else:
                print("your are entering wrong vote plz..... check while entering")
        else:
            print("your not aa voter are you have voted already")
            break