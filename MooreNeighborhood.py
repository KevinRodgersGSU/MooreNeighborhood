import matplotlib.pyplot as plt
taxis = []
zaxis = []
xaxis=[]
CurrentInfected = 1
TotalInfected = 1
PI = 1

for t in range(1,50):
  PI = CurrentInfected
  CurrentInfected = (2*t+1) ** 2 - TotalInfected
  TotalInfected += CurrentInfected 
  taxis.append(t)
  xaxis.append(CurrentInfected/PI)
  zaxis.append(PI/CurrentInfected)


##CurrentInfected = 10000 - TotalInfected
##taxis.append(50)
##xaxis.append(CurrentInfected/PI)
##zaxis.append(PI/CurrentInfected)



plt.title("Moore's Neighborhood")
plt.plot(taxis,xaxis, color=(0,0,1), linewidth=1.0, label='T+1/T')
plt.plot(taxis,zaxis, color=(1,0,0), linewidth=1.0, label='T/T+1')
plt.legend()
plt.xlabel("TIME STEPS")
plt.grid(True)
plt.show()
