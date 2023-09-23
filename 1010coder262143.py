i = int(input("Введите число: "))
n = 1
# 262143 last number
# every 0 number "number * 2 + 1"
i1 = i // 2
ii1 = i % 2
if ii1 == 0:
    p1 = 0
if ii1 > 0:
    p1 = 1
if i1 == 1:
    print(n, p1)
i2 = i1 // 2
ii2 = i1 % 2
if ii2 == 0:
    p2 = 0
if ii2 > 0:
    p2 = 1
if i2 == 1:
    print(n, p2, p1)
i3 = i2 // 2
ii3 = i2 % 2
if ii3 == 0:
    p3 = 0
if ii3 > 0:
    p3 = 1
if i3 == 1:
    print(n, p3, p2, p1)
i4 = i3 // 2
ii4 = i3 % 2
if ii4 == 0:
    p4 = 0
if ii4 > 0:
    p4 = 1
if i4 == 1:
    print(n, p4, p3, p2, p1)
i5 = i4 // 2
ii5 = i4 % 2
if ii5 == 0:
    p5 = 0
if ii5 > 0:
    p5 = 1
if i5 == 1:
    print(n, p5, p4, p3, p2, p1)
i6 = i5 // 2
ii6 = i5 % 2
if ii6 == 0:
    p6 = 0
if ii6 > 0:
    p6 = 1
if i6 == 1:
    print(n, p6, p5, p4, p3, p2, p1)
i7 = i6 // 2
ii7 = i6 % 2
if ii7 == 0:
    p7 = 0
if ii7 > 0:
    p7 = 1
if i7 == 1:
    print(n, p7, p6, p5, p4, p3, p2, p1)
i8 = i7 // 2
ii8 = i7 % 2
if ii8 == 0:
    p8 = 0
if ii8 > 0:
    p8 = 1
if i8 == 1:
    print(n, p8, p7, p6, p5, p4, p3, p2, p1)
i9 = i8 // 2
ii9 = i8 % 2
if ii9 == 0:
    p9 = 0
if ii9 > 0:
    p9 = 1
if i9 == 1:
    print(n, p9, p8, p7, p6, p5, p4, p3, p2, p1)
i10 = i9 // 2
ii10 = i9 % 2
if ii10 == 0:
    p10 = 0
if ii10 > 0:
    p10 = 1
if i10 == 1:
    print(n, p10, p9, p8, p7, p6, p5, p4, p3, p2, p1)
i11 = i10 // 2
ii11 = i10 % 2
if ii11 == 0:
    p11 = 0
if ii11 > 0:
    p11 = 1
if i11 == 1:
    print(n, p11, p10, p9, p8, p7, p6, p5, p4, p3, p2, p1)
i12 = i11 // 2
ii12 = i11 % 2
if ii12 == 0:
    p12 = 0
if ii12 > 0:
    p12 = 1
if i12 == 1:
    print(n, p12, p11, p10, p9, p8, p7, p6, p5, p4, p3, p2, p1)
i13 = i12 // 2
ii13 = i12 % 2
if ii13 == 0:
    p13 = 0
if ii13 > 0:
    p13 = 1
if i13 == 1:
    print(n, p13, p12, p11, p10, p9, p8, p7, p6, p5, p4, p3, p2, p1)
i14 = i13 // 2
ii14 = i13 % 2
if ii14 == 0:
    p14 = 0
if ii14 > 0:
    p14 = 1
if i14 == 1:
    print(n, p14, p13, p12, p11, p10, p9, p8, p7, p6, p5, p4, p3, p2, p1)
i15 = i14 // 2
ii15 = i14 % 2
if ii15 == 0:
    p15 = 0
if ii15 > 0:
    p15 = 1
if i15 == 1:
    print(n, p15, p14, p13, p12, p11, p10, p9, p8, p7, p6, p5, p4, p3, p2, p1)
i16 = i15 // 2
ii16 = i15 % 2
if ii16 == 0:
    p16 = 0
if ii16 > 0:
    p16 = 1
if i16 == 1:
    print(n, p16, p15, p14, p13, p12, p11, p10, p9, p8, p7, p6, p5, p4, p3, p2, p1)
i17 = i16 // 2
ii17 = i16 % 2
if ii17 == 0:
    p17 = 0
if ii17 > 0:
    p17 = 1
if i17 == 1:
    print(n, p17, p16, p15, p14, p13, p12, p11, p10, p9, p8, p7, p6, p5, p4, p3, p2, p1)
if i17 > 1:
    print("Script error")
