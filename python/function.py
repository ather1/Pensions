#trying to write a square function

def Square(x):
    return x*x;

def main():
    for i in range(1,10,2):
        print("{} squared equals {}".format(i,Square(i)));

if __name__ =="main":
    main();