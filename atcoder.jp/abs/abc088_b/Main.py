N = int(input())
a = sorted(map(int, input().split()))[::-1]
#2行目のデータをスペースで分けて要素を整数化
#それをソートで昇順にするsorted(新しいリスト作成している）
#－1末尾からとる。降順にできる
print(sum(a[::2])-sum(a[1::2]))
#[::2]は2つごと（0，2，4）の要素をとる
#[1::2]はindex1から2つごとに要素を取る