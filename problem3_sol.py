def func():
    import sys
    input = sys.stdin.read
    data = input().split()

    N = int(data[0])
    M = int(data[1])
    neighborhoods = list(map(int, data[2:]))

    def can_place_pickup_points(max_dist):
        count = 1
        last_position = neighborhoods[0]

        for i in range(1, N):
            if neighborhoods[i] - last_position > max_dist:
                count += 1
                last_position = neighborhoods[i]
                if count > M:
                    return False
        return True

    left, right = 0, neighborhoods[-1] - neighborhoods[0]

    while left < right:
        mid = (left + right) // 2
        if can_place_pickup_points(mid):
            right = mid
        else:
            left = mid + 1

    print(left)

if __name__ == "__main__":
    func()
