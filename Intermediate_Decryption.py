# Decryption Program

# Just some empty variables to store things later!
list_1 = []
list_2 = []
list_3 = []
list_4 = []
list_5 = []
swap_list = []
length_raw_text = ""
noise_text = ""
new_text = ""
new_text_1 = ""
new_digi = ""
Finale = ""
num_swap_digit = 0
count = 0
raw_text = str(input("Key in something you want to decrpyt please!"))

for i in raw_text:
    list_1.append(i)

#
Num_Digit_length = int(list_1[1])
print(f"Number of Digit for Length of Text: {Num_Digit_length}")

for ii in range(3, Num_Digit_length + 3):
    length_raw_text += str(list_1[ii])

print(f"Length of Text: {length_raw_text}")

for iii in range(0, Num_Digit_length + 3):
    del list_1[0]

print(f"Length of List: {len(list_1)}")
print(list_1)

list_1_len = len(list_1)

for iii in range(-1, -(list_1_len), -1):
    chrlist_1 = ord(list_1[iii])
    if (33 <= chrlist_1 <= 47) or (chrlist_1 >= 58):
        if chrlist_1 == 64:
            pass
        else:
            noise_text += str(list_1[iii])
    else:
        pass

noise_text_2 = noise_text[::-1]

print(f"Length of Noise: {len(noise_text_2)}")
print(noise_text_2)

for iiii in range(0, len(noise_text_2)):
    list_1.pop()

print(f"Length of List: {list_1_len}")
print(list_1)

for iv in list_1:
    new_text += str(iv)

print(new_text)

for vi in noise_text_2:
    new_digi += str(ord(vi))

print(new_digi)

new_digi_1 = int(new_text) + int(new_digi)

if int(new_text[0:1]) == 0:
    new_digi_1 = "0" + str(new_digi_1)

print(new_digi_1)

length_digits = len(str(new_digi_1))

if length_digits % 3 == 0:
    num_swap_digit = 3
    print("3 swap digit")
elif (length_digits - 2) % 3 == 0:
    num_swap_digit = 2
    print("2 swap digit")
else:
    num_swap_digit = 1
    print("1 swap digit")

print(num_swap_digit)

for vtr in str(new_digi_1):
    list_2.append(vtr)

print(list_2)

for vvi in range(-1, -(num_swap_digit) - 1, -1):
    nig = list_2[vvi]
    swap_list.append(nig)

print(swap_list)

if int(length_raw_text) >= 4:
    for vvti in swap_list:
        aa = list_2[int(vvti)]
        bb = list_2[int(vvti) + 1]
        list_2[int(vvti)] = bb
        list_2[int(vvti) + 1] = aa
else:
    print("Your Mum Gae!")

print(list_2)

for vvvv in range(0, num_swap_digit):
    list_2.pop()

print(list_2)

for vvti in list_2:
    if count < 3:
        new_text_1 += str(vvti)
        count += 1
    elif count == 3:
        list_3.append(new_text_1)
        new_text_1 = ""
        new_text_1 += str(vvti)
        count = 1

list_3.append(new_text_1)

print(list_3)

if int(length_raw_text) < 4:
    for ix in list_3:
        list_4.append(int((int(ix) - 23) / 7))

    for iz in list_4:
        strtxt = chr(int(iz))
        Finale += str(strtxt)

    print(Finale)

else:
    midswap = int((int(length_raw_text) - 2) / 2)
    if midswap == 1:
        midswap += 1
    else:
        print("I'm a Failure!")

    ax = list_3[1]
    bx = list_3[midswap]

    list_3[1] = bx
    list_3[midswap] = ax

    cx = list_3[0]
    dx = list_3[-1]

    list_3[0] = dx
    list_3[-1] = cx

    for iix in list_3:
        list_4.append(int((int(iix) - 23) / 7))

    print(list_4)

    for iy in list_4:
        strtxt = chr(int(iy))
        Finale += str(strtxt)

    print(Finale)


