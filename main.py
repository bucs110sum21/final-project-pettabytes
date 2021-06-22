#import your controller
import pygame

def main():
    #Create an instance on your controller object
    pygame.init()
    team = {"lead": "Dennis Shin", "backend": "Ryan Levine", "frontend": "Eyal Hakimi"}
    print("Software Lead is: ", team["lead"])
    print("Backend is:", team["backend"])
    print("Frontend is:", team["frontend"])
main()
