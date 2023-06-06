class Song(object):
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

#happy_bday = Song(["Happy bday", "to you"])


#in_da_club = Song(["yo shawty", "its yo birthday"])

love_sosa = Song(["******* love sosa", "let them know then", "raries and rover"])


#imagine this song.sing_me_a_song
#happy_bday.sing_me_a_song()

# self or the instance of the class in this case is represented as happy_bday and in_da_club
#in_da_club.sing_me_a_song()

love_sosa.sing_me_a_song()