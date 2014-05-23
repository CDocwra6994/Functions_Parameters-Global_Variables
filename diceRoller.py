#Die Roll Program
#To get and display a die roll

import random
import time

s1 = "- - - - -\n|       |\n|   O   |\n|       |\n- - - - -\n"
s2 = "- - - - -\n| O     |\n|       |\n|     O |\n- - - - -\n"
s3 = "- - - - -\n| O     |\n|   O   |\n|     O |\n- - - - -\n"
s4 = "- - - - -\n| O   O |\n|       |\n| O   O |\n- - - - -\n"
s5 = "- - - - -\n| O   O |\n|   O   |\n| O   O |\n- - - - -\n"
s6 = "- - - - -\n| O   O |\n| O   O |\n| O   O |\n- - - - -\n"

roll = random.randint(1,6)
    
print("Rolling.....")
time.sleep(1)

if roll == 1:
        print(s1)
elif roll == 2:
        print(s2)
elif roll == 3:
        print(s3)
elif roll == 4:
        print(s4)
elif roll == 5:
        print(s5)
elif roll == 6:
        print(s6)
