import requests
import datetime
url = "https://notify-api.line.me/api/notify" 
token = "jrdUyfN20qiCwLWaffyloI04JyexDPP4krDNFLqgTYH"
headers = {"Authorization" : "Bearer "+ token} 
message =  "booting my desktop......"
amessage="server is beginning..."
payload = {"message" :  message}
wake={"message": amessage}

def awake():
    requests.post(url,headers=headers, params=wake)

def send():
    requests.post(url, headers = headers, params=payload)

def err(err):
    dead = {"message" : err}
    requests.post(url,headers = headers, params=dead)

def checktime(stime):
    nt=datetime.datetime.now
    print(nt.hour-stime)
    if nt.hour-stime==2:
        send()
        return nt.hour

if __name__=="__main__":
    send()
