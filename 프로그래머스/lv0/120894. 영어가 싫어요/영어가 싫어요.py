def solution(numbers):
    answer = 0
    nums = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    # enumerate : 값을 가져오는 것
    for idx, num in enumerate(nums):
        numbers = numbers.replace(num, str(idx))
        
    return int(numbers)