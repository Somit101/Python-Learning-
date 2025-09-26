# Multiplayer game lobby

class Players:
    def __init__(self,name1,age1,kills1):
        self.name1 = name1
        self.age1 = age1
        self.kills1 = kills1

    def __str__(self):
        return f"------------------\nName : {self.name1}\nAge : {self.age1}\nKills : {self.kills1}\n------------------"
    

Player_count = 0
Lobby = []
class Functions:
    def __init__(self):
        self.player = []

    def create_id(self,player):
        self.player.append(player)

    def invite_player(self,name):
        global Player_count
        for player in self.player:
            found = False
            if player.name1 == name:

              print(f"{name} added in lobby")
              Lobby.append(name)
              Player_count += 1
              found = True
        if not found:
               print("Player do not exist")

    def leaving_lobby(self,name):
        global Player_count
        found = False
        for player in self.player:
          
          if player.name1 == name and name in Lobby:
            print("Press 1 to leave lobby")
            U = int(input(""))
            if U == 1:
                Lobby.remove(name)
                if Player_count == 0:
                    print("No player exists")
                else:    
                   Player_count -= 1
                print("Left lobby successfully") 
                found = True
            else:
               print("Input only 1")    
        if not found:
           print("No player exist")        

    def view(self):
        if self.player == []:
            print("No player exists")
        else:
            for player in self.player:
                print(player)
    
    def start_match(self):
        global Player_count
        if Player_count == 4:
            print("Matching")

        elif Player_count < 4:
            print("Not sufficient players to start matching")

        elif Player_count > 4:
            print("Only 4 players are allowed")

        else:
            print("4 Players should be inside lobby")

function = Functions()            

def login():
    print("\n<<<<<<<<<< Lobby >>>>>>>>>>")
    print("1. Create ID")
    print("2. View all players")
    print("3. Invite player")
    print("4. Leave lobby")
    print("5. Start matching")
    print("6. Exit")

while True:
    login()
    try:
      user = int(input("Enter what you want to do (1,2,3,4,5,6): "))
    except:
        print("Enter integers only")  
    else:    
     if user == 1:
        
        Name = str(input("Enter ingame name: "))
        try:
         Age = int(input("Enter your age: "))
        except:
            print("Enter integers only") 
        else:  
         try:  
          Kills = int(input("Enter your kills: "))
         except:
            print("Enter integers only") 
         else:   
          Assign = Players(Name,Age,Kills)
          function.create_id(Assign)

     elif user == 2:
        function.view()

     elif user == 3:
        name = str(input("Enter the name of player you want to invite: "))
        function.invite_player(name)   

     elif user == 4:
        pname = str(input("Enter your name: "))
        function.leaving_lobby(pname)   

     elif user == 5:
        function.start_match()

     elif user == 6:
        break


     else:
        print("Please enter valid inputs")    




                                  
            


        


        

