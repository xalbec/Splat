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

    # Adds objects to the quadtree
    def insert(self, block):

        # Only consider inserting it if it is even in the view of the quadtree
        if self.rect.colliderect(block.rect):

            # If the branch is not divided
            if not self.is_divided:

                # If there is still room for another object add it
                if len(self.objects) < self.cap:

                    self.objects.append(block)
                # Otherwise just subdivide
                else:

                    self.subdivide()
            # If it is divided then you need to try to add it to the subbranches
            else:

                self.NE.insert(block)
                self.NW.insert(block)
                self.SE.insert(block)
                self.SW.insert(block)

    # Splits the tree into 4 smaller trees
    def subdivide(self):
        self.NE = Quadtree(self.rect.x + self.rect.w/2, self.rect.y, self.rect.w/2, self.rect.h/2)
        self.NW = Quadtree(self.rect.x, self.rect.y, self.rect.w/2, self.rect.h/2)
        self.SE = Quadtree(self.rect.x + self.rect.w/2, self.rect.y + self.rect.h/2, self.rect.w/2, self.rect.h/2)
        self.SW = Quadtree(self.rect.x, self.rect.y + self.rect.w/2, self.rect.w/2, self.rect.h/2)

        # Take the objects from the outer branch and give it to its subbranches
        for obj in self.objects:
            self.NE.insert(obj)
            self.NW.insert(obj)
            self.SE.insert(obj)
            self.SW.insert(obj)

        # clear the outer branches memory
        self.objects = []

    # Returns the list of objects that are within the given rect
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

    def render(self, screen):
        pygame.draw.rect(screen, [255, 255, 255], self.rect)
        if self.is_divided:
            self.NE.render(screen)
            self.NW.render(screen)
            self.SE.render(screen)
            self.SW.render(screen)
