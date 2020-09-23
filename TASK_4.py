def task_4(n):
  for x in range(3, int(n**0.5)+1):
    if n%x==0:
      return "not prostoe chislo"
  return "prostoe chislo"







g