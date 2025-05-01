import pygame
import random
import sys
import os

# Initialize Pygame
pygame.init()
pygame.font.init()
pygame.mixer.init()
pygame.display.set_caption("Meower 3000")

# Set up the display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
FPS = 30
clock = pygame.time.Clock()
color = (255, 255, 255)  # White background
screen.fill(color)

# Get the absolute path to the assets folder
BASE_DIR = os.path.dirname(__file__)
ASSETS_DIR = os.path.join(BASE_DIR, "assets")

# Load images
def load_image(name, scale=1):
    image_path = os.path.join(ASSETS_DIR, name)
    image = pygame.image.load(image_path).convert_alpha()
    if scale != 1:
        image = pygame.transform.scale(image, (int(image.get_width() * scale), int(image.get_height() * scale)))
    return image

# Load sounds
def load_sound(name):
    sound_path = os.path.join(ASSETS_DIR, name)
    return pygame.mixer.Sound(sound_path)

# Main game loop
def main():
    # Load assets
    cat_image = load_image("kitty.png", scale=0.5)  # Example image
    meow_sound = load_sound("cat_meow.mp3")  # Example sound

    # Get the image's rectangle for positioning
    cat_rect = cat_image.get_rect(center=(WIDTH // 2, HEIGHT // 2))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Play the meow sound on mouse click
                meow_sound.play()

        # Fill the screen with white
        screen.fill(color)

        # Draw the cat image
        screen.blit(cat_image, cat_rect)

        # Update the display
        pygame.display.flip()

        # Limit the frame rate
        clock.tick(FPS)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()