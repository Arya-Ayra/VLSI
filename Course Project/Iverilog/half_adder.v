`timescale 1ns/10ps

module half_adder(A , B , sum ,carry);
    input A;
    input B;
    output sum;
    output carry;

    assign sum = A^B;
    assign carry = A&B;
endmodule