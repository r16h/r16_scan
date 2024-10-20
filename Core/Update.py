# ORIGINAL CREATOR: Luca Garofalo (Lucksi)
# AUTHOR: Luca Garofalo (Lucksi)
# Copyright (C) 2021-2023 Lucksi <lukege287@gmail.com>
# License: GNU General Public License v3.0

import os
import shutil
from configparser import ConfigParser
from Core.Support import Font
from Core.Support import Language
from time import sleep

Conf_file = "Configuration/Configuration.ini"
Parser = ConfigParser()
Parser.read(Conf_file)
filename = Language.Translation.Get_Language()
filename


class Downloader:

    @staticmethod
    def Check_Creds():
        Attempts = 5
        Password = Parser["Settings"]["Password"]
        while Attempts > 0:
            Pass = str(input(
                Font.Color.BLUE + "\n[+]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Update", "Insert", "None").format(Attempts) + "\n\n" + Font.Color.GREEN + "[#R16 TEAM#]" + Font.Color.WHITE + "-->"))
            while Pass == "":
                Pass = str(input(
                   Font.Color.BLUE + "\n[+]" + Font.Color.WHITE + Language.Translation.Translate_Language(filename, "Update", "Insert", "None").format(Attempts) + "\n\n" + Font.Color.GREEN + "[#R16 TEAM#]" + Font.Color.WHITE + "-->"))
            if Pass == Password:
                Downloader.Update()
            else:
                Attempts = Attempts - 1
                print(Font.Color.RED + "\n[!]" + Font.Color.WHITE +
                      Language.Translation.Translate_Language(filename, "Update", "Wrong", "None").format(Attempts))
        inp = input(Font.Color.RED + "\n[!]" + Font.Color.WHITE +
            Language.Translation.Translate_Language(filename, "Update", "Failed", "None").format(Attempts))

    @staticmethod
    def Update():
        Path = Parser["Settings"]["Path"]
        os.chdir(Path)
        if os.path.exists("R16 TEAM_Old"):
            shutil.rmtree("R16 TEAM_Old",)
        if os.name == "nt":
            os.system("rename R16 TEAM R16 TEAM_Old 2>NUL >NUL")
        else:
            os.system("mv R16 TEAM R16 TEAM_Old &>/dev/null")
        os.system("git clone https://github.com/r16h/r16_scan")
        choice = int(input(Font.Color.BLUE + "\n[+]" + Font.Color.WHITE +
                     Language.Translation.Translate_Language(filename, "Update", "Choice", "None")))
        if choice == 1:
            os.remove("R16 TEAM_Old")
            print(Font.Color.WHITE + Language.Translation.Translate_Language(filename,
                  "Update", "Delete", "None"))
        else:
            print(Font.Color.WHITE + Language.Translation.Translate_Language(filename,
                  "Update", "Keep", "None"))
        sleep(3)
        print("\n")        
        inp = input(Font.Color.WHITE + Language.Translation.Translate_Language(
            filename, "Update", "Success", "None"))
