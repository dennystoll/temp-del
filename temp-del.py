import os , shutil, countdown, time

path = (r"/tmp")

def tmp_del():
    for file_name in os.listdir(path):
        file = os.path.join (path, file_name)
        if os.path.isfile(file):
            try:
                os.remove(file)
            except:
                continue
        else: 
            try:
                shutil.rmtree(file)
            except:
                continue

def main():
    while True:
        time.sleep(60)
        time.sleep(countdown.mins_left * 60)
        tmp_del()



main()