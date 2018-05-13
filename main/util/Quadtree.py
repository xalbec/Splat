import pygame


class Quadtree:

    def __init__(self, x, y, w, h):
        self.rect = pygame.Rect(x, y, w, h)
        self.NE = None
        self.NW = None
        self.SE = None
        self.SW = None
        self.objects = []
        self.cap = 4
        self.is_divided = False

    def insert(self, block):

        if self.rect.colliderect(block.rect):

            if not self.is_divided:

                if len(self.objects) < self.cap:

                    self.objects.append(block)

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

        for obj in self.objects:
            self.NE.insert(obj)
            self.NW.insert(obj)
            self.SE.insert(obj)
            self.SW.insert(obj)

        self.objects = []

    def query(self, rect):

        found = []

        if self.rect.colliderect(rect):
            if self.is_divided:
                found.append(self.NE.query(rect))
                found.append(self.NW.query(rect))
                found.append(self.SE.query(rect))
                found.append(self.SW.query(rect))
            else:
                for obj in self.objects:
                    if obj.rect.colliderect(rect):
                        found.append(obj)
        return found
