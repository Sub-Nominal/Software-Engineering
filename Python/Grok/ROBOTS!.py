line = str(input('Line: '))
line1 = line.lower()
line = line.split()
line1 = line1.split()
if "robot" in line:
    print('There is a small robot in the line.')
elif "ROBOT" in line:
    print('There is a big robot in the line.')
elif "robot" and "ROBOT" not in line and "robot" not in line1:
    print("No robots here.")
else:
    print('There is a medium sized robot in the line.')