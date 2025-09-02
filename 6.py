# so hello now i ma writing pyhton and liek i will do just 30 mins everyday and let us see, i will not leave it just 
#30 mins a day and then we will see how much i can get in day 1, done thus than bro.. let us go..
#iterators and generators
#question 6
# reading numbers from file with exception handling 
def read_numbers(filename):
    try:
        with open(filename, "r") as f:
            for line in f:
                try:
                    num = int(line.strip())   # try to convert line to int
                    print("Read number:", num)
                except ValueError:
                    print("Invalid data:", line.strip())
    except FileNotFoundError:
        print("File not found:", filename)
# example
read_numbers("numbers.txt")
