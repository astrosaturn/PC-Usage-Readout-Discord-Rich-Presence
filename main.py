from pypresence import Presence
import time
import psutil
import GPUtil
from dotenv import load_dotenv
import os

load_dotenv() # I will use dotenv to store the client ID for privacy reasons

client_id = os.getenv("CLIENT_ID") # Put the ID of your application here. Should look
RPC = Presence(client_id)          # like a regular user id (ie 1180481858185)
RPC.connect()


while(True):
    cpu_per = round(psutil.cpu_percent(), 1)
    
    mem = psutil.virtual_memory()
    mem_per = round(psutil.virtual_memory().percent,1)
    mem_used = round((mem_per/100) * 64, 1)
    
    gpu = GPUtil.getGPUs()
    gpu_util = round(gpu[0].load * 100,1)

    RPC.update(
            details=f"i9-13900k: {cpu_per}% | RTX 4090: {gpu_util}%",
            state=f"Memory: {mem_used}/64 GB ({mem_per}%)",
        )
    
    time.sleep(3)