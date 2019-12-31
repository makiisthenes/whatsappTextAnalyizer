import os
import string

path = os.getcwd()
alpha = string.ascii_lowercase
with open(r'C:\Users\Michael\Documents\Coding Projects\Python PROJECTS\Random Python Projects\Trackers Software\Whatsapp Analysis\__main__\langAnalysis\english-words.txt', encoding='utf8') as fullfile:
        for line in fullfile:
            for x in range(len(alpha)):
                if line[0].lower() == alpha[x].lower():
                    print(alpha[x])
                    with open(path + r'\savefile'+ alpha[x].upper() +'_PATH.txt', 'a') as savefile:
                        savefile.write(line + '\n')
                        print('DONE for ' + alpha[x]+ ' list.')
                else:
                    pass
