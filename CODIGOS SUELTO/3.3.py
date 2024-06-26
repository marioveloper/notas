'''Dada la siguiente letra5, obtenga la misma pero sustituyendo la palabra voices por sounds:
song = \'''You look so beautiful in this light
Your silhouette over me
The way it brings out the blue in your eyes
Is the Tenerife sea
And all of the voices surrounding us here
They just fade out when you take a breath
Just say the word and I will disappear
Into the wildernes\''' '''

song = '''You look so beautiful in this light
Your silhouette over me
The way it brings out the blue in your eyes
Is the Tenerife sea
And all of the voices surrounding us here
They just fade out when you take a breath
Just say the word and I will disappear
Into the wildernes'''

song_split = song.partition('voices')
posicion = song_split.index('voices')
song_split=list(song_split)
print(posicion)
song_split[posicion]='sounds'
song=str(song_split)

print(song)