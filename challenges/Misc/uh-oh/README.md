# Uh Oh!

## Description

Uh Oh! While trying to add passwords to my wordlist, I accidentally added my own phone number! Can you tell me what line it's on?

https://en.wikipedia.org/wiki/North_American_Numbering_Plan#Modern_plan

Make sure the phone number follows this format: (NPA) XXX-XXXX

For example (123) 456-7890

*Flag format: PCTF{linenumber_phonenumonlynumbers}*

*Author: @angr404*

## Files

* [rockyou.zip](files/rockyou.zip)

## Solution

After the challenge description was updated, the ctf confirmed the specific phone number format we were looking for. The grep command below grabs the phone number from the rockyou.txt file. Thenwe can just build the flag in the right format.


```
grep -n -Eo '\([2-9][0-9]{2}\) [2-9][0-9]{2}-[0-9]{4}' rockyou.txt
```

```
PCTF{7731484_4043037283}
```
