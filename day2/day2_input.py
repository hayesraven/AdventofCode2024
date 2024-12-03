import re

def parse_input(input: str) -> list:
    reports = []
    
    for num in input.split('\n'):
        report = [int(x) for x in num.split()]
        reports.append(report)
    
    return reports

def safety_check(report: list) -> bool:

    prev = report[0]
    report_len = len(report)
        
    if not (sorted(report) == report) and not (sorted(report,reverse=True) == report):
        return False        
    else:        
        for i in range(1, report_len):
            curr = report[i]
            if not (1 <= abs(prev - curr) <= 3):
                return False
                break
            prev = curr
            
    return True

def part_2(input: str) -> int:
    ans = 0
    reports = parse_input(input)
    
    for report in reports:        
        if safety_check(report):
            ans += 1
        else:
            report_len = len(report)
            
            for i in range(0, report_len):
                if safety_check(report[:i] + report[i+1:]):
                    ans += 1
                    break
            
    return ans
    
def part_1(input: str) -> int:
    '''
    Part_1
    Return the total number of safe reports in a total list. A report is
    considered safe if:
        - The levels are all increasing or decreasing
        - The levels increase/decrease at least once and no more than 3
    '''
    ans = 0
    reports = parse_input(input)
    

    for report in reports:     
        if safety_check(report):
            ans += 1
        
    return ans

def main():
    with open('day2_input.txt', 'r') as f:
        input = f.read()
        
    # Part 1
    ans = part_1(input)
    print(f"Part 1's answer is: {ans}")    
    
    # Part 1
    ans = part_2(input)
    print(f"Part 2's answer is: {ans}")    
    
if __name__ == "__main__":
    main()