def make_readable(seconds):
    x1=0
    x2=0
    x3=0
    x1=seconds//3600
    if x1==0:
        x2=(seconds) // 60
        if x2==0:
            x3=seconds

        else:
            x3=seconds - (x2 * 60)

    else:
        x2=(seconds - x1 * 3600) // 60

        x3=seconds - (x1 * 3600) - (x2 * 60)

    if x3<10:
        x3="0"+str(x3)
    if x2<10:
        x2="0"+str(x2)
    if x1<10:
        x1="0"+str(x1)
    print(str(x1)+":"+str(x2)+":"+str(x3))
make_readable(35666)
