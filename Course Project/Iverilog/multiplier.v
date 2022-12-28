`timescale 1ns/10ps

module multiplier(A0 ,A1, A2, A3,B0 ,B1, B2, B3,P0,P1,P2,P3,P4,P5,P6,CC5);

input A0 ,A1, A2, A3;
input B0 ,B1, B2, B3;
output P0,P1,P2,P3,P4,P5,P6,CC5;
wire O1,O2,O3,O4,O5,O6,O7,O8,O9,O10,O11,O12,O13,O14,O15;
wire C1,C2,C3,C4,C5,C6,C7,C8,C9,C10,C11;
wire S1,S2,S3,S4,S5,S6,S7;

assign P0 = B0 & A0;
assign O1 = B3 & A3;
assign O2 = B2 & A3;
assign O3 = B3 & A2;
assign O4 = B3 & A1;
assign O5 = B1 & A3;
assign O6 = B2 & A2;
assign O7 = B1 & A2;
assign O8 = B0 & A3;
assign O9 = B3 & A0;
assign O10 = B2 & A1;
assign O11 = B1 & A1;
assign O12 = B0 & A2;
assign O13 = B2 & A0;
assign O14 = B0 & A1;
assign O15 = B1 & A0;

// full_adder(A , B, C, sum, carry)
// half_adder(A , B , sum ,carry)

half_adder subckt1(O14 , O15 , P1 , C1);
half_adder subckt2(O11 , O12 , S1 , C2);
half_adder subckt3(O7  , O8  , S2 , C3);

full_adder subckt4(O13 , S1 , C1 , P2 , C4);
full_adder subckt5(O10 , S2 , C2 , S3 , C5);
full_adder subckt6(C3 , O6 , O5 , S4 , C6);

full_adder subckt7(C4 , S3 , O9 , P3 , C7);
full_adder subckt8(O4 , S4 , C5 , S5 , C8);
full_adder subckt9(O2 , O3, C6 , S6 , C9);

half_adder subckt10(C7 , S5 , P4 , C10);
full_adder subckt11(C8 , C10 , S6 , P5 , C11);
full_adder subckt12(O1 , C9 , C11 , P6 , CC5);

// always @*
// $display("%b %b %b %b %b %b %b %b %b %b %b %b %b %b %b",O1,O2,O3,O4,O5,O6,O7,O8,O9,O10,O11,O12,O13,O14,O15);
// $display("%b %b %b %b %b %b %b %b %b %b %b",C1,C2,C3,C4,C5,C6,C7,C8,C9,C10,C11);
// $display("%b %b %b %b %b %b %b %b", CC5,P6,P5,P4,P3,P2,P1,P0);
endmodule