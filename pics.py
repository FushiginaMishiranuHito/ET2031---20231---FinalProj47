#Global var
self.game_result = ""

#check_guess()
if not game_decided:
    self.game_result = "W"

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
        