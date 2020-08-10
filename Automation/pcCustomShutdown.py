# https://docs.python.org/3/library/time.html#time.struct_time

import os
import time

def main():
    shutdown = input("Shutdown? y/N: ").lower()
    if shutdown == "y":
        whatTime = input("What time? (HH:MM): ")
        flag = True
        while(flag):
            try:
                whatTime = whatTime.split(":")
                whatTime = [int(item) for item in whatTime]
                if(whatTime[0] in range(24) and whatTime[1] in range(60)):
                    flag = False
            except:
                print("\nPlease enter a a time in 24h format like so:\nHH:MM\nWhere HH is the hour, MM is the minutes")
                whatTime = input("Time: ")
                
        print(whatTime)
        info = time.localtime()
        hr = info[3]
        mn = info[4]
        print(hr, mn)
    elif shutdown == "n":
        exit()
    else:
        main()

if __name__=="__main__":
    main()
    