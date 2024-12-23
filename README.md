# Quantization-HW
Edge ML HW

# Test with:
python3 input.py [0.5,-1,1,0,0.66,0.45,0.82] 8 1 -1

python3 input.py [0.5,-1,1,0,0.66,0.45,0.82] 16 1 -1

python3 input.py [0.5,-1,1,0,0.66,0.45,0.82] 4 1 -1

# Results should be:
[63, -127, 127, 0, 84, 57, 104]

[16383, -32767, 32767, 0, 21626, 14745, 26869]

[3, -7, 7, 0, 4, 3, 6]