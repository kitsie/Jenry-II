#imports
import json
import os
from COMMANDS import * #imports files from the folder COMMANDS

#import settings
with open("settings.json") as settings_file:
    settings = json.load(settings_file)
    
print("Hello! My name is " + settings["NAME"] + ".")

# main loop
while True:
    cmd=input("input command: ").lower()  
    
    ## built-in commands
    if cmd in ["q","quit","exit"]:
        cm=input("Are you sure? (y/n): ").lower()
        if cm in ["y","yes"]: break
        else: print("treated input as no, continuing operation. ")           
    
    elif cmd=="info":
        print(settings["information"])
        
    elif cmd=="nf":
        text= input("What do you want to write?: ")
        name= input("What would be the filename?: ").lower()
        with open(name+ '.txt', 'w') as nf:
            nf.write(text)

    elif cmd=="clear":
        os.system('cls')
        
           
    ## imported commands
    elif cmd == "hw": sample.hello_world()  
    elif cmd == "echo": sample.echo(settings['NAME'])
    elif cmd == "jenry": tribute.jenry()
    elif cmd == "game": game.gameLoop()
    
    ## help
    elif cmd == "help":
        print("Here's a list of commands and what they do:\n\n" +
              
              "q/quit   :    terminates program\n"  +
              "info     :    prints current settings and credits\n" +
              "nf       :    creates a new text file with your input\n" +
              "clear    :    clears console\n")
        if settings["information"]["mode"] == 0:
            print(
                "SAMPLE\n"+
                sample.help_hw + 
                sample.help_echo +
                tribute.help_jenry +
                game.help_game)
            
        
    else: 
        print("err: command: " + cmd + " does not exist. Use command 'help' for list of commands..")
        
        