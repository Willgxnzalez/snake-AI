import pygame as pg
from pygame.math import Vector2

class Node:
    NODE_SIZE = 25
    def __init__(self, node_x, node_y, dir=(0,0)):
        self.rect = pg.Rect(node_x * self.NODE_SIZE, node_y * self.NODE_SIZE, self.NODE_SIZE, self.NODE_SIZE)
        self.dir = dir  # cannot be (0,0) if snake initalizes with more than just head node

class Fruit(Node):
    def __init__(self, x, y):
        super().__init__(x, y)

    def draw(self, surface, color):
        pg.draw.rect(surface, color, self.rect)

class Snake:
    turns = {}
    def __init__(self, start_x, start_y):
        self.head = Node(start_x, start_y)
        self.body = [self.head]

    def move(self,keys):
        head_pos = (self.head.rect.x, self.head.rect.y)

        if keys[pg.K_w]:
            self.turns[head_pos] = (0,-1)
        if keys[pg.K_a]:
            self.turns[head_pos] = (-1,0)
        if keys[pg.K_s]:
            self.turns[head_pos] = (0, 1)
        if keys[pg.K_d]:
            self.turns[head_pos] = (1, 0)

        for node in self.body:
            pos = (node.rect.x, node.rect.y)
            if pos in self.turns:
                if node != self.body[-1]: #if node is not the tail of snake
                    node.dir = self.turns[pos]
                else:
                    node.dir = self.turns.pop(pos)
        
            node.rect.x += (node.dir[0] * node.NODE_SIZE)
            node.rect.y += (node.dir[1] * node.NODE_SIZE)
    
    def screen_wrap(self, width, height):
        for node in self.body:
            if node.rect.left < 0:
                node.rect.x = width - node.NODE_SIZE
            if node.rect.right > width:
                node.rect.x = 0
            if node.rect.top < 0:
                node.rect.y = height - node.NODE_SIZE
            if node.rect.bottom > height:
                node.rect.y = 0
        
    def draw(self, surface, color):
        for node in self.body:
            pg.draw.rect(surface, color, node.rect)
    
    
        