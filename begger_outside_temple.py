"""
https://www.scaler.com/academy/mentee-dashboard/class/34448/assignment/problems/440/?navref=cl_pb_nv_tb
There are A beggars sitting in a row outside a temple. Each beggar initially has an empty pot. When the devotees come to the temple, they donate some amount of coins to these beggars. Each devotee gives a fixed amount of coin(according to their faith and ability) to some K beggars sitting next to each other.

Given the amount P donated by each devotee to the beggars ranging from L to R index, where 1 <= L <= R <= A, find out the final amount of money in each beggar's pot at the end of the day, provided they don't fill their pots by any other means.
For ith devotee B[i][0] = L, B[i][1] = R, B[i][2] = P, Given by the 2D array B
"""

solve(A, B):
        result = [0]*A
        for i in range(0, len(B)): # n 
            for j in range(B[i][0]-1, B[i][1]): #A
                result[j] += B[i][2]
        return(result)

solve(5, [[1, 2, 10], [2, 3, 20], [2, 5, 25]])


"""
    T.C = O(n*A)
    S.C = O(n)
""" 
""" ===================================================== Better Approach ============================================================ """

# @param A : integer
# @param B : list of list of integers
# @return a list of integers
def solve(A, B):
    result = [0]*A
    for i in range(0, len(B)):
        result[B[i][0]-1] += B[i][2]
        if(B[i][1] < A):
            result[B[i][1]] -= B[i][2]
            
    # prefix sum
    for i in range(1, A):
        result[i] += result[i-1]
    return result
  
  
solve(5, [[1, 2, 10], [2, 3, 20], [2, 5, 25]])
"""

T.C O(max(N+A))
S.C = O(A)

"""
