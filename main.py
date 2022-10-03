import itertools, ltp, ptp
gen=itertools.combinations_with_replacement('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', 30)

def x(pwd):
    x=''.join(pwd)
    if ltp.b64d(x+"09"):
        ptp.app("pwds", x)

for pwd in gen:
    x(pwd)