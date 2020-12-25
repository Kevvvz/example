sh = input("Enter hours")
sr = input("Enter rates")
fh = float(sh)
fr = float(sr)
if fh > 40:
    reg = fh * fr
    otp = (fh-40)*(0.5*fr)
    xp = reg + otp
    print(xp)
elif fh <= 40:
    reg = fh * fr
    print(reg)