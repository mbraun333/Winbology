
# coding: utf-8

# In[68]:


import random
import os
import tkinter as tk
import tkinter.messagebox
from PIL import ImageTk,Image #(type: pip install pillow)
from sys import platform


# In[69]:

#THIS NEEDS TO BE STANDARDIZED OR IN THE TIKINTER
#Initialize Lists for Each Regions
#Eastern Region this year
south_Fav = [1,8,5,4,6,3,7,2]
south_Upset = [16,9,12,13,11,14,10,15]
south_Teams = {1:"1 Auburn",2:"2 Mich St.",3:"3 Iowa St.",4:"4 Texas A&M",5:"5 Michigan",6:"6 Ole Miss",7:"7 Marquette",8:"8 Louisville",
                9:"9 Creighton",10:"10 New Mexico",11:"11 SDSU/UNC",12:"12 UC San Diego",13:"13 Yale",14:"14 Lipscomb",15:"15 Bryant",16:"16 ALST/SFPA"}
list_south_Teams = []
for i in south_Teams:
    list_south_Teams.append(south_Teams[i])

#Midwest Region
midwest_Fav = [1,8,5,4,6,3,7,2]
midwest_Upset = [16,9,12,13,11,14,10,15]
midwest_Teams = {1:"1 Houston",2:"2 Tennessee",3:"3 Kentucky",4:"4 Purdue",5:"5 Clemson",6:"6 Illinois",7:"7 UCLA",8:"8 Gonzaga",
                9:"9 Georgia",10:"10 Utah St.",11:"11 TEX/XAV",12:"12 McNeese",13:"13 High Point",14:"14 Troy",15:"15 Wofford",16:"16 SIUE"}
list_midwest_Teams = []
for i in midwest_Teams:
    list_midwest_Teams.append(midwest_Teams[i])
    
# West Region
west_Fav = [1,8,5,4,6,3,7,2]
west_Upset = [16,9,12,13,11,14,10,15]
west_Teams = {1:"1 Florida",2:"2 St. John's",3:"3 Texas Tech",4:"4 Maryland",5:"5 Memphis",6:"6 Missouri",7:"7 Kansas",8:"8 UConn",
                9:"9 Oklahoma",10:"10 Arkansas",11:"11 Drake",12:"12 Colorado St.",13:"13 Grand Canyon",14:"14 UNC Wilmington",15:"15 Omaha",16:"16 Norfolk St."}
list_west_Teams = []
for i in west_Teams:
    list_west_Teams.append(west_Teams[i])
    
#Southern Region
east_Fav = [1,8,5,4,6,3,7,2]
east_Upset = [16,9,12,13,11,14,10,15]
east_Teams = {1:"1 Duke",2:"2 Alabama",3:"3 Wisconsin",4:"4 Arizona",5:"5 Oregon",6:"6 BYU",7:"7 Saint Mary's",8:"8 Miss St.",
               9:"9 Baylor",10:"10 Vanderbilt",11:"11 VCU",12:"12 Liberty",13:"13 Akron",14:"14 Montana",15:"15 Robert Morris",16:"16 AMER/MSM"}
list_east_Teams = []
for i in east_Teams:
    list_east_Teams.append(east_Teams[i])
    
#Conference Teams
acc = ["1 Duke","11 SDSU/UNC","5 Clemson"]
sec = ["2 Tennessee","3 Kentucky","1 Auburn","2 Alabama","8 Miss St.","4 Texas A&M","1 Florida","11 TEX/XAV","9 Georgia","10 Arkansas","6 Missouri","10 Vanderbilt","6 Ole Miss","9 Oklahoma"]
big10 = ["2 Michigan St.","3 Wisconsin","4 Purdue","6 Illinois","7 UCLA","5 Michigan","4 Maryland","5 Oregon"]
big12 = ["1 Houston","6 BYU","3 Texas Tech","9 Baylor","4 Arizona","7 Kansas","11 TEX/XAV","3 Iowa St."]
pac12 = [""]
bigeast = ["8 UConn","9 Creighton","7 Marquette","11 TEX/XAV","2 St. John's"]
#Team selection structure (dictionaries with seed keys)
#all_Teams = {1:"Kansas",2:"Duke"}
#print(all_Teams[1])
#print(all_Teams[2])
#print(west_Teams[2])


# In[70]:


#Basic Model
#Creating Randomizer For Each Region

def ConferenceRandomizer(FavoriteSeeds,UpsetSeeds):

    roundone_Outcomes = []
    roundtwo_List1 = []
    roundtwo_List2 = []
    roundtwo_Fav = []
    roundtwo_Upset = []

    for seed in range(len(FavoriteSeeds)):

        total_Seeds = FavoriteSeeds[seed] + UpsetSeeds[seed]
        randnum = random.randint(1,total_Seeds)

        if randnum > FavoriteSeeds[seed]:
            roundone_Outcomes.append(FavoriteSeeds[seed])
            
        else:
            roundone_Outcomes.append(UpsetSeeds[seed])
    
    for i in range(len(roundone_Outcomes)):
        if i % 2 == 0:
          roundtwo_List1.append(roundone_Outcomes[i])
        else:
          roundtwo_List2.append(roundone_Outcomes[i])

    for i in range(len(roundtwo_List1)):
        if roundtwo_List1[i] < roundtwo_List2[i]:
          roundtwo_Fav.append(roundtwo_List1[i])
          roundtwo_Upset.append(roundtwo_List2[i])
        else:
          roundtwo_Fav.append(roundtwo_List2[i])
          roundtwo_Upset.append(roundtwo_List1[i])
###################################################################

    roundtwo_Outcomes = []
    roundthree_List1 = []
    roundthree_List2 = []
    roundthree_Fav = []
    roundthree_Upset = []

    for seed in range(len(roundtwo_Fav)):

        total_Seeds = roundtwo_Fav[seed] + roundtwo_Upset[seed]
        randnum = random.randint(1,total_Seeds)

        if randnum > roundtwo_Fav[seed]:
            roundtwo_Outcomes.append(roundtwo_Fav[seed])
            
        else:
            roundtwo_Outcomes.append(roundtwo_Upset[seed])
    
    for i in range(len(roundtwo_Outcomes)):
        if i % 2 == 0:
          roundthree_List1.append(roundtwo_Outcomes[i])
        else:
          roundthree_List2.append(roundtwo_Outcomes[i])

    for i in range(len(roundthree_List1)):
        if roundthree_List1[i] < roundthree_List2[i]:
          roundthree_Fav.append(roundthree_List1[i])
          roundthree_Upset.append(roundthree_List2[i])
        else:
          roundthree_Fav.append(roundthree_List2[i])
          roundthree_Upset.append(roundthree_List1[i])

#########################################################################
    roundthree_Outcomes = []
    roundfour_List1 = []
    roundfour_List2 = []
    roundfour_Fav = []
    roundfour_Upset = []

    for seed in range(len(roundthree_Fav)):

        total_Seeds = roundthree_Fav[seed] + roundthree_Upset[seed]
        randnum = random.randint(1,total_Seeds)

        if randnum > roundthree_Fav[seed]:
            roundthree_Outcomes.append(roundthree_Fav[seed])
            
        else:
            roundthree_Outcomes.append(roundthree_Upset[seed])
    
    for i in range(len(roundthree_Outcomes)):
        if i % 2 == 0:
          roundfour_List1.append(roundthree_Outcomes[i])
        else:
          roundfour_List2.append(roundthree_Outcomes[i])

    for i in range(len(roundfour_List1)):
        if roundfour_List1[i] < roundfour_List2[i]:
          roundfour_Fav.append(roundfour_List1[i])
          roundfour_Upset.append(roundfour_List2[i])
        else:
          roundfour_Fav.append(roundfour_List2[i])
          roundfour_Upset.append(roundfour_List1[i])

####################################################################
    roundfour_Outcome = []
    for seed in range(len(roundfour_Fav)):

        total_Seeds = roundfour_Fav[seed] + roundfour_Upset[seed]
        randnum = random.randint(1,total_Seeds)

        if randnum > roundfour_Fav[seed]:
            roundfour_Outcome.append(roundfour_Fav[seed])
            
        else:
            roundfour_Outcome.append(roundfour_Upset[seed])

    return roundone_Outcomes,roundtwo_Outcomes,roundthree_Outcomes,roundfour_Outcome


# In[71]:


#ACC Model
#Creating Randomizer For Each Region

def ConferenceRandomizerACC(FavoriteSeeds,UpsetSeeds,Teams,ACCTeams):

    roundone_Outcomes = []
    roundtwo_List1 = []
    roundtwo_List2 = []
    roundtwo_Fav = []
    roundtwo_Upset = []
    ACC_seeds = []
    ACC_TeamFav = 0
    ACC_TeamUpset = 0
    
# Tracking ACC Teams in Region   
    for i in range(len(Teams)):
        if ACCTeams.count(Teams[i]) > 0:
            ACC_seeds.append(i+1)
            
    for seed in range(len(FavoriteSeeds)):
# Noting if the seed is an ACC team

        if ACC_seeds.count(FavoriteSeeds[seed]) > 0:
            ACC_TeamFav = 1           
        else:
            ACC_TeamFav = 0
            
        if ACC_seeds.count(UpsetSeeds[seed]) > 0:
            ACC_TeamUpset = 1            
        else:
            ACC_TeamUpset = 0

        total_Seeds = FavoriteSeeds[seed] + UpsetSeeds[seed]
        randnum = random.randint(1,total_Seeds)
        
# Giving Extra Chances 

        if (ACC_TeamFav == 1) and (ACC_TeamUpset == 1):
            randnum = randnum
            
        else:

            if (ACC_TeamFav == 1) and (randnum <= FavoriteSeeds[seed]):
                randnum = random.randint(1,total_Seeds)
            
            if (ACC_TeamUpset == 1) and (randnum > FavoriteSeeds[seed]):
                randnum = random.randint(1,total_Seeds)
                if randnum > FavoriteSeeds[seed]:
                    randnum = random.randint(1,total_Seeds)
                    if randnum > FavoriteSeeds[seed]:
                        randnum = random.randint(1,total_Seeds)
                        if randnum > FavoriteSeeds[seed]:
                                randnum = random.randint(1,total_Seeds)

        if randnum > FavoriteSeeds[seed]:
            roundone_Outcomes.append(FavoriteSeeds[seed])
            
        else:
            roundone_Outcomes.append(UpsetSeeds[seed])
    
    for i in range(len(roundone_Outcomes)):
        if i % 2 == 0:
          roundtwo_List1.append(roundone_Outcomes[i])
        else:
          roundtwo_List2.append(roundone_Outcomes[i])

    for i in range(len(roundtwo_List1)):
        if roundtwo_List1[i] < roundtwo_List2[i]:
          roundtwo_Fav.append(roundtwo_List1[i])
          roundtwo_Upset.append(roundtwo_List2[i])
        else:
          roundtwo_Fav.append(roundtwo_List2[i])
          roundtwo_Upset.append(roundtwo_List1[i])
###################################################################

    roundtwo_Outcomes = []
    roundthree_List1 = []
    roundthree_List2 = []
    roundthree_Fav = []
    roundthree_Upset = []

    for seed in range(len(roundtwo_Fav)):

        if ACC_seeds.count(roundtwo_Fav[seed]) > 0:
            ACC_TeamFav = 1           
        else:
            ACC_TeamFav = 0
            
        if ACC_seeds.count(roundtwo_Upset[seed]) > 0:
            ACC_TeamUpset = 1            
        else:
            ACC_TeamUpset = 0

        total_Seeds = roundtwo_Fav[seed] + roundtwo_Upset[seed]
        randnum = random.randint(1,total_Seeds)
        
        if (ACC_TeamFav == 1) and (ACC_TeamUpset == 1):
            randnum = randnum
            
        else:
            if (ACC_TeamFav == 1) and (roundtwo_Upset[seed] >= 13):
                randnum = 13
            
            if (ACC_TeamFav == 1) and (randnum <= roundtwo_Fav[seed]):
                randnum = random.randint(1,total_Seeds)

            if (ACC_TeamUpset == 1) and (randnum > roundtwo_Fav[seed]):
                randnum = random.randint(1,total_Seeds)
                if randnum > roundtwo_Fav[seed]:
                    randnum = random.randint(1,total_Seeds)
                    if randnum > roundtwo_Fav[seed]:
                        randnum = random.randint(1,total_Seeds)
                        if randnum > roundtwo_Fav[seed]:
                            randnum = random.randint(1,total_Seeds)

        if randnum > roundtwo_Fav[seed]:
            roundtwo_Outcomes.append(roundtwo_Fav[seed])
            
        else:
            roundtwo_Outcomes.append(roundtwo_Upset[seed])
    
    for i in range(len(roundtwo_Outcomes)):
        if i % 2 == 0:
          roundthree_List1.append(roundtwo_Outcomes[i])
        else:
          roundthree_List2.append(roundtwo_Outcomes[i])

    for i in range(len(roundthree_List1)):
        if roundthree_List1[i] < roundthree_List2[i]:
          roundthree_Fav.append(roundthree_List1[i])
          roundthree_Upset.append(roundthree_List2[i])
        else:
          roundthree_Fav.append(roundthree_List2[i])
          roundthree_Upset.append(roundthree_List1[i])

#########################################################################
    roundthree_Outcomes = []
    roundfour_List1 = []
    roundfour_List2 = []
    roundfour_Fav = []
    roundfour_Upset = []

    for seed in range(len(roundthree_Fav)):

        if ACC_seeds.count(roundthree_Fav[seed]) > 0:
            ACC_TeamFav = 1           
        else:
            ACC_TeamFav = 0
            
        if ACC_seeds.count(roundthree_Upset[seed]) > 0:
            ACC_TeamUpset = 1            
        else:
            ACC_TeamUpset = 0

        total_Seeds = roundthree_Fav[seed] + roundthree_Upset[seed]
        randnum = random.randint(1,total_Seeds)
        
        if (ACC_TeamFav == 1) and (ACC_TeamUpset == 1):
            randnum = randnum
            
        else:
            if (ACC_TeamFav == 1) and (roundthree_Upset[seed] >= 12):
                randnum = 12
                
            if (ACC_TeamFav == 1) and (randnum <= roundthree_Fav[seed]):
                randnum = random.randint(1,total_Seeds)

            if (ACC_TeamUpset == 1) and (randnum > roundthree_Fav[seed]):
                randnum = random.randint(1,total_Seeds)
                if randnum > roundthree_Fav[seed]:
                    randnum = random.randint(1,total_Seeds)

        if randnum > roundthree_Fav[seed]:
            roundthree_Outcomes.append(roundthree_Fav[seed])
            
        else:
            roundthree_Outcomes.append(roundthree_Upset[seed])
    
    for i in range(len(roundthree_Outcomes)):
        if i % 2 == 0:
          roundfour_List1.append(roundthree_Outcomes[i])
        else:
          roundfour_List2.append(roundthree_Outcomes[i])

    for i in range(len(roundfour_List1)):
        if roundfour_List1[i] < roundfour_List2[i]:
          roundfour_Fav.append(roundfour_List1[i])
          roundfour_Upset.append(roundfour_List2[i])
        else:
          roundfour_Fav.append(roundfour_List2[i])
          roundfour_Upset.append(roundfour_List1[i])

####################################################################
    roundfour_Outcome = []
    for seed in range(len(roundfour_Fav)):

        if ACC_seeds.count(roundfour_Fav[seed]) > 0:
            ACC_TeamFav = 1           
        else:
            ACC_TeamFav = 0
            
        if ACC_seeds.count(roundfour_Upset[seed]) > 0:
            ACC_TeamUpset = 1            
        else:
            ACC_TeamUpset = 0

        total_Seeds = roundfour_Fav[seed] + roundfour_Upset[seed]
        randnum = random.randint(1,total_Seeds)
        
        if (ACC_TeamFav == 1) and (ACC_TeamUpset == 1):
            randnum = randnum
            
        else:
            if (ACC_TeamFav == 1) and (roundfour_Upset[seed] >= 12):
                randnum = 12
                
            if (ACC_TeamFav == 1) and (randnum <= roundfour_Fav[seed]):
                randnum = random.randint(1,total_Seeds)

            if (ACC_TeamUpset == 1) and (randnum > roundfour_Fav[seed]):
                randnum = random.randint(1,total_Seeds)
                if randnum > roundfour_Fav[seed]:
                    randnum = random.randint(1,total_Seeds)

        if randnum > roundfour_Fav[seed]:
            roundfour_Outcome.append(roundfour_Fav[seed])
            
        else:
            roundfour_Outcome.append(roundfour_Upset[seed])

    return roundone_Outcomes,roundtwo_Outcomes,roundthree_Outcomes,roundfour_Outcome


# In[72]:


# Creating Randomizer For Final Four
def FinalFour(southwin, westwin, eastwin, midwestwin, southteams, westteams, eastteams, midwestteams):
    roundfive_Outcome = []
    roundfive_Teams = [southteams[southwin[0]],westteams[westwin[0]],eastteams[eastwin[0]],midwestteams[midwestwin[0]]]
    finals_Teams = []
    win_Team = []
    
    fSouth = southwin[0]
    fWest = westwin[0]
    fEast = eastwin[0]
    fMidwest = midwestwin[0]
    
    randnum = random.randint(1,fSouth+fWest)
    if randnum > fSouth:
        roundfive_Outcome.append(fSouth)
        finals_Teams.append(roundfive_Teams[0])
        
    else:
        roundfive_Outcome.append(fWest)
        finals_Teams.append(roundfive_Teams[1])
        
    randnum = random.randint(1,fEast+fMidwest)
    if randnum > fEast:
        roundfive_Outcome.append(fEast)
        finals_Teams.append(roundfive_Teams[2])
        
    else:
        roundfive_Outcome.append(fMidwest)
        finals_Teams.append(roundfive_Teams[3])
        
    randnum = random.randint(1,roundfive_Outcome[0]+roundfive_Outcome[1])
    if randnum > roundfive_Outcome[0]:
        winner = roundfive_Outcome[0]
        win_Team.append(finals_Teams[0])
        
    else:
        winner = roundfive_Outcome[1]
        win_Team.append(finals_Teams[1])
        
    return roundfive_Outcome, winner, finals_Teams, win_Team


# In[73]:


# Creating Labels For The Basic Model
def basic(south, west, east, midwest, finalFour):
    root = tk.Toplevel(main)
    root.title("Bracket")
    root.geometry("1300x720")
    tk.Label(root, text = "Your Bracket", font=("Roboto Serif",20)).pack()
    
    #a = os.getlogin()
    
    #This needs to get revamped
    
    #if platform == "win32":
    path1 = "/home/mbraun33/Documents/Winbology/2025_bracket.png"
        
    #else:
        #path1 = a+"/Downloads/Winbology/2023_bracket2.png"
    
    img=Image.open(path1)

    # Resize the image using resize() method
    root.resizable(width=False, height=False)
    resize_image = img.resize((1270, 700))

    img = ImageTk.PhotoImage(resize_image)

    # create label and add resize image
    label1 = tk.Label(root, image=img)
    label1.image = img
    label1.pack()

    ###################################################################################################################
    #South
    ###################################################################################################################
    #Placing South Labels (First Round)
    x1 = 205
    y1 = 90
    for i in range(len(south[0])):
        team = south_Teams[south[0][i]]
        label = tk.Label(root,text=team,bg="white",fg="orange")
        label.pack()
        label.place(x=x1, y=y1, anchor=tk.CENTER)
        y1 = y1+40

    # Placing South Labels (Second Round)
    x1 = 313
    y1 = 110
    for i in range(len(south[1])):
        team = south_Teams[south[1][i]]
        label = tk.Label(root,text=team,bg="white",fg="orange")
        label.pack()
        label.place(x=x1, y=y1, anchor=tk.CENTER)
        y1 = y1+80    

    # Placing South Labels (Third Round)
    x1 = 423
    y1 = 145
    for i in range(len(south[2])):
        team = south_Teams[south[2][i]]
        label = tk.Label(root,text=team,bg="white",fg="orange")
        label.pack()
        label.place(x=x1, y=y1, anchor=tk.CENTER)
        y1 = y1+163  

    # Placing South Labels (Fourth Round)
    x1 = 532
    y1 = 227
    for i in range(len(south[3])):
        team = south_Teams[south[3][i]]
        label = tk.Label(root,text=team,bg="white",fg="orange")
        label.pack()
        label.place(x=x1, y=y1, anchor=tk.CENTER)

    ###################################################################################################################
    #West
    ###################################################################################################################
    #Placing West Labels (First Round)
    x1 = 205
    y1 = 415
    for i in range(len(west[0])):
        team = west_Teams[west[0][i]]
        label = tk.Label(root,text=team,bg="white",fg="blue")
        label.pack()
        label.place(x=x1, y=y1, anchor=tk.CENTER)
        y1 = y1+40

    # Placing West Labels (Second Round)
    x1 = 313
    y1 = 435
    for i in range(len(west[1])):
        team = west_Teams[west[1][i]]
        label = tk.Label(root,text=team,bg="white",fg="blue")
        label.pack()
        label.place(x=x1, y=y1, anchor=tk.CENTER)
        y1 = y1+80    

    # Placing West Labels (Third Round)
    x1 = 423
    y1 = 473
    for i in range(len(west[2])):
        team = west_Teams[west[2][i]]
        label = tk.Label(root,text=team,bg="white",fg="blue")
        label.pack()
        label.place(x=x1, y=y1, anchor=tk.CENTER)
        y1 = y1+163  

    # Placing West Labels (Fourth Round)
    x1 = 532
    y1 = 555
    for i in range(len(west[3])):
        team = west_Teams[west[3][i]]
        label = tk.Label(root,text=team,bg="white",fg="blue")
        label.pack()
        label.place(x=x1, y=y1, anchor=tk.CENTER)

    ###################################################################################################################
    #East
    ###################################################################################################################
    #Placing East Labels (First Round)
    x1 = 1095
    y1 = 90
    for i in range(len(east[0])):
        team = east_Teams[east[0][i]]
        label = tk.Label(root,text=team,bg="white",fg="green")
        label.pack()
        label.place(x=x1, y=y1, anchor=tk.CENTER)
        y1 = y1+40

    # Placing East Labels (Second Round)
    x1 = 983
    y1 = 110
    for i in range(len(east[1])):
        team = east_Teams[east[1][i]]
        label = tk.Label(root,text=team,bg="white",fg="green")
        label.pack()
        label.place(x=x1, y=y1, anchor=tk.CENTER)
        y1 = y1+80    

    # Placing East Labels (Third Round)
    x1 = 875
    y1 = 145
    for i in range(len(east[2])):
        team = east_Teams[east[2][i]]
        label = tk.Label(root,text=team,bg="white",fg="green")
        label.pack()
        label.place(x=x1, y=y1, anchor=tk.CENTER)
        y1 = y1+163  

    # Placing East Labels (Fourth Round)
    x1 = 767
    y1 = 227
    for i in range(len(east[3])):
        team = east_Teams[east[3][i]]
        label = tk.Label(root,text=team,bg="white",fg="green")
        label.pack()
        label.place(x=x1, y=y1, anchor=tk.CENTER)

    ###################################################################################################################
    #MidWest
    ###################################################################################################################
    #Placing MidWest Labels (First Round)
    x1 = 1095
    y1 = 415
    for i in range(len(midwest[0])):
        team = midwest_Teams[midwest[0][i]]
        label = tk.Label(root,text=team,bg="white",fg="red")
        label.pack()
        label.place(x=x1, y=y1, anchor=tk.CENTER)
        y1 = y1+40

    # Placing MidWest Labels (Second Round)
    x1 = 983
    y1 = 435
    for i in range(len(midwest[1])):
        team = midwest_Teams[midwest[1][i]]
        label = tk.Label(root,text=team,bg="white",fg="red")
        label.pack()
        label.place(x=x1, y=y1, anchor=tk.CENTER)
        y1 = y1+80

    # Placing MidWest Labels (Third Round)
    x1 = 875
    y1 = 473
    for i in range(len(midwest[2])):
        team = midwest_Teams[midwest[2][i]]
        label = tk.Label(root,text=team,bg="white",fg="red")
        label.pack()
        label.place(x=x1, y=y1, anchor=tk.CENTER)
        y1 = y1+163

    # Placing MidWest Labels (Fourth Round)
    x1 = 767
    y1 = 555
    for i in range(len(midwest[3])):
        team = midwest_Teams[midwest[3][i]]
        label = tk.Label(root,text=team,bg="white",fg="red")
        label.pack()
        label.place(x=x1, y=y1, anchor=tk.CENTER)
        
    # Placing Final Four Labels
    x1 = 485
    y1 = 390
    for i in range(len(finalFour[0])):
        team = finalFour[2][i]
        if list_south_Teams.count(team) > 0:
            color = "orange"
            
        if list_west_Teams.count(team) > 0:
            color = "blue"
            
        if list_east_Teams.count(team) > 0:
            color = "green"
            
        if list_midwest_Teams.count(team) > 0:
            color = "red"
            
        label = tk.Label(root,text=team,fg=color)
        label.pack()
        label.place(x=x1, y=y1, anchor=tk.CENTER)
        x1 = x1+332
    if list_south_Teams.count(finalFour[3][0]) > 0:
            color = "orange"
            
    if list_west_Teams.count(finalFour[3][0]) > 0:
            color = "blue"
            
    if list_east_Teams.count(finalFour[3][0]) > 0:
            color = "green"
            
    if list_midwest_Teams.count(finalFour[3][0]) > 0:
            color = "red"    
    label = tk.Label(root,text=finalFour[3][0],fg=color,font=("Source Code Pro",15))
    label.pack()
    label.place(x=650, y=395, anchor=tk.CENTER)
    
    #def addie():
    #    su_label = tk.Label(root,text="Syracuse",fg="Orange",font=("Source Code Pro",15))
    #    su_label.pack()
    #    su_label.place(x=650,y=395,anchor=tk.CENTER)
    #
    #suu_label = tk.Label(root,text="Addie's Syracuse \n Button",bg="white")
    #suu_label.pack()
    #suu_label.place(x=650,y=540,anchor=tk.CENTER)
    #su_button = tk.Button(root, text = "Syracuse", bd = "5", width=15, height=1, 
    #                      bg="orange", fg="blue", font="bold",command = addie)
    #su_button.pack()
    #su_button.place(x=650,y=580,anchor="c")
    
    root.mainloop()


# In[74]:


# Functions To Be Activated By Each Button
def BasicModel():
    south = ConferenceRandomizer(south_Fav,south_Upset)
    west = ConferenceRandomizer(west_Fav,west_Upset)
    east = ConferenceRandomizer(east_Fav,east_Upset)
    midwest = ConferenceRandomizer(midwest_Fav,midwest_Upset)
    finalFour = FinalFour(south[3],west[3],east[3],midwest[3],south_Teams,west_Teams,east_Teams,midwest_Teams)
    basic(south,west,east,midwest,finalFour)
    
def ACCModel():
    south = ConferenceRandomizerACC(south_Fav,south_Upset,list_south_Teams,acc)
    west = ConferenceRandomizerACC(west_Fav,west_Upset,list_west_Teams,acc)
    east = ConferenceRandomizerACC(east_Fav,east_Upset,list_east_Teams,acc)
    midwest = ConferenceRandomizerACC(midwest_Fav,midwest_Upset,list_midwest_Teams,acc)
    finalFour = FinalFour(south[3],west[3],east[3],midwest[3],south_Teams,west_Teams,east_Teams,midwest_Teams)
    basic(south,west,east,midwest,finalFour)
    
def SECModel():
    south = ConferenceRandomizerACC(south_Fav,south_Upset,list_south_Teams,sec)
    west = ConferenceRandomizerACC(west_Fav,west_Upset,list_west_Teams,sec)
    east = ConferenceRandomizerACC(east_Fav,east_Upset,list_east_Teams,sec)
    midwest = ConferenceRandomizerACC(midwest_Fav,midwest_Upset,list_midwest_Teams,sec)
    finalFour = FinalFour(south[3],west[3],east[3],midwest[3],south_Teams,west_Teams,east_Teams,midwest_Teams)
    basic(south,west,east,midwest,finalFour)

def Big10Model():
    south = ConferenceRandomizerACC(south_Fav,south_Upset,list_south_Teams,big10)
    west = ConferenceRandomizerACC(west_Fav,west_Upset,list_west_Teams,big10)
    east = ConferenceRandomizerACC(east_Fav,east_Upset,list_east_Teams,big10)
    midwest = ConferenceRandomizerACC(midwest_Fav,midwest_Upset,list_midwest_Teams,big10)
    finalFour = FinalFour(south[3],west[3],east[3],midwest[3],south_Teams,west_Teams,east_Teams,midwest_Teams)
    basic(south,west,east,midwest,finalFour)
    
def Big12Model():
    south = ConferenceRandomizerACC(south_Fav,south_Upset,list_south_Teams,big12)
    west = ConferenceRandomizerACC(west_Fav,west_Upset,list_west_Teams,big12)
    east = ConferenceRandomizerACC(east_Fav,east_Upset,list_east_Teams,big12)
    midwest = ConferenceRandomizerACC(midwest_Fav,midwest_Upset,list_midwest_Teams,big12)
    finalFour = FinalFour(south[3],west[3],east[3],midwest[3],south_Teams,west_Teams,east_Teams,midwest_Teams)
    basic(south,west,east,midwest,finalFour)
    
def Pac12Model():
    south = ConferenceRandomizerACC(south_Fav,south_Upset,list_south_Teams,pac12)
    west = ConferenceRandomizerACC(west_Fav,west_Upset,list_west_Teams,pac12)
    east = ConferenceRandomizerACC(east_Fav,east_Upset,list_east_Teams,pac12)
    midwest = ConferenceRandomizerACC(midwest_Fav,midwest_Upset,list_midwest_Teams,pac12)
    finalFour = FinalFour(south[3],west[3],east[3],midwest[3],south_Teams,west_Teams,east_Teams,midwest_Teams)
    basic(south,west,east,midwest,finalFour)
    
def BigEastModel():
    south = ConferenceRandomizerACC(south_Fav,south_Upset,list_south_Teams,bigeast)
    west = ConferenceRandomizerACC(west_Fav,west_Upset,list_west_Teams,bigeast)
    east = ConferenceRandomizerACC(east_Fav,east_Upset,list_east_Teams,bigeast)
    midwest = ConferenceRandomizerACC(midwest_Fav,midwest_Upset,list_midwest_Teams,bigeast)
    finalFour = FinalFour(south[3],west[3],east[3],midwest[3],south_Teams,west_Teams,east_Teams,midwest_Teams)
    basic(south,west,east,midwest,finalFour)


# In[75]:


# Main GUI Screen
main = tk.Tk()
main.title("Winbology")
main.geometry("600x650")
main.configure(bg="white")
main.resizable(width=False, height=False)
label3 = tk.Label(text="Welcome To Winbology!", font=("Arial",30), bg="#FFFFFF")
label3.pack()    

#b = os.getlogin()

#This needs to be revamped
#if platform == "win32":
path2 = "/home/mbraun33/Documents/Winbology/2025_bracket.png"
    
#else:
    #path2 = b+"/Downloads/Winbology/bracket2.png"

img=Image.open(path2)
resize_image = img.resize((round(835), round(583)))
#resize_image = img.resize((round(516*1.3), round(611*1.3)))
img = ImageTk.PhotoImage(resize_image)
labelB = tk.Label(main, image=img, anchor="nw")
labelB.image = img
labelB.pack()
     
basic_btn = tk.Button(main, text = "Generate Basic Model", bd = "5", command = BasicModel, width=25, height=2, bg="black", fg="white", font="bold")
basic_btn.pack()
basic_btn.place(x=400,y=90+15,anchor="c")

sec_btn = tk.Button(main, text = "Generate SEC Model", bd = "5", command = SECModel, width=25, height=2, bg="red", fg="white", font="bold")
sec_btn.pack()
sec_btn.place(x=400,y=160+15,anchor="c")

acc_btn = tk.Button(main, text = "Generate ACC Model", bd = "5", command = ACCModel, width=25, height=2, bg="orange", fg="blue", font="bold")
acc_btn.pack()
acc_btn.place(x=400,y=230+15,anchor="c")

big10_btn = tk.Button(main, text = "Generate Big 10 Model", bd = "5", command = Big10Model, width=25, height=2, bg="green", fg="white", font="bold")
big10_btn.pack()
big10_btn.place(x=400,y=300+15,anchor="c")

big12_btn = tk.Button(main, text = "Generate Big 12 Model", bd = "5", command = Big12Model, width=25, height=2, bg="yellow", fg="green", font="bold")
big12_btn.pack()
big12_btn.place(x=400,y=370+15,anchor="c")

bigeast_btn = tk.Button(main, text = "Generate Big East Model", bd = "5", command = BigEastModel, width=25, height=2, bg="blue", fg="white", font="bold")
bigeast_btn.pack()
bigeast_btn.place(x=400,y=440+15,anchor="c")

pac12_btn = tk.Button(main, text = "Generate Pac-12 Model", bd = "5", command = Pac12Model, width=25, height=2, bg="#11A5FA", fg="yellow", font="bold")
pac12_btn.pack()
pac12_btn.place(x=400,y=510+15,anchor="c")

import webbrowser

def callback():
   webbrowser.open_new_tab("https://www.ncaa.com/")
   
exper_btn = tk.Button(main, text = "Safe Bracket", bd = "5", command = callback, width=25, height=2, bg="black", fg="white", font="bold")
exper_btn.pack()
exper_btn.place(x=400,y=580+15,anchor="c")

    
main.mainloop()
