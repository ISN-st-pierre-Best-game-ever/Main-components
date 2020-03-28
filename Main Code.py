import pygame

print("loading...")

pygame.init()
screen_size = screen_width, screen_height = 800, 800
screen = pygame.display.set_mode(screen_size)
done = False

pos_player_1 = (0, 0)
pos_player_2 = (0, 0)

player_turn = 1
speed = 20

# fais en sorte que le joueur spawne dans l'écran


def in_screen():
    return max(min(pygame.mouse.get_pos(), (screen_width, screen_height)), (10, 10))

# Rafraichir l'écran et la position des cercles


def refresh():
    screen.fill((0, 0, 0))
    pygame.draw.circle(screen, (209, 0, 108), pos_player_1, 20)
    pygame.draw.circle(screen, (0, 139, 209), pos_player_2, 20)
    pygame.display.flip()


print("ready !")

# Boucle principale


while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("Game ended")
            done = True

# Position initiale joueurs

        if event.type == pygame.MOUSEBUTTONUP:

            if player_turn == 2:
                pygame.draw.circle(screen, (0, 139, 209), in_screen(), 20)
                player_turn += 1
                pos_player_2 = pygame.mouse.get_pos()
                print("Player 2 spawned in", pos_player_2)

            if player_turn == 1:
                pygame.draw.circle(screen, (209, 0, 108), in_screen(), 20)
                player_turn += 1
                pos_player_1 = pygame.mouse.get_pos()
                print("Player 1 spawned in", pos_player_1)

            pygame.display.flip()

# Opérations touches

        if player_turn == 3 and event.type == pygame.KEYDOWN:
            abs_p1 = pos_player_1[0]
            ord_p1 = pos_player_1[1]
            abs_p2 = pos_player_2[0]
            ord_p2 = pos_player_2[1]

# Exit
            if event.key == pygame.K_ESCAPE:
                print("Game left (pressed Escape)")
                done = True

# Deplacement Joueur 1 (Flèches)

            if event.key == pygame.K_LEFT and abs_p1 > 10:
                abs_p1 -= speed
                pos_player_1 = [abs_p1, ord_p1]
                refresh()

            if event.key == pygame.K_RIGHT and abs_p1 < screen_width - 10:
                abs_p1 += speed
                pos_player_1 = [abs_p1, ord_p1]
                refresh()

            if event.key == pygame.K_UP and ord_p1 > 10:
                ord_p1 -= speed
                pos_player_1 = [abs_p1, ord_p1]
                refresh()

            if event.key == pygame.K_DOWN and ord_p1 < screen_height - 10:
                ord_p1 += speed
                pos_player_1 = [abs_p1, ord_p1]
                refresh()

# Deplacement Joueur 2 (ZQSD) + reconnait le clavier comme QWERTY

            if event.key == pygame.K_a and abs_p2 > 10:
                abs_p2 -= speed
                pos_player_2 = [abs_p2, ord_p2]
                refresh()

            if event.key == pygame.K_d and abs_p2 < screen_width - 10:
                abs_p2 += speed
                pos_player_2 = [abs_p2, ord_p2]
                refresh()

            if event.key == pygame.K_w and ord_p2 > 10:
                ord_p2 -= speed
                pos_player_2 = [abs_p2, ord_p2]
                refresh()

            if event.key == pygame.K_s and ord_p2 < screen_height - 10:
                ord_p2 += speed
                pos_player_2 = [abs_p2, ord_p2]
                refresh()

