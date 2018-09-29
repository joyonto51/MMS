def counter(number):
    if number > 0:
      print(number)
      number+=1
      counter(number)
counter(1)
