import pygame
from sympy import *
from random import *
from functools import reduce

# hardcoded in. Could later add a difficulty method that would alter this
NUM_OF_FUNCTIONS = 2

pygame.init()

def product_rule():
    """ Returns a tuple containing the a function (composed fo functions multiplied together, depending on the difficulty level)
    and the derivative with respect to x
    """
    functions = []
    for i in range(NUM_OF_FUNCTIONS):
        # randomises whether the function or its reciprocal is used
        if randint(1,2) == 1:
            functions.append(choice(FUNCTIONS))
        else:
            functions.append((choice(FUNCTIONS))**(-1))
    # multiply the generated functions together 
    product = reduce(Mul, functions)
    ans = diff(product, x)
    return simplify(product), simplify(ans)


def composite_rule():
    """ Returns a tuple containing the composition of a number of functions (eg f(g(h(x))) determined by the difficulty set, 
    and the derivative with respect to x
    """
    function = choice(FUNCTIONS)
    if NUM_OF_FUNCTIONS == 1:
        function = choice(FUNCTIONS)
    else: 
        for _i in range(NUM_OF_FUNCTIONS - 1):
            function = function.subs(x,choice(FUNCTIONS)) 
    ans = diff(function, x)
    return simplify(function), simplify(ans)



def random_function():
    """ Returns a random function (either generatede)"""
    j = randint(1,2)
    if j == 1:
        return simplify(product_rule())
    if j == 2:
        return simplify(composite_rule())
    
# screen size
WIDTH = 900
HEIGHT = 600
COLOUR = "#ffebcd"

# generating some random values
x = symbols('x')
score = 0
incorrect = 0
N = randint(1,NUM_OF_FUNCTIONS*2)
a = randint(1,NUM_OF_FUNCTIONS*2)
b = randint(1,NUM_OF_FUNCTIONS*2)
FUNCTIONS = [sin(x), cos(x), tan(x), x, pow(x,N), log(x), sec(x), cot(x), csc(x), sqrt(x), pow(x,a), x + a]

# generating the screen
background = pygame.image.load("graphics/background-main.png")     # image from https://saurabhkgp.itch.io/pixel-art-forest-background-simple-seamless-parallax-ready-for-2d-platformer-s 5/4/24
background_scaled = pygame.transform.scale(background, (WIDTH, HEIGHT))

screen = pygame.display.set_mode((WIDTH, HEIGHT))

# generating fonts for display 
game_text = pygame.font.SysFont("Arial", 40)
game_text2 = pygame.font.SysFont("Arial", 30)
game_text3 = pygame.font.SysFont("Arial", 30)


i = 0 # tracks the movement of the character and the scrolling of the screen
counter = 0
points = 0   # correct points 
incorrect_counter = 0
TOTAL_LIVES = 5
WIDTH = screen.get_width()
CENTRE = 230
LEFT = 30
LIVES_COORDS = (LEFT,10)
DELAY = 200    

# wolf running animation from https://craftpix.net/freebies/free-werewolf-sprite-sheets-pixel-art/
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

run = True
clock = pygame.time.Clock()

# while application is loaded
while run:
        function_generated = random_function()
        q_text, ans_text = str(function_generated[0]), str(function_generated[1])
        q_text = f'Differentiate {q_text} with respect to x.'
        q_instruction = "Press 1, 2 or 3 to enter your answer, and escape to quit."
        false_1_text = str(random_function()[1])
        false_2_text = str(random_function()[1])

        # no doubles
        while ans_text == false_1_text or ans_text == false_2_text:
             false_1_text = str(random_function()[1])
             false_2_text = str(random_function()[1])
        q_disp = pygame.font.SysFont("Arial", 50)

       
        # randomly ordering the answers 
        answer_num = randint(1,3)
        if answer_num == 1:
             answers_list = [ans_text, false_1_text, false_2_text]
        elif answer_num == 2:
             answers_list = [false_1_text, ans_text, false_2_text]
        else:
             answers_list = [false_1_text, false_2_text, ans_text] 

        # creating surfaces from text that can be displayed
        q_disp = game_text.render(q_text, True, (0, 0, 0))
        q_instruction = game_text.render(q_instruction, True, (0, 0, 0))
        a1_disp = game_text2.render("1: " + answers_list[0], True, (0, 0, 0))
        a2_disp = game_text2.render("2: " + answers_list[1], True, (0, 0, 0))
        a3_disp = game_text2.render("3: " + answers_list[2], True, (0, 0, 0))
        lives_disp = game_text3.render(f"{TOTAL_LIVES - incorrect_counter} lives remaining", True, (0, 0, 0))
        
        lives_box = pygame.Surface((250, 35))
        pygame.surface.Surface.fill(lives_box, "#add8e6")      
        
        
        question = True
        # while you are on a set question 
        while question:
                # displaying q and a on screen until an answer is given
                clock.tick(60)
                q_box = pygame.Surface((WIDTH-20, 340))
                pygame.surface.Surface.fill(q_box, "#add8e6")                
                screen.blits([(background_scaled, ((-i)%(2*WIDTH)-WIDTH,0)),
                              (background_scaled, ((-i-WIDTH)%(2*WIDTH)-WIDTH,0)),
                              (wolf_run[(i)%8], (350, 360)),
                              (q_box, (LEFT-20, 90)),
                              (q_disp, (LEFT, 100)),
                              (q_instruction, (LEFT, 145)),(a1_disp, (LEFT, 250)),
                              (a2_disp, (LEFT, 300)), (a3_disp, (LEFT, 350)),
                              (lives_box, (LIVES_COORDS)),
                              (lives_disp, (LIVES_COORDS))])
                pygame.display.update()

                # display animation when answer is correct, and increase correct score counter
                def correct_ans():
                    global points
                    points += 1
                    global i
                    counter = 0

                    # create boxes and text 
                    correct_ans_box = pygame.Surface((710, 100))
                    pygame.surface.Surface.fill(correct_ans_box, "#90EE90")
                    game_text_4 = pygame.font.SysFont("Arial", 100)
                    correct_ans_text = game_text_4.render("You are correct!", True, (COLOUR))
                    text_centre = correct_ans_text.get_rect(center = (900/2, 600/2))          #https://stackoverflow.com/questions/23982907/how-to-center-text-in-pygame
                   
                    while counter < 40:
                        clock.tick(20)
                        i += 2
                        screen.blits([(background_scaled, ((-i)%(2*WIDTH)-WIDTH,0)),
                              (background_scaled, ((-i-WIDTH)%(2*WIDTH)-WIDTH,0)),
                              (wolf_run[(i)%8], (350, 360)), (correct_ans_box, (text_centre)),
                              (lives_box, (LIVES_COORDS)),
                              (lives_disp, (LIVES_COORDS)),(correct_ans_text, (text_centre))])
                        pygame.display.update()
                        counter += 1

                # display animation for incorrect answer and update lives counter
                def incorrect_ans(answer_num):
                    global incorrect_counter
                    incorrect_counter += 1
                    global points
                    points += 1
                    global i
                    counter = 0

                    # create incorrect answer information 
                    incorrect_ans_box = pygame.Surface((880, 80))
                    pygame.surface.Surface.fill(incorrect_ans_box, "#ff3333")
                    game_text_5 = pygame.font.SysFont("Arial", 60)
                    incorrect_ans_text = game_text_5.render(f"You are incorrect (answer was {answer_num})", True, COLOUR)
                    text_centre = incorrect_ans_text.get_rect(center = (900/2, 600/2))          #https://stackoverflow.com/questions/23982907/how-to-center-text-in-pygame

                    while counter < 40:
                        clock.tick(20)
                        screen.blits([(background_scaled, ((-i)%(2*WIDTH)-WIDTH,0)),
                              (background_scaled, ((-i-WIDTH)%(2*WIDTH)-WIDTH,0)),
                              (wolf_run[(i)%8], (350, 360)),
                              (incorrect_ans_box, (text_centre)),
                              (lives_box, (LIVES_COORDS)),
                              (lives_disp, (LIVES_COORDS)),(incorrect_ans_text, (text_centre)),
                              ])
                        pygame.display.update()
                        counter += 1
                     
                
                # detecting keyboard input 
                key_states = pygame.key.get_pressed()
                if key_states[pygame.K_1]:
                        if answer_num == 1:
                             correct_ans()
                        else:
                             incorrect_ans(answer_num)
                        question = False
                        pygame.time.delay(DELAY)
                if key_states[pygame.K_2]:
                        if answer_num == 2:
                             correct_ans()
                        else:
                             incorrect_ans(answer_num)
                        question = False
                        pygame.time.delay(DELAY)
                if key_states[pygame.K_3]:
                        if answer_num == 3:
                             correct_ans()
                        else:
                             incorrect_ans(answer_num)
                        question = False
                        pygame.time.delay(DELAY)
                if key_states[pygame.K_ESCAPE]:
                        with open("forestudy.py") as file:
                             exec(file.read())
                pygame.event.pump()   # needed to handle events 
                
                # if the player runs out of lives 
                if incorrect_counter == TOTAL_LIVES:
                     lose_box = pygame.Surface((450, 80))
                     pygame.surface.Surface.fill(lose_box, "#add8e6")
                     game_text_4 = pygame.font.SysFont("Arial", 30)
                     you_lose = game_text_4.render("You lose! Press escape to leave.", True, (COLOUR))
                     text_centre = you_lose.get_rect(center = (900/2, 600/2))          #https://stackoverflow.com/questions/23982907/how-to-center-text-in-pygame  

                     # display losing screen until escape is pressed
                     counter = 0
                     while True:
                        clock.tick(20)
                        screen.blits([(background_scaled, ((-i)%(2*WIDTH)-WIDTH,0)),
                              (background_scaled, ((-i-WIDTH)%(2*WIDTH)-WIDTH,0)),
                              (wolf_run[(i)%8], (350, 360)), (lose_box, text_centre),
                              (you_lose, text_centre)])
                        pygame.display.update()
                        pygame.event.pump()
                        key_states = pygame.key.get_pressed()
                        if key_states[pygame.K_ESCAPE]:
                            with open("forestudy.py") as file:
                                exec(file.read())
                        
                        


