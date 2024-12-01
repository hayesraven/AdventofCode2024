def parse_input(input: str) -> tuple:
    list1 = []
    list2 = []
    
    for num in input.split('\n'):
        pair = num.split()
        list1.append(int(pair[0]))
        list2.append(int(pair[1]))
        
    list1 = sorted(list1)
    list2 = sorted(list2)
    
    return (list1, list2)

def part_2(input: str) -> int:
    '''
    Part_2
    Given input, find the number of times a number in list 1 appears in
    list 2. Multiply the number by this count, sum these and return it.
    '''
    ans = 0
    
    list1, list2 = parse_input(input)
    
    pairs = len(list1)
    
    for num in list1:
        num_count = list2.count(num)
        ans += num * num_count
        
    return ans

def part_1(input: str) -> int:
    '''
    Part_1
    Given input, parse the input as two lists, sort them, and then find the 
    distance between each number in a pair, where the pairs are from 
    shortest to longest. Sum this and return it.
    '''
    ans = 0
        
    list1, list2 = parse_input(input)
    
    pairs = len(list1)
    
    for i in range(0, pairs):
        ans += abs(list1[i] - list2[i])  
    
    return ans

def main():
    with open('day1_input.txt', 'r') as f:
        input = f.read()
        
    # Part 1
    ans = part_1(input)
    print(f"Part 1's answer is: {ans}")
    
    # Part 2
    ans = part_2(input)
    print(f"Part 2's answer is: {ans}")
    
if __name__ == "__main__":
    main()