if __name__ == "__main__":
    def factorial(num):
      fact = 1
      for i in range(1,num+1):
        fact*= i
      return fact

    factorial(5)