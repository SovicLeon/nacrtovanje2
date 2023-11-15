import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Mouse Lines")

# Define colors
black = (0, 0, 0)
white = (255, 255, 255)
blue = (0, 0, 255)

# Store mouse positions
mouse_positions = []

circle_positions = []

# Main game loop
running = True
while running:
    # Get mouse position
    mouse_pos = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            circle_positions.append(mouse_pos)

    # Append mouse position to the list
    mouse_positions.append(mouse_pos)

    # Draw lines between consecutive mouse positions
    if len(mouse_positions) > 1:
        pygame.draw.lines(screen, white, False, mouse_positions, 2)

    # Draw circles for each position in circle_positions
    for pos in circle_positions:
        pygame.draw.circle(screen, blue, pos, 3)

    # Update the display
    pygame.display.flip()

    # Fill the screen with black to clear previous lines
    screen.fill(black)

# Quit Pygame
pygame.quit()
sys.exit()
