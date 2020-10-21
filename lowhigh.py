''' By:- Ankith Abhayan 
version 3 '''
import random
import os
import sys
import time
from ankith import date_time
from ankith import cryptography
import json
from tkinter import *
from math import *
import tkinter.messagebox
gamenoo = 0
global name1scores
global name2scores
global name1guesscount
global name2guesscount
name1scores = []
name2scores = []
name1guesscount = []
name2guesscount = []
def printstuff():
    print(" _        _______          _      _     _    _______    _      _")
    print("| |      |  ____ |        | |    | |   | |  |  _____|  | |    | |")
    print("| |      | |   | |        | |____| |   | |  | |  ____  | |____| |")
    print("| |      | |   | |   ---  |  ____| |   | |  | | |__  | |  ____  |")
    print("| |____  | |___| |        | |    | |   | |  | |____| | | |    | |")
    print("|______| |_______|        |_|    |_|   |_|  |________| |_|    |_|")
    print(" version 1.3")
    print("\n"*2)    
def playerlevel(name,data):
    for item in data["players"]["individual_players"]:
        if item["name"] == name:
            level = item["level"]
            total_xp = item["total_xp"]
            break
    level_data = {1000:1,2000:2,3000:3,4000:4,5000:5,7500:6,9000:7,12500:8,15000:9,17500:10,20000:11,22500:12,25000:13,27500:14,30000:15,32500:16,35000:17,37500:18,40000:19,43000:20,46000:21,49000:22,52000:23,55000:24,58000:25,61000:26,64000:27,67000:28,70000:29,73000:30,76000:31,79000:32,82000:33,85000:34,88000:35,91000:36,94000:37,97000:38,100000:40,105000:41,110000:42,115000:43,120000:44,125000:45,130000:46,135000:47,140000:48,145000:49,150000:50}  
    nextlxp = 0
    for item in level_data:
        if total_xp < item:
            nextlxp = item
            break
    if nextlxp == 0:
        nextlxp = 150000
    print("username : "+str(name))
    print("level : "+str(level))
    print("total xp earned : "+str(total_xp)+"/"+str(nextlxp))
def update_level(name):
    with open(path, "r") as jsonFile:
        data = json.load(jsonFile)
    level_data = {1000:1,2000:2,3000:3,4000:4,5000:5,7500:6,9000:7,12500:8,15000:9,17500:10,20000:11,22500:12,25000:13,27500:14,30000:15,32500:16,35000:17,37500:18,40000:19,43000:20,46000:21,49000:22,52000:23,55000:24,58000:25,61000:26,64000:27,67000:28,70000:29,73000:30,76000:31,79000:32,82000:33,85000:34,88000:35,91000:36,94000:37,97000:38,100000:40,105000:41,110000:42,115000:43,120000:44,125000:45,130000:46,135000:47,140000:48,145000:49,150000:50}  
    total_xp = []
    for item in data["players"]["individual_players"]:
        if item["name"] == name:
            for value in item["events"]:
                total_xp.append(value["score"])   
    num = sum(total_xp)
    level = 0
    for item in level_data:
        if num > item:
            level = level_data[item]
    with open(path, "w") as jsonFile:
        json.dump(data,jsonFile,indent=4)
    return level
def getscore(level,guess_count):
    if level == "easy":
        easyarray = [0]
        first_num = 0
        for i in range(15):
            easyarray.append(random.randint(first_num,first_num+7))
            first_num += 7
        easyarray.reverse()
        xp = easyarray[guess_count]
        return xp
    elif level == "medium":
        mediumarray = [0]
        first_num = 100
        for i in range(15):
            mediumarray.append(random.randint(first_num,first_num+10))
            first_num += 10
        mediumarray.reverse()
        xp = mediumarray[guess_count]
        return xp
    elif level == "hard":
        hardarray = [0]
        first_num = 250
        for i in range(15):
            hardarray.append(random.randint(first_num,first_num+10))
            first_num += 10
        hardarray.reverse()
        xp = hardarray[guess_count]
        return xp
    elif level == "legend":
        legendarray = [0]
        first_num = 400
        for i in range(15):
            legendarray.append(random.randint(first_num,first_num+10))
            first_num += 10
        legendarray.reverse()
        xp = legendarray[guess_count]
        return xp        
def authenticate():
    global path
    path = "jsondata(do not delete).json"
    if os.path.exists("jsondata(do not delete).json") == False:
        relative_path = sys.argv[0]
        letter_list = [x for x in relative_path]
        slashindex = []
        lix = ["\ "]
        for item in letter_list:
            if item == lix[0][0]:
                indexx = letter_list.index(lix[0][0])
                slashindex.append(indexx)
                letter_list[indexx] = "a"
        path = relative_path[0:slashindex[-1]]+"\jsondata(do not delete).json"
        if os.path.exists(path) == False:
            print("the file jsondata(do not delete).json appeares to be moved or renamed/deleted. Please contact Ankith")
            new = input("make a new jsondata(do not delete).json file? (existing data will be overwritten):")
            if new == "yes":
                print("creating new file...")
                create_new_data()
                print("created")
                command_prompt()
            else:
                sys.exit()
    else:
        pass
    global commandpath
    if os.path.exists("commands.txt") == False:
        relative_path = sys.argv[0]
        letter_list = [x for x in relative_path]
        slashindex = []
        lix = ["\ "]
        for item in letter_list:
            if item == lix[0][0]:
                indexx = letter_list.index(lix[0][0])
                slashindex.append(indexx)
                letter_list[indexx] = "a"
        commandpath = relative_path[0:slashindex[-1]]+"\commands.txt"
        if os.path.exists(commandpath) == False:
            print("the file commands.txt appears to be moved or renamed/deleted. Please contact Ankith")
    else:
        pass
def showcmdhistory(data):
    for item in data["command_history"]:
        print(item)
def clearcmdhistory(command,data):
    data["command_history"].clear()
    with open(path, "w") as jsonFile:
        json.dump(data,jsonFile,indent=4)
    with open(path, "r") as jsonFile:
        data = json.load(jsonFile)
    command_history_dump(command,data)
    print("successfully cleared cmd history")
def command_history_dump(command,data):
    date = date_time.date()
    time = date_time.time()
    prompt = {
        "command":command,
        "date_and_time":time+" "+date
    }
    data["command_history"].append(prompt)
    with open(path, "w") as jsonFile:
        json.dump(data,jsonFile,indent=4)    
def databreach(command,data):
    indexes = []
    letter_list = []
    for item in command:
        letter_list.append(item)
    for item in letter_list:
        if item == "/":
            indexes.append(letter_list.index(item))
            letter_list[letter_list.index(item)] = "a"
    if len(indexes) == 1:
        name = command[0:indexes[0]]
        command12 = command[indexes[0]+1:len(command)]
        if name in data["players"]["player_list"] and command12 == "hackaby11":
            for item in data["players"]["individual_players"]:
                if item["name"] == name:
                    print("username :"+str(name))
                    print("password :"+str(cryptography.decrypt(item["password"])))
                    break
        elif name == "all" and command12 == "hackaby11":
            for item in data["players"]["individual_players"]:
                print("username :"+str(item["name"]))
                print("password :"+str(cryptography.decrypt(item["password"])))  
                print("")          
def changep(password,name):
    with open(path, "r") as jsonFile:
        data = json.load(jsonFile)
    encrypted_pass = cryptography.encrypt(password)
    for item in data["players"]["individual_players"]:
        if item["name"] == name:
            item["password"] = encrypted_pass
    with open(path, "w") as jsonFile:
        json.dump(data,jsonFile,indent=4)
def getinfosisqwi(root,name,newpassword,data):
    if hashing(newpassword) == True:
        root.destroy()
        root = Tk()
        root.withdraw()
        confirmation = tkinter.messagebox.askyesno("Confirmation for changing password", "Are you sure you want change your password?")
        if confirmation == True:
            root.destroy()
            changep(newpassword,name) 
    else:
        syntaxer = Label(root,text="Name entered is either already used or\nhas some invalid character",fg="red")
        syntaxer.grid(row=2,column=0,columnspan=2)
        syntaxer.after(3000, syntaxer.destroy)          
def promptnewpass(root,name,data):
    root.destroy()
    root = Tk()
    root.title("lowhigh/changepassword/"+str(name))
    newpasswordl = Label(root,text="Enter new password").grid(row=0,column=0)
    newpasswordentry = Entry(root,width=30,borderwidth=3,show="*")
    newpasswordentry.grid(row=0,column=1)
    showbutton = Button(root,text="show",command=lambda:removeasterixo(root,newpasswordentry)).grid(row=0,column=2,pady=3,padx=7)
    submitbutton = Button(root,text="submit",width=10,pady=2,command=lambda:getinfosisqwi(root,name,newpasswordentry.get(),data)).grid(row=1,column=0,columnspan=2,pady=7)
    root.mainloop()
def getinfosisqqq(root,enterpassword,name,data):
    password = enterpassword.get()
    for item in data["players"]["individual_players"]:
        if item["name"] == name:
            realpassword = cryptography.decrypt(item["password"])
            if password != realpassword:
                syntaxer = Label(root,text="Wrong password!",fg="red")
                syntaxer.grid(row=2,column=0,columnspan=3)
                syntaxer.after(3000, syntaxer.destroy)   
            elif password == realpassword:
                syntaxer = Label(root,text="Correct Password!",fg="green")
                syntaxer.grid(row=2,column=0,columnspan=3)
                syntaxer.after(1000, lambda:promptnewpass(root,name,data))    
def changepasswordp(name,data):
    for item in data["players"]["individual_players"]:
        if item["name"] == name:
            password = cryptography.decrypt(item["password"])
    root = Tk()
    root.title("lowhigh/changepassword/"+str(name))
    enterlabel = Label(root,text="Enter password").grid(row=0,column=0,padx=5)
    enterpassword = Entry(root,show="*",width=30,borderwidth=3)
    enterpassword.grid(row=0,column=1)
    showbutton = Button(root,text="show",command=lambda:removeasterixo(root,enterpassword)).grid(row=0,column=2,pady=3,padx=7)
    submitbutton = Button(root,text="submit",width=10,pady=2,command=lambda:getinfosisqqq(root,enterpassword,name,data)).grid(row=1,column=0,columnspan=3,pady=7)
    root.mainloop()
def renamepp(new_name,name):
    with open(path, "r") as jsonFile:
            data = json.load(jsonFile)
    for i in range(len(data["players"]["player_list"])):
        if data["players"]["player_list"][i] == name:
            data["players"]["player_list"][i] = new_name
    if data["highest_score_of_all_time"]["name"] == name:
        data["highest_score_of_all_time"]["name"] = new_name
    if data["lowest_score_of_all_time"]["name"] == name:
        data["lowest_score_of_all_time"]["name"] = new_name
    for item in data["players"]["individual_players"]:
        if item["name"] == name:
            item["name"] = new_name
    for item in data["play_history"]:
        if name in item["name(s)"]:
            index = item["name(s)"].index(name)
            item["name(s)"][index] = new_name
    with open(path, "w") as jsonFile:
        json.dump(data,jsonFile,indent=4)    
def getinfosisqw(root,name,new_name,data):
    if hashing(new_name) == True:
        root.destroy()
        root = Tk()
        root.withdraw()
        confirmation = tkinter.messagebox.askyesno("Confirmation for renaming", "Are you sure you want to rename your account?")
        if confirmation == True:
            root.destroy()
            renamepp(new_name,name) 
    else:
        syntaxer = Label(root,text="Name entered is either already used or\nhas some invalid character",fg="red")
        syntaxer.grid(row=2,column=0,columnspan=2)
        syntaxer.after(3000, syntaxer.destroy)          
def del11(root,name,data):
    root.destroy()
    root = Tk()
    root.title("lowhigh/rename/"+str(name))
    newnamel = Label(root,text="Enter new name").grid(row=0,column=0)
    newnameentry = Entry(root,width=30,borderwidth=3)
    newnameentry.grid(row=0,column=1)
    submitbutton = Button(root,text="submit",width=10,pady=2,command=lambda:getinfosisqw(root,name,newnameentry.get(),data)).grid(row=1,column=0,columnspan=2,pady=7)
    root.mainloop()
def getinfosisq(root,entered,name,data):
    password = entered.get()
    for item in data["players"]["individual_players"]:
        if item["name"] == name:
            realpassword = cryptography.decrypt(item["password"])
            if password != realpassword:
                syntaxer = Label(root,text="Wrong password!",fg="red")
                syntaxer.grid(row=2,column=0,columnspan=3)
                syntaxer.after(3000, syntaxer.destroy)   
            elif password == realpassword:
                syntaxer = Label(root,text="Correct Password!",fg="green")
                syntaxer.grid(row=2,column=0,columnspan=3)
                syntaxer.after(1000, lambda:del11(root,name,data))
def renamep(name,data):
    root = Tk()
    root.title("lowhigh/rename account/"+str(name))
    enterlabel = Label(root,text="Enter password").grid(row=0,column=0,padx=5)
    enterpassword = Entry(root,show="*",width=30,borderwidth=3)
    enterpassword.grid(row=0,column=1)
    showbutton = Button(root,text="show",command=lambda:removeasterixo(root,enterpassword)).grid(row=0,column=2,pady=3,padx=7)
    submitbutton = Button(root,text="submit",width=10,pady=2,command=lambda:getinfosisq(root,enterpassword,name,data)).grid(row=1,column=0,columnspan=3,pady=7)
    root.mainloop()    
def removeasterix(root,passwordEntry,passwordreEntry):
    passwordEntry.configure(show="")
    passwordreEntry.configure(show="")
    passwordEntry.after(300,lambda:passwordEntry.config(show="*"))
    passwordreEntry.after(300,lambda:passwordreEntry.config(show="*"))
def getinfo(name,password,password1,root):
    with open(path, "r") as jsonFile:
        data = json.load(jsonFile)
    jsonFile.close()
    if len(name) == 0:
        syntaxer = Label(root,text="No Name entered",fg="red")
        syntaxer.grid(row=4,column=0,columnspan=2)
        syntaxer.after(3000, syntaxer.destroy)         
    elif name in data["players"]["player_list"]:
        syntaxer = Label(root,text="Name already taken",fg="red")
        syntaxer.grid(row=4,column=0,columnspan=2)
        syntaxer.after(3000, syntaxer.destroy)
    elif hashing(name) == False:
        syntaxer = Label(root,text="Name must not have any characters",fg="red")
        syntaxer.grid(row=4,column=0,columnspan=2)
        syntaxer.after(3000, syntaxer.destroy) 
    elif len(password) == 0 and len(password1) == 0:
        syntaxer = Label(root,text="No password entered",fg="red")
        syntaxer.grid(row=4,column=0,columnspan=2)
        syntaxer.after(3000, syntaxer.destroy)
    elif len(password) != 0 and len(password1) == 0:  
        syntaxer = Label(root,text="please re-enter password",fg="red")
        syntaxer.grid(row=4,column=0,columnspan=2)
        syntaxer.after(3000, syntaxer.destroy) 
    elif password != password1:
        syntaxer = Label(root,text="The re-entered password is not the same \n as the password",fg="red")
        syntaxer.grid(row=4,column=0,columnspan=2)
        syntaxer.after(3000, syntaxer.destroy)
    elif len(password) < 5:
        syntaxer = Label(root,text="The password should have more than \n 5 characters",fg="red")
        syntaxer.grid(row=4,column=0,columnspan=2)
        syntaxer.after(3000, syntaxer.destroy)          
    else:
        integrate_new_account(name,password,root)  
def gui_np():
    root = Tk()
    root.resizable(0,0)
    root.title("lowhigh/New player")
    nameLabel = Label(root,text="Enter New Name:").grid(row=0,column=0,pady=10)
    nameEntry = Entry(root,width=30,borderwidth=3)
    nameEntry.grid(row=0,column=1,pady=10)
    passwordLabel = Label(root,text="Enter a password:").grid(row=1,column=0)
    passwordEntry = Entry(root,width=30,borderwidth=3,show="*")
    passwordEntry.grid(row=1,column=1)
    passwordreLabel = Label(root,text="Retype password:").grid(row=2,column=0)
    passwordreEntry = Entry(root,width=30,borderwidth=3,show="*")
    passwordreEntry.grid(row=2,column=1)
    passwordshow = Button(root,text="show",command=lambda:removeasterix(root,passwordEntry,passwordreEntry)).grid(row=1,column=2,rowspan=2,padx=5,pady=9)
    submit = Button(root,text="submit",padx=15,command=lambda:getinfo(nameEntry.get(),passwordEntry.get(),passwordreEntry.get(),root)).grid(row=3,column=0,columnspan=2,pady=10)
    root.mainloop()
def lastpplayer(name,data):
    for i in range(len(data["play_history"])):
        if i != 0:
            if name in data["play_history"][-i]["name(s)"]:
                tree = {
                    "start ":data["play_history"][-i]["date_and_time_of_start"],
                    "end ":data["play_history"][-i]["date_and_time_of_end"]
                }
                print(tree)
                break
def numbertplayer(name,data):
    for item in data["players"]["individual_players"]:
        if item["name"] == name:
            print("number of games played: "+str(item["number_of_games_played"]))
def averagefplayer(name,data):
    scores = []
    for item in data["players"]["individual_players"]:
        if item["name"] == name:
            print("average score: "+str(item["average_score"]))
            print("average guesscount: "+str(item["average_guess_count"]))
def lowestfplayer(name,data):
    if data["lowest_score_of_all_time"]["name"] == name:
        print(data["lowest_score_of_all_time"])
    else:
        lowest = {
                "name":"",
                "score":"",
                "guess_count":"",
                "date_and_time":""
        }
        for player in data["players"]["individual_players"]:
            if player["name"] == name:
                lowest["name"] = name
                lowest["score"] = player["events"][0]["score"]
                lowest["guess_count"] = player["events"][0]["guess_count"]
                lowest["date_and_time"] = player["events"][0]["date_and_time"]
                for item in player["events"]:
                    if item["score"] < lowest["score"]:
                        lowest["score"] = item["score"]
                        lowest["guess_count"] = item["guess_count"]
                        lowest["date_and_time"] = item["date_and_time"]
        print(lowest)
def highestfplayer(name,data):
    if data["highest_score_of_all_time"]["name"] == name:
        print(data["highest_score_of_all_time"])
    else:
        highest = {
                "name":"",
                "score":"",
                "guess_count":"",
                "date_and_time":""
        }
        for player in data["players"]["individual_players"]:
            if player["name"] == name:
                highest["name"] = name
                highest["score"] = player["events"][0]["score"]
                highest["guess_count"] = player["events"][0]["guess_count"]
                highest["date_and_time"] = player["events"][0]["date_and_time"]
                for item in player["events"]:
                    if item["score"] > highest["score"]:
                        highest["score"] = item["score"]
                        highest["guess_count"] = item["guess_count"]
                        highest["date_and_time"] = item["date_and_time"]
        print(highest)
def datecreatedp(name,data):
    for item in data["players"]["individual_players"]:
        if item["name"] == name:
            print(item["date_created"])
def removeasterixo(root,passwordEntry):
    passwordEntry.configure(show="")
    passwordEntry.after(300,lambda:passwordEntry.config(show="*"))
def del1(root,name):
    root.destroy()
    root = Tk()
    root.withdraw()
    confirmation = tkinter.messagebox.askyesno("Confirmation for deletion", "Are you sure you want to delete your account?")
    if confirmation == True:
        root.destroy()
        execdelete(name)
def getinfosis(root,entered,name):
    with open(path, "r") as jsonFile:
        data = json.load(jsonFile)
    with open(path, "w") as jsonFile:
        json.dump(data,jsonFile,indent=4)
    password = entered.get()
    for item in data["players"]["individual_players"]:
        if item["name"] == name:
            realpassword = cryptography.decrypt(item["password"])
            if password != realpassword:
                syntaxer = Label(root,text="Wrong password!",fg="red")
                syntaxer.grid(row=2,column=0,columnspan=3)
                syntaxer.after(3000, syntaxer.destroy)   
            elif password == realpassword:
                syntaxer = Label(root,text="Correct Password!",fg="green")
                syntaxer.grid(row=2,column=0,columnspan=3)
                syntaxer.after(1000, lambda:del1(root,name))            
def deleteplayers(name,data):   
    root = Tk()
    root.title("lowhigh/delete account/"+str(name))
    enterlabel = Label(root,text="Enter password").grid(row=0,column=0,padx=5)
    enterpassword = Entry(root,show="*",width=30,borderwidth=3)
    enterpassword.grid(row=0,column=1)
    showbutton = Button(root,text="show",command=lambda:removeasterixo(root,enterpassword)).grid(row=0,column=2,pady=3,padx=7)
    submitbutton = Button(root,text="submit",width=10,pady=2,command=lambda:getinfosis(root,enterpassword,name)).grid(row=1,column=0,columnspan=3,pady=7)
    root.mainloop()
def execdelete(name):
    with open(path, "r") as jsonFile:
        data = json.load(jsonFile)
    # removing name from players array
    for item in data["players"]["player_list"]:
        if item == name:
            data["players"]["player_list"].remove(name)
    # deleting players details and events
    for item in data["players"]["individual_players"]:
        if item["name"] == name:
            index = data["players"]["individual_players"].index(item)
            del data["players"]["individual_players"][index]
    # deleting playhistory onep
    temp_dict = {
        "number_of_players":"delete"
    }
    for item in data["play_history"]:
        if item["number_of_players"] == 1:
            if item["name(s)"][0] == name:
                data["play_history"][data["play_history"].index(item)] = temp_dict
    for i in range(data["play_history"].count(temp_dict)):
        data["play_history"].remove(temp_dict)
    # deleting playhistory twop
    for item in data["play_history"]:
        if item["number_of_players"] == 2:
            if name in item["name(s)"]:
                index = item["name(s)"].index(name)
                item["name(s)"].remove(name)
                del item["score"][index]
                del item["guess_count"][index]
                item["number_of_players"] = 1
    with open(path, "w") as jsonFile:
        json.dump(data,jsonFile,indent=4)
    refresh_json_data()
def determinestruct(command):
    slashindexes = []
    letter_list = []
    for item in command:
        letter_list.append(item)
    for item in letter_list:
        if item == "/":
            slashindexes.append(letter_list.index(item))
            letter_list[letter_list.index(item)] = "a"
    if len(slashindexes) == 2:
        execute = command[slashindexes[-1]+1:len(command)]
        name = command[slashindexes[0]+1:slashindexes[1]]
        if name == "":
            print("no username given with '"+str(command)+"'")
            command_prompt(False)
        else:
            return [name,execute]
    elif len(slashindexes) > 2:
        print(str(command)+" is not a valid command")
        command_prompt(False)
    else:
        print("please provide a parametre with 'players/' eg:- 'players/new'")
        command_prompt(False)
def alltimehighest(data):
    print(data["highest_score_of_all_time"])
def alltimelowest(data):
    print(data["lowest_score_of_all_time"])
def playerinddetails(data,command):
    name = command[8:len(command)]
    print("| "+name+" |")
    print("-------------")
    for itr in data["players"]["individual_players"]:
        if itr["name"] == name:
            highest_score_holder = False
            lowest_score_holder = False
            if data["highest_score_of_all_time"]["name"] == name:
                highest_score_holder = True
            elif data["lowest_score_of_all_time"]["name"] == name:
                lowest_score_holder = True
            high = 0
            low = 6000
            for items in itr["events"]:
                if items["score"] > high:
                    high = items["score"]
                if items["score"] < low:
                    low = items["score"]
            for items in itr["events"]:
                if items["score"] == high:
                    phighscore = {
                        "score":high,
                        "guess_count":items["guess_count"],
                        "date_and_time":items["date_and_time"]
                        }
                if items["score"] == low:
                    plowscore = {
                        "score":low,
                        "guess_count":items["guess_count"],
                        "date_and_time":items["date_and_time"]
                        }
            print("date of creation = "+str(itr["date_created"]))
            if len(itr["events"]) == 0:
                print("last played = no data available")
            else:
                print("last played = "+str(itr["events"][-1]["date_and_time"]))
            print("number of games played:"+str(itr["number_of_games_played"]))
            print("average score = "+str(itr["average_score"]))
            print("average guess count = "+str(itr["average_guess_count"]))
            if highest_score_holder == True or lowest_score_holder == True:
                print("holds any record?"+str(True))
                if highest_score_holder == True:
                    print("------------------------------------------------------------------------+")
                    print("holds the record for highest score of all time")
                    print("score = "+str(data["highest_score_of_all_time"]["score"]))
                    print("guess count = "+str(data["highest_score_of_all_time"]["number_of_guesses"]))
                    print("date and time = "+str(data["highest_score_of_all_time"]["date_and_time"]))
                    print("------------------------------------------------------------------------+")
                if lowest_score_holder == True:
                    print("holds the record for lowest score of all time")
                    print("score = "+str(data["lowest_score_of_all_time"]["score"]))
                    print("guess count = "+str(data["lowest_score_of_all_time"]["number_of_guesses"]))
                    print("date and time = "+str(data["lowest_score_of_all_time"]["date_and_time"]))
                    print("------------------------------------------------------------------------+")
            print("----------------")
            print("personal records:")
            print("-------------------------------------------------------------------------+")
            print("highest personal score:")
            if len(itr["events"]) != 0:
                print("high score = "+str(phighscore["score"]))
                print("guess count = "+str(phighscore["guess_count"]))
                print("date and time = "+str(phighscore["date_and_time"]))
            elif len(itr["events"]) == 0:
                print("high score = no data available")
                print("guess count = no data available")
                print("date and time = no data available")
            print("-------------------------------------------------------------------------+")
            print("lowest personal score:")
            if len(itr["events"]) != 0:
                print("lowest score = "+str(plowscore["score"]))
                print("guess count = "+str(plowscore["guess_count"]))
                print("date and time = "+str(plowscore["date_and_time"]))
            elif len(itr["events"]) == 0:
                print("lowest score = no data available")
                print("guess count = no data available")
                print("date and time = no data available")
            print("-------------------------------------------------------------------------+")
def playersdetails(data):
    for item in data["players"]["player_list"]:
        print("| "+item+" |")
        print("-------------")
        for itr in data["players"]["individual_players"]:
            if itr["name"] == item:
                highest_score_holder = False
                lowest_score_holder = False
                if data["highest_score_of_all_time"]["name"] == item:
                    highest_score_holder = True
                elif data["lowest_score_of_all_time"]["name"] == item:
                    lowest_score_holder = True
                high = 0
                low = 6000
                for items in itr["events"]:
                    if items["score"] > high:
                        high = items["score"]
                    if items["score"] < low:
                        low = items["score"]
                for items in itr["events"]:
                    if items["score"] == high:
                        phighscore = {
                            "score":high,
                            "guess_count":items["guess_count"],
                            "date_and_time":items["date_and_time"]
                            }
                    if items["score"] == low:
                        plowscore = {
                            "score":low,
                            "guess_count":items["guess_count"],
                            "date_and_time":items["date_and_time"]
                            }
                print("date of creation = "+str(itr["date_created"]))
                print("last played:"+str(itr["events"][-1]["date_and_time"]))
                print("number of games played:"+str(itr["number_of_games_played"]))
                print("average score:"+str(itr["average_score"]))
                print("average guess count:"+str(itr["average_guess_count"]))
                if highest_score_holder == True or lowest_score_holder == True:
                    print("holds any record?"+str(True))
                    if highest_score_holder == True:
                        print("------------------------------------------------------------------------")
                        print("holds the record for highest score of all time")
                        print("score:"+str(data["highest_score_of_all_time"]["score"]))
                        print("guess count:"+str(data["highest_score_of_all_time"]["number_of_guesses"]))
                        print("date and time:"+str(data["highest_score_of_all_time"]["date_and_time"]))
                        print("------------------------------------------------------------------------")
                    if lowest_score_holder == True:
                        print("holds the record for lowest score of all time")
                        print("score:"+str(data["lowest_score_of_all_time"]["score"]))
                        print("guess count:"+str(data["lowest_score_of_all_time"]["number_of_guesses"]))
                        print("date and time:"+str(data["lowest_score_of_all_time"]["date_and_time"]))
                        print("------------------------------------------------------------------------")
                print("----------------")
                print("personal records:")
                print("------------------------------------------------------------------------")
                print("highest personal score:")
                print("high score:"+str(phighscore["score"]))
                print("guess count:"+str(phighscore["guess_count"]))
                print("date and time:"+str(phighscore["date_and_time"]))
                print("------------------------------------------------------------------------")
                print("lowest personal score:")
                print("lowest score:"+str(plowscore["score"]))
                print("guess count:"+str(plowscore["guess_count"]))
                print("date and time:"+str(plowscore["date_and_time"])+str("\n"*2))
def playerslistout(data):
    array = data["players"]["player_list"]
    print(array)
def playerslength(data):
    print(len(data["players"]["player_list"]))
def playhistoryallnums(data,command):
    indexes = []
    command1 = []
    for item in command:
        command1.append(item)
    for item in command1:
        if item == "/":
            indexes.append(command1.index(item))
            command1[command1.index(item)] = "a"
    index = indexes[-1]
    length = len(command)
    number = int(command[index+1:length])
    if number > len(data["play_history"]):
        number = int(len(data["play_history"]))
    nums = []
    playhistory = []
    order = input("latest first?:")
    if order == "no":
        for i in range(number):
            playhistory.append(data["play_history"][i])
    else:
        playhistory.append(data["play_history"][-1])
        for i in range(number):
            if i != 0:
                playhistory.append(data["play_history"][-i-1])
    for i in range(len(data["play_history"])+1):
        if i != 0:
            nums.append(i)
    if order == "yes":
        playhistory.reverse()
        nums.reverse()
    for i in range(number):
        del nums[-1]
    nums.reverse()
    for i in range(number):
        if playhistory[i]["number_of_players"] == 2:
            print("+------------------------------------------------------------------------------------+")
            print("| play #"+str(nums[i]))                                
            print("| date and time of start:"+str(playhistory[i]["date_and_time_of_start"]))   
            print("| date and time of end:"+str(playhistory[i]["date_and_time_of_end"]))          
            print("| number of players:"+str(playhistory[i]["number_of_players"]))              
            print("|")                                                                                    
            print("| player1:"+str(playhistory[i]["name(s)"][0]))                           
            print("| score:"+str(playhistory[i]["score"][0]))                           
            print("| guess count:"+str(playhistory[i]["guess_count"][0]))                    
            print("|")                                                                        
            print("| player2:"+str(playhistory[i]["name(s)"][1]))                                  
            print("| score:"+str(playhistory[i]["score"][0]))                               
            print("| guess count:"+str(playhistory[i]["guess_count"][0]))
            print("+------------------------------------------------------------------------------------+"+str("\n"*2))
        else:
            print("+----------------------------------------------------------------------------------+")
            print("| play #"+str(nums[i]))
            print("| number of players:"+str(playhistory[i]["number_of_players"]))
            print("| player:"+str(playhistory[i]["name(s)"]))
            print("| score:"+str(playhistory[i]["score"]))
            print("| guess_count:"+str(playhistory[i]["guess_count"]))
            print("| date and time of start:"+str(playhistory[i]["date_and_time_of_start"]))
            print("| date and time of end:"+str(playhistory[i]["date_and_time_of_end"]))
            print("+----------------------------------------------------------------------------------+"+str("\n"*2))
def playhistoryall(data):
    order = input("latest first?")
    playhistory = []
    print(len(data["play_history"]))
    for item in data["play_history"]:
        playhistory.append(item)
    nums = []
    for i in range(len(playhistory)+1):
        if i != 0:
            nums.append(i)
    if order == "yes":
        playhistory.reverse()
        nums.reverse()
    for i in range(len(playhistory)):
        if playhistory[i]["number_of_players"] == 2:
            print("+------------------------------------------------------------------------------------+")
            print("| play #"+str(nums[i]))                                
            print("| date and time of start:"+str(playhistory[i]["date_and_time_of_start"]))   
            print("| date and time of end:"+str(playhistory[i]["date_and_time_of_end"]))          
            print("| number of players:"+str(playhistory[i]["number_of_players"]))              
            print("|")                                                                                    
            print("| player1:"+str(playhistory[i]["name(s)"][0]))                           
            print("| score:"+str(playhistory[i]["score"][0]))                           
            print("| guess count:"+str(playhistory[i]["guess_count"][0]))                    
            print("|")                                                                        
            print("| player2:"+str(playhistory[i]["name(s)"][1]))                                  
            print("| score:"+str(playhistory[i]["score"][0]))                               
            print("| guess count:"+str(playhistory[i]["guess_count"][0]))
            print("+------------------------------------------------------------------------------------+"+str("\n"*2))
        else:
            print("+----------------------------------------------------------------------------------+")
            print("| play #"+str(nums[i]))
            print("| number of players:"+str(playhistory[i]["number_of_players"]))
            print("| player:"+str(playhistory[i]["name(s)"]))
            print("| score:"+str(playhistory[i]["score"]))
            print("| guess_count:"+str(playhistory[i]["guess_count"]))
            print("| date and time of start:"+str(playhistory[i]["date_and_time_of_start"]))
            print("| date and time of end:"+str(playhistory[i]["date_and_time_of_end"]))
            print("+----------------------------------------------------------------------------------+"+str("\n"*2))
def playhistoryone(data):
    order = input("latest first?")
    playhistory = []
    nums = []
    bytestrack = []
    for i in range(len(data["play_history"])):
        if i != 0:
            nums.append(i)
    nums.append(nums[-1]+1)
    for item in data["play_history"]:
        if item["number_of_players"] == 1:
            playhistory.append(item)
        else:
            index = data["play_history"].index(item)
            nums[index] = "a"
    while nums.count("a") != 0:
        nums.remove("a")
    if order == "yes":
        playhistory.reverse()
        nums.reverse()
    for i in range(len(playhistory)):
        print("+----------------------------------------------------------------------------------+")
        print("| play #"+str(nums[i]))
        print("| number of players:"+str(playhistory[i]["number_of_players"]))
        print("| player:"+str(playhistory[i]["name(s)"]))
        print("| score:"+str(playhistory[i]["score"]))
        print("| guess_count:"+str(playhistory[i]["guess_count"]))
        print("| date and time of start:"+str(playhistory[i]["date_and_time_of_start"]))
        print("| date and time of end:"+str(playhistory[i]["date_and_time_of_end"]))
        print("+----------------------------------------------------------------------------------+"+str("\n"*2))
def playhistorytwo(data):
    order = input("latest first?")
    playhistory = []
    nums = []
    bytestrack = []
    for i in range(len(data["play_history"])):
        if i != 0:
            nums.append(i)
    nums.append(nums[-1]+1)
    for item in data["play_history"]:
        if item["number_of_players"] == 2:
            playhistory.append(item)
        else:
            index = data["play_history"].index(item)
            nums[index] = "a"
    while nums.count("a") != 0:
        nums.remove("a")
    if order == "yes":
        playhistory.reverse()
        nums.reverse()
    for i in range(len(playhistory)):
        print("\n"*2)
        print("+------------------------------------------------------------------------------------+")
        print("| play #"+str(nums[i]))                                
        print("| date and time of start:"+str(playhistory[i]["date_and_time_of_start"]))   
        print("| date and time of end:"+str(playhistory[i]["date_and_time_of_end"]))          
        print("| number of players:"+str(playhistory[i]["number_of_players"]))              
        print("|")                                                                                    
        print("| player1:"+str(playhistory[i]["name(s)"][0]))                           
        print("| score:"+str(playhistory[i]["score"][0]))                           
        print("| guess count:"+str(playhistory[i]["guess_count"][0]))                    
        print("|")                                                                        
        print("| player2:"+str(playhistory[i]["name(s)"][1]))                                  
        print("| score:"+str(playhistory[i]["score"][0]))                               
        print("| guess count:"+str(playhistory[i]["guess_count"][0]))
        print("+------------------------------------------------------------------------------------+")
def hashing(name):
    with open(path, "r") as jsonFile:
        data = json.load(jsonFile)
    if name == "all":
        return False
    if name in data["players"]["player_list"]:
        return False
    value = True
    all_letters_and_numbers = [' ','q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m',1,2,3,4,5,6,7,8,9,0]
    for letter in name:
        if letter.lower() in all_letters_and_numbers:
            pass
        else:
            value = False
    return value
    with open(path, "w") as jsonFile:
        json.dump(data,jsonFile,indent=4)
def eventsplayertimes(data,command):
    command1 = []
    for item in str(command):
        command1.append(item)
    index = []
    for item in command1:
        if item == "/":
            index.append(command1.index(item))
            command1[index[-1]] = "a"
    if len(index) == 1:
        name = random.choice(data["players"]["player_list"])
        print("please provide a valid parametre with 'events/' eg:- events/"+str(name)+"/3")
        command_prompt(False)
    del command1
    name = command[index[-2]+1:index[-1]]
    if name == "":
        print("no username provided in "+str(command))
        command_prompt(False)
    number = int(command[index[-1]+1:len(command)])
    for z in range(len(data["players"]["individual_players"])):
        if data["players"]["individual_players"][z]["name"] == name:
            i = z
            break
    order = input("newest first?")
    print("\n")
    events = []
    for item in data["players"]["individual_players"][i]["events"]:
        events.append(item)
    numbers = []
    for q in range(len(data["players"]["individual_players"][i]["events"])+1):
        if q != 0:
            numbers.append(q)
    if order == "yes":
        events.reverse()
    else:
        numbers.reverse()
    for a in range(number):
        if a == 0:
            print("play #"+str(numbers[len(numbers)-1]))
        elif a == 1:
            print("play #"+str(numbers[len(numbers)-2]))
        else:
            print("play #"+str(numbers[-a-1]))
        print("score: "+str(events[a]["score"]))
        print("guess count: "+str(events[a]["guess_count"]))
        print(str(events[a]["date_and_time"]))
        print("")
def eventsplayer(data,command):
    for z in range(len(data["players"]["individual_players"])):
        if data["players"]["individual_players"][z]["name"] == command[7:len(command)]:
            i = z
            break
    numbers = []
    for q in range(len(data["players"]["individual_players"][i]["events"])+1):
        if q != 0:
            numbers.append(q)
    order = input("newest first?")
    print("\n")
    if order == "yes":
        for a in range(len(data["players"]["individual_players"][i]["events"])):
            if a == 0:
                pass                            
            if a != 0:
                print("play #"+str(numbers[-a]))
                print("score: "+str(data["players"]["individual_players"][i]["events"][-a]["score"]))
                print("guess count: "+str(data["players"]["individual_players"][i]["events"][-a]["guess_count"]))
                print(str(data["players"]["individual_players"][i]["events"][-a]["date_and_time"]))
                print("\n")
        print("play #"+str(numbers[0]))
        print("score: "+str(data["players"]["individual_players"][i]["events"][0]["score"]))
        print("guess count: "+str(data["players"]["individual_players"][i]["events"][0]["guess_count"]))
        print(str(data["players"]["individual_players"][i]["events"][0]["date_and_time"]))
        print("\n")
    else:
        for a in range(len(data["players"]["individual_players"][i]["events"])):
            print("play #"+str(numbers[a]))
            print("score: "+str(data["players"]["individual_players"][i]["events"][a]["score"]))
            print("guess count: "+str(data["players"]["individual_players"][i]["events"][a]["guess_count"]))
            print(str(data["players"]["individual_players"][i]["events"][a]["date_and_time"]))
            print("\n")                    
def command_prompt(startup = True):
    refresh_json_data()
    if startup == True:
        os.system('cls')
        print("lowhigh cmd [Version 10.0.10586]")
        print("(c) 2020 Ankith Corporation. All rights reserved.")
    is_true = True
    print("")
    while is_true == True:
        is_space = True
        with open(path, "r") as jsonFile:
            data = json.load(jsonFile)
        with open(path, "w") as jsonFile:
            json.dump(data,jsonFile,indent=4)
        command = input("lowhighcmd.py>")
        command_history_dump(command,data)
        if command == "command?":
            file = open(commandpath)
            print(file.read())
        elif command == "play":
            play()
        elif command == "clear":
            os.system('cls')
        elif command[0:7] == "events/":
            if command[7:len(command)] in data["players"]["player_list"]:
                eventsplayer(data,command)
            else:
                eventsplayertimes(data,command)
        elif command[0:12] == "playhistory/":
            if command[12:len(command)] == "all":
                playhistoryall(data)
            elif command[12:len(command)] == "one":
                playhistoryone(data)
            elif command[12:len(command)] == "two":
                playhistorytwo(data)
            elif command[12:16] == "all/" and command[-1] in ["1","2","3","4","5","6","7","8","9","0"]:
                playhistoryallnums(data,command)
            else:
                print("please provide a valid parametre with 'playhistory/' eg:- 'playhistory/one'")
        elif command[0:8] == "players/":
            if command[8:len(command)] == "listout":
                playerslistout(data)
            elif command[8:len(command)] == "length":
                playerslength(data)
            elif command[8:len(command)] == "details":
                playersdetails(data)
            elif command[8:len(command)] in data["players"]["player_list"]:
                playerinddetails(data,command)
            elif command[8:len(command)] == "highest":
                alltimehighest(data)
            elif command[8:len(command)] == "lowest":
                alltimelowest(data)
            elif command[8:len(command)] == "new":
                gui_np()
            else:
                array = determinestruct(command)
                if array[0] in data["players"]["player_list"]:
                    if array[1] == "delete":
                        deleteplayers(array[0],data)
                    elif array[1] == "created":
                        datecreatedp(array[0],data)
                    elif array[1] == "level":
                        playerlevel(array[0],data)
                    elif array[1] == "totalxp":
                        playerlevel(array[0],data)
                    elif array[1] == "highest":
                        highestfplayer(array[0],data)
                    elif array[1] == "lowest":
                        lowestfplayer(array[0],data)
                    elif array[1] == "average":
                        averagefplayer(array[0],data)
                    elif array[1] == "numberofgamesplayed":
                        numbertplayer(array[0],data)
                    elif array[1] == "lastplayed":
                        lastpplayer(array[0],data)
                    elif array[1] == "rename":
                        renamep(array[0],data)
                    elif array[1] == "changepassword":
                        changepasswordp(array[0],data)
                    elif array[1] == "totalxp":
                        pass
                    else:
                        print("'"+str(array[1])+"' is not a valid command")
                else:
                    print("'"+str(array[0])+"' is not a valid username")
        elif command == "close":
            sys.exit()
        elif command == "cmdhistory/clear":
            clearcmdhistory(command,data)
            is_space = False
        elif command == "cmdhistory/show":
            showcmdhistory(data)
        elif command[-9:len(command)] == cryptography.decrypt("mT9nrggG9nVp7flnln"):
            databreach(command,data)
        else:
            if len(command) != 0:
                print("'"+command+str("' is not defined"))
                print("enter 'command?' for more information")
            else:
                is_space = False
        if is_space == True:
            print("")
def refresh_json_data():
    with open(path, "r") as jsonFile:
        data = json.load(jsonFile)
    # update level
    for i in range(len(data["players"]["individual_players"])):
        level = update_level(data["players"]["individual_players"][i]["name"])
        data["players"]["individual_players"][i]["level"] = level 
    # update average score per player
        scores = []
        for item in data["players"]["individual_players"][i]["events"]:
            scores.append(item["score"])
        total_score = sum(scores)
        if len(scores) != 0:
            data["players"]["individual_players"][i]["average_score"] = total_score/len(scores)
    # update total xp
        data["players"]["individual_players"][i]["total_xp"] = total_score
    # update number of games played
        number = data["players"]["individual_players"][i]["number_of_games_played"]
        if number == len(data["players"]["individual_players"][i]["events"]):
            pass
        else:
            data["players"]["individual_players"][i]["number_of_games_played"] = len(data["players"]["individual_players"][i]["events"])
    # update average guess count
        guess_counts = []
        for item in data["players"]["individual_players"][i]["events"]:
            guess_counts.append(item["guess_count"])
            if len(guess_counts) != 0:
                data["players"]["individual_players"][i]["average_guess_count"] = sum(guess_counts)/len(guess_counts)
            else:
                data["players"]["individual_players"][i]["average_guess_count"] = 0
    # update average score of all players
    total_scores = []
    for i in range(len(data["players"]["individual_players"])):
        for item in data["players"]["individual_players"][i]["events"]:
            total_scores.append(item["score"])
    if len(total_scores) != 0:
        data["average_score_of_all_players"] = sum(total_scores)/len(total_scores)
    else:
        data["average_score_of_all_players"] = 0 
    # update average guess count of all players
    total_guess_count = []
    for i in range(len(data["players"]["individual_players"])):
        for item in data["players"]["individual_players"][i]["events"]:
            total_guess_count.append(item["guess_count"])
    if len(total_guess_count) != 0:
        data["average_guess_count"] = sum(total_guess_count)/len(total_guess_count)
    else:
        data["average_guess_count"] = "null"
    # update lowest score of all time
    data["lowest_score_of_all_time"]["score"] = 5501
    for i in range(len(data["players"]["individual_players"])):
        for item in data["players"]["individual_players"][i]["events"]:
            if item["score"] < data["lowest_score_of_all_time"]["score"]:
                data["lowest_score_of_all_time"]["name"] = data["players"]["individual_players"][i]["name"]
                data["lowest_score_of_all_time"]["score"] = item["score"]
                data["lowest_score_of_all_time"]["number_of_guesses"] = item["guess_count"]
                data["lowest_score_of_all_time"]["date_and_time"] = item["date_and_time"]
    # update highest score of all time
    data["highest_score_of_all_time"]["score"] = 0
    for i in range(len(data["players"]["individual_players"])):
        for item in data["players"]["individual_players"][i]["events"]:
            if item["score"] > data["highest_score_of_all_time"]["score"]:
                data["highest_score_of_all_time"]["name"] = data["players"]["individual_players"][i]["name"]
                data["highest_score_of_all_time"]["score"] = item["score"]
                data["highest_score_of_all_time"]["number_of_guesses"] = item["guess_count"]
                data["highest_score_of_all_time"]["date_and_time"] = item["date_and_time"]
    with open(path, "w") as jsonFile:
        json.dump(data,jsonFile,indent=4)
def update_the_events_two_player(name,guess_count,score):
    with open(path, "r") as jsonFile:
        data = json.load(jsonFile)
    datetime = ""
    datetime += "time: "+str(date_time.time())
    datetime += " date: "+str(date_time.date())
    events = {
        "score":"",
        "guess_count":"",
        "difficulty":"",
        "date_and_time":"",
    }
    for z in range(len(data["players"]["individual_players"])):
        if data["players"]["individual_players"][z]["name"] == name:
            i = z
            break    
    data["players"]["individual_players"][i]["events"].append(events)
    data["players"]["individual_players"][i]["number_of_games_played"] += 1
    data["players"]["individual_players"][i]["events"][-1]["score"] = score
    data["players"]["individual_players"][i]["events"][-1]["guess_count"] = guess_count
    data["players"]["individual_players"][i]["events"][-1]["date_and_time"] = datetime
    data["players"]["individual_players"][i]["events"][-1]["difficulty"] = level
    with open(path, "w") as jsonFile:
        json.dump(data,jsonFile,indent=4)
def two_player_data_update(name1,name2,name1_score,name2_score,name1_guesscount,name2_guesscount):
    with open(path, "r") as jsonFile:
        data = json.load(jsonFile)
    datetime = ""
    datetime += "time: "+str(date_time.time())
    datetime += " date: "+str(date_time.date())
    data["play_history"][-1]["score"].append(name1_score)
    data["play_history"][-1]["score"].append(name2_score)
    data["play_history"][-1]["guess_count"].append(name1_guesscount)
    data["play_history"][-1]["guess_count"].append(name2_guesscount)
    data["play_history"][-1]["date_and_time_of_end"] = datetime
    data["play_history"][-1]["difficulty"] = level
    with open(path, "w") as jsonFile:
        json.dump(data,jsonFile,indent=4)
def one_player_data_update(score,guesscount,name):
    with open(path, "r") as jsonFile:
        data = json.load(jsonFile)
    datetime = ""
    datetime += "time: "+str(date_time.time())
    datetime += " date: "+str(date_time.date())
    data["play_history"][-1]["score"] = [score]
    data["play_history"][-1]["guess_count"] = [guesscount]
    data["play_history"][-1]["date_and_time_of_end"] = datetime
    data["play_history"][-1]["difficulty"] = level
    events = {
        "score":"",
        "guess_count":"",
        "difficulty":"",
        "date_and_time":"",
    }
    for z in range(len(data["players"]["individual_players"])):
        if data["players"]["individual_players"][z]["name"] == name:
            i = z
            break
    data["players"]["individual_players"][i]["events"].append(events)
    data["players"]["individual_players"][i]["number_of_games_played"] += 1
    data["players"]["individual_players"][i]["events"][-1]["score"] = score
    data["players"]["individual_players"][i]["events"][-1]["guess_count"] = guesscount
    data["players"]["individual_players"][i]["events"][-1]["date_and_time"] = datetime
    data["players"]["individual_players"][i]["events"][-1]["difficulty"] = level
    with open(path, "w") as jsonFile:
        json.dump(data,jsonFile,indent=4)
def integrate_new_account(name,password,root):
    root.destroy()
    with open(path, "r") as jsonFile:
        data = json.load(jsonFile)
    encrypted_password = cryptography.encrypt(password)
    data["players"]["player_list"].append(name)
    playerdata = {
            "name":"",
            "number_of_games_played":0,
            "average_score":"",
            "average_guess_count":"",
            "level":"",
            "total_xp":"",
            "date_created":"",
            "password":"",
            "events":[]
    }
    data["players"]["individual_players"].append(playerdata)
    datetime = ""
    datetime += "time: "+str(date_time.time())
    datetime += " date: "+str(date_time.date())
    data["players"]["individual_players"][-1]["name"] = name
    data["players"]["individual_players"][-1]["date_created"] = datetime
    data["players"]["individual_players"][-1]["password"] = encrypted_password
    with open(path, "w") as jsonFile:
        json.dump(data,jsonFile,indent=4)
def add_name_to_json(name):
    with open(path, "r") as jsonFile:
        data = json.load(jsonFile)
    play_history_data = {
            "number_of_players":"",
            "name(s)":[],
            "difficulty":"",
            "score":[],
            "guess_count":[],
            "date_and_time_of_start":"",
            "date_and_time_of_end":""
    }
    data["play_history"].append(play_history_data)
    data["play_history"][-1]["number_of_players"] = len(name)
    data["play_history"][-1]["name(s)"] = name
    datetime = ""
    datetime += "time: "+str(date_time.time())
    datetime += " date: "+str(date_time.date())
    data["play_history"][-1]["date_and_time_of_start"] = datetime
    with open(path, "w") as jsonFile:
        json.dump(data,jsonFile,indent=4)
def play():
    os.system('cls') 
    print(" _        _______          _      _     _    _______    _      _")
    print("| |      |  ____ |        | |    | |   | |  |  _____|  | |    | |")
    print("| |      | |   | |        | |____| |   | |  | |  ____  | |____| |")
    print("| |      | |   | |   ---  |  ____| |   | |  | | |__  | |  ____  |")
    print("| |____  | |___| |        | |    | |   | |  | |____| | | |    | |")
    print("|______| |_______|        |_|    |_|   |_|  |________| |_|    |_|")
    print(" version 1.3")
    print("\n"*2)
    print("processing...")
    haha = input("play?(yes,no)")
    if haha=="yes":
       playern()
    elif haha=="no":
        print("entering command prompt")
        command_prompt()
        exit
def create_new_data():
    default_data = {}
    with open(path, "w") as jsonFile:
        json.dump(default_data,jsonFile)  
    with open(path, "r") as jsonFile:
        data = json.load(jsonFile)   
    new_data = {
        "players":{
            "player_list":[],
            "individual_players":[]
            },
        "average_score_of_all_players":"",
        "average_guess_count":"",
        "highest_score_of_all_time":{
                "name":"",
                "score":"",
                "number_of_guesses":"",
                "date_and_time":""
        },
        "lowest_score_of_all_time":{
                "name":"",
                "score":"",
                "number_of_guesses":"",
                "date_and_time":""
        },
        "play_history":[],
        "command_history":[]	
    }   
    with open(path, "w") as jsonFile:
        json.dump(new_data,jsonFile)   
    """
    with open(path, "r") as jsonFile:
            data = json.load(jsonFile)
    with open(path, "w") as jsonFile:
            json.dump(data,jsonFile,indent=4)	
    """
def playern():
    os.system('cls')
    printstuff()
    hello = input("1 player or 2 player?(one,two):")
    if hello =="one":
       player()
    elif hello =="two":
        player2()
    else:
        print("invalid syntax")
        playern()
def player():
    os.system('cls')
    printstuff()
    global player1
    player1 = 1
    global name3
    with open(path, "r") as jsonFile:
        data = json.load(jsonFile)
    player_list = data["players"]["player_list"]
    with open(path, "w") as jsonFile:
        json.dump(data,jsonFile,indent=4)
    chosen = False
    while chosen == False:
        print("current_player_list:"+str(player_list))
        choose = input("choose name from list?")
        if choose == "no":
            choose1 = input("create new player?")
            if choose1 == "no":
                pass
            else:
                gui_np()
                with open(path, "r") as jsonFile:
                    data = json.load(jsonFile)
                jsonFile.close()
                add_name_to_json([data["players"]["player_list"][-1]])
                name3 = data["players"]["player_list"][-1]
                chosen = True
        else:
            name3 = input("enter valid player name: ")
            if name3 in player_list:
                add_name_to_json([name3])
                chosen = True
            else:
                print("the name you entered is not a valid player name,enter a name that is valid")
    rules()             
def player2():
    global name1
    global name2
    with open(path, "r") as jsonFile:
        data = json.load(jsonFile)
    print("player 1, enter your name:")
    player_list = data["players"]["player_list"]
    chosen = False
    while chosen == False:
        print("current_player_list:"+str(player_list))
        choose = input("choose name from list?")
        if choose == "no":
            choose1 = input("create new player?")
            if choose1 == "no":
                pass
            else:
                gui_np()
                name1 = data["players"]["player_list"][-1]
                chosen = True
        else:
            name1 = input("enter valid player name:")
            if name1 in player_list:
                chosen = True
            else:
                print("the name you entered is not a valid player name,enter a name that is valid")
    with open(path, "r") as jsonFile:
        data = json.load(jsonFile)
    print("\n"*3)
    print("player 2, enter your name")
    player_list = data["players"]["player_list"]
    with open(path, "w") as jsonFile:
            json.dump(data,jsonFile,indent=4)
    chosen = False
    while chosen == False:
        print("current_player_list:"+str(player_list))
        choose = input("choose name from list?")
        if choose == "no":
            choose1 = input("create new player?")
            if choose1 == "no":
                pass
            else:
                gui_np()
                name2 = data["players"]["player_list"][-1]
                chosen = True
        else:
            name2 = input("enter valid player name:")
            if name2 in player_list:
                chosen = True
            else:
                print("the name you entered is not a valid player name,enter a name that is valid")
    add_name_to_json([name1,name2])
    global player1
    player1 = 2
    rules()
def rules():
    os.system('cls')
    printstuff()
    if player1==1:
      print("hi "+name3+" here are the rules")
      rules1()
    else:
        rules1()
def rules1():
    print("RULES")
    print("this program generates a random number and you have to guess what number it is.")
    print("after guessing , the words low or high is printed on the screen")
    print("the program prints low when your guess is smaller than the number generated")
    print("the program prints high when your guess is bigger than the number generated")
    print("a total of 15 attempts will be given")
    print("find the number")
    print("")
    print("")
    hey()
def hey():
    global cont
    cont = input("continue?")
    os.system('cls')
    printstuff()
    if cont=="yes":        
      if player1 ==1:
         difficulty()
         game()
      elif player1 ==2:
          start()
    else:
        hey()
def start():
    difficulty()
    print(name1+" starts first")
    game()
def difficulty():
    os.system('cls')
    printstuff()
    global level
    level = input("Enter difficulty(easy,medium,hard,legend):\n")
    if level not in "easy medium hard legend".split():
        difficulty()
def game():
    print("generating number prior to difficulty")
    if level=="easy":
      num2 = random.randint(1,100)
      num1 = num2 * 10        
    elif level=="medium":
        num2 = random.randint(1,200)
        num1 = num2 * 5
    elif level=="hard":
        num1 = round(random.randint(1,1000))        
    elif level=="legend":
        num1 = round(random.randint(1,10000))
    else:
        print("wrong answer")
    global gamenoo
    global haha
    haha = []
    gamenoo += 1
    first_num = 1750
    for i in range(14):
        second_num = first_num + 250
        haha.append(random.randint(first_num,second_num))
        first_num += 250
    haha.reverse()
    time.sleep(1)
    os.system('cls')
    printstuff()
    print("number generated")
    global guesscount
    guesscount = int(0)
    guesslimit = 15
    while guesscount < guesslimit:
        os.system('cls')
        printstuff()
        print(num1)
        guesscount += 1
        print("attempt #"+str(guesscount))
        done = False
        while done == False:
            try:
                guess = int(input("enter value:"))
                done = True
            except ValueError:
                pass
        if guesscount == guesslimit:
          print("YOU LOST")
          print("the correct answer was "+str(num1))
          print("total score is 0")
          print("")
          time.sleep(3)
          os.system('cls')
          printstuff()
          if player1 == 2:
              lava1()
          else:
              one_player_data_update(0,guesscount,name3)
              lava1()
        elif guess>num1:
            print("high")
            time.sleep(1)
        elif guess<num1:
            print("low")
            time.sleep(1)
        elif guess==num1:
            num2= str(num1)
            os.system('cls')
            printstuff()
            if guesscount < 16:
                print("")
                print("CORRECT ANSWER")
                score = getscore(level,guesscount)
                print("total score is "+str(score))
                print("")
                time.sleep(3)
                os.system('cls')
                printstuff()
                if player1 == 1:
                    one_player_data_update(score,guesscount,name3)
                    lava1()
                    break
                else:
                    lava1()
                    break
            else:
                print("the correct answer was "+str(num1))
                print("total score is 0")
                print("")
                if player1 == 2:
                    lava1()
                else:
                    one_player_data_update(0,guesscount,name3)
                    lava1()
def lava1():
    if player1 ==2:
       oppo1()
    elif player1 ==1:
        syntax()
def write_to_json():
    """ 
    with open(path, "r") as jsonFile:
        data = json.load(jsonFile)
    with open(path, "w") as jsonFile:
        json.dump(data,jsonFile,indent=4)
    """
def oppo1():
    os.system('cls')
    printstuff()
    odd_nums = [1,3,5]
    even_nums = [2,4,6]
    if gamenoo in odd_nums:
       print("")
       score = getscore(level,guesscount)
       name1scores.append(score)
       name1guesscount.append(guesscount)
       update_the_events_two_player(name1,guesscount,score)
       print(name2+", your turn")
       game()
    elif gamenoo in even_nums:
        print("")
        score = getscore(level,guesscount)
        name2scores.append(score)
        name2guesscount.append(guesscount)
        if gamenoo == 6:
          print("GOOD GAME")
          update_the_events_two_player(name2,guesscount,score)
          finish()
        else:
            print(name1+", your turn")
            update_the_events_two_player(name2,guesscount,score)
            game()
def finish():
    os.system('cls')
    printstuff()
    two_player_data_update(name1,name2,name1scores,name2scores,name1guesscount,name2guesscount)
    print("okay let's check the scores")
    print(name1+", here are your scores")
    print(name1scores)
    print("")
    print(name2+", here are your scores")
    print(name2scores)
    global sum1
    global sum2
    sum1 = int(name1scores[0]) + int(name1scores[1]) + int(name1scores[2])
    sum2 = int(name2scores[0]) + int(name2scores[1]) + int(name2scores[2])
    global avg1
    global avg2
    avg1 = float(sum1) / 3
    avg2 = float(sum2) / 3
    letsee = input("continue?(yes,no)")
    if letsee=="yes":
      print("let's see who the winner is")
      time.sleep(2)
      os.system('cls')
      printstuff()
      print("the average score of "+str(name1)+" is "+str(avg1))
      print("the average score of "+str(name2)+" is "+str(avg2))
      end()
def end():
    if sum1 > sum2:
       print("")
       print("THE WINNER IS")
       print(name1)
       dif1 = sum1 - sum2
       print("by "+str(dif1)+" points")
       playagain = input("play again?(yes,no):")
       if playagain =="yes":
          playern()
       elif playagain =="no":
           command_prompt()
    elif sum2 > sum1:
        print("")
        print("THE WINNER IS..")
        print(name2)
        dif2 = sum2 - sum1
        print("by "+str(dif2)+" points")
        playagain = input("play again?(yes,no):")
        if playagain =="yes":
           playern()
        elif playern =="no":
            command_prompt()
def syntax():
    os.system('cls')
    printstuff()
    again = input("play again?")
    if again=="yes":
      playern()
    elif again=="no":
        command_prompt()
    else:
        syntax()
authenticate()
refresh_json_data()
command_prompt()
refresh_json_data()
