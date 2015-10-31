import webbrowser

class Movie():
    """This class provides a way to store movies related information"""
    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    def __init__(self, title, story_line, poster_image, trailer_youtube):
        self.title = title
        self.storyline = story_line
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
