import os

for i in range(0 , 256):
    file_ptr = open("main_tb_pre.v" , "r")
    file_ptr_write = open("main_tb.v","w")
    A0 = (i>>0)&1
    A1 = (i>>1)&1
    A2 = (i>>2)&1
    A3 = (i>>3)&1
    B0 = (i>>4)&1
    B1 = (i>>5)&1
    B2 = (i>>6)&1
    B3 = (i>>7)&1

    for line in file_ptr:
        str0 = "        A0=0;\n"
        str1 = "        A1=0;\n"
        str2 = "        A2=0;\n"
        str3 = "        A3=0;\n"
        str4 = "        B0=0;\n"
        str5 = "        B1=0;\n"
        str6 = "        B2=0;\n"
        str7 = "        B3=0;\n"

        if line == str0:
            replace_string = f"A0={A0};\n"
            file_ptr_write.write(line.replace(str0, replace_string))
        elif line == str1:
            replace_string = f"A1={A1};\n"
            file_ptr_write.write(line.replace(str1, replace_string))
        elif line == str2:
            replace_string = f"A2={A2};\n"
            file_ptr_write.write(line.replace(str2, replace_string))
        elif line == str3:
            replace_string = f"A3={A3};\n"
            file_ptr_write.write(line.replace(str3, replace_string))
        elif line == str4:
            replace_string = f"B0={B0};\n"
            file_ptr_write.write(line.replace(str4, replace_string))
        elif line == str5:
            replace_string = f"B1={B1};\n"
            file_ptr_write.write(line.replace(str5, replace_string))
        elif line == str6:
            replace_string = f"B2={B2};\n"
            file_ptr_write.write(line.replace(str6, replace_string))
        elif line == str7:
        
            replace_string = f"B3={B3};\n"
            file_ptr_write.write(line.replace(str7, replace_string))
        else:
            file_ptr_write.write(line)

    file_ptr_write.close()
    file_ptr.close()
    cmd = "iverilog -o main_tb main_tb.v multiplier.v full_adder.v half_adder.v"
    cmd2 = "vvp main_tb"
    os.system(cmd)
    os.system(cmd2)
