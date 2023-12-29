class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics # 歌词实际上传递给了lyrics参数，self.lyrics是新创建的属性
# self是自带的默认参数，用于方便创建其他属性
    def sing_me_a_song(self):
        for line in self.lyrics: # 写self是为了操作实例属性
            print(line)

happy_bday = Song(["Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there"])

bulls_on_parade = Song(["They rally around tha family",
                        "With pockets full of shells"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()