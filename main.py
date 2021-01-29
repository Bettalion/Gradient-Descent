import random
# Basic Gradient descent algorithm
DATA = [[0,1],[2,2],[3,4],[5,4]]



def find_SSR(slope,intercept): # sum of the squared residual
  ssr = 0
  for coord in DATA: # summation
    sr = (coord[1] - (intercept + slope * coord[0]))**2  # the squared residual
    ssr+=sr
  return ssr

def find_d_slope(slope,intercept): # derivative of the loss function in relation to slope
  d_slope = 0
  for coord in DATA: # summation
    sr = 2(coord[1] - (intercept + slope * coord[0])) * (-coord[0])
    ssr+=sr
  return ssr

def gradient_descent():
  print(DATA)
  slope = 1 # initial slope
  intercept = 0 # initial intercept
  ssr = find_SSR(slope,intercept) 
  print(f'SSR: {ssr}')
  d_slope = 0
  
  d_intercept = 
  


if __name__ == '__main__':
  print('Program starting\n')
  gradient_descent()
  print('\nProgram ending')

