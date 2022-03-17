
class Movie:
    def __init__(self,movieName=None,noOfTickets=0,totalCost=0) -> None:
        self.movieName  = movieName
        self.noOfTickets = noOfTickets
        self.totalCost = totalCost
    
    def __repr__(self) -> str:
       return "Movie : {}\nNumber of Tickets : {}\nTotal Cost : {}".format(self.movieName,self.noOfTickets,self.totalCost)

if __name__ == "__main__":
    name = input()
    n = int(input().strip())
    cost = int(input().strip())
    
    p1 = Movie(name,n,cost)
    print(p1)
        