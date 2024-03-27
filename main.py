import os
import datetime
import time

today = datetime.datetime.now().strftime('%Y-%m-%d')
print(today)
# today = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')

directory = "F:\\"

folders = next(os.walk('.'))[1]

with open(directory + "folders.txt", "w") as fp:
    for folder in folders:
        #
        c_time = os.stat(os.path.join(directory, folder)).st_ctime
        timestamp_str = datetime.datetime.fromtimestamp(c_time).strftime('%Y-%m-%d')
        print(timestamp_str)
        if timestamp_str == today:
            fp.write("%s\n" % folder)
    print("Done")


