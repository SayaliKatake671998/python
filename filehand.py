import os

fp=open("Sayali.txt","w")
fp.write("Sunday")
fp.write("Monday")
os.remove("Sayali.txt")
fp1=open("abc.txt","x")

fp.close()
