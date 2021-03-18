import string
import turtle as t
import random
from typing import Dict, Tuple

MIN_FONT_SIZE = 8
MAX_FONT_SIZE = 128
MARGIN_PCT = 0.7


class WordCloud:

    def __init__(self):
        screen = t.getscreen()
        # Sets the overall window to be 100% of monitor
        screen.setup(width=1.0, height=1.0)
        # Sets the CANVAS to be the size of the screen (subtract out some border pixels to avoid scrollbar)
        screen.screensize(canvwidth=screen.window_width() - 30, canvheight=screen.window_height() - 30)
        self.half_screen_w = screen.canvwidth // 2
        self.half_screen_h = screen.canvheight // 2

        # set to RGB mode
        t.colormode(255)

        t.hideturtle()
        t.speed(0)  # 0 is fastest
        t.penup()

    def random_coord(self) -> Tuple[int, int]:
        # Leave a margin
        x = random.randint(- int(self.half_screen_w * MARGIN_PCT), int(self.half_screen_w * MARGIN_PCT))
        y = random.randint(- int(self.half_screen_h * MARGIN_PCT), int(self.half_screen_h * MARGIN_PCT))
        return x, y

    def random_pen_color(self) -> Tuple[int, int, int]:
        red = random.randint(0, 200)
        green = random.randint(0, 200)
        blue = random.randint(0, 200)
        return red, green, blue

    def strip_punctuation(self, text: str) -> str:
        return text.translate(str.maketrans('', '', string.punctuation))

    def write_word(self, word: str, color: Tuple[int, int, int], font_size: int) -> None:
        t.pencolor(color)
        t.write(word, align="center", font=("Arial", font_size, "normal"))

    def analyze_text(self, filename: str) -> Dict:
        """
        Opens the file and analyzes all of the words in the text. Removes all punctuation and converts all
        letters to lowercase
        :param filename: name of the file
        :return: a dictionary where the key is the word and the value is the frequency of the word in the text
        """

        with open(filename, "r") as f:
            text = f.read()

        stats = {}
        for word in text.split():
            word = self.strip_punctuation(word)
            word = word.lower()
            if word in stats:
                stats[word] += 1
            else:
                stats[word] = 1

        # TODO Write code to analyze the text in the file.
        # Hints: read the file into a string split it into words, remove punctuation (see helper method above),
        #        convert to lowercase, store your frequencies in a dictionary and return that dictionary

        return stats

    def draw_word_cloud(self, filename: str) -> None:
        """
        Given the file, draws words on a Turtle canvas where their font size corresponds to the frequency of the
        word in the file. The location of the word should be random.
        :param filename: name of the file to draw
        :return: None
        """

        # Generate the word frequencies
        stats = self.analyze_text(filename)

        for word in stats:
            color = self.random_pen_color()
            t.goto(self.random_coord())
            self.write_word(word, color, stats[word]) 1

        # TODO Write code to draw the word cloud.
        # Hints:
        # Use the helper methods provided
        # Draw the lower frequency words first so they are in the background
        # You may skip words that have  frequencies of only 1 or 2
        # You can just use the frequency count as the font_size to keep things simple


if __name__ == "__main__":
    cloud = WordCloud()
    cloud.draw_word_cloud("dracula.txt")
    t.done()
