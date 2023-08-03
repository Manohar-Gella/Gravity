import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Constants for the window size
WIDTH, HEIGHT = 400, 300

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Function to draw text on the screen
def draw_text(text, size, color, x, y):
    font = pygame.font.Font(None, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.center = (x, y)
    screen.blit(text_surface, text_rect)

# Function to handle game events
def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

# Function to start a new game
def start_new_game():
    return random.randint(1, 100)

# Main game loop
def game_loop():
    number_to_guess = start_new_game()
    attempts = 0

    while True:
        handle_events()

        # Clear the screen
        screen.fill(WHITE)

        # Draw the game title
        draw_text("Guess the Number", 30, BLACK, WIDTH // 2, 50)

        # Draw instructions
        draw_text("Guess a number between 1 and 100", 20, BLACK, WIDTH // 2, 100)

        # Draw number of attempts
        draw_text(f"Attempts: {attempts}", 20, BLACK, WIDTH // 2, 130)

        # Check for player input
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            try:
                player_guess = int(input_box.text)
                attempts += 1

                if player_guess == number_to_guess:
                    draw_text("Congratulations! You guessed the number!", 20, BLACK, WIDTH // 2, 200)
                elif player_guess < number_to_guess:
                    draw_text("Try a higher number.", 20, BLACK, WIDTH // 2, 200)
                else:
                    draw_text("Try a lower number.", 20, BLACK, WIDTH // 2, 200)

                pygame.display.update()
                pygame.time.delay(1000)

                # Start a new game after displaying the result for 1 second
                number_to_guess = start_new_game()
                attempts = 0
            except ValueError:
                # Handle non-integer input
                pass

        # Update the display
        pygame.display.update()

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Guess the Number")

# Run the game loop
game_loop()

