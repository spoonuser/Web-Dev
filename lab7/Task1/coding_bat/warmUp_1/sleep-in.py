def sleep_in(weekday, vacation):
  if weekday == False and vacation == False:
    return True
  elif weekday == True and vacation == False:
    return False
  elif weekday == False and vacation == True:
    return True
  else:
    return True
sleep_in(False, False) 
sleep_in(True, False) 
sleep_in(False, True) 