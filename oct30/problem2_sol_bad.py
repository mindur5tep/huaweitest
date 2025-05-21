def func():
    # Read input values
    n = int(input().strip())
    serialized_tree = list(map(int, input().strip().split()))

    # Step 1: Parse the tree structure from serialized input
    samples = []
    children = []
    index = 0
    while index < len(serialized_tree):
        if serialized_tree[index] == -1:
            children.append([])
            index += 1
        else:
            samples.append(serialized_tree[index])
            children.append([])
            index += 1
            # Read all child nodes until we encounter a -1
            while index < len(serialized_tree) and serialized_tree[index] != -1:
                children[-1].append(len(samples) - 1 + (len(children[-1]) + 1))
                index += 1
            index += 1  # Skip the -1 separator

    # Step 2: Calculate the total sample count for each node including its descendants
    def calculate_total_samples(node):
        total = samples[node]
        for child in children[node]:
            total += calculate_total_samples(child)
        samples[node] = total
        return total

    # Start the calculation from the root (node 0)
    calculate_total_samples(0)

    # Step 3: Generate the output format
    output = []
    child_index = 0
    for i in range(len(samples)):
        output.append(samples[i])
        output.append(-1)  # Each node ends with a -1 separator
        for child in children[i]:
            output.append(child)
        output.append(-1)  # End children list with -1

    print(" ".join(map(str, output)))

if __name__ == "__main__":
    func()
