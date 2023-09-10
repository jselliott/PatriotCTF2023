# Mason Competitive Cyber

## Description

A member of our cyber club tried to be clever and send us a secret messed encoded using our club's name. We want to make sure it can't be deciphered if someone managed to get ahold of our message, can you try breaking the encoding for us?

*Flag format: PCTF{}*

*Author: @txnner*

## Files

* [MasonCompetitiveCyber.txt](files/MasonCompetitiveCyber.txt)

## Solution

The provided file appears to just have the club name repeated a lot but, depending on your text editor, you may also see there are a lot of unicode zero-width characters interspersed throughout the file.

After extracting these characters, we can replace \xe2808c with 0 and \xe2808d with 1, which produces a binary string:


01010000010000110101010001000110011110110100110101000000011100110010010000110000010011100101111101000011010011110110110101010000001100110111010000110001011101000011000101010110010001010101111101000011010110010100001000110011011100100010000101111101

Plugging this into CyberChef, we get:

```PCTF{M@s$0N_COmP3t1t1VE_CYB3r!}```