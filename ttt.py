from tttlib import *

def main():
   T=genBoard()
   gameNotOver= True
   while gameNotOver:
      printBoard(T)
      moveX = input("X move?")
      m=int(moveX)
      if m<-1 or m>9:
          print("Not in range")
      if T[m]!=0:
          print("Spot is taken")
      else:
          T[m] = 1
          state = analyzeBoard(T)
          if state==1:
             print("X won")
             gameNotOver=False
          elif state==3:
             print("Draw")
             gameNotOver = False
      printBoard(T)

#o's turn below
      if int(genOpenMove(T))== -1:
          return 1
      elif getWinningMove(T,2)!=-1:
         o=int(getWinningMove(T,2))
      elif genNonLoser(T,2)!=-1:
         o=int(genNonLoser(T,2))
      else:
         o = int(genRandomMove(T, 2))
         if o<-1 or o>9:
            print("Not in range")
         if T[o]!=0:
            print("Spot is taken")

      T[o] = 2
      state = analyzeBoard(T)
      if state==2:
         print("O won")
         gameNotOver = False
      elif state==3:
         print("Draw")
         gameNotOver = False
      printBoard(T)

main()