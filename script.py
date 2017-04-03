import random;
lines = open('/log/log.log').read().splitlines()
myline =random.choice(lines)
print(myline)
