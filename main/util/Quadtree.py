import pygame


class Quadtree:

    def __init__(self, x, y, w, h):
        self.rect = pygame.Rect(x, y, w, h)
        self.NE = None
        self.NW = None
        self.SE = None
        self.SW = None
        self.blocks = []
        self.cap = 4
        self.is_divided = False

    def insert(self, block):

        if self.rect.colliderect(block.rect):

            if not self.is_divided:

                if len(self.blocks) < self.cap:

                    self.blocks.append(block)

                else:

                    self.subdivide()

            else:

                self.NE.insert(block)
                self.NW.insert(block)
                self.SE.insert(block)
                self.SW.insert(block)

    def subdivide(self):
        self.NE = Quadtree(self.rect.x + self.rect.w/2, self.rect.y, self.rect.w/2, self.rect.h/2)
        self.NW = Quadtree(self.rect.x, self.rect.y, self.rect.w/2, self.rect.h/2)
        self.SE = Quadtree(self.rect.x + self.rect.w/2, self.rect.y + self.rect.h/2, self.rect.w/2, self.rect.h/2)
        self.SW = Quadtree(self.rect.x, self.rect.y + self.rect.w/2, self.rect.w/2, self.rect.h/2)

        for block in self.blocks:
            self.NE.insert(block)
            self.NW.insert(block)
            self.SE.insert(block)
            self.SW.insert(block)

        self.blocks = []

    def query(self, rect):

        found = []

        if self.rect.colliderect(rect):
            if self.is_divided:
                found.append(self.NE.query(rect))
                found.append(self.NW.query(rect))
                found.append(self.SE.query(rect))
                found.append(self.SW.query(rect))
            else:
                for block in self.blocks:
                    if block.rect.colliderect(rect):
                        found.append(block)
        return found
