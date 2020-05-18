#!/usr/bin/python3
#/data/data/com.termux/files/usr/bin/python        
import readline
readline.parse_and_bind("tab:complete")
from time import sleep
from os import system

#=============( The functions of The porogramm )

def banner(colors=["\033[1;31m","\033[1;37m"]):
    print(f"{colors[0]}                          ".center(50))
    print("        GGGGGGGGGGGGG       ".center(50))
    print("     GGG::::::::::::G       ".center(50))
    print("   GG:::::::::::::::G       ".center(50))
    print("  G:::::GGGGGGGG::::G       ".center(50))
    print(" G:::::G       GGGGGG       ".center(50))
    print("G:::::G                     ".center(50))
    print("G:::::G                     ".center(50))
    print("G:::::G    GGGGGGGGGp       ".center(50))
    print("G:::::G    G::::::::G       ".center(50))
    print("G:::::G    GGGGG::::G       ".center(50))
    print("G:::::G        G::::G       ".center(50))
    print(" G:::::G       G::::G       ".center(50))
    print("  G:::::GGGGGGGG::::G       ".center(50))
    print("   GG:::::::::::::::G       ".center(50))
    print("     GGG::::::GGG:::G       ".center(50))
    print("        GGGGGG   GGGG       ".center(50))
    print(f"{colors[-1]}                            ".center(50))
    print("██╗     ██╗███████╗████████╗".center(50))
    print("██║     ██║██╔════╝╚══██╔══╝".center(50))
    print("██║     ██║███████╗   ██║   ".center(50))
    print("██║     ██║╚════██║   ██║   ".center(50))
    print("███████╗██║███████║   ██║   ".center(50))
    print("╚══════╝╚═╝╚══════╝   ╚═╝   ".center(50))
    print()
def pro_input(A):
    FF=True
    while FF:
        try:
            en=input(A)
            if en:
                FF=False
        except:
            print()
    class db:
        pass
    OPC=db()
    for n,i in enumerate(en.split()):
        setattr(OPC,f"com{n}",i)
    setattr(OPC,"len",len(en.split()))
    return OPC

def Upper(word,repeat=3,color="\033[1;36m"):
    re=0
    rr=""
    while re != repeat:
        for n,i in enumerate(word) :
            if n%4  == 0 :
                rr = "" if rr == "٠٠٠" else rr+"٠"
            letter=word[:n]+color+word[n][0].upper()+"\033[0m"+word[n+1:]+rr+"   "
            sleep(0.1)
            print("[*]",letter,end="\r")
        re+=1
    print(" "*(3+len(letter)),end="\r")

def Exit(A):
    sleep(2)
    Upper(A,repeat=2,color="\033[1;31m")
    sleep(1)

def Fcommand(Fcom):
    print(f"    \033[1;31m[\033[5;37m ! \033[0m\033[1;31m]\033[0m\033[1;37m {Fcom} is not commmand !".center(50))

def dontUse(Fcom):
    print(f"    \033[1;31m[\033[5;37m ? \033[0m\033[1;31m]\033[0m\033[1;37m {Fcom} Don't Use like that !".center(50))

def show_options(file="pass.txt",mode="w"):
    print()
    if mode =="w" :
        humode="newfile"
    else:
        humode="oldfile"
    print("╔═╗╦ ╦╔═╗╦ ╦  ╔═╗╔═╗╔╦╗╦╔═╗╔╗╔╔═╗".center(50))
    print("╚═╗╠═╣║ ║║║║  ║ ║╠═╝ ║ ║║ ║║║║╚═╗".center(50))
    print("╚═╝╩ ╩╚═╝╚╩╝  ╚═╝╩   ╩ ╩╚═╝╝╚╝╚═╝".center(50))
    print("┌──────────────────────────┐".center(50))
    print(f"   file : {file}           ".center(50))
    print(f"   mode : {humode}           ".center(50))
    print("└──────────────────────────┘".center(50))
    print()


def about():
    print("╔═╗╔╗ ╔═╗╦ ╦╔╦╗  ╔═╗╔═╗╦═╗╦╔═╗╔╦╗".center(50))
    print("╠═╣╠╩╗║ ║║ ║ ║   ╚═╗║  ╠╦╝║╠═╝ ║ ".center(50))
    print("╩ ╩╚═╝╚═╝╚═╝ ╩   ╚═╝╚═╝╩╚═╩╩   ╩ ".center(50))
    print("┌──────────────────────────┐".center(50))
    print("│ By : AhmedBaglab         │".center(50))
    print("└──────────────────────────┘".center(50))
    print("┌──────────────────────────┐".center(50))
    print("│  [*] Version : 0.3 v     │".center(50))
    print("└──────────────────────────┘".center(50))
    print("┌──────────────────────────┐".center(50))
    print("│ date : 28-04-2020 *      │".center(50))
    print("└──────────────────────────┘".center(50))
    print()

def Blen(passwords,B=25):
    for password in passwords :
        if len(password) > B :
            B=len(password)
    return B

def show_passwords(passwords):
    print()
    print("╔═╗╔═╗╔═╗╔═╗╦ ╦╔═╗╦═╗╔╦╗╔═╗".center(50))
    print("╠═╝╠═╣╚═╗╚═╗║║║║ ║╠╦╝ ║║╚═╗".center(50))
    print("╩  ╩ ╩╚═╝╚═╝╚╩╝╚═╝╩╚══╩╝╚═╝".center(50))
    blen=Blen(passwords)
    D=f"┌"+"─"*blen+"┐"
    print(D.center(50))
    for password in passwords :
        print(password.center(50))
    E=f"└"+"─"*blen+"┘"
    print(E.center(50))
    print("┌──────────────────────────┐".center(50))
    print(f" YOU HAVE {len(passwords)} PASSWORD".center(50))
    print("└──────────────────────────┘".center(50))
    print()


def show_info(passwords):
    print("╦╔╗╔╔═╗╔═╗╦═╗╔╦╗╔═╗╔╦╗╦╔═╗╔╗╔".center(50))
    print("║║║║╠╣ ║ ║╠╦╝║║║╠═╣ ║ ║║ ║║║║".center(50))
    print("╩╝╚╝╚  ╚═╝╩╚═╩ ╩╩ ╩ ╩ ╩╚═╝╝╚╝".center(50))
    blen=Blen(passwords)
    D=f"┌"+"─"*blen+"┐"
    print(D.center(50))
    for password in passwords :
        print(password.center(50))
    E=f"└"+"─"*blen+"┘"
    print(E.center(50))
    print("┌──────────────────────────┐".center(50))
    print(f" YOU HAVE {len(passwords)} INFORMATION ".center(50))
    print("└──────────────────────────┘".center(50))


def set_passwords(lis):
    print()
    print("╔═╗╔═╗╔╦╗  ╦╔╗╔╔═╗╔═╗╦═╗╔╦╗╔═╗╔╦╗╦╔═╗╔╗╔".center(50))
    print("╚═╗║╣  ║   ║║║║╠╣ ║ ║╠╦╝║║║╠═╣ ║ ║║ ║║║║".center(50))
    print("╚═╝╚═╝ ╩   ╩╝╚╝╚  ╚═╝╩╚═╩ ╩╩ ╩ ╩ ╩╚═╝╝╚╝".center(50))
    print()
    lis=set(lis)
    while True:
        a=pro_input(f"     Info({len(lis)}) : ")
        if a.com0 == "exit":
            break;
        else:
            lis.add(a.com0)
    print()
    return lis
def Help():
    print("╔═╗╦ ╦╔═╗╦ ╦  ╦ ╦╔═╗╦  ╔═╗".center(50))
    print("╚═╗╠═╣║ ║║║║  ╠═╣║╣ ║  ╠═╝".center(50))
    print("╚═╝╩ ╩╚═╝╚╩╝  ╩ ╩╚═╝╩═╝╩  ".center(50))
    print("┌────────────────────────────────────────────────┐".center(50))
    print("│                                                │".center(50))
    print("│  [*]  exit                                     │".center(50))
    print("│     if you want close this Tool use it         │".center(50))
    print("│     or to stop insert information              │".center(50))
    print("│                                                │".center(50))
    print("│  [*]  help                                     │".center(50))
    print("│   use this command to show this Help           │".center(50))
    print("│                                                │".center(50))
    print("│  [*]  banner                                   │".center(50))
    print("│    use this command to show banner             │".center(50))
    print("│                                                │".center(50))
    print("│  [*] set information                           │".center(50))
    print("│   use this command to add information to Tool  │".center(50))
    print("│                                                │".center(50))
    print("│  [*] show information                          │".center(50))
    print("│   use this command to show information         │".center(50))
    print("│                                                │".center(50))
    print("│  [*] show passwords                            │".center(50))
    print("│   use this command to show passwords           │".center(50))
    print("│                                                │".center(50))
    print("│  [*] show options                              │".center(50))
    print("│   use this command to show options             │".center(50))
    print("│                                                │".center(50))
    print("│  [*] set file namefile.txt                     │".center(50))
    print("│   use to this command to select a name of file │".center(50))
    print("│                                                │".center(50))
    print("│  [*] set mode [ newfile or oldfile ]           │".center(50))
    print("│                                                │".center(50))
    print("│                                                │".center(50))
    print("│  [*] remove passswords password                │".center(50))
    print("│      use this command to remove any password   │".center(50))
    print("│                                                │".center(50))
    print("│  [*] remove information info                   │".center(50))
    print("│      use this command to remove any info       │".center(50))
    print("│                                                │".center(50))
    print("│  [*] save                                      │".center(50))
    print("│  use this command to save passwds in the file  │".center(50))
    print("│                                                │".center(50))
    print("│                                                │".center(50))
    print("│                                                │".center(50))
    print("└────────────────────────────────────────────────┘".center(50))

def save(File,Mode,List):
    with open(File,Mode) as F:
        for i in List :
            F.write(f"{i}\n")
        F.close()
    print("┌──────────────────────────┐".center(50))
    print(f" Successful {len(List)} Saved".center(50))
    print("└──────────────────────────┘".center(50))
    print()
#===================(Varibles)=====================
class db:
    def __init__(self,words):
        self.words=words
        self.fx=None
    def qp(self,fx,index):
        if fx != self.fx :
            self.superlist=[i for i in self.words if i.startswith(fx)]
            self.fx=fx
        try:
            return self.superlist[index]+" "
        except IndexError :
            return None

commands=["information","clear","options","newfile","oldfile","banner","exit","show","set","passwords","remove","file","mode","about","save"]
ddbb=db(commands)
readline.parse_and_bind('tab:complete')
readline.set_completer(ddbb.qp)
unpass=set()
info=set()
filee="pass.txt"
mode="w"
#===================(start the program )=============
Upper("The goodlist tool is ranning ")
banner()
while True :
    print("\033[0m\033[1;37m",end="")
    Entre = pro_input("(GoodLisT): ") 
    if Entre.len == 1 :
        #================(if the command is one word)=============
        if Entre.com0.lower() == "exit":
            Exit("The goodlist tool is stoping ")
            print()
            break ;
        elif Entre.com0.lower() == "banner":
            banner()
        elif Entre.com0.lower() == "about":
            about()
        elif Entre.com0.lower() == "help":
            Help()
        elif Entre.com0.lower() == "clear":
            system("clear")
        elif Entre.com0.lower() == "save":
            save(filee,mode,set([x+y for x in info for y in info])-unpass)
        else:
            if Entre.com0.lower() in commands :
                dontUse(Entre.com0)
            else:
                Fcommand(Entre.com0)
        #================(if the command is Two words)=============
    elif Entre.len == 2 :
        if Entre.com0.lower() == "show" :
            if Entre.com1.lower() == "options":
                show_options(filee,mode)
            elif Entre.com1.lower() == "information":
                show_info(info)
            elif Entre.com1.lower() == "passwords":
                show_passwords(set([x+y for x in info for y in info])-unpass)
            else:
                if Entre.com0.lower() in commands :
                    dontUse(Entre.com0)
                else:
                    Fcommand(Entre.com0)
        elif Entre.com0.lower() == "set" :
            if Entre.com1.lower() == "information":
                info.update(list(set_passwords(info)))
            else:
                if Entre.com0.lower() in commands :
                    dontUse(Entre.com0)
                else:
                    Fcommand(Entre.com0)

    elif Entre.len == 3 :
        #================(if the command is Three words)=============
        if Entre.com0.lower() == "set" :
            if Entre.com1.lower() == "file" :
                filee=Entre.com2
            elif Entre.com1.lower() == "mode" :
                if Entre.com2.lower() == "newfile":
                    mode="w"
                elif Entre.com2.lower() == "oldfile":
                    mode="a"
                else:
                    dontUse(Entre.com0)
        elif Entre.com0.lower() == "remove" :
            if Entre.com1.lower() == "passwords" :
                if Entre.com2 in set([x+y for x in info for y in info]) - unpass :
                    unpass.add(Entre.com2)
                else:
                    dontUse(Entre.com0)
            elif Entre.com1.lower() == "information" :
                if Entre.com2 in info:
                    info.remove(Entre.com2)
                else:
                    dontUse(Entre.com0)

        else:
            if Entre.com0.lower() in commands :
                dontUse(Entre.com0)
            else:
                Fcommand(Entre.com0)
