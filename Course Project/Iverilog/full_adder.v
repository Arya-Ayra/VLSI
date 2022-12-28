`timescale 1ns/10ps

module full_adder(A , B, C, sum, carry);
    input A,B,C;
    output sum,carry;
    wire w1,x2,x3;

    assign w1 = A ^ B;
    assign x2 = A & B;
    assign sum = w1 ^ C;
    assign x3 = C & w1;
    assign carry = x3 | x2;
endmodule