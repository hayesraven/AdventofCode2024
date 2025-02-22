import re

def part_1(input: list) -> int:
    ans = 0
    rows = len(input)
    columns = len(input[0])
    
    for i in range(0, rows):
        for j in range(0, columns):
            if input[i][j] == 'X':
                # Found an X, search for XMAS now
                if j > 2 and input[i][j - 3:j + 1] == 'SAMX': # Search backwards
                    ans += 1
                if columns - j > 3 and input[i][j:j + 4] == 'XMAS': # Search forwards
                    ans += 1
                if i > 2 and input[i - 3:i + 1][j] == 'SAMX': # Search north
                    ans += 1
                if columns - i > 3 and input[i:i + 4][j] == 'XMAS': # Search south
                    ans += 1
                if j > 2 
                        
        
    
    return ans
    
def main():
    with open('test_input.txt', 'r') as f:
        input = f.read().splitlines()
        
    ans = part_1(input)
    print(f"Part_1's answer is: {ans}")
    
if __name__ == "__main__":
    main()