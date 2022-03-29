def main():
    #your code goes here
    num = int(input("Enter a number:"))
    if num %3 == 0 and num %5 == 0:
      print("fizzbuzz")
    elif num % 5 == 0:
      print("buzz")
    elif num %3 == 0 :
      print("fizz")
    else:
      print(num)
if __name__ =='__main__':
    main()
