import discord as d
import subprocess as s
import sys
args="cowsay -f daemon daemon is included!"
res=s.run(args.split(),capture_output=True,text=True)
d.alert(res.stdout)
