import requests
url="https://discord.com/api/webhooks/1252589753388371968/0C01nSZj5Vn2JC3KATeHTTzDXd1utS3BVK7irAJhajdP3uUODApH30-1m-pbravX3c3l"
url2="https://discord.com/api/webhooks/1252812851517591652/QfaOdGMI5JxwQrIYPpR0cMdzdh_pgEsIv2EjwgeTVcLR1S0vlZ_RunhsQkPc1mjUsIyz"
url3="https://discord.com/api/webhooks/1289220738301034547/1TfIkCl7ft_-ysMF_4HnbfFir3nmMKWXFUvArgvIAfe2csLCp9RBh6HY2hop0V2utrQK"
def send(msg:str):
	requests.post(url,data={'content':msg})

def send_temp(tmp:str):
	requests.post(url2,data={'content':tmp})

def alert(msg:str):
	requests.post(url3,data={'content':msg})

if __name__=="__main__":
	send("Hello World!")
