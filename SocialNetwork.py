#import libraries
import turtle
import math

#create class to create the user
class User:
    #set initial attributes
    def __init__(self, name, userID):
        self.username = username
        self.userID = userID
        self.connections = []

    #add another user's ID number to one's connection list
    def addConnections(self, connectionID):
        self.connections.append(connectionID)
        #connectionID == userID

    def getUserName(self):
        return self.username

    def getUserID(self):
        return self.userID

    def getConnection(self):
        return self.connections

#create a network class
class Network:
    def __init__(self):
        self.users = []

    #find the length of the list of connections
    def numUsers(self):
        return len(self.users)
    #creating a new username to the Network
    def addUsers(self, username):
        for user in self.users:
            #if username is already taken
            if username == user.getUserName():
                print("already taken")
                return
        #if user is not in Network --> create the new user
        userID = len(self.users)
        #add new user to the network
        self.users.append(User(username, userID))

    #get user id from user class from getUserID function
    def getUserID(self, username):
        #the username is not existant because there is nothing in the list
        userID = -1
        for user in self.users:
            if username == user.getUserName():
                userID = user.getUserID()
            return userID
    #add connections
    def addConnections(self, user1, user2):
        #creating 2 user variables that get the user id
        user1_id = self.getUserID(user1)
        user2_id = self.getUserID(user2)
        #declaring that the user is equal to its user id in the self.users list
        user1 = self.users[user1_id]
        user2 = self.users[user2_id]
        #username that you are trying to add is not existant
        if user1_id == -1 or user2_id == -1:
            print("Sorry, one or more username is not correct. Try again.")
            return False
        #user is trying to add itself as a connection/friend
        elif user1_id == user2_id:
            print("sorry, connections must be between two different users. Try again.")
            return False
        #users are already connected/friends
        elif user2_id in user1.getConnections():
            print("{} and {} are already connected!".format(user1.getUserName(), user2.getUserName()))
            return True
        #connect the two users
        else:
            self.users[user1_id].addConnection(user2_id)
            self.users[user2_id].addConnection(user1_id)
            return True
        #print all users in network
        def printUsers(self):
            print("Network Users: ")
            for user in self.users:
                print("\tUser {}: {}".format(user.getUserID(0, user.getUserName()))

        def printConnections(self, username):
            user = self.users[self.getUserID(username)]
            connections = user.getConnections()
            print("{}'s connections:".format(user.getUserName()))
            for friendID in connections:
                friend = self.users[friendID]
                print("\t{}".format(friend.getUserName()))


def main():
    mynetwork = Network()
    done = False
    while not done:
        action = input("""\nWhat would you like to do?
            Add a user (u), print users (p),
            add connection (c), print connections (pc),
            quit (q)?
            """)

        if action == "p":
            mynetwork.printUsers()
        elif action == "u":
            username = input("What username? ")
            mynetwork.addUser(username)
        elif action == "pc":
            user = input("For which user? ")
            mynetwork.printConnections(user)
        elif action == "c":
            if mynetwork.numUsers() < 2:
                print("You need at least two users to make a connection.")
                continue
            user1 = input("First username: ")
            user2 = input("Second username: ")
            mynetwork.addConnection(user1, user2)
        elif action == "q":
            print("Sorry to see you go so soon!")
            break
        else:
            print("Sorry, I didn't understand that.")

if __name__ == '__main__':
    main()
