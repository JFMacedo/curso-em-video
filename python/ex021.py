from pygame import mixer
mixer.init()
mixer.music.load('ex021.mp3')
mixer.music.play()
input('\033[34mAgora você escuta?\033[m')