import os

# for i in range(0 , 256):
file_ptr_a_text = open("a.txt" , "w")
file_ptr_a_text.close()

for i in range(1,256):
    file_ptr = open("NAND.spice" , "r")
    file_ptr_write = open("NAND_modified.cir","w")
    A0 = (i>>0)&1
    A1 = (i>>1)&1
    A2 = (i>>2)&1
    A3 = (i>>3)&1
    B0 = (i>>4)&1
    B1 = (i>>5)&1
    B2 = (i>>6)&1
    B3 = (i>>7)&1
    file_ptr_a_text = open("a.txt" , "a")
    file_ptr_a_text.write(f"\nA3,A2,A1,A0 : {A3,A2,A1,A0}         B3,B2,B1,B0 : {B3,B2,B1,B0}\n")
    file_ptr_a_text.close()

    for line in file_ptr:
        str0 = "VinA0 A0 0 dc 1\n"
        str1 = "VinA1 A1 0 dc 1\n"
        str2 = "VinA2 A2 0 dc 1\n"
        str3 = "VinA3 A3 0 dc 1\n"
        str4 = "VinB0 B0 0 dc 1\n"
        str5 = "VinB1 B1 0 dc 1\n"
        str6 = "VinB2 B2 0 dc 1\n"
        str7 = "VinB3 B3 0 dc 1\n"

        if line == str0:
            replace_string = f"VinA0 A0 0 dc {A0}\n"
            file_ptr_write.write(line.replace(str0, replace_string))
        elif line == str1:
            replace_string = f"VinA1 A1 0 dc {A1}\n"
            file_ptr_write.write(line.replace(str1, replace_string))
        elif line == str2:
            replace_string = f"VinA2 A2 0 dc {A2}\n"
            file_ptr_write.write(line.replace(str2, replace_string))
        elif line == str3:
            replace_string = f"VinA3 A3 0 dc {A3}\n"
            file_ptr_write.write(line.replace(str3, replace_string))
        elif line == str4:
            replace_string = f"VinB0 B0 0 dc {B0}\n"
            file_ptr_write.write(line.replace(str4, replace_string))
        elif line == str5:
            replace_string = f"VinB1 B1 0 dc {B1}\n"
            file_ptr_write.write(line.replace(str5, replace_string))
        elif line == str6:
            replace_string = f"VinB2 B2 0 dc {B2}\n"
            file_ptr_write.write(line.replace(str6, replace_string))
        elif line == str7:
        
            replace_string = f"VinB3 B3 0 dc {B3}\n"
            file_ptr_write.write(line.replace(str7, replace_string))
        else:
            file_ptr_write.write(line)

    file_ptr_write.close()
    file_ptr.close()
    cmd = "ngspice NAND_modified.cir"
    os.system(cmd)