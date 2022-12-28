`timescale 1ns/10ps

module main_tb;

reg A0,A1,A2,A3,B0,B1,B2,B3;
wire P0,P1,P2,P3,P4,P5,P6,CC5;

multiplier multi4 (A0,A1,A2,A3,B0,B1,B2,B3,P0,P1,P2,P3,P4,P5,P6,CC5);

initial
    begin
        $dumpfile("main_tb.vcd");
        $dumpvars(0,main_tb);

        A0=0;
        A1=0;
        A2=0;
        A3=0;
        B0=0;
        B1=0;
        B2=0;
        B3=0;

    end

always @*
    if( (P0==1 || P0 == 0)&& 
        (P1==1 || P1 == 0)&& 
        (P2==1 || P2 == 0)&& 
        (P3==1 || P3 == 0)&& 
        (P4==1 || P4 == 0)&& 
        (P5==1 || P5 == 0)&& 
        (P6==1 || P6 == 0)&& 
       (CC5==1 || CC5 == 0) )
        $display("%b%b%b%b * %b%b%b%b = %b%b%b%b%b%b%b%b\n",A3,A2,A1,A0,B3,B2,B1,B3,CC5,P6,P5,P4,P3,P2,P1,P0);

endmodule
