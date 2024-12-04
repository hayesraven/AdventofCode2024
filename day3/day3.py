import re

def part_1(input: str) -> int:
    ans = 0
    reg_pattern = r'mul\(([1-9][0-9]{0,2}),([1-9][0-9]{0,2})\)'
    
    reg_obj = re.compile(reg_pattern)
    matches = reg_obj.findall(input)
    
    for pair in matches:
        ans += int(pair[0]) * int(pair[1])
    
    return ans

def part_2(input: str) -> int:
    ans = 0
    input = "do()" + input + "don't()"
    reg_pattern = r"(do\(\).*?)(?=don't\(\))"
    
    reg_obj = re.compile(reg_pattern)
    matches = reg_obj.findall(input)
    
    for match in matches:
        ans += part_1(match)
    
    return ans

def main():
    with open('day3_input.txt', 'r') as f:
        input = f.read()
        
    ans = part_1(input)
    print(f"Part_1's answer is: {ans}")
    
    ans = part_2(input)
    print(f"Part_2's answer is: {ans}")
    
if __name__ == "__main__":
    main()