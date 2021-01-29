import random
from matplotlib import pyplot as plt
# Basic Gradient descent algorithm
DATA = [[1,1],[2,3],[3,1],[4,5],[5,3]]
MAX_RANGE = 1000
LEARNING_RATE = 0.01

def openFiles():
  try:
    f1 = open('Log.txt','a') # all outputs
  except:
    f1 = open('Log.txt','w') # all outputs
  try:
    f2 = open('I & S.txt','a') # intercept & slope outputs
  except:
    f2 = open('I & S','w') # intercept & slope outputs
  return [f1,f2]

def find_SSR(slope,intercept): # sum of the squared residual
  ssr = 0
  for coord in DATA: # summation
    sr = (coord[1] - (intercept + slope * coord[0]))**2  # the squared residual
    ssr+=sr
  return ssr

def find_d_slope(slope,intercept): # derivative of the loss function in relation to slope
  d_slope = 0
  for coord in DATA: # summation
    d = 2*(coord[1] - (intercept + slope * coord[0])) * (-coord[0])
    d_slope+=d
  return d_slope

def find_d_intercept(slope,intercept): # derivative of the loss function in relation to intercept
  d_intercept = 0
  for coord in DATA: # summation
    d = 2*(coord[1] - (intercept + slope * coord[0])) * (-1)
    d_intercept+=d
  return d_intercept

def gradient_descent(slope,intercept):
  f1,f2 = openFiles()
  print(DATA)
  print(f'Slope: {slope}\nIntercept: {intercept}')
  f1.write(f'Initial:\n\nSlope: {slope}\nIntercept: {intercept}\n')
  f2.write(f'Initial:\n\nSlope: {slope}\nIntercept: {intercept}\n')
  for count in range(MAX_RANGE):
    print(f'Iteration {count}:')
    f1.write(f'Iteration {count}:\n')
    f2.write(f'Iteration {count}:\n')
    ssr = find_SSR(slope,intercept) 
    print(f'SSR: {ssr}')
    f1.write(f'SSR: {ssr}\n')
    d_slope = find_d_slope(slope,intercept)
    d_intercept = find_d_intercept(slope,intercept)
    print(f'd_slope: {d_slope}\nd_intercept: {d_intercept}')
    f1.write(f'd_slope: {d_slope}\nd_intercept: {d_intercept}\n')
    step_size_slope = LEARNING_RATE * d_slope
    step_size_intercept = LEARNING_RATE * d_intercept
    print(f'step size slope: {step_size_slope}\nStep size intercept: {step_size_intercept}')
    f1.write(f'step size slope: {step_size_slope}\nStep size intercept: {step_size_intercept}\n')
    slope -= step_size_slope # get new slope
    intercept -= step_size_intercept # get new intercept
    print(f'Slope: {slope}\nIntercept: {intercept}')
    f1.write(f'Slope: {slope}\nIntercept: {intercept}\n')
    f2.write(f'Slope: {slope}\nIntercept: {intercept}\n')
    if abs(step_size_slope) <= 0.001 and abs(step_size_intercept) <= 0.001: # exit if optimal values reached
      print('\nGraph is close')
      f1.write(f'Final:\n\nSlope: {slope}\nIntercept: {intercept}\n')
      f2.write(f'Final:\n\nSlope: {slope}\nIntercept: {intercept}\n')
      f1.close()
      f2.close()
      return [slope,intercept]
    f1.write('\n')
    f2.write('\n')
    print('')
  f1.write(f'Final:\n\nSlope: {slope}\nIntercept: {intercept}\n')
  f2.write(f'Final:\n\nSlope: {slope}\nIntercept: {intercept}\n')
  f1.close()
  f2.close()
  return [slope,intercept]
  

SIGFIG = 5 # number of characters to be truncated
if __name__ == '__main__':
  print('Program starting\n')
  result = gradient_descent(1,0) # initial slope & initial intercept, result is the final ones
  print(f'Final:\n\nSlope: {str(result[0])[:SIGFIG]}\nIntercept: {str(result[1])[:SIGFIG]}')
  print('\nProgram ending')

