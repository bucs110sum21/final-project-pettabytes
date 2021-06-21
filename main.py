#import your controller
import pygame

def main():
    #Create an instance on your controller object
    pygame.init()
    team = {"lead": "?", "backend": "Ryan Levine", "frontend": "?"}
    print("Software Lead is: ", team["lead"])
    print("Backend is:", team["backend"])
    print("Frontend is:", team["frontend"])
main()
