from collections import defaultdict


def main():
    n = int(input())
    folders = defaultdict(int)

    for _ in range(n):
        folder_name = input()

        if folders[folder_name] == 0:
            print(f"{folder_name}")
        else:
            print(f"{folder_name}({folders[folder_name]})")

        folders[folder_name] += 1


if __name__ == "__main__":
    main()
