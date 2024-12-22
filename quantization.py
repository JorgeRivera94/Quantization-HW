import sys
import ast

# Scaling factor that divides the range of values into partitions
def CalculateScalingFactor(beta: float, alpha: float, bits: int) -> float:
	scaling_factor = (beta - alpha) / ((2 ** bits) - 1) 
	return scaling_factor

# Maps the real values to integer values. Quantized values are uniformly spaced. 
# In Simmetric Quantization, the zero point Z = 0
def UniformSymmetricQuantization(input: float, scaling_factor: float) -> int:
	quantized = int(input / scaling_factor)
	return quantized

def main():
	if len(sys.argv) > 1:
		# List representing a vector containing a list of real numbers
		array = ast.literal_eval(sys.argv[1])
		
		# number of bits needed
		bits = int(sys.argv[2])
		
		# the maximum real number possible
		beta = float(sys.argv[3])
		
		# the minimum real number possible
		alpha = float(sys.argv[4])
		
		# calculate the scaling factor
		scaling_factor = CalculateScalingFactor(beta, alpha, bits)
		
		# perform quantization
		for i in range(len(array)):
			array[i] = UniformSymmetricQuantization(array[i], scaling_factor)

		print(array)

if __name__ == "__main__":
	#test with:
	#python3 input.py [0.5,-1,1,0,0.66,0.45,0.82] 8 1 -1
	#python3 input.py [0.5,-1,1,0,0.66,0.45,0.82] 16 1 -1
	#python3 input.py [0.5,-1,1,0,0.66,0.45,0.82] 4 1 -1

	#results should be:
	#[63, -127, 127, 0, 84, 57, 104]
	#[16383, -32767, 32767, 0, 21626, 14745, 26869]
	#[3, -7, 7, 0, 4, 3, 6]
	
    main()