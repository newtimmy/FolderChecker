import os
import datetime

END_OF_FILE_NAME="tbd"

today = datetime.datetime.now().strftime('%Y-%m-%d')
print(today)
# today = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')

directory = "C:\\test\\"

folders = next(os.walk(directory))[1]

print(folders)


def check_for_zip_file(folder):
    for file in os.listdir(folder):
        if file.endswith(folder.split("\\")[len(folder.split("\\"))-1] + END_OF_FILE_NAME):
            print(os.path.join(folder, file))
            return True
    return False


with open(directory + "folders.txt", "w") as fp:
    for folder in folders:
        to_be_checked_folder = os.path.join(directory, folder)
        print(to_be_checked_folder)
        c_time = os.stat(to_be_checked_folder).st_ctime
        timestamp_str = datetime.datetime.fromtimestamp(c_time).strftime('%Y-%m-%d')
        print(timestamp_str)
        if str(timestamp_str) == str(today):
            if check_for_zip_file(to_be_checked_folder):
                fp.write("%s %s\n" % (to_be_checked_folder, c_time))
    print("Done")


