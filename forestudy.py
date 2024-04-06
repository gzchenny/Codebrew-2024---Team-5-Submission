import pygame
import sys 
import json
import os
import math
from sympy import *
from random import *
from functools import reduce

pygame.init()
music = pygame.mixer.music.load('graphics/background-music.mp3')
pygame.mixer.music.play(-1)


# Getting font
def get_font(size):
    return pygame.font.Font("graphics/font.otf", size)


def menu():
        """Main Menu Page which displays the name, 'My Decks' option, and 'Create Deck' option."""
        WIDTH = 900
        HEIGHT = 600

        background = pygame.image.load("graphics/background-main.png")     # image from https://saurabhkgp.itch.io/pixel-art-forest-background-simple-seamless-parallax-ready-for-2d-platformer-s 5/4/24
        background_scaled = pygame.transform.scale(background, (WIDTH, HEIGHT))

        screen = pygame.display.set_mode((WIDTH, HEIGHT))

        
        i = 0
        counter = 0
        width = screen.get_width()

        # wolf running animation
        wolf_run_1 = pygame.image.load('graphics/wolfrun1.png')
        wolf_run_2 = pygame.image.load('graphics/wolfrun2.png')
        wolf_run_3 = pygame.image.load('graphics/wolfrun3.png')
        wolf_run_4 = pygame.image.load('graphics/wolfrun4.png')
        wolf_run_5 = pygame.image.load('graphics/wolfrun5.png')
        wolf_run_6 = pygame.image.load('graphics/wolfrun6.png')
        wolf_run_7 = pygame.image.load('graphics/wolfrun7.png')
        wolf_run_8 = pygame.image.load('graphics/wolfrun8.png')
        wolf_run = [wolf_run_1, wolf_run_2, wolf_run_3, wolf_run_4, wolf_run_5, wolf_run_6, wolf_run_7, wolf_run_8]
        player_index = 0
        player_surf = wolf_run[player_index]
        wolf_x_position = 0

        pygame.font.init()
        pygame.display.set_caption('forestudy')

        menu = True

        #(game_text, (game_text.get_rect(center=(width/2, 100)

        RGB = (0, 34, 68)

        game_text = pygame.font.Font("graphics/font.otf", 60)
        game_text2 = pygame.font.Font("graphics/font.otf", 30)
        display_text = game_text.render('forestudy', True, "#ffebcd")
        display_text2 = game_text2.render('press 1 to create new deck', True, "#ffebcd")
        display_text3 = game_text2.render('press 2 to open my decks', True, "#ffebcd")
        display_text4 = game_text2.render('press 3 to quit', True, "#ffebcd")
        run_menu = True

        CENTRE = 300


        while run_menu:
                clock = pygame.time.Clock()
                clock.tick(10)
                screen.blits([(background_scaled, ((-i)%(2*width)-width,0)),(background_scaled, ((-i-width)%(2*width)-width,0)),(wolf_run[(i)%8], (350, 360)),(display_text, (CENTRE, 230)),(display_text2, (CENTRE-70, 290)),(display_text3, (CENTRE-40, 320)), (display_text4, (CENTRE+30, 350))])
                pygame.display.update()
                i += 10
                key_states = pygame.key.get_pressed()

                if key_states[pygame.K_3]:
                        sys.exit()
                        run_menu = False
                if key_states[pygame.K_2]:
                        my_deck()
                        run_menu = False
                if key_states[pygame.K_1]:
                        name_deck()
                        run_menu = False
                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                                sys.exit()
                pygame.display.update()
                clock.tick(50)        
        
# DO NOT DELOW BELOW
        """while True:
                clock = pygame.time.Clock()
                clock.tick(10)
                screen.blits([(background_scaled, ((-i)%(2*width)-width,0)),(background_scaled, ((-i-width)%(2*width)-width,0)),(wolf_run[(i)%8], (350, 360)),(display_text, (CENTRE, 230)),(display_text2, (CENTRE-70, 290)),(display_text3, (CENTRE-40, 320)), (display_text4, (CENTRE+30, 350))])
                pygame.display.update()
                i += 10
                key_states = pygame.key.get_pressed()

                menu_events()
        
def menu_events():
        for event in pygame.get():
                if event.type == pygame.QUIT:
                        sys.exit()
                elif event.type == pygame.KEYDOWN:
                        if key_states[pygame.K_3]:
                                sys.exit()
                                elif key_states[pygame.K_2]:
                                        my_deck()
                                elif key_states[pygame.K_1]:
                                        name_deck()
                pygame.display.update()
                clock.tick(50)"""

def create_deck():
        """This page allows the user to create a deck by adding the front and back of a card."""
        global deck, final_dict

        deck = {}

        with open('my_file') as json_file:
                fileData  = json_file.read()
                if fileData == '':
                       dictionary_from_file = {}
                else:
                        dictionary_from_file = json.loads(fileData)

        final_dict = {}

        for key in dictionary_from_file:
                final_dict[key] = dictionary_from_file[key]
         
        def append_record(record):
                with open('my_file', 'w') as f:
                        json.dump(record, f)
                        f.write(os.linesep)

        SCREEN_WIDTH = 900
        SCREEN_HEIGHT = 600
        # Load background image
        background_image = pygame.image.load('graphics/background-main.png')
        background_scaled = pygame.transform.scale(background_image,(SCREEN_WIDTH,SCREEN_HEIGHT))
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption('Add Card')

        pygame.display.set_caption("Forestudy")  # Set the window title

        user_ip_question = ''
        user_ip_answer = ''
        font = pygame.font.Font("graphics/font.otf", 15)
        question_font = pygame.font.Font("graphics/font.otf", 20)
        text_box_question = pygame.Rect(200, 150, 500, 75)
        text_box_answer = pygame.Rect(200, 275, 500, 75)
        big_box = pygame.Rect(165, 100, 600, 400)
        button_add_card = pygame.Rect(300, 375, 150, 50)
        button_return_menu = pygame.Rect(500, 375, 150, 50)
        active_question = False
        active_answer = False
        color_outline = pygame.Color('white')
        color_answer = pygame.Color('white')
        clock = pygame.time.Clock()
        # Blit background image
        screen.blit(background_scaled, (0, 0))

        # Main game loop
        while True:
              for events in pygame.event.get():
                if events.type == pygame.QUIT:
                        pygame.quit()
                        quit()
                if events.type == pygame.MOUSEBUTTONDOWN:
                        if text_box_question.collidepoint(events.pos):
                                active_question = True
                                active_answer = False  # Deactivate answer box
                        elif text_box_answer.collidepoint(events.pos):
                                active_answer = True
                                active_question = False  # Deactivate question box
                        elif button_add_card.collidepoint(events.pos):
                                # Display message on button click
                                add_card_message = font.render("Add Card button clicked!", True, pygame.Color('white'))
                                screen.blit(add_card_message, (400, 450))  # Adjust position as needed
                                pygame.display.update()
                                pygame.time.delay(1000)  # Display message for 1 second
                                if deck_name in final_dict.keys():
                                       deck = final_dict[deck_name]
                                       question = user_ip_question
                                       answer = user_ip_answer
                                       deck[question] = answer
                                else:
                                       question = user_ip_question
                                       answer = user_ip_answer
                                       deck[question] = answer
                                       final_dict[deck_name] = deck
                             
                                append_record(final_dict)

                                # Clear the text boxes after adding the card
                                user_ip_question = ''
                                user_ip_answer = ''
                                
                        elif button_return_menu.collidepoint(events.pos):
                                menu()
                        else:
                                active_question = False
                                active_answer = False
                if events.type == pygame.KEYDOWN:
                        if active_question:
                                if events.key == pygame.K_BACKSPACE:
                                       user_ip_question = user_ip_question[:-1]
                                else:
                                        user_ip_question += events.unicode
                        elif active_answer:
                                if events.key == pygame.K_BACKSPACE:
                                        user_ip_answer = user_ip_answer[:-1]
                                else:
                                        user_ip_answer += events.unicode
                

                pygame.draw.rect(screen, "#668C8E", big_box)

                # Render and display the question text and box
                question_surf = question_font.render("Question", True, pygame.Color('white'))
                screen.blit(question_surf, (text_box_question.x, text_box_question.y - 30))
                pygame.draw.rect(screen, color_outline, text_box_question, 2)
                surf_question = font.render(user_ip_question, True, 'white')
                screen.blit(surf_question, (text_box_question.x + 5, text_box_question.y + 5))
                
                # Render and display the answer text and box
                answer_surf = question_font.render("Answer", True, pygame.Color('white'))
                screen.blit(answer_surf, (text_box_answer.x, text_box_answer.y - 30))
                pygame.draw.rect(screen, color_answer, text_box_answer, 2)
                surf_answer = font.render(user_ip_answer, True, 'white')
                screen.blit(surf_answer, (text_box_answer.x + 5, text_box_answer.y + 5))

                # Render and display the buttons
                add_card_text = font.render("Add Card", True, pygame.Color('white'))
                pygame.draw.rect(screen, color_outline, button_add_card, 2)
                screen.blit(add_card_text, (button_add_card.x + 35, button_add_card.y + 15))
                
                return_menu_text = font.render("Save & Exit", True, pygame.Color('white')) # Renamed 'Return to Menu' button to 'Save & Exit'
                pygame.draw.rect(screen, color_outline, button_return_menu, 2)
                screen.blit(return_menu_text, (button_return_menu.x + 20, button_return_menu.y + 15))

                pygame.display.update()
                clock.tick(50)

def name_deck():
    global text_box_answer, deck_name
        
    SCREEN_WIDTH = 900
    SCREEN_HEIGHT = 600
    # Load background image
    background_image = pygame.image.load('graphics/background-main.png')
    background_scaled = pygame.transform.scale(background_image,(SCREEN_WIDTH,SCREEN_HEIGHT))
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Add Card')

    pygame.display.set_caption("Forestudy")  # Set the window title

    name_of_deck = ''
    font = pygame.font.Font("graphics/font.otf", 15)
    font_nameofdeck = pygame.font.Font("graphics/font.otf", 50)
    question_font = pygame.font.Font("graphics/font.otf", 30)
    text_box_nameyourdeck = pygame.Rect(200, 250, 500, 75)
    big_box = pygame.Rect(165, 100, 600, 400)
    button_save_1 = pygame.Rect(300, 375, 150, 50)
    button_exit_1 = pygame.Rect(500, 375, 150, 50)
    active_question = False
    color_outline = pygame.Color('white')
    clock = pygame.time.Clock()
    # Blit background image
    screen.blit(background_scaled, (0, 0))
    # Main game loop
    while True:
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                pygame.quit()
                quit()
            if events.type == pygame.MOUSEBUTTONDOWN:
                if text_box_nameyourdeck.collidepoint(events.pos):
                    active_question = True
                elif button_save_1.collidepoint(events.pos):
                    deck_name = name_of_deck
                    create_deck()
                elif button_exit_1.collidepoint(events.pos):
                        menu()
                else:
                    active_question = False
            if events.type == pygame.KEYDOWN:
                if active_question:
                    if events.key == pygame.K_BACKSPACE:
                        name_of_deck = name_of_deck[:-1]
                    else:
                        name_of_deck += events.unicode
            
        pygame.draw.rect(screen, "#668C8E", big_box)

        # Render and display the question text and box
        question_surf = question_font.render("Name your deck:", True, pygame.Color('white'))
        screen.blit(question_surf, (text_box_nameyourdeck.x, text_box_nameyourdeck.y - 60))
        pygame.draw.rect(screen, color_outline, text_box_nameyourdeck, 2)
        surf_question = font_nameofdeck.render(name_of_deck, True, 'white')
        screen.blit(surf_question, (text_box_nameyourdeck.x + 5, text_box_nameyourdeck.y + 5))

        # Render and display the buttons
        add_card_text = font.render("Save", True, pygame.Color('white'))
        pygame.draw.rect(screen, color_outline, button_save_1, 2)
        screen.blit(add_card_text, (button_save_1.x + 40, button_save_1.y + 15))


        return_menu_text = font.render("Exit", True, pygame.Color('white'))
        pygame.draw.rect(screen, color_outline, button_exit_1, 2)
        screen.blit(return_menu_text, (button_exit_1.x + 25, button_exit_1.y + 15))

        pygame.display.update()
        clock.tick(50)

def my_deck():
    global deck_pointer
    # function that opens my_file and then turns into final_dict
    
    with open('my_file') as json_file:
        fileData  = json_file.read()
        if fileData == '':
                dictionary_from_file = {}
        else:
                dictionary_from_file = json.loads(fileData)

        final_dict = {} 

        for key in dictionary_from_file:
                final_dict[key] = dictionary_from_file[key]

    SCREEN_WIDTH = 900
    SCREEN_HEIGHT = 600
    # Load background image
    background_image = pygame.image.load('graphics/background-main.png')
    background_scaled = pygame.transform.scale(background_image,(SCREEN_WIDTH,SCREEN_HEIGHT))
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('My Decks')
    
    font = pygame.font.Font("graphics/font.otf", 15)
    big_box = pygame.Rect(165, 100, 600, 400)
    clock = pygame.time.Clock()
    question_font = pygame.font.Font("graphics/font.otf", 20)
    list_of_decks = pygame.Rect(200, 200, 500, 75)
    my_deck_exitbutton = pygame.Rect(575, 425, 150, 50)
    screen.blit(background_scaled, (0, 0))
    my_deck_run = True
    
    # Main game loop
    while my_deck_run:

        list_of_deck_names = list(final_dict.keys()) # eg. [Maths, Geography, French]
        len_deck_names = len(list_of_deck_names) # eg. 3
        
        key_states = pygame.key.get_pressed()
        if key_states[pygame.K_1] and len_deck_names >= 1:
              deck_pointer = list_of_deck_names[0]
              choose_mode()
              my_deck_run = False
        if key_states[pygame.K_2] and len_deck_names >= 2:
              deck_pointer = list_of_deck_names[1]
              choose_mode()
              my_deck_run = False
        if key_states[pygame.K_3] and len_deck_names >= 3:
              deck_pointer = list_of_deck_names[2]
              choose_mode()
              my_deck_run = False
        if key_states[pygame.K_4] and len_deck_names >= 4:
              deck_pointer = list_of_deck_names[3]
              choose_mode()
              my_deck_run = False
        if key_states[pygame.K_5] and len_deck_names >= 5:
              deck_pointer = list_of_deck_names[4]
              choose_mode()
              my_deck_run = False
        if key_states[pygame.K_6] and len_deck_names >= 6:
              deck_pointer = list_of_deck_names[5]
              choose_mode()
              my_deck_run = False
        if key_states[pygame.K_7] and len_deck_names >= 7:
              deck_pointer = list_of_deck_names[6]
              choose_mode()
              my_deck_run = False
        if key_states[pygame.K_8] and len_deck_names >= 8:
              deck_pointer = list_of_deck_names[7]
              choose_mode()
              my_deck_run = False
        if key_states[pygame.K_9] and len_deck_names > 9:
              deck_pointer = list_of_deck_names[8]
              choose_mode()
              my_deck_run = False
        if key_states[pygame.K_9] and len_deck_names > 9:
              deck_pointer = list_of_deck_names[9]
              choose_mode()
              my_deck_run = False
        if key_states[pygame.K_0]:
              with open('maths_mode.py') as game:
                    exec(game.read(), globals())         # https://stackoverflow.com/questions/71527797/scope-of-globals-locals-use-with-exec

        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                        if my_deck_exitbutton.collidepoint(event.pos):
                                menu()
    
        pygame.draw.rect(screen, "#668C8E", big_box)
    
        # Render deck labels dynamically
        deckcount = 1
        while deckcount < len_deck_names + 1 and deckcount <=9: #Render decks 1-9.
                key =  list_of_deck_names[deckcount-1]
                deck_label = f"{deckcount}: {key}"
                deck_surf = question_font.render(deck_label, True, pygame.Color('#ffebcd'))
                y_position = list_of_decks.y + (deckcount - 1) * 30  # Adjust vertical spacing
                screen.blit(deck_surf, (list_of_decks.x, y_position))
                deckcount += 1
    
        return_menu_text = font.render("Exit", True, pygame.Color('#ffebcd'))
        pygame.draw.rect(screen, pygame.Color('#ffebcd'), my_deck_exitbutton, 2)
        screen.blit(return_menu_text, (my_deck_exitbutton.x + 10, my_deck_exitbutton.y + 15))
        
        # Instructions for the clueless user.
        tell_user_to_press_key = question_font.render("Use number keys to access your decks.", True, pygame.Color('#ffebcd'))
        screen.blit(tell_user_to_press_key, (200, 110))
        the_word_deck = question_font.render("Decks:", True, pygame.Color('#ffebcd'))
        screen.blit(the_word_deck, (200, 140))
        leilas_deck = question_font.render("0: Auto-Generated Maths Deck", True, pygame.Color('#ffebcd'))
        screen.blit(leilas_deck, (200, 170))
        
        
        pygame.display.update()
        clock.tick(50)
        
def flashcard_mode():
    pygame.init()
    pygame.font.init()

    SCREEN_WIDTH = 900
    SCREEN_HEIGHT = 600
    ANSWER = False
    flashcard_mode_exitbutton = pygame.Rect(500, 275, 150, 50)
    font = pygame.font.Font("graphics/font.otf", 20)
    # colours for flashcards
    FLASHCARD_COLOUR = "#2e3856"
    FLIPPED_COLOUR = "#595e6d"

    # sample data for testing
    with open('my_file') as json_file:
        fileData = json_file.read()
        dictionary_from_file = json.loads(fileData)

    # print(dictionary_from_file)

    demo_string_data = {}
    temp_dict = {}

    temp_dict[deck_pointer] = dictionary_from_file[deck_pointer]
    demo_string_data = temp_dict[deck_pointer]

    # initialising cards
    current_question = ""
    current_answer = ""
    card_turned = False
    index = 0

    wolf_x_position = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    background = pygame.image.load('graphics/forest.png')

    # wolf idle animation
    wolf_idle_1 = pygame.image.load('graphics/wolfidle1.png')
    wolf_idle_2 = pygame.image.load('graphics/wolfidle2.png')
    wolf_idle_3 = pygame.image.load('graphics/wolfidle3.png')
    wolf_idle_4 = pygame.image.load('graphics/wolfidle4.png')
    wolf_idle_5 = pygame.image.load('graphics/wolfidle5.png')
    wolf_idle_6 = pygame.image.load('graphics/wolfidle6.png')
    wolf_idle_7 = pygame.image.load('graphics/wolfidle7.png')
    wolf_idle = [wolf_idle_1, wolf_idle_2, wolf_idle_3, wolf_idle_4, wolf_idle_5, wolf_idle_6, wolf_idle_7]
    player_index = 0
    player_surf = wolf_idle[player_index]

    # animates the player's avatar
    def player_animation():
        global player_surf, player_index, wolf_x_position
        player_index = 0
        wolf_x_position = 0
        player_index += 0.05
        if player_index >= len(wolf_idle): player_index = 0
        player_surf = wolf_idle[int(player_index)]

    while True:
        screen.blit(background, (0, 0))
        player_animation()
        screen.blit(player_surf, (wolf_x_position, 400))

        key = pygame.key.get_pressed()
        if key[pygame.K_a]:
            ANSWER = True
            wolf_x_position += 1
        else:
            ANSWER = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if flashcard_mode_exitbutton.collidepoint(event.pos):
                    choose_mode()
            if event.type == pygame.KEYDOWN:
                if pygame.key.get_pressed()[pygame.K_SPACE]:
                    card_turned = not card_turned
                elif pygame.key.get_pressed()[pygame.K_RIGHT] and index < len(demo_string_data) - 1:
                    index += 1
                    card_turned = False
                elif pygame.key.get_pressed()[pygame.K_LEFT] and index > 0:
                    index -= 1
                    card_turned = False

        current_question = list(demo_string_data)[index]
        current_answer = list(demo_string_data.values())[index]
        current_question_object = get_font(20).render(current_question, True, "white")
        current_question_rect = current_question_object.get_rect(center=(450, 200))
        current_answer_object = get_font(20).render(current_answer, True, "white")
        current_answer_rect = current_answer_object.get_rect(center=(450, 200))
        current_index_object = get_font(20).render(f"<{index + 1}/{len(demo_string_data)}>", True, "white")
        current_index_rect = current_index_object.get_rect(center=(275, 325))

        if not card_turned:
            pygame.draw.rect(screen, FLASHCARD_COLOUR, (227, 100, 450, 250), 0, 6, 6, 6, 6)
            screen.blit(current_question_object, current_question_rect)
        else:
            pygame.draw.rect(screen, FLIPPED_COLOUR, (227, 100, 450, 250), 0, 6, 6, 6, 6)
            screen.blit(current_answer_object, current_answer_rect)

        return_menu_text = font.render("Exit", True, pygame.Color('white'))
        pygame.draw.rect(screen, pygame.Color('white'), flashcard_mode_exitbutton, 2)
        screen.blit(return_menu_text, (flashcard_mode_exitbutton.x + 50, flashcard_mode_exitbutton.y + 15))
        screen.blit(current_index_object, current_index_rect)
        pygame.display.update()
        
enemy_index = 0
player_index = 0

 # values for correct/wrong answer
correct_counter = 0
prev_correct_counter = 0
incorrect_counter = 0
prev_incorrect_counter = 0
incremant = 1

# ninja idle animation
ninja_idle_1 = pygame.image.load('graphics/ninjaidle1.png')
ninja_idle_2 = pygame.image.load('graphics/ninjaidle2.png')
ninja_idle = [ninja_idle_1, ninja_idle_2]
#enemy_index = 0
enemy = ninja_idle[enemy_index]

# ninja run animation
ninja_run_1 = pygame.image.load('graphics/ninjarun1.png')
ninja_run_2 = pygame.image.load('graphics/ninjarun2.png')
ninja_run_3 = pygame.image.load('graphics/ninjarun3.png')
ninja_run = [ninja_run_1, ninja_run_2, ninja_run_3]
#enemy_index = 0
enemy = ninja_run[enemy_index]

# attack animation
ninja_attack_1 = pygame.image.load('graphics/ninjaattack1.png')
ninja_attack_2 = pygame.image.load('graphics/ninjaattack2.png')
ninja_attack_3 = pygame.image.load('graphics/ninjaattack3.png')
ninja_attack_4 = pygame.image.load('graphics/ninjaattack4.png')
ninja_attack = [ninja_attack_1, ninja_attack_2, ninja_attack_3, ninja_attack_4]
#enemy_index = 0
enemy = ninja_attack[enemy_index]

# enemy down animation
ninja_down_1 = pygame.image.load('graphics/ninjadie1.png')
ninja_down_2 = pygame.image.load('graphics/ninjadie2.png')
ninja_down_3 = pygame.image.load('graphics/ninjadie3.png')
ninja_down = [ninja_down_1, ninja_down_2, ninja_down_3]
#enemy_index = 0
enemy = ninja_down[enemy_index]

# wolf idle animation
wolf_idle_1 = pygame.image.load('graphics/wolfidle1.png')
wolf_idle_2 = pygame.image.load('graphics/wolfidle2.png')
wolf_idle_3 = pygame.image.load('graphics/wolfidle3.png')
wolf_idle_4 = pygame.image.load('graphics/wolfidle4.png')
wolf_idle_5 = pygame.image.load('graphics/wolfidle5.png')
wolf_idle_6 = pygame.image.load('graphics/wolfidle6.png')
wolf_idle_7 = pygame.image.load('graphics/wolfidle7.png')
wolf_idle = [wolf_idle_1, wolf_idle_2, wolf_idle_3, wolf_idle_4, wolf_idle_5, wolf_idle_6, wolf_idle_7]
#player_index = 0
player_surf = wolf_idle[player_index]

# wolf running animation
wolf_run_1 = pygame.image.load('graphics/wolfrun1.png')
wolf_run_2 = pygame.image.load('graphics/wolfrun2.png')
wolf_run_3 = pygame.image.load('graphics/wolfrun3.png')
wolf_run_4 = pygame.image.load('graphics/wolfrun4.png')
wolf_run_5 = pygame.image.load('graphics/wolfrun5.png')
wolf_run_6 = pygame.image.load('graphics/wolfrun6.png')
wolf_run_7 = pygame.image.load('graphics/wolfrun7.png')
wolf_run_8 = pygame.image.load('graphics/wolfrun8.png')
wolf_run = [wolf_run_1, wolf_run_2, wolf_run_3, wolf_run_4, wolf_run_5, wolf_run_6, wolf_run_7, wolf_run_8]
#player_index = 0
player_surf = wolf_run[player_index]
wolf_x_position = 0

# wolf attacking animation
wolf_attack_1 = pygame.image.load('graphics/wolfattack1.png')
wolf_attack_2 = pygame.image.load('graphics/wolfattack2.png')
wolf_attack_3 = pygame.image.load('graphics/wolfattack3.png')
wolf_attack = [wolf_attack_1, wolf_attack_2, wolf_attack_3]
#player_index = 0
player_surf = wolf_run[player_index]

def type_in_mode():
    pygame.init()
    pygame.font.init()

    SCREEN_WIDTH = 900
    SCREEN_HEIGHT = 600

    # values for correct/wrong answer
    correct_counter = 0
    prev_correct_counter = 0
    incorrect_counter = 0
    prev_incorrect_counter = 0
    incremant = 1




    def draw_exit_button():
        #pygame.draw.rect(screen, pygame.Color('red'), exit_button)
        exit_text = exit_button_font.render("Exit", True, pygame.Color('white'))
        text_rect = exit_text.get_rect(center=exit_button.center)
        screen.blit(exit_text, text_rect)
        
    def check_exit_button_click(pos):
        if exit_button.collidepoint(pos):
            pygame.quit()
            menu()

    def get_font(size):
        return pygame.font.Font("graphics/font.otf", size)

    # colours for flashcards
    FLASHCARD_COLOUR = "#2e3856"
    CORRECT_COLOUR = "#00FF00"
    WRONG_COLOUR = "#FF0000"

    # Answer Box
    answer_box = pygame.Rect(275,225,354,75)
    answer_box_font = pygame.font.Font("graphics/font.otf", 13)
    submit_box = pygame.Rect(350,200,100,75)
    submit_box_font = pygame.font.Font("graphics/font.otf", 30)
    color_question = pygame.Color('white')
    active_answerbox = False
    answer_box_value = ''
    exit_button = pygame.Rect(400, 500, 100, 50)
    exit_button_font = pygame.font.Font("graphics/font.otf", 20)

    # retrieving our data
    with open('my_file') as json_file:
        fileData  = json_file.read()
        dictionary_from_file = json.loads(fileData)

    demo_string_data = {}
    temp_dict = {}

    temp_dict[deck_pointer] = dictionary_from_file[deck_pointer]
    demo_string_data = temp_dict[deck_pointer]
        
    # initialising cards
    current_question = ""
    current_answer = ""
    card_turned = False
    game_end = False
    index = 0


    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    background = pygame.image.load('graphics/forest.png')

    # animates the player's avatar
    def player_animation(player_pose): 
        global player_surf, player_index
        # player idle
        if player_pose == 1:
            player_index += 0.05
            if player_index >= len(wolf_idle): player_index = 0
            player_surf = wolf_idle[int(player_index)]
        # player running
        if player_pose == 2:
            player_index += 0.05
            if player_index >= len(wolf_run): player_index = 0
            player_surf = wolf_run[int(player_index)]
        if player_pose == 3:
            player_index += 0.05
            if player_index >= len(wolf_attack): player_index = 0
            player_surf = wolf_attack[int(player_index)]

    def enemy_animation(enemy_pose): 
        global enemy, enemy_index, ninja_idle, ninja_run
        if enemy_pose == 1:
            enemy_index += 0.01
            if enemy_index >= len(ninja_idle): enemy_index = 0
            enemy = ninja_idle[int(enemy_index)]
        if enemy_pose == 2:
            enemy_index += 0.05
            if enemy_index >= len(ninja_run): enemy_index = 0
            enemy = ninja_run[int(enemy_index)]
        if enemy_pose== 3:
            enemy_index += 0.05
            if enemy_index >= len(ninja_attack): enemy_index = 0
            enemy = ninja_attack[int(enemy_index)]
        if enemy_pose == 4:
            enemy_index += 0.05
            if enemy_index >= len(ninja_down): enemy_index = 0
            enemy = ninja_down[int(enemy_index)]

    #global index, current_question, current_answer, card_turned, active_answerbox, answer_box_value, prev_correct_counter, incremant, prev_incorrect_counter, game_end
    wolf_x_position = 0
    enemy_x_position = 750
    enemy_pose = 1
    player_pose = 1
    font = pygame.font.Font("graphics/font.otf", 13)

    while True:

        for event in pygame.event.get():
                
                
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                exit()

            if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        answer_box_value = answer_box_value[:-1]
                    else:
                        answer_box_value += event.unicode

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                        pos = pygame.mouse.get_pos()
                        check_exit_button_click(pos)            
            
            if event.type == pygame.KEYDOWN:
                if pygame.key.get_pressed()[pygame.K_RETURN]:
                    card_turned = not card_turned
                    if str(answer_box_value.strip()) in current_answer.split('/'):
                        correct_counter += 1
                    else:
                        incorrect_counter += 1
                elif pygame.key.get_pressed()[pygame.K_RIGHT] and index < len(demo_string_data) - 1:
                    index += 1
                    card_turned = False
                    player_pose = 1
                    answer_box_value = ''
                    enemy_x_position = 750
                    enemy_pose = 1
                elif pygame.key.get_pressed()[pygame.K_LEFT] and index > 0:
                    index -= 1
                    card_turned = False
                elif pygame.key.get_pressed()[pygame.K_RIGHT] and (index+1) == len(demo_string_data):
                    game_end = True

        print(correct_counter)
        print(incorrect_counter)
        step = ((SCREEN_WIDTH-200)/math.ceil(((len(demo_string_data)) * 0.7))) # Pass around 70% of the flashcards
        
        # wolf walking forward every right answer
        if correct_counter > prev_correct_counter:
            player_pose = 2
            if wolf_x_position < (step*incremant): 
                wolf_x_position += 1
            if wolf_x_position == (step*incremant):
                player_pose = 1
                prev_correct_counter = correct_counter
                incremant += 1
            
        # enemy attacking every wrong answer
        if incorrect_counter > prev_incorrect_counter:
            enemy_pose = 2
            if enemy_x_position > (wolf_x_position+100):
                enemy_x_position -= 1
            if enemy_x_position == (wolf_x_position+100):
                enemy_pose = 3
                prev_incorrect_counter = incorrect_counter

        screen.blit(background, (0, 0))
        player_animation(player_pose)
        enemy_animation(enemy_pose)
        screen.blit(enemy, (enemy_x_position, 400))
        screen.blit(player_surf, (wolf_x_position, 400))

        current_question = list(demo_string_data)[index]
        current_answer = list(demo_string_data.values())[index]
        current_question_object = get_font(20).render(current_question, True, "white")
        current_question_rect = current_question_object.get_rect(center=(450, 150))
        current_answer_object = get_font(20).render(current_answer, True, "white")
        current_answer_rect = current_answer_object.get_rect(center=(450, 150))
        current_index_object = get_font(20).render(f"<{index + 1}/{len(demo_string_data)}>", True, "white")
        current_index_rect = current_index_object.get_rect(center=(275, 325))
        submit_box_object = get_font(20).render(current_question, True, "white")

        if not card_turned:
            pygame.draw.rect(screen, FLASHCARD_COLOUR, (227, 100, 450, 250), 0, 6, 6, 6, 6)
            screen.blit(current_question_object, current_question_rect)
        else:
            if str(answer_box_value.strip()) in current_answer.split('/'):
                pygame.draw.rect(screen, CORRECT_COLOUR, (227, 100, 450, 250), 0, 6, 6, 6, 6)
                screen.blit(current_answer_object, current_answer_rect)
            else:
                pygame.draw.rect(screen, WRONG_COLOUR, (227, 100, 450, 250), 0, 6, 6, 6, 6)
                screen.blit(current_answer_object, current_answer_rect)

        # checking if player reaches the end
        if game_end:  
            pygame.draw.rect(screen, 'white', (227, 100, 450, 250), 0, 6, 6, 6, 6)
            screen.blit(current_question_object, current_question_rect)
            if wolf_x_position < 690:
                you_lost_message = (pygame.font.Font("graphics/font.otf", 30)).render("YOU LOSE! :(", True, pygame.Color('red'))
                screen.blit(you_lost_message, (350, 220))
                draw_exit_button()
            if wolf_x_position > 690:
                enemy_pose = 4
                player_pose = 3
                you_win_message = (pygame.font.Font("graphics/font.otf", 30)).render("YOU WIN! :)", True, pygame.Color('green'))
                screen.blit(you_win_message, (350, 220))
                draw_exit_button()

        screen.blit(current_index_object, current_index_rect)
            
        # Render and display the answer box
        moving_keys_message = font.render("Use arrow keys to move cards", True, pygame.Color('white'))
        screen.blit(moving_keys_message, (315, 317))
        answertotypein = answer_box_font.render("Type your answer (Press 'Enter' to submit):", True, pygame.Color('white'))
        screen.blit(answertotypein, (answer_box.x, answer_box.y - 35))
        pygame.draw.rect(screen, color_question, answer_box, 2)
        test_value = answer_box_font.render(answer_box_value, True, 'white')
        screen.blit(test_value, (answer_box.x + 5, answer_box.y + 5))

        pygame.display.update()
                
def choose_mode():
    SCREEN_WIDTH = 900
    SCREEN_HEIGHT = 600
    background_image = pygame.image.load('graphics/background-main.png')
    background_scaled = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Choose Mode')
    big_box = pygame.Rect(165, 100, 600, 400)
    font = pygame.font.Font("graphics/font.otf", 20)
    button_flashcard = pygame.Rect(250, 200, 400, 50)
    button_typein = pygame.Rect(250, 275, 400, 50)
    button_edit = pygame.Rect(250, 350, 400, 50)
    choose_mode_exitbutton = pygame.Rect(500, 425, 150, 50)
    clock = pygame.time.Clock()
    screen.blit(background_scaled, (0, 0))

    # Main game loop
    while True:
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                pygame.quit()
                quit()
            if events.type == pygame.MOUSEBUTTONDOWN:
                if button_flashcard.collidepoint(events.pos):
                    flashcard_mode()  # Call flashcard_mode function
                elif button_typein.collidepoint(events.pos):
                    type_in_mode()  # Call type_in_mode function
                elif button_edit.collidepoint(events.pos):
                        edit_card()
                elif choose_mode_exitbutton.collidepoint(events.pos):
                    menu()

        pygame.draw.rect(screen, "#668C8E", big_box)
        font_2 = pygame.font.Font("graphics/font.otf", 30)
        title_surf = font_2.render("Choose Mode", True, pygame.Color('white'))
        screen.blit(title_surf, (SCREEN_WIDTH // 2 - title_surf.get_width() // 2, 140))
        
        #Button for Flashcard Mode 
        flashcard_text = font.render("Flashcard Mode", True, pygame.Color('white'))
        pygame.draw.rect(screen, pygame.Color('white'), button_flashcard, 2)
        screen.blit(flashcard_text, (button_flashcard.x + 25, button_flashcard.y + 10))

        #Button for Type In Mode 
        typein_text = font.render("Type In Mode", True, pygame.Color('white'))
        pygame.draw.rect(screen, pygame.Color('white'), button_typein, 2)
        screen.blit(typein_text, (button_typein.x + 25, button_typein.y + 10))
        
        #Button for Edit Mode 
        edit_text = font.render("Edit Mode", True, pygame.Color('white'))
        pygame.draw.rect(screen, pygame.Color('white'), button_edit, 2)
        screen.blit(edit_text, (button_edit.x + 25, button_edit.y + 10))

        #Button for Exit 
        return_menu_text = font.render("Exit", True, pygame.Color('white'))
        pygame.draw.rect(screen, pygame.Color('white'), choose_mode_exitbutton, 2)
        screen.blit(return_menu_text, (choose_mode_exitbutton.x + 10, choose_mode_exitbutton.y + 10))



        pygame.display.update()
        clock.tick(50)


def edit_card():

    global wolf_x_position, ANSWER, index, current_question, current_answer, card_turned

    pygame.init()
    pygame.font.init()

    SCREEN_WIDTH = 900
    SCREEN_HEIGHT = 600
    ANSWER = False

    # colours for flashcards
    FLASHCARD_COLOUR = "#2e3856"
    FLIPPED_COLOUR = "#595e6d"

    #sample data fo
    with open('my_file') as json_file:
        fileData  = json_file.read()
        dictionary_from_file = json.loads(fileData)

    demo_string_data = {}
    temp_dict = {}

    temp_dict[deck_pointer] = dictionary_from_file[deck_pointer]
    demo_string_data = temp_dict[deck_pointer]
        
    # initialising cards
    current_question = ""
    current_answer = ""
    card_turned = False
    index = 0


    # font
    def get_font(size):
        return pygame.font.Font("graphics/font.otf", size)


    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    background = pygame.image.load('graphics/forest.png')


    def load_question_and_ans(q, a):
        type_q = q
        type_a = a
        return type_q, type_a

    def append_record(record):
        with open('my_file', 'w') as f:
            json.dump(record, f)
            f.write(os.linesep)


    def build_dict(keys, values):
        res = dict(map(lambda i,j : (i,j) , keys,values))
        return res

    # load first card in deck
    current_question = list(demo_string_data)[index]
    current_answer = list(demo_string_data.values())[index]
    type_question, type_answer = load_question_and_ans(current_question, current_answer)

    
    demo_keys = list(demo_string_data.keys())
    demo_values = list(demo_string_data.values())

    while True:
        screen.blit(background, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                edited_deck = build_dict(demo_keys, demo_values)
                dictionary_from_file[deck_pointer] = edited_deck
                append_record(dictionary_from_file)
                run = False
                pygame.quit()
                exit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if submit_edited_deck_rect.collidepoint(event.pos):
                    edited_deck = build_dict(demo_keys, demo_values)
                    dictionary_from_file[deck_pointer] = edited_deck
                    append_record(dictionary_from_file)
                    menu()

            if event.type == pygame.KEYDOWN:
                if pygame.key.get_pressed()[pygame.K_RETURN]:
                    card_turned = not card_turned
                elif pygame.key.get_pressed()[pygame.K_RIGHT] and index < len(demo_string_data) - 1:
                    demo_keys[index] = type_question
                    demo_values[index] = type_answer

                    index += 1

                    current_question = demo_keys[index]
                    current_answer = demo_values[index]
                    type_question, type_answer = load_question_and_ans(current_question, current_answer)
                    card_turned = False

                elif pygame.key.get_pressed()[pygame.K_LEFT] and index > 0:

                    demo_keys[index] = type_question
                    demo_values[index] = type_answer
                    index -= 1
                    current_question = demo_keys[index]
                    current_answer = demo_values[index]
                    type_question, type_answer = load_question_and_ans(current_question, current_answer)
                    card_turned = False

                if not card_turned:
                    if event.key == pygame.K_BACKSPACE:
                        type_question = type_question[:-1]
                    else:
                        type_question += event.unicode
                    
                else:
                    if event.key == pygame.K_BACKSPACE:
                        type_answer = type_answer[:-1]
                    else:
                        type_answer += event.unicode


        current_question_object = get_font(20).render(type_question, True, "white")
        current_question_rect = current_question_object.get_rect(center=(450, 200))
        current_answer_object = get_font(20).render(type_answer, True, "white")
        current_answer_rect = current_answer_object.get_rect(center=(450, 200))
        current_index_object = get_font(20).render(f"{index + 1}/{len(demo_string_data)}", True, "white")
        current_index_rect = current_index_object.get_rect(center=(275, 325))
        submit_edited_deck_object = get_font(15).render("Save & Exit", True, "white")
        submit_edited_deck_rect = submit_edited_deck_object.get_rect(center=(700, 500))
        

        if not card_turned:
            pygame.draw.rect(screen, FLASHCARD_COLOUR, (227, 100, 450, 250), 0, 6, 6, 6, 6)
            screen.blit(current_question_object, current_question_rect)
        else:
            pygame.draw.rect(screen, FLIPPED_COLOUR, (227, 100, 450, 250), 0, 6, 6, 6, 6)
            screen.blit(current_answer_object, current_answer_rect)

        screen.blit(current_index_object, current_index_rect)
        screen.blit(submit_edited_deck_object, submit_edited_deck_rect)

        pygame.display.update()
        
             

       
menu()

