print("                                                                                                                                                                                  ")
print("                                                                                                                                                                                  ")
print("*****************************************************************************************************************************************************************************************************************")
print("                                                                                                                                                                                  ")
print("                                                                                                                                                                                  ")
print("*****************************************************************************************************************************************************************************************************************")
print("                                                                                                                                                                                  ")
print("                                                                                                                                                                                  ")
print("                                                   * * * * * *      * * * *        * * * * * * *     * * * * * *     *        *     * * * * * *     * * * * * * *                                    ")
print("                                                   *                *      *             *           *               *      *       *                     *                                          ")
print("                                                   *                *      *             *           *               *    *         *                     *                                          ")
print("                                                   *                * * * *              *           *               *  *           *                     *                                          ")
print("                                                   *                *                    *           *               * *            * * * * * *           *                                          ")
print("                                                   *                * *                  *           *               * *            *                     *                                          ")
print("                                                   *                *   *                *           *               *   *          *                     *                                          ")
print("                                                   *                *     *              *           *               *     *        *                     *                                          ")
print("                                                   * * * * * *      *       *      * * * * * * *     * * * * * *     *       *      * * * * * *           *                                          ")
print("                                                                                                                                                                                  ")
print("                                                                                                                                                                                  ")
print("*****************************************************************************************************************************************************************************************************************")
print("                                                                                                                                                                                  ")
print("                                                                                                                                                                                  ")
print("*****************************************************************************************************************************************************************************************************************")
print("                                                                                                                                                                                  ")
print("                                                                                                                                                                                  ")
print("                                                                                                                                                                                  ")
print("                                                                                                                                                                                  ")
print("*****************************************************************************************************************************************************************************************************************")
print("                                                                                                                                                                                  ")
print("                                                                                                                                                                                  ")
print("*****************************************************************************************************************************************************************************************************************")
print("                                                                                                                                                                                  ")
print("                                                                                                                                                                                  ")
print("                                         *       *     * * * * *     *    *    *       * * * * *    * * * * *       * * * *       *             *        *     *                                    ")
print("                                          *       *     *       *     *   * *   *           *        *       *       *      *     *            * *         *  *                                     ")
print("                                           * * * * *    *        *    *  *   *  *           *        *        *      * * * *      *           *   *         *                                      ")
print("                                          *       *     *       *     * *     * *           *        *       *       *            *          * * * *       *                                       ")
print("                                         *       *     * * * * *     *         *           *        * * * * *       *            * * * *    *       *     *                                        ")
print("                                                                                                                                                                                  ")
print("                                                                                                                                                                                  ")
print("*****************************************************************************************************************************************************************************************************************")
print("                                                                                                                                                                                  ")
print("                                                                                                                                                                                  ")
print("*****************************************************************************************************************************************************************************************************************")
print("                                                                                                                                                                                  ")
print("                                                                                                                                                                                  ")
print(" 1. This game is almost as same as cricket but you will play against the computer and you and computer will have only one wicket.                                                 ")
print("                                                                                                                                                                                  ")
print(" 2. First you have to choose for the toss(Heads or Tails) against the computer.                                                                                                   ")
print("                                                                                                                                                                                  ")
print(" 3. If you get Heads you win the toss and you choose to bowl or bat.                                                                                                              ")
print("                                                                                                                                                                                  ")
print(" 4. If you get Tails you lose the toss and computer chooses to bowl or bat.                                                                                                       ")
print("                                                                                                                                                                                  ")
print(" 5. Now for playing you have to choose a number between 0 to 10 and enter in the input section. The computer also does the same.This process is repeated until you are not out(if you   are batting) or until you take a wicket(if you are bowling). ")
print("                                                                                                                                                                                  ")
print(" 6. If the number you entered is not same as the number which the computer chooses, then it will be added to your total score(If you are batting and computer is bowling) and to the    computer's score( If you are bowling and computer is batting).")
print("                                                                                                                                                                                  ")
print(" 7. If the number you entered is same as the number which the computer chooses, then you will be out(If you are batting) or you then took the wicket(if you are bowling) ")
print("                                                                                                                                                                                  ")
print(" 8. The total score will be the sum of all numbers you entered until you are out(If you are batting) or until you take the wicket(If you are bowling). ")
print("                                                                                                                                                                                  ")
print(" 9. If you have more total score than the computer you win , else the computer wins.   ")
print("                                                                                                                                                                                  ")
print("                                                                                                                                                                                  ")
print("                                                                                                                                                                                  ")
print("                                                                                                                                                                                  ")
print("                                                                                  ENJOY THE GAME :)                                                                               ")
print("                                                                                                                                                                                  ")
print("                                                                                                                                                                                  ")
import random 
# function for whole game
user_score = 0
computer_score=0
def cricket_match():
    # function for user batting and computer bowling
    global user_score
    global computer_score  
    
    def user_batting():
        global user_score
        status = "not out"
        while status == "not out" :
            user_bat_choice=int(input("Enter the number: "))
            computer_bowl_choice=random.choice([0,1,2,3,4,5,6,7,8,9,10])
            print("The computer's number was ",computer_bowl_choice)        
            if int(user_bat_choice)<= 10:
                if user_bat_choice == computer_bowl_choice: 
                    status = "out"
                    print("                     ")
                    print("That was a good catch")
                    print("         ")
                    print("You are out") 
                    print("          ")
                    print("Your total score is",user_score)
                    print("                                                ")
                else :
                    user_score += user_bat_choice
                    print("Current Score : ",user_score)
                    print("                    ")
            else :
                print("The number is invalid. Enter a number between 0 and 10 only.") 
                print("                                           ")
    
    #function for user bowling and computer batting
    
    def user_bowling():
        global computer_score
        status = "not out"
        # checking for out or not out
        
        while status == "not out" : 
            user_bowl_choice=int(input("Enter the number : "))
            computer_bat_choice=random.choice([0,1,2,3,4,5,6,7,8,9,10])
            print("The computer's number was : ",computer_bat_choice)
            if user_bowl_choice <=10:
                if user_bowl_choice == computer_bat_choice :
                    status = "out"
                    print("                     ")
                    print("Wow that was a LBW")
                    print("                     ")
                    print("You took the computer's wicket.")
                    print("                    ")
                    print("Total computer score : ",computer_score)
                    print("                       ")
                else :
                    computer_score += int(computer_bat_choice)
                    print("Current Score : ",computer_score)
                    print("                              ")
            else :
                print("It is an invalid number.Enter a number between only 0 and 10")
                print("                                                             ")
            



   # toss
    
    toss_choice=random.choice(["Heads","Tails"])
    bat_bowl_choice=["Bat","Bowl"]
    user_toss_input=str(input("Enter Heads or Tails: "))
    print("                                       ")
    print("The side was",toss_choice) 
    print("                          ")
    # choosing player's choice
            
    if user_toss_input == toss_choice : 
        print("You have won the toss. Now choose to bowl or bat")
        print("                             ")
        user_choice_input=str(input("Enter Bat or Bowl : "))
        print("                     ")
        #choosing bat or bowl
        
        if user_choice_input=="Bat":
            print("You have chosen to bat. Good luck :)")
            print("                     ")
            user_batting()
            print("                    ")
            print("Now batting is over. Now take the computer's wicket.")
            print("                    ")
            
            user_bowling()
        else :
            print("You have chosen to bowl. Good Luck :)")
            print("                     ")
            user_bowling()
            print("                     ")
            print("            ")
            print("Now bowling is over. Now score against the computer.")
            print("                     ")
            user_batting()
    
    else:
        print("You lost the toss")
        print("                                             ")
        computer_choice_input=random.choice(bat_bowl_choice)
        
        # choosing computer's choice
        if computer_choice_input == "bat" : 
            print("The computer has chosen to bat. Now take the computer's wicket. Good Luck :)")
            print("                     ")
            user_bowling()
            print("                    ")
            print("The computer's wicket is gone. Now score against the computer.")
            print("                     ")
            user_batting()
            
        else :
            print("The computer has chosen to bowl. Now score. Good Luck :)")
            print("                     ")
            user_batting()
            print("                    ")
            print("Your wicket is gone. Now take the computer's wicket")
            print("                     ")
            user_bowling()
    
    # checking who has won
    print("Your Total Score :",user_score)
    print("                              ")
    print("Computer's Total Score :",computer_score)
    print("                                         ")
    if user_score > computer_score :
        print("You have won the match.")
        print("Hurray")
        print("                ")
    elif user_score < computer_score:
        print("You have lost the match.")
        print("Losing is the victory to success. Dont lose you hope. Try playing again. :)")
        print("                ")
    
    print(" I hope you have liked my game :) ")
    print("                    ")
    print(" Do you want to play again ? ")
    print("                    ")
    user_score = 0  #for clearing the scores if the user want to play again
    computer_score=0
    #checking if the user want to play again or not
    
    game_playing_choice= str(input(" Enter Y to play to play again. Enter Q to quit the game."))
    print("                    ")
    if game_playing_choice == "Y" :
        print("Enjoy your game again :) ")
        print("                                                                                                                                                                                  ")
        print("                                                                                                                                                                                  ")
        cricket_match()
    elif game_playing_choice == "Q":
        print("Thank you for spending your valuable time on playing my game :) .")
        print("                    ")
        print("                                                                                                                                                                                  ")
        print("                                                                                                                                                                                  ")
        print("*****************************************************************************************************************************************************************************************************************")
        print("                                                                                                                                                                                  ")
        print("                                                                                                                                                                                  ")
        print("*****************************************************************************************************************************************************************************************************************")
        print("                                                                                                                                                                                  ")
        print("                                                                                                                                                                                  ")
        print("                                                      * *   * *       *       * * *    * * * *      * * *      *   *                                                                                              ")
        print("                                                      *   *   *      * *      *    *   *            *    *      * *                                                                                                  ")
        print("                                                      *       *     *   *     *    *   * * * *      * * *        *                                                                                            ")
        print("                                                      *       *    * * * *    *    *   *            *    *      *                                                                                                ")
        print("                                                      *       *   *       *   * * *    * * * *      * * *      *                                                                                                   ")
        print("                                                                                                                                                                                  ")
        print("                                                                                                                      S. Sankara Naaarayanan :)                                                          ")
        print("                                                                                                                                                                                  ")
        print("                                                                                                                                                                                  ")
        print("*****************************************************************************************************************************************************************************************************************")
        print("                                                                                                                                                                                  ")
        print("                                                                                                                                                                                  ")
        print("*****************************************************************************************************************************************************************************************************************")
        print("                                                                                                                                                                                  ")
        print("                                                                                                                                                                                  ")
# running the game    
cricket_match()
