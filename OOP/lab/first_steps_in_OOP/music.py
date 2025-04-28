class Music:
    def __init__(self, title, artist, lyrics):
        self.title: str = title
        self.artist: str = artist
        self.lyrics: str = lyrics

    def print_info(self):
        return f'This is "{self.title}" from "{self.artist}"'

    def play(self):
        return self.lyrics