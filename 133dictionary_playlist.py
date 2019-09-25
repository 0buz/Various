playlist = {
    'title': 'bus',
    'author': 'Adi',
    'songs': [
        {
            'title':'song1',
            'artist':['blue'],
            'duration': 2.8
        },
        {
            'title': 'song2',
            'artist': ['white','black'],
            'duration': 6.2
        },
        {
            'title': 'song',
            'artist': ['red'],
            'duration': 3.0
        }
    ]
}

total_duration=0
for song in playlist['songs']:
    print(song['title'], " ", song['duration'])
    total_duration+=song['duration']
print("\nTotal playlist time: ", total_duration)
