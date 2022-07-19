"""
高橋君はレベル N の赤い宝石を 1 個持っています


レベル n の赤い宝石 (n は 2 以上) を
    「レベル n−1 の赤い宝石 1 個と、レベル n の青い宝石 X 個」に変換する。

レベル n の青い宝石 (n は 2 以上) を
    「レベル n−1 の赤い宝石 1 個と、レベル n−1 の青い宝石 Y 個」に変換する。

高橋君はレベル 1 の青い宝石ができるだけたくさんほしいです
操作によって高橋君はレベル 1 の青い宝石を最大何個入手できますか？
"""


def main():
    n, x, y = map(int, input().split())

    red, blue = [0] * n, [0] * n

    red[0] = 1

    for i in range(1, n):
        red[i] = blue[i - 1] + red[i - 1] * y
        blue[i] = blue[i - 1] + red[i] * x

    print(blue[n - 1])


if __name__ == "__main__":
    main()
