import random
import pygame
import sys

# Initialize pygame
pygame.init()

# Set up the screen with window size and resizable option
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption('Rock Paper Scissors')

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# ASCII Art for Rock, Paper, and Scissors (side views)
rock_hand = '''
   -----] 
 --       ]
          ]
          ]
 --       ]
   -------        
'''

paper_hand = '''
   -------] 
 --       -----]
          -----]
          -----]
 --       -----]
   -------
'''

scissors_hand = '''
   ------- 
 --       -----]
          -----]
          ]
 --       ]
   -------
'''

# Fonts
font = pygame.font.SysFont("Courier", 20)  # Use fixed-width font for ASCII art

def show_message(message, y_offset=0):
    if isinstance(message, list):  # If the message is a list of lines (for ASCII art)
        for i, line in enumerate(message):
            text = font.render(line, True, WHITE)
            screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 + y_offset + i * 30))
    else:
        text = font.render(message, True, WHITE)
        screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 + y_offset))


def show_start_screen():
    screen.fill(BLACK)  # Black background
    show_message("ROCK! PAPER! SCISSORS!", -100)
    show_message("Press R for Rock, P for Paper, S for Scissors", 50)
    show_message("Press Q to Quit", 100)
    pygame.display.update()


def show_transition_screen(user_choice, comp_choice):
    screen.fill(BLACK)  # Black background
    user_art = get_ascii_art(user_choice)
    comp_art = get_ascii_art(comp_choice)

    # Display user art on the left
    for i, line in enumerate(user_art):
        show_message(line, -60 + i * 30)  # Display user art, starting at top left

    # Display computer art on the right
    for i, line in enumerate(comp_art):
        show_message(line, -60 + i * 30 + 300)  # Display computer art, offset to the right side

    pygame.display.update()


def show_game_screen(user_choice, comp_choice):
    screen.fill(BLACK)  # Black background

    # Get the ASCII art for user and computer choices
    user_art = get_ascii_art(user_choice)
    comp_art = get_ascii_art(comp_choice)

    # Display user ASCII art on the left
    for i, line in enumerate(user_art):
        show_message(line, -100 + i * 30)  # Display user art, starting at top left

    # Display computer ASCII art on the right
    for i, line in enumerate(comp_art):
        show_message(line, -100 + i * 30)  # Display comp art, offset to the right side

    pygame.display.update()


def get_ascii_art(choice):
    if choice == "rock":
        return rock_hand.splitlines()
    elif choice == "paper":
        return paper_hand.splitlines()
    elif choice == "scissors":
        return scissors_hand.splitlines()
    else:
        return []


def show_result(result):
    screen.fill(BLACK)  # Black background
    if result == "DRAW":
        show_message("<== It's a tie! ==>", 0)
    elif result == "USER":
        show_message("<== User wins! ==>", 0)
    else:
        show_message("<== Computer wins! ==>", 0)

    show_message("Press any key to play again", 50)
    pygame.display.update()


def main():
    # Start screen
    show_start_screen()
    waiting_for_input = True
    while waiting_for_input:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:  # Quit the game if 'Q' is pressed
                    pygame.quit()
                    sys.exit()
                waiting_for_input = False

    while True:
        # Ask the user for their choice
        user_choice = ""
        waiting_for_input = True
        while waiting_for_input:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    # Capture keypresses
                    if event.key == pygame.K_r:
                        user_choice = "rock"
                        waiting_for_input = False
                    elif event.key == pygame.K_p:
                        user_choice = "paper"
                        waiting_for_input = False
                    elif event.key == pygame.K_s:
                        user_choice = "scissors"
                        waiting_for_input = False
                    elif event.key == pygame.K_q:  # Quit the game if 'Q' is pressed
                        pygame.quit()
                        sys.exit()

        # Computer makes a random choice
        comp_choice = random.choice(["rock", "paper", "scissors"])

        # Show choices on screen (transition between choices and result)
        show_transition_screen(user_choice, comp_choice)

        # Add a short delay before showing the result
        pygame.time.delay(1000)

        # Determine the winner
        if user_choice == comp_choice:
            result = "DRAW"
        elif (user_choice == "rock" and comp_choice == "scissors") or \
                (user_choice == "paper" and comp_choice == "rock") or \
                (user_choice == "scissors" and comp_choice == "paper"):
            result = "USER"
        else:
            result = "COMPUTER"

        # Display the result
        show_result(result)

        # Wait for user to decide if they want to play again or quit
        waiting_for_input = True
        while waiting_for_input:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:  # Quit the game if 'Q' is pressed
                        pygame.quit()
                        sys.exit()
                    waiting_for_input = False
                    show_start_screen()  # Show the start screen again after the round ends

if __name__ == "__main__":
    main()
