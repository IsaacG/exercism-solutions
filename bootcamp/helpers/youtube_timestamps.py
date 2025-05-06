import re

lines = []
vid = input("Video ID: ")
hh, mm, ss = 0, 0, 0
while True:
  try:
    a, b = input("Title: ").split(maxsplit=1)
  except:
    break
  ps = re.split(r"[ :;.]", a)
  ss = int(ps[-1])
  if len(ps) > 1:
    mm = int(ps[-2])
  if len(ps) > 2:
    hh = int(ps[-3])
  seconds = ((hh * 60) + mm) * 60 + ss
  lines.append(f"* [{hh:02}:{mm:02}:{ss:02}](<https://youtu.be/{vid}?t={seconds}>) {b}")

print("\n\n" + "\n".join(lines))
