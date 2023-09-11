import sys
import pygame as pg
from snake import Snake, Fruit, Node
import random
import pathlib

print(pathlib.PureWindowsPath())

pg.init()
pg.font.init()

WIDTH, HEIGHT = 525, 525
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Snake")

FPS = 10
CLOCK = pg.time.Clock()
COLORS = {"murasaki":(79, 40, 75), "white":(255,255,255), "magenta":(100, 40, 75), "pink": (255, 0, 127), "blue":(152,218,242)}

EXTEND = pg.USEREVENT + 1



def font(size):
    return pg.font.SysFont("impact", size)

def draw_background(surface):
    surface.fill(COLORS["murasaki"])
    for pos in range(0, WIDTH, 25):
        pg.draw.line(surface, COLORS["magenta"], (pos,0), (pos, HEIGHT))
        pg.draw.line(surface, COLORS["magenta"], (0,pos), (WIDTH, pos))

def generate_fruit():
    return Fruit(random.randint(0,20), random.randint(0,20))

def collision_between(rect1, rect2):
    return rect1.colliderect(rect2)

def show_score(surface, score):
    score_font = font(40).render(str(score), 1, COLORS["white"])
    surface.blit(score_font, (WIDTH//2 - (score_font.get_width()//2), 10))

def gameover(surface, score):

    gameover_text = font(100).render("GAMEOVER", 1, COLORS["white"])
    final_score_text = font(50).render("score: " + str(score), 1, COLORS["white"])
    surface.blit(gameover_text, (WIDTH//2 -(gameover_text.get_width()//2) , HEIGHT//2 - (gameover_text.get_height())))
    surface.blit(final_score_text, (WIDTH//2 -(final_score_text.get_width()//2) , HEIGHT//2))
    pg.display.update()
    pg.time.delay(1200)


def main():
    snake = Snake(10,10)
    fruit = generate_fruit()
    score = 0

    while True:
        pg.time.delay(50)
        CLOCK.tick(FPS)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return

            if event.type == EXTEND:
                score += 1
                fruit = generate_fruit()
                tail = snake.body[-1]
                new_x = (tail.rect.x //25) - tail.dir[0]
                new_y = (tail.rect.y //25) - tail.dir[1]
                snake.body.append(Node(new_x, new_y, (tail.dir[0], tail.dir[1])))

        draw_background(screen)

        if collision_between(snake.head.rect, fruit.rect):
            pg.event.post(pg.event.Event(EXTEND))

        for node in snake.body[1:]:
            if collision_between(snake.head.rect, node.rect):
                gameover(screen, score)
                return
            
        snake.move(pg.key.get_pressed())
        snake.screen_wrap(WIDTH, HEIGHT)

        fruit.draw(screen, COLORS["pink"])
        snake.draw(screen, COLORS["blue"])

        show_score(screen, score)

        pg.display.update()
    
if __name__ == "__main__":
    main()
    pg.quit()
    sys.exit()
        
