# N桁を超える行を抽出
N = 10

file = open("input.txt", "r")

while True:
  line = file.readline()
  if not line:
    break
  if len(str(line)) > N:
    print(line)
