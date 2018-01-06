import os
import sys
import json

class Movie:
    id=0
    name=" "
    year=0
    seats=0
    #time=[0,0] #Tof the movie, represented in array, hour[0]= hour and hour[1]= minutes ex: h[0]=14 hour[1]=32 (14:32)

    def __init__(self, id, name, year):
        self.id=id
        self.name=name
        self.year=year
        self.seats=100

    def listMovie(self):
        return str(self.id) +". " + self.name


def listDeff():
    movie1 = Movie(1, "Fred", "2017")
    movie2 = Movie(2, "Chicken", "2016")
    movie3 = Movie(3, "Steve", "2015")
    movie4 = Movie(4, "Anna", "2014")
    movie5 = Movie(5, "Bell", "2013")
    ls = [movie1, movie2, movie3, movie4, movie5]


def halp():
    print("l) List Movies/List Details")
    print("r) Reserve Selected Movie")
    print("h) List MyReserves")
    print("\n")
    print("?) Prints this menu")
    menu()

def menu():
    cmd = input("Select Action >  ")
    print("\n")

    if cmd == "l":
        print("Se listeaza filmele: \n")

    elif cmd == "r":
        print("Coming Soon\n")
    elif cmd == "?":
        halp()

    menu()

def main():
    halp()




    #JSONMovies=open("movies.json","r+")


if __name__ == '__main__':
    main()