import random
from matplotlib import pyplot as plt
# Basic Gradient descent algorithm
DATA = [[1,1],[2,3],[3,1],[4,5],[5,3]]
MAX_RANGE = 1000
LEARNING_RATE = 0.01


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
  print(DATA)
  print(f'Slope: {slope}\nIntercept: {intercept}')
  for count in range(MAX_RANGE):
    ssr = find_SSR(slope,intercept) 
    # print(f'SSR: {ssr}')
    d_slope = find_d_slope(slope,intercept)
    d_intercept = find_d_intercept(slope,intercept)
    # print(f'd_slope: {d_slope}\nd_intercept: {d_intercept}')
    step_size_slope = LEARNING_RATE * d_slope
    step_size_intercept = LEARNING_RATE * d_intercept
    # print(f'step size slope: {step_size_slope}\nStep size intercept: {step_size_intercept}')
    slope -= step_size_slope
    intercept -= step_size_intercept
    print(f'Slope: {slope}\nIntercept: {intercept}')
    if abs(step_size_slope) <= 0.001 and abs(step_size_intercept) <= 0.001:
      print('Graph is close')
      return [slope,intercept]
    print('')
  return [slope,intercept]
  

SIGFIG = 5
if __name__ == '__main__':
  print('Program starting\n')
  result = gradient_descent(1,0) # initial slope & initial intercept, result is the final ones
  print(f'Final:\nSlope: {str(result[0])[:SIGFIG]}\nIntercept: {str(result[1])[:SIGFIG]}')
  print('\nProgram ending')

