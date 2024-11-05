from collections import deque

def func():
    # Read input values
    first_line = input().strip()
    second_line = input().strip()

    # Parse the input
    n, w = map(int, first_line.split())
    trust_sequence = list(map(int, second_line.split()))

    # Deque to store indexes of useful elements for each window
    deq = deque()
    result = []

    for i in range(n):
        # Remove elements not within the window
        if deq and deq[0] < i - w + 1:
            deq.popleft()

        # Remove elements that are larger than the current element as they are not useful
        while deq and trust_sequence[deq[-1]] > trust_sequence[i]:
            deq.pop()

        # Add the current element index
        deq.append(i)

        # Append the minimum value for the current window to the result list
        if i >= w - 1:
            result.append(trust_sequence[deq[0]])

    # Print the result as space-separated values
    print(" ".join(map(str, result)))

if __name__ == "__main__":
    func()
