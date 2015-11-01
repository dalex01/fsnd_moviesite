import webbrowser

class Video():
    def __init__(self, title, duration):
        self.title = title
        self.duration = duration

    def show_duration(self):
        return self.duration

class Movie(Video):
    """This class provides a way to store movies related information"""
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    def __init__(self, title, duration, story_line, poster_image, trailer_youtube):
        Video.__init__(self, title, duration)
        self.storyline = story_line
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)

class TvShow(Video):
    def __init__(self, title, duration, season, episode, tv_station):
        Video.__init__(self, title, duration)
        self.season = season
        self.episode = episode
        self.tv_station = tv_station