# ログを出力
import os
from datetime import datetime

def print_logs(status, campus):
    print("-------- log start --------\n")
    
    print("[Time] : " + str(datetime.now()) + '(UTC)\n')
    
    print("[ENV_STATE]")
    env_list = ["EmergencyTweet", "NormalTweet", "TestTweet"]
    for i in env_list:
        print(i + " : " + os.environ[i])
    print("")
    
    print("[CAMPUS_STATE]")
    for i in range(len(status)):
        print(campus[i] + " : " + status[i])
    print("")
    
    print("-------- log end --------")
