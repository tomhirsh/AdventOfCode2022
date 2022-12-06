def compute_marker_time(all_different_count):
    i = 0
    while len(set(signal[i:i+all_different_count])) != all_different_count:
        i += 1
        continue
    return i+all_different_count


if __name__ == "__main__":
    with open('data.txt','r') as f:
        signal = f.readline()

    # part 1
    marker_time = compute_marker_time(4)
    print(marker_time)

    # part 2
    marker_time = compute_marker_time(14)
    print(marker_time)