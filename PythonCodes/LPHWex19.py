#Function and variable
def movie(genre1, name, nominations, award):
    print(f".... and the award for best {genre1} goes to {name} its the {award}th award and {nominations}th nomination")

#now getting user input for passing parameters in the funtion movie
print("enter the genre of the movie ")
genre = input(">>>")
print("enter the name of the movie")
name = input(">>>")
print("enter the numberof nominations")
nominations = input(">>>")
print("Enter te number of awards")
award = input(">>>")

movie(genre,name,nominations,award)

# bassicaly passing user input as argumnets for the functions.