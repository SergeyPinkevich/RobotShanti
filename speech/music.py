from urllib.request import urlopen
from pydub import AudioSegment
from pydub.playback import play

# mp3file = urlopen("https://cs9-19v4.userapi.com/p1/d722df69efb593.mp3")
# with open('./test.mp3', 'wb') as output:
#     output.write(mp3file.read())
#
# song = AudioSegment.from_mp3("./test.mp3")
# play(song)

from rapidconnect import RapidConnect
rapid = RapidConnect('robotshanti_5a4f3a79e4b09c6b28427e54', 'f9379269-6068-433b-a882-e22a4655ebd8')

result = rapid.call('SpotifyPublicAPI', 'searchTracks', {
	'accessToken': 'robotshanti_5a4f3a79e4b09c6b28427e54',
	'query': 'I am not Afraid'
})

print(result)