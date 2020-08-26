import numpy as np

# Acao UP:
T_up = np.zeros((12,12))

T_up[0][0] = 0.1
T_up[0][1] = 0.8
T_up[0][3] = 0.1

T_up[1][2] = 0.8
T_up[1][1] = 0.2

T_up[2][2] = 0.9
T_up[2][5] = 0.1

T_up[3][0] = 0.1
T_up[3][3] = 0.8
T_up[3][6] = 0.1

T_up[5][2] = 0.1
T_up[5][5] = 0.8 
T_up[5][8] = 0.1

T_up[6][3] = 0.1 
T_up[6][7] = 0.8
T_up[6][9] = 0.1 

T_up[7][7] = 0.1
T_up[7][8] = 0.8 
T_up[7][10] = 0.1 

T_up[8][5] = 0.1
T_up[8][8] = 0.8
T_up[8][11] = 0.1 

T_up[9][9] = 0.1
T_up[9][6] = 0.1
T_up[9][10] = 0.8

# Acao Down:
T_down = np.zeros((12,12))

T_down[0][0] = 0.9
T_down[0][3] = 0.1

T_down[1][0] = 0.8
T_down[1][1] = 0.2

T_down[2][1] = 0.8
T_down[2][2] = 0.1
T_down[2][5] = 0.1

T_down[3][0] = 0.1
T_down[3][3] = 0.8
T_down[3][6] = 0.1

T_down[5][2] = 0.1
T_down[5][5] = 0.8 
T_down[5][8] = 0.1

T_down[6][3] = 0.1 
T_down[6][6] = 0.8
T_down[6][9] = 0.1 

T_down[7][7] = 0.1
T_down[7][6] = 0.8 
T_down[7][10] = 0.1 

T_down[8][5] = 0.1
T_down[8][7] = 0.8
T_down[8][11] = 0.1 

T_down[9][9] = 0.9
T_down[9][6] = 0.1

# Acao Left:
T_left = np.zeros((12,12))

T_left[0][0] = 0.9
T_left[0][1] = 0.1

T_left[1][0] = 0.1
T_left[1][1] = 0.8
T_left[1][2] = 0.1

T_left[2][2] = 0.9
T_left[2][1] = 0.1

T_left[3][0] = 0.8
T_left[3][3] = 0.2

T_left[5][2] = 0.8
T_left[5][5] = 0.2

T_left[6][3] = 0.8
T_left[6][6] = 0.1
T_left[6][7] = 0.1 

T_left[7][7] = 0.8
T_left[7][6] = 0.1
T_left[7][8] = 0.1 

T_left[8][5] = 0.8
T_left[8][8] = 0.1
T_left[8][7] = 0.1 

T_left[9][6] = 0.8
T_left[9][9] = 0.1
T_left[9][10] = 0.1

# Acao Right:
T_right = np.zeros((12,12))

T_right[0][0] = 0.1
T_right[0][1] = 0.1
T_right[0][3] = 0.8

T_right[1][0] = 0.1
T_right[1][1] = 0.8
T_right[1][2] = 0.1

T_right[2][2] = 0.1
T_right[2][1] = 0.1
T_right[2][5] = 0.8

T_right[3][6] = 0.8
T_right[3][3] = 0.2

T_right[5][8] = 0.8
T_right[5][5] = 0.2

T_right[6][9] = 0.8
T_right[6][6] = 0.1
T_right[6][7] = 0.1 

T_right[7][10] = 0.8
T_right[7][6] = 0.1
T_right[7][8] = 0.1 

T_right[8][11] = 0.8
T_right[8][8] = 0.1
T_right[8][7] = 0.1 

T_right[9][9] = 0.9
T_right[9][10] = 0.1
