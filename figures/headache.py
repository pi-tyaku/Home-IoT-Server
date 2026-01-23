import requests
import datetime as d
import os
from dotenv import load_dotenv
from matplotlib import pyplot as pyp
from matplotlib.ticker import MultipleLocator
from . import discord_pic
load_dotenv()
def get_Headache_data():
    region_id = os.getenv("REGION_ID")
    print(region_id)
    url = f"https://zutool.jp/api/getweatherstatus/{region_id}"

    response = requests.get(url)
    data = response.json()
    todaydata= data["today"]
    return todaydata

def return_now_time_headache_warn():
    now=d.datetime.now()
    now=int(now.hour)
    todaydata=get_Headache_data()
    nowtime=todaydata[now]
    
    print(f"{now}時の天気頭痛の警戒度")

    return_value=""
    if nowtime["pressure_level"]=="0":
        return_value="😊"+"\n"+"Normal"
    elif nowtime["pressure_level"]=="1":
        return_value="😐"+"\n"+"little Caution"
    elif nowtime["pressure_level"]=="2":
        return_value="☹️"+"\n"+"Caution"
    elif nowtime["pressure_level"]=="3":
        return_value="😖"+"\n"+"Warning!"
    elif nowtime["pressure_level"]=="4":
        return_value="😨"+"\n"+"Super Warning!"

    print(return_value)
def return_today_headache_warn_graph():
    URL = os.getenv("FIG_URL")
    
    todaydata=get_Headache_data()
    pyp.rcParams["font.family"]="IPAexGothic"
    
    graph_value=[]
    for v in todaydata:
        graph_value.append(int(v["pressure_level"]))
    label=[f"{i}時" for i in range(len(graph_value))]

    fig, ax = pyp.subplots(figsize=(8, 4))
    pyp.ylim(-0.2,4.2)
    ax.plot(label,graph_value,"-", c="Blue", linewidth=1, marker='o', alpha=1)
    pyp.grid(True)
    
    ax.yaxis.set_major_locator(MultipleLocator(1))

    fig.subplots_adjust(
    left=0.04,
    right=0.99,
    bottom=0.1,
    top=0.95
)
    fig.savefig("./today_headache_warngraph.png")
    discord_pic.send_to_discord(URL,"./today_headache_warngraph.png","今日の頭痛警戒度数")
    
if __name__=="__main__":
    return_now_time_headache_warn()
    return_today_headache_warn_graph()
   

