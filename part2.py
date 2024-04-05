# should use three FIFO queues
def FCFS(waiting, ready, running): # waiting should have all the processes, ready and running should be empty
  time = 0; # counter for time
  while(watiing.empty()):
    ready.put(waiting.get())
    if(running.empty()):
      running.put(waiting.get())
    # probably add time manipulation here
    time++;
  while(ready.empty()):
    running.put(watiing.get())
    # running.get() when burst time is over

# now using 2d arrays
def SJF(waiting, ready, running):
  for i in range(len(waiting)):  # Sorting process according to their Burst Time.
    index = i
    for j in range(i + 1, len(waiting)):
        if waiting[j][1] < waiting[index][1]:
            index = j
    temp = waiting[i][1]
    waiting[i][1] = waiting[index][1]
    waiting[index][1] = temp
    temp = waiting[i][0]
    waiting[i][0] = waiting[index][0]
    waiting[index][0] = temp
  # and then you can probably put that list into a queue and into FCFS
  q = queue.queue()
  for i in waiting:
    q.put(i)
  FCFS(waiting)

# burstTime should just be an int
def SRT(waiting, ready, running, burstTime):
  # i think just arrays for this?
  # run all processes for the burstTime once
  for i in waiting:
    running[i] = i
    i.timeRemaining -= burstTime
  # then just keep looping and running by burstTime
  while(len(running) != 0):
    min = waiting[0]
    minTime = waiting[0].timeRemaining
    for i in waiting:
      if(i.timeRemaining < minTime):
        min = i
        minTime = i.timeRemaining
    # run the process
    min.timeRemaining -= burstTime
    for i in waiting:
      if (i.timeRemaining <= 0):
        # remove i

def RR(waiting, ready, running, slice):
  # run all processes once
  for i in waiting:
    running[i] = i
    i.timeRemaining -= slice
  for i in running:
    i.timeRemaining -= slice
    if(i.timeRemaining <= 0):
      # remove i
      # add time manipulation
