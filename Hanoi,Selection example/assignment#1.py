## Algorithm & Their application assignment #1


def Hanoi_sum(n):
    
    if n == 1:     # Return end value for the recursive func which condition is that the disk is only one.
        return 2
   
    else:
        return 3*Hanoi_sum(n-1)+2    # Return recursive function that justified in 2-(a)
    

# 2-(b). Hanoi problem.

# Calculate summation number of moving disks
# n is natural number here.
def Hanoi_viaB(N, Start, Aux, End):

	if N == 1: # Return end value for the recursive func which condition is that the disk is only one.

		print(Start, '->', End)
		return 2

	else:

        # 4 steps that described in 2-(a) justification.
        #step 1
		Hanoi_viaB(N-1, Start, Aux, End)
        #step 2
		Hanoi_viaB(N-1, Start, End, Aux)
        #step 3
		Hanoi_viaB(1, Start, Aux, End)
        #step 4
		Hanoi_viaB(N-1, Aux, Start, End)
        
        # return total sum of step 1~4
		return 3*Hanoi_viaB(N-1, Start, Aux, End)+2  
        
        
# 3. Selection Algorithm

# Calculate entire number of case - choosing 'k' in 'n' candidates.
# n is natural nuber // k is integer which is >= 0
def Combination(n, k):
    
    if k == 0 or n == k:      #Return end(k=0) / exceptional(n=k) value for the reculsive function.
        return 1
    else:
        return Combination(n-1, k-1) + Combination(n-1, k)
""" 
# Description.
 Pulling k out of n equals the sum of the cases in which, after selecting particular one,
 the number of cases in which k is pulled out of it (n-1), and the number in which k-1 is selected including it.

""" 
    
    
    
    
# 4. Newton's Method

# Input ans as your starting rough guessing number
# tol is abbreviation of tollerance, the parameter that you think that the gap is good enough
def MySqrt(num, ans, tol):
    if abs(ans*ans - num) <= tol:
        return ans      # if the gap btw guessing num and real one is close enough, than return the newly guessing number.
    else:
        return MySqrt(num,(ans*ans + num)/(2*ans), tol) # Newton method that defined as average btw (ans & num/ans)
    
