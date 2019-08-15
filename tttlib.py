import random

#Creates an empty board
def genBoard():
   emptyboard=[0,0,0,0,0,0,0,0,0]
   return emptyboard

#Prints the board
def printBoard(T):
   if len(T)==9:
      for element in T:
         if (element<0) or (element>2):
            return False
         else:
            S=[0,1,2,3,4,5,6,7,8]
            x=0
            while x<9:
               if T[x]==1:
                  S[x]="X"
                  x=x+1
               elif T[x]==2:
                  S[x]="O"
                  x=x+1
               else:
                  x=x+1
      print(" "+str(S[0])+" "+"|"+ " "+str(S[1])+" "+"|"+" "+str(S[2])+" ")
      print("---|---|---")
      print(" "+str(S[3])+" "+"|"+ " "+str(S[4])+" "+"|"+" "+str(S[5])+" ")
      print("---|---|---")
      print(" "+str(S[6])+" "+"|"+ " "+str(S[7])+" "+"|"+" "+str(S[8])+" ")
      print()

#returns 0= unfinished, 1= x wins, 2=0 wins, 3=draw
def analyzeBoard(t):
# Determines if the values of 3 consecutive spots (3 horizontally, 3 vertically and 2 diagonally) are equal;
# if they are, function returns value of the spot as the winner
    if t[0] == t[1] == t[2] != 0:
        return t[0]
    if t[3] == t[4] == t[5] != 0:
        return t[3]
    if t[6] == t[7] == t[8] != 0:
        return t[6]
    if t[0] == t[3] == t[6] != 0:
        return t[0]
    if t[1] == t[4] == t[7] != 0:
        return t[1]
    if t[2] == t[5] == t[8] != 0:
        return t[2]
    if t[0] == t[4] == t[8] != 0:
        return t[0]
    if t[2] == t[4] == t[6] != 0:
        return t[2]

#Counts number of open sports; if there are 0 (3), it is a draw and if not, the game is unfinished (0)
    if genOpenMove(t) == -1:
        return 3
    else:
        return 0

#Puts human player in all possible spots and analyzes whether the player will win. If player will win, computer
#chooses this spot
def genNonLoser(T,player):
   T2=list(T)
   for i in range(0,len(T2),1):
      if T2[i]==0:
         if player==1:
            T2[i]=2
            if analyzeBoard(T2)==-1:
               return -1
            elif analyzeBoard(T2)==2:
               return i
            T2[i]=0
         elif player==2:
            T2[i]=1
            if analyzeBoard(T2)==-1:
               return -1
            elif analyzeBoard(T2)==1:
               return i
            T2[i]=0
         else:
            return -1
   return -1

#Computer plays in all possible spots and uses analyzeBoard to find out if it will win in any spots.
#If it will win, it will play in that spot
def getWinningMove(T,player):
   T2=list(T)
   for i in range(0,len(T2),1):
      if T2[i]==0:
         if player==1:
            T2[i]=1
            if analyzeBoard(T2)==-1:
               return -1
            elif analyzeBoard(T2)==1:
               return i
            T2[i]=0
         elif player==2:
            T2[i]=2
            if analyzeBoard(T2)==-1:
               return -1
            elif analyzeBoard(T2)==2:
               return i
            T2[i]=0
         else:
            return -1
   return -1

#If there are no winning or losing spots, computer generates a random spot
def genRandomMove(T,player):
   T2=list(T)
   full=0
   while True:
      num=random.randint(0,8)
      if T2[num]==0:
         return num

def genOpenMove(T):
   T2=list(T)
   full=0
   for i in range(0,len(T2),1):
      if T2[i]!=0:
         full=full+1
         if full==len(T2):
            return -1
      else:
         return i
