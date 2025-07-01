#dj rewind mode '
#add 10 songs to the playlist
#show the play list in normal and reverse order
n=int(input("Enter the range of list "))
songs=[]
for i in range(n):
    temp=input("Enter the Songs ")
    songs.append(temp)
print(songs)
print(songs[::-1])    