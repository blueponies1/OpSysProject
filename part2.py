def FCFS(waiting, ready, running):
  while(len(running) == 0):
    running.append(ready.pop)

def SJF(waiting, ready, running):
  min = ready[0].runTime
  shortestJob = ready[0]
  for i in (ready):
    if(i.runTime < min):
      min = i.runTime
      shortestJob = i
  running.append(shortestJob)

def SRT(waiting, ready, running):
  min = ready[0].remainingTime
  shortestJob = ready[0]
  for i in (ready):
    if(i.remainingTime < min):
      min = i.remainingTime
      shortestJob = i
  running.append(shortestJob)

def RR(waiting, ready, running. slice):
  while(len(waiting != 0)):
    ready.append(waiting.pop)
  if(len(running) != 0):
    saved = running.append(ready.pop)
  if(saved.remainingTime - slice > 0):
    waiting.append(saved)
