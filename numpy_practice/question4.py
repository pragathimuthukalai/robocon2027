n=int(input("Enter a Number:"))
def frequency(n):
    freq = {}
    for digit in str(n):
        if digit in freq:
            freq[digit] += 1
        else:
            freq[digit] = 1
    return freq

result = frequency(n)
print("Frequency of digits in", n, "is:", result)
