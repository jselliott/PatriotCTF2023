# Checkmate

## Description

Get your adrenaline pumping as you navigate the thrilling world of Crypto Web for Capture the Flag.

Minor brute force is allowed, but you should not need over 4000 tries.

*Flag format: PCTF{}*

*Author: @sau_12*

## Solution

For this challenge, you are directed to a website with a simple login form. The actual form does not submit to a remote script though, it just runs a javascript validation on it.

First, it checks the username which is simply a reversed string, "adminjyu".

```js
function checkName(name){

    var check  = name.split("").reverse().join("");
    return check === "uyjnimda" ? !0 : !1;
}
```

Next, it checks the password.

```js 
function checkLength(pwd){
     return (password.length % 6 === 0 )? !0:!1;
    }
function checkValidity(password){
    const arr = Array.from(password).map(ok);
    function ok(e){
        if (e.charCodeAt(0)<= 122 && e.charCodeAt(0) >=97 ){
        return e.charCodeAt(0);
    }}

    let sum = 0;
    for (let i = 0; i < arr.length; i+=6){
        var add = arr[i] & arr[i + 2]; 
        var or = arr[i + 1] | arr[i + 4]; 
        var xor = arr[i + 3] ^ arr[i + 5];
        if (add === 0x60   && or === 0x61   && xor === 0x6) sum += add + or - xor; 
    }
   return  sum === 0xbb ? !0 : !1;
}
```

Using this logic, we can simply create a script that iterates through every possible six-character password that meets the requirements. This produces 3,696 possible passwords. However, we still don't know how to actually use it to get the flag.

Another thing to note is that there is comment referencing check.php in the script which brings us to another page where we are able to check passwords. Using the script below, we can brute-force the passwords we generate and find the correct one.

```python
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
        print(R.text)
        exit()

```

Eventually, the script reaches the password "sadsau" which logs in successfully and gives the flag.

```PCTF{Y0u_Ch3k3d_1t_N1c3lY_149}```