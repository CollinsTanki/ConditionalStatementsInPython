for number in range(3):
  print("Attempt")

  #|Printing indexes
  for number in range(3):
    print("Attempt", number)

    #Adding 1 to the number
    for number in range(3):
      print("Attempt", number+1)

      #Adding 1 to the number
      #for number in range(3):
       # print("Attempt", nummber + 1, (number + 1) * ".")

        
      #Adding 1 to the number multiply by a "." 
      for number in range(1, 4):
        print("Attempt", number, (number + 1) * ".")

        #condition where 2 is a step
        for number in range(1, 10, 2):
          print("Attempt", number, number * ".")
