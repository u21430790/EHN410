####################################################################################
#Question 1 [50]

#1.1
LE_ans = ['88908304','949A9C57','D24DC3E3','9D079A25','46F969B2'] #[10] (from index 0 to index 4)
RE_ans = ['32106C2A','60B441BD','6A35FCE9','0936026C','AC67D47E'] #[10] (from index 0 to index 4)
C11_ans = ['555BB81048E6A0ED'] #[5]

#1.2
LD_ans = ['F61B90D1','7AD7E943','8256B493','2605CAF4','5E020204'] #[10] (from index 4 to index 0)
RD_ans = ['4BB7A718','592D751C','D8AAAA4A','B626C0BD','74858780'] #[10] (from index 4 to index 0)
P12_ans = ['5E02020474858780'] #[5]



####################################################################################
#Question 2 [30]

RC4_stream1_ans = '13C90612BC233BC1D4D21D89789AE92C5973651B' 	#[10]
C21_ans = 'D6D36000B633F1C8DC4B665BEB99C2A8887E6D5A' 		   	#[5]

RC4_stream2_ans = 'BDB1AE23E869A4FB16B2DAABD3D37FEBD188A1C2' 	#[10]
P22_ans = '9C918EAF04709CF317FF5E2BC23BF7498399A11A' 			#[5]

####################################################################################
#Question 3 [60]

X3_ans = '430151632012712D48732B4C1E2E63715F240219' #[20] #decrypted M3 (in HEX)

#For HMAC calculation
Si_ans = 'C16DA4FC'   	#[2](in HEX)
H_in1_ans = 'C16DA4FC430151632012712D48732B4C1E2E6371' #[2] input to first hash function (in HEX)
H_out1_ans = '73DD78D5' #[6] output of first hash function (in HEX)
S0_ans = 'AB07CE96' 	#[2](in HEX)
HMAC_ans = '5F240219' 	#[6] output of HMAC algorithm (in HEX)
AUTH_ans = 'YES' 	#[2] 'YES' or 'NO'

H_in1_alt_ans = 'C16DA4FC01124C73712D2E1E48712B6320516343'
H_out1_alt_ans = '5E8C3AEB' 
HMAC_alt_ans = '72754027'

P3_ans = '10011E1D02564E3D042F086F51251D4E' #[20] decrypted X3 with HMAC removed (in HEX)
P3_alt_ans = '01566F2F4E3D2551044E081D021E1D10'


####################################################################################
#Question 4 [30]

R0_41_ans = ['634B','0136','4ECC','EBBE','624E','5DA7','C862'] ; #[5] (from index 0 to index 6)
R1_41_ans = ['0136','4ECC','EBBE','624E','5DA7','C862','EFA0'] ; #[5] (from index 0 to index 6)
K_41W_ans = '09C1C862EFA0' #[5]

R0_42_ans = ['75F3','8169','E3BD','BD51','8074','98C1','4F7B'] ; #[5] (from index 0 to index 6)
R1_42_ans = ['0E41','75F3','8169','E3BD','BD51','8074','98C1'] ; #[5] (from index 0 to index 6)
K_42_ans = '4F7B98C1'	   #[5]





