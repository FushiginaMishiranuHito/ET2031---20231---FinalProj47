import pygame
import sys
import random
from words import *

class WordleGame:
    class Letter:
        def __init__(self, game, text, bg_position):
            self.game = game
            self.bg_color = "white"
            self.text_color = "black"
            self.bg_position = bg_position
            self.bg_x = bg_position[0]
            self.bg_y = bg_position[1]
            self.bg_rect = (self.bg_x, self.bg_y, int(75 * self.game.a), int(75 * self.game.a))
            self.text = text
            self.text_position = (self.bg_x + int(36 * self.game.a), self.bg_position[1] + int(34 * self.game.a))
            self.text_surface = pygame.font.Font("assets/FreeSansBold.otf", int(50 * self.game.a)).render(self.text, True, self.text_color)
            self.text_rect = self.text_surface.get_rect(center=self.text_position)

        def draw(self):
            pygame.draw.rect(self.game.SCREEN, self.bg_color, self.bg_rect)
            if self.bg_color == "white":
                pygame.draw.rect(self.game.SCREEN, self.game.FILLED_OUTLINE, self.bg_rect, int(3 * self.game.a))
            self.text_surface = self.game.GUESSED_LETTER_FONT.render(self.text, True, self.text_color)
            self.game.SCREEN.blit(self.text_surface, self.text_rect)
            pygame.display.update()

        def delete(self):
            pygame.draw.rect(self.game.SCREEN, "white", self.bg_rect)
            pygame.draw.rect(self.game.SCREEN, self.game.OUTLINE, self.bg_rect, 2)
            pygame.display.update()

    class Indicator:
        def __init__(self, game, x, y, letter):
            self.game = game
            self.x = x
            self.y = y
            self.text = letter
            self.rect = (self.x, self.y, int(57 * self.game.a), int(75 * self.game.a))
            self.bg_color = self.game.OUTLINE

        def draw(self):
            pygame.draw.rect(self.game.SCREEN, self.bg_color, self.rect)
            text_surface = self.game.AVAILABLE_LETTER_FONT.render(self.text, True, "white")
            text_rect = text_surface.get_rect(center=(self.x + int(27 * self.game.a), self.y + int(30 * self.game.a)))
            self.game.SCREEN.blit(text_surface, text_rect)
            pygame.display.update()

    def __init__(self):
        pygame.init()

        # Constants
        self.a = 2 / 3
        self.WIDTH, self.HEIGHT = int(self.a * 633), int(self.a * 900)

        # Resize image
        self.image_ = pygame.image.load("./assets/StartingTiles.png")
        self.y_image = int(self.image_.get_height() * self.a)
        self.x_image = int(self.image_.get_width() * self.a)
        self.image_ = pygame.transform.scale(self.image_, (self.x_image, self.y_image))

        self.SCREEN = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.BACKGROUND = self.image_
        self.BACKGROUND_RECT = self.BACKGROUND.get_rect(center=(int(317 * self.a), int(300 * self.a)))
        self.ICON = pygame.image.load("assets/Icon.png")

        self.GREEN = "#6aaa64"
        self.YELLOW = "#c9b458"
        self.GREY = "#787c7e"
        self.OUTLINE = "#d3d6da"
        self.FILLED_OUTLINE = "#878a8c"
        
        self.CORRECT_WORD = random.choice(WORDS)

        self.ALPHABET = ["QWERTYUIOP", "ASDFGHJKL", "ZXCVBNM"]

        self.GUESSED_LETTER_FONT = pygame.font.Font("assets/FreeSansBold.otf", int(50 * self.a))
        self.AVAILABLE_LETTER_FONT = pygame.font.Font("assets/FreeSansBold.otf", int(25 * self.a))

        self.LETTER_X_SPACING = int((85 * 2 / 3))
        self.LETTER_Y_SPACING = int((12 * self.a))
        self.LETTER_SIZE = int(75 * 2 / 3)

        pygame.display.set_caption("Wordle!")
        pygame.display.set_icon(self.ICON)

        self.SCREEN.fill("white")
        self.SCREEN.blit(self.BACKGROUND, self.BACKGROUND_RECT)
        pygame.display.update()

        # Global variables
        self.guesses_count = 0
        self.guesses = [[]] * 6
        self.current_guess = []
        self.current_guess_string = ""
        self.current_letter_bg_x = int(110 * self.a)

        # Indicators is a list storing all the Indicator object.
        # An indicator is that button thing with all the letters you see.
        self.indicators = []

        self.game_result = ""

        self.setup_indicators()

    def setup_indicators(self):
        indicator_x, indicator_y = int(20 * self.a), int(600 * self.a)

        for i in range(3):
            for letter in self.ALPHABET[i]:
                new_indicator = self.Indicator(self, indicator_x, indicator_y, letter)
                self.indicators.append(new_indicator)
                new_indicator.draw()
                indicator_x += int(60 * self.a)
            indicator_y += int(100 * self.a)
            if i == 0:
                indicator_x = int(50 * self.a)
            elif i == 1:
                indicator_x = int(105 * self.a)

    def check_guess(self, guess_to_check):
        game_decided = False
        for i in range(5):
            lowercase_letter = guess_to_check[i].text.lower()
            if lowercase_letter in self.CORRECT_WORD:
                if lowercase_letter == self.CORRECT_WORD[i]:
                    guess_to_check[i].bg_color = self.GREEN
                    for indicator in self.indicators:
                        if indicator.text == lowercase_letter.upper():
                            indicator.bg_color = self.GREEN
                            indicator.draw()
                    guess_to_check[i].text_color = "white"
                    if not game_decided:
                        self.game_result = "W"
                else:
                    guess_to_check[i].bg_color = self.YELLOW
                    for indicator in self.indicators:
                        if indicator.text == lowercase_letter.upper():
                            indicator.bg_color = self.YELLOW
                            indicator.draw()
                    guess_to_check[i].text_color = "white"
                    self.game_result = ""
                    game_decided = True
            else:
                guess_to_check[i].bg_color = self.GREY
                for indicator in self.indicators:
                    if indicator.text == lowercase_letter.upper():
                        indicator.bg_color = self.GREY
                        indicator.draw()
                guess_to_check[i].text_color = "white"
                self.game_result = ""
                game_decided = True
            guess_to_check[i].draw()
            pygame.display.update()

        self.guesses_count += 1
        self.current_guess = []
        self.current_guess_string = ""
        self.current_letter_bg_x = 110 * self.a

        if self.guesses_count == 6 and self.game_result == "":
            self.game_result = "L"

    def play_again(self):
        pygame.draw.rect(self.SCREEN, "white", (int(10 * self.a), int(600 * self.a), int(1000 * self.a), int(600 * self.a)))
        play_again_font = pygame.font.Font("assets/FreeSansBold.otf", int(40 * self.a))
        play_again_text = play_again_font.render("Press ENTER to Play Again!", True, "black")
        play_again_rect = play_again_text.get_rect(center=(int(self.WIDTH / 2), int(700 * self.a)))
        word_was_text = play_again_font.render(f"The word was {self.CORRECT_WORD}!", True, "black")
        word_was_rect = word_was_text.get_rect(center=(int(self.WIDTH / 2), int(650 * self.a)))
        self.SCREEN.blit(word_was_text, word_was_rect)
        self.SCREEN.blit(play_again_text, play_again_rect)
        pygame.display.update()

    def reset(self):
        self.SCREEN.fill("white")
        self.SCREEN.blit(self.BACKGROUND, self.BACKGROUND_RECT)
        self.guesses_count = 0
        self.CORRECT_WORD = random.choice(WORDS)
        print(self.CORRECT_WORD)
        self.guesses = [[]] * 6
        self.current_guess = []
        self.current_guess_string = ""
        self.game_result = ""
        pygame.display.update()
        for indicator in self.indicators:
            indicator.bg_color = self.OUTLINE
            indicator.draw()

    def create_new_letter(self, key_pressed):
        self.current_guess_string += key_pressed
        new_letter = self.Letter(
            self, key_pressed, (
                self.current_letter_bg_x, 
                int(self.guesses_count * 100 * self.a) + self.LETTER_Y_SPACING))
        self.current_letter_bg_x += self.LETTER_X_SPACING
        self.guesses[self.guesses_count].append(new_letter)
        self.current_guess.append(new_letter)
        for guess in self.guesses:
            for letter in guess:
                letter.draw()

    def delete_letter(self):
        self.guesses[self.guesses_count][-1].delete()
        self.guesses[self.guesses_count].pop()
        self.current_guess_string = self.current_guess_string[:-1]
        self.current_guess.pop()
        self.current_letter_bg_x -= self.LETTER_X_SPACING

    def run_game_loop(self):
        print(self.CORRECT_WORD)
        while True:
            if self.game_result != "":
                self.play_again()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        if self.game_result != "":
                            self.reset()
                        else:
                            if len(self.current_guess_string) == 5 and self.current_guess_string.lower() in WORDS:
                                self.check_guess(self.current_guess)
                    elif event.key == pygame.K_BACKSPACE:
                        if len(self.current_guess_string) > 0:
                            self.delete_letter()
                    else:
                        key_pressed = event.unicode.upper()
                        if key_pressed in "QWERTYUIOPASDFGHJKLZXCVBNM" and key_pressed != "":
                            if len(self.current_guess_string) < 5:
                                self.create_new_letter(key_pressed)

if __name__ == "__main__":
    WordleGame().run_game_loop()
