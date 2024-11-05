def func():
    # Read input values
    first_line = input().strip()
    second_line = input().strip()

    # Parse the input
    n, w = map(int, first_line.split())
    trust_sequence = list(map(int, second_line.split()))

    # Initialize the result list to store minimum trust values for each window
    result = []

    # Iterate over each window and find the minimum in that window
    for i in range(n - w + 1):
        min_value = min(trust_sequence[i:i + w])
        result.append(min_value)

    # Print the result as space-separated values
    print(" ".join(map(str, result)))

if __name__ == "__main__":
    func()
