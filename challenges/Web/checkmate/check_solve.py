import requests
from tqdm import tqdm
import itertools

v1 = []
v2 = []
v3 = []

for i in range (97,123):
    for j in range(97,123):
        if i & j == 0x60:
            v1.append([i,j])
        if i | j == 0x61:
            v2.append([i,j])
        if i ^ j == 0x6:
            v3.append([i,j])

for a,b,c in tqdm(itertools.product(v1,v2,v3),total=len(v1)*len(v2)*len(v3)):
    pwd = "".join([chr(i) for i in [a[0],b[0],a[1],c[0],b[1],c[1]]])
    R = requests.post("http://chal.pctf.competitivecyber.club:9096/check.php",data={"password":pwd})

    if "incorrect password" not in R.text:
        print(pwd)
        print(R.text)
        exit()



