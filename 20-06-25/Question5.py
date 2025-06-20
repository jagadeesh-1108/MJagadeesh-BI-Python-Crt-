#write a py program to print Alphabets from A to z using recurssion
def Alphabets(ch):
    if ch>=ord('A') and ch<=ord('Z'):
        print(chr(ch))
        return Alphabets(ch-1)
ch=90
Alphabets(ch)
    