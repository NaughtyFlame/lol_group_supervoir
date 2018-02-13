import os
import sys
import time
import self_functions

os.system("clear")

#-------------------------------------------------------------------------------
print("Script Info".center(110,"*"))
print("Script_Name:",sys.argv[0])
for i in range(1,len(sys.argv)):
    print("Arg",i,"",sys.argv[i])

#-------------------正式开始-----------------------------------------------------

print("\n","Summoner Info".center(110,"*"))
try:
    summoner_dict = self_functions.Request_summoner_name(sys.argv[1])
except:
    print("Summoner Info ERROR")
else:
    for a in summoner_dict:
        print(a,":",summoner_dict[a])


print("\n","Current match".center(110,"*"))
#Request_current()
try:
    current_str = Request_current()
except:
    print(sys.argv[1],"is not in game")
else:
    print(summoner_dict["name"]+" is in the game")


print("\n","Recent matches".center(110,"*"))
matches_dict = self_functions.Request_matches()
for a in range(len(matches_dict["matches"])):
            print(str(a+1).ljust(3),time.strftime("%Y-%m-%d %H:%M", time.localtime(int(matches_dict["matches"][a]["timestamp"])/1000)),"",
                                       "gameId:",str(matches_dict["matches"][a]["gameId"]).ljust(11),
                                     "champion:",
                                     str(self_functions.get_champion_name(matches_dict["matches"][a]["champion"])).center(11,"-"),
                                     #str(matches_dict["matches"][a]["champion"]).center(3),
                                         "lane:",str(matches_dict["matches"][a]["lane"]).ljust(7)
                                    )
            match_dict = self_functions.Request_match(str(matches_dict["matches"][a]["gameId"]))
            self_functions.match_info(match_dict)

print("\n\n","Script End".center(110,"*"))
