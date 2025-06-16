import numpy as np

# BLOWFISH
#GIVEN
K1 = '659F94E9'
P11 = '8890830432106C2A'
C12 = 'B28BCB76F804598E'
Sbox1 = ['5582B2D0','14D882D1','2E2F58F9','4E65ADD3','2CDBD51A','E9BA6B6B','539A24C3','BD757524','C70F1F69','467CF97B','5F199D2C','EF2E3115','C7449EB9','0370592C','69B56C85','341C54DD','29A29807','1FFEF8D4','DBFCAA65','780EB01D','70894322','6BBD0F42','44E2D075','3880BDC2','1FBE729B','03686F7E','49513497','EA424297','F0E9AA89','27A49382','C54E44D2','A2189A7D','4C25D959','F0050290','16D263BD','F3C848DF','4FC33230','C8231E2E','610C6BF6','3DF3C8D5','4A6CD29C','7AB9DDF4','DBACD51A','2B85B8A8','4E9B7279','9296F007','3382E7C1','EC2E269F','A22D382D','65D11E8A','F8BF39DD','EA16D74C','755AB171','828237BA','0F5A604F','7E0CFDA5','E487E65A','0DC0F1F0','30B0BB7B','192F7E4A','5BA3BB63','6C117C6F','6B2C61BA','2F28B25F','9FDEA5D9','ECB61BFD','24EB5635','D45F2DA6','6793A386','7DE93BAB','482837BD','36D3B37A','F50871BE','5656CAEE','D9ED8BF2','C28DC729','CA1E44BF','612A7AF7','59B25E8C','807A30B7','13958A95','1F65A28A','F5872298','3AE5846E','E9A10ADC','9BE95A05','7E89E91C','E5BAB157','8C5E9DEE','D1C6537D','0FAB69B2','6BB8474A','27951881','299BC85F','A92F756D','42BCEF61','F8F7EF27','257027C9','C5A35AE2','E64BBAA4','A5426F6F','A9ADA7C0','BFB0EE7C','9A201B83','041B1121','65DCE4F6','33EC5C07','2240C271','4980A839','FF47701F','CF49ECF4','9BE69B15','FF0CF99E','BE6F6F72','432C1BAB','BD34F631','8546BA3E','2FB48FE6','41DD5468','77862F41','0E8C6170','60F548AF','5E69EE82','8242D7F2','3EE714CC','7F30FF25','BF87AD0F','33F4CFC9','39DE4974','A3623B21','2A837F13','C2742E6F','EE19A551','7D984E17','4FDB8EC3','D44A35A8','CAD810B0','2E8FB00A','214A794A','6A484501','C0A1E9AA','BE4D9097','BCF642B9','DE664531','55552F41','18A93375','312FFF6D','27C4214B','0ADB834E','4F8A6502','C2D0A234','5F8EE1D2','9469FE99','B3750E04','DBC34650','229BCF0C','48CBE986','89571AC4','5A948004','F81EB177','B9E63F0E','77602C94','94DFB347','F10BBEED','1345BB35','C15B7FC4','93E80F80','1059EEA2','ECDA9E47','D2F733BF','6A3ADC9B','42513F9C','02C3A54B','F35391AD','53CD484D','B4E073AE','7C8B4C31','34D1BB18','55A7EF9C','CFB6FDCC','A2F1D82D','975E005D','833BDA38','7FF831C4','4BAB2F39','E62C7932','CF6668D1','F1285F48','FF9122C3','E1DDC4EF','62D7254B','9BC06FDC','FFDE9682','80786A27','37394E4C','49E62E11','A4C25601','0644D8CD','0C3B7DF0','1F87DD44','0524768D','D56DD17B','794C330F','B8B8243B','5B9AD548','F2A1FC25','507A3E68','F9867F41','CD1283CE','22BD2B3D','4DCFDAD5','71849AAB','36157480','200B10A6','9C307649','ABCDA0DC','AEC42C0E','16E7EA18','DE73A736','4E970AFF','C5BD65BA','E5EEBD1A','5151E5BD','4ED947D1','5936283A','770861BB','8DBC8C73','4501943F','2190D098','4E9045C7','CEE618A8','6E0AAFFB','3718F726','DC249709','704FA347','39611F27','5F86F66B','0F2A265C','3974EFAA','A662D48F','D15C38BC','1654F0E1','8E0BBA65','3B79C063','4161EE73','7CB2D90A','31DD28DF','DC0298FF','A74578E8','4BCC4CC5','571835A2','7F26138A','BAC1207F','C64B3CF0','5A2AA19F','9C0553E2']
Sbox2 = ['25F77C6F','3E36E970','1F8FBB80','7EBAF7B1','5E0158C8','F39BA458','B103571D','4992629B','7FC548B7','85C3A1D2','F072A92E','45F18380','97E00461','71A4C6AB','E042ECEB','7D4B5534','402F9C52','AE03C2FF','341ED30E','CF9DDEE5','848245ED','4918911A','4457EF17','601D6564','3221880F','C5F6271E','E2D6C3C9','84847AB5','C4B0B13F','34A6BBF7','2A087A3D','770394F6','49B110D8','5CB9FA29','DCDAAF34','504008A9','E4A5741C','809B6D6F','D14470EB','B5944ADD','5B82A71D','02D3C31A','05AE18B5','C313E8D4','02B01793','ADEF721C','3A411080','F2B5F6A7','B334DAAE','2C7033DF','1CA0EB9E','90FA6C34','82AE6132','5BA26F27','F5929A09','4669E6CC','0B30D445','00A370B2','5974890E','6190F6EB','5D31F203','754BAE03','062A3ADE','AED7A63F','FBDA69EC','81B08F72','AE21E621','B3C61F85','A5F18F72','D1C5228C','33CE2A75','A5EB34F6','DDF84A66','15B54009','66DC9368','8CFE9042','1FB06126','8AC4DD25','D7245B29','004DC264','6D3D28EA','D6B7804A','96277563','6D64DE53','07ECB601','CF631E22','2220CD52','20CC2598','43F65086','63529B85','707338A6','B9A1B4AD','3BF94EAB','E9CD5129','E6C07412','3A36A58E','C0B2EFD7','23EE172D','9885D60E','92D62394','02B5D787','6903A242','6F488C0F','53C6313F','6ADA7935','2109D3E4','0A0005D1','6147273E','2DCED41F','9167165A','F9643F5F','8AF3EEB0','05D1C0D9','F6EA7963','90C21426','639DC2C8','BC43870E','2010F513','38640801','D9C135F1','F905A755','7775193C','8B62834A','2A815361','0E0F1D6E','D6EEF682','B380FE4F','D28D3FD6','E6AAB415','3ED8B838','5F35825B','03F4644A','258E3A3F','D2CB55E2','319F246A','9C8D357B','3AC2F58D','A8960D60','AC74CEEC','BADF75F0','CE3E09BD','58060A21','20205A9D','408CAAD0','C145BFCE','0370CA97','AC0EFA21','B6808DEE','9929A0E2','66D389A6','4B1E2E7F','F1F8A87B','9D3FC9D6','934F5427','A9276C75','C10ACEA1','F2C6165A','268F7F58','CB79E433','DFB40489','F34D7A11','B2204E45','87A307AF','C93A6C9D','8E775F13','17DCC84B','86ED1FC9','1FB55BAF','EF8BC45B','097C9C8E','08D85A11','16A76527','88735346','181D16F7','92F39DBD','7BA07A25','41AB1A35','1A2E7438','B8C39475','C1D9C1F9','1DF7F87A','D5DF0F47','8F152291','7EAA74E2','C3D1E160','5BF07584','D2B40F7E','77F04A35','EC4230FA','17DE9DB7','AD6799DD','F9FDC0A1','830259EF','DA8E0AA4','46DEED18','AFF0B0D7','40CFEB0F','5DC0E134','A1EF4AB9','06ED41B8','D07D53AE','B661990C','BD4117EA','849A3D91','0CB13F8D','9EC2FEB5','DB1EE951','F7A38E76','2EBFCCDF','42573D53','3D72DEB8','FE1B041A','03B6378C','80CF2B8A','B709A351','7821F3F1','F5F35D65','6A04065C','CA1A570A','41914BE1','CB4082A5','574F1328','695B9C61','B0AA1E5D','08F212CA','8D8ADDC3','5C2DEE8F','28A017F9','12C8281F','0595F8AA','8A2D525F','8CD069FF','5B188139','186C57A6','B30E2868','42139410','45BF0CFF','C9833FBE','4E8DE6C4','E5FC1968','02A823FC','6DF321A5','3500F573','A93AD088','76673237','C090E068','F6EAD3EC','FB5B6EDA','4E888FC7','9D3D173D','584128CC','FE8049E2','D7DCF494','538229D8','24EE4117','A32178AE']
Sbox3 = ['9B21CFB3','646DE5EB','055F0962','AA30AAF8','24F6FBF3','9CB50F26','EE1C7DF7','71C34CAD','4E3A965B','574E1133','898E3C0C','85C368E6','B6D11B92','9E05420B','11B32EBD','E1F28A35','7D79DF04','9873D72A','27A1EA9C','AD5DDEA5','EB2DE5E6','E6FDAC1E','58511FE0','78E765F0','F040B692','840A5D05','75D5ED36','414721FD','E9E3DEEE','DD424A94','AD418635','8DDD8731','850A2615','D9C80E5E','404B0B0E','DAD142BB','CC0F8C98','9861134A','3D650536','D2DA1000','3EC29DBF','394E4F3A','B495902E','4C66E991','7FEEC81E','CADD3961','BC1BFF0A','9211760A','9254D472','92817A5D','B65BC1A8','B896BCE2','7F7C1E1B','0B37626A','7A54FCB2','192BB92D','CD343CA2','102EC526','10667D80','5690E9BC','91859595','F5BFB122','FFA8DF5A','12EDD9E2','F89D9951','91705989','2EA77DDE','9B5EE8B8','D2B3F327','047BEEF9','423F90CC','6A98BE6C','7E224518','5C7722EF','8BC33618','CA54A14D','63B6E89D','A80BC914','F75D10F0','B3D0D9D3','F390446E','D94C7A5D','58F95D3F','A8EBBA89','781887A5','22BCF358','9A76E662','6C6C90EB','2EFF62AC','8554E203','AB3507D8','DD9C300E','3363BEEB','AC8CFDB6','B85271B9','452CF04F','29AAE986','584B9739','EFD5F7DA','9940ECE7','F0A7DA80','19AD2A5F','D86165E7','8DEB503B','10969FDA','84CC369D','35C42B9A','B5F00D8B','1D6D9760','BF697A4C','F097D429','DC1FC90C','9766BDAD','1E119F83','0E7B5F86','0BC367E4','A5508E55','7ED29156','50959595','8E0704D6','7B5FC25E','4E86AE9B','42503620','7F2811D1','09193BAD','A73C1C32','4E3C9084','5F3BB038','F4873C47','D16C5060','66E16ACC','AF4F36C6','4E66A663','B42755A2','5B8B3706','D683524C','BDB68C40','9EB3BD31','29D8FBDD','308C072E','A59C3016','A531FB37','7632AB69','F8DF6CF0','D52AA401','4320B178','8BD0CA5B','E2507330','265B0CE1','F87E0767','9D27992B','D82B540B','D71A1ED2','1CDA45C6','6D675ADE','9D3E5258','5BD6C976','8B7954D6','90FC6D00','2271DFA4','3E3E188B','0259401B','024C482D','15E6868E','8AF815DA','0698176F','BC139B56','ECAD5A49','1D027BFF','C050C3F8','36B315CB','923728B3','47A2729F','2DD110A5','911E9A50','47C5F09D','F0B1E868','21C4A73B','B3D62E08','9B9165D5','22CCC8FB','D0CF298B','EAE6C70F','FD384941','06371F44','9C82898D','C4A480F3','1C15751F','40ABD7A0','096DC830','04585498','009BADD0','D205590E','4D9ECB4A','BD1DBE2F','60E64F64','AFE7CD54','93C013F6','93C2254E','CDCFAD1A','0E026071','AEA0504A','108C00BD','FFBAC5AC','8DDBC744','6790CD5C','E178308B','26428B52','D3710357','1E42F358','1F2140BB','5759229B','14DF8483','06CD9C4A','99ED4391','B45D32FC','BE745493','5A6CCB4B','4E4E394F','B7E63C7C','3BE72A60','4A525855','715756BA','F9CF6026','E87ABD15','9F3F8DC3','E713CCCE','8004E417','B0D4FBEA','2FC15551','E0EE069C','320E0476','54C1D324','96C0EBCF','6B7BBF0A','7A8F4478','DC2F9CA4','99823F69','6A81C606','D737D5CB','7A5F8524','3A6CAB97','1589E537','1FD781EB','28432C45','16696214','80C8B78B','00E40E30','7AF192E2','743DF944','D909F21B','ED1859A1','D5D76693','3B241C66','280B14F7','CF13B238']
Sbox4 = ['5FBB89CF','94B702CD','9CD9E188','99299527','1F5871AD','EC938A73','971EC5E5','FBCF90EA','4484CBFE','82BC9A3A','156059A9','C4F144E6','963EB269','1E09C74B','CE14A68E','01714859','C4A9FECF','83250697','87DD3769','9B995D68','93FBBA89','D88181FD','59C6E738','ED250197','FFBC0C4F','DD43D422','36A2F5F4','D369967A','A086F33E','A2BE71B2','D94A46C8','EFC43B5D','E9872F24','6434B3D3','2E81F2D4','7E9DD605','0E4E62ED','6924831F','A6ED5EFB','8BB5B62F','2102605F','380D039D','69F73E7A','C692F66B','4BFAE8AF','2865A032','628D28ED','66F11D37','7D36E7E8','A60BBD70','93DB82C9','85C6D256','396D42A5','44865B34','873E925B','8539CED9','AD8BC2E1','8D291B5B','6742C76B','BACAB765','3EE89341','4FDF8DF0','EE015873','DF875AC8','A0EDEF11','A423D043','A32F1DC1','483CFB34','586BA9A4','58F6EF2E','D8133C60','F0CD7AEA','0915B7AE','CC708E21','A4DF17FA','2AF7337D','1EA74D0C','A02F974D','2DC56D62','3EEEC25A','74C3E4F5','DEFB0587','C39B2D26','8C8CDE3F','8DC3E8BF','CE7CBCBC','87975F4C','52C618D7','B606CC1F','B17D6E96','4837BD57','1F05EA09','9EFED401','2398C6F9','019CCF2C','B8A697B1','71A19A1A','75700460','D2C07AE3','DFA3BD6F','53E15D89','639E34B4','80402C99','8BA2F056','1486144F','78196DC4','C8F065A2','2DBFC16A','41830CDC','97C5DFE5','789D7113','9B6B6751','C48A1074','6FCDA383','DE83D9DF','E241A3E0','57866B0E','57B3BA45','40091D43','6CC6B48D','D79402BD','E872A66E','701C733F','CC38A363','741A6525','0EDBE117','0A157B29','3FAA8B5F','304246F2','5D3EA5A3','8BE2D3A9','2AD5655A','EF48DA21','7156CF84','0C48001E','3C07F658','D0BA0233','04B18A3C','DD56BDB1','C4FEDBCE','8E955BD0','DB53F964','80F47F4C','395BF112','594C01CE','EDD841C2','0AF0FE37','7F4BFFBC','56882041','1116CB7C','20C38337','CB8014A0','8BDD8BD9','6AC174C1','463232EB','576622A9','46BA3EEC','23CA0168','1B8A4ECE','871B646D','1BD22CE7','03642718','4863085F','F94DE472','3C299FBC','1E545718','F7889E77','B38020D2','B86A491A','ECEE507C','BB0C07C6','1112F6FB','520A6C83','F5BDE6A5','C83E379B','F5E250FD','4FA77B4E','2AB7DEBB','5C3B46E7','3BB3015E','A27737BD','A3C97066','ED254D23','1DF6C5A8','254529FC','7AC271D8','E5925089','6B9D67F8','0D704312','D2FABEA9','6AC7C0BD','46961CAA','28F403DB','0210B90D','8D146C28','65544F0A','53367629','669FEF28','88A83CEC','79FC5BFE','615FBD1E','4EE5CE2C','B77CB003','D1AB913C','A8B8518C','1A009C20','E5C96653','E2097961','414B9CDC','681D351C','6D89F00B','464AAB28','2E2E16D7','AD7A498D','6149AB62','D81A8661','CF5588C9','2A450F2C','0B2E7343','0951518D','51CD3F86','6BEDA86F','E5D5080B','E7B28456','CE998AF5','DDE1F0D6','779C8024','01BC7FDC','D651C824','84810DFA','31CDCFCC','041CAB0B','6561756E','0F60D7ED','779D3D90','BC47501C','66B06388','392FA5FC','1408F07A','9DEEC2DB','D38332A9','E53A89FF','3E19913D','41EA0B95','033CB439','6E91D37B','A742136F','2A9EC129','65F7C7D8','257CC65E','4E18932E','1336A1F4','194C0380','DE6FC52F','67008485','36705D53']

P = ['8DBB5650','9B30F457','BEE45566','54FFDAB2','6B805DB6','9CA3F887','083377D8','A340D055']

# XOR P AND S BOXES
def xor(hex1,hex2):
     xor = int(hex1,16)^int(hex2,16)
     return f"{xor:08X}"

def init_p_s(P,K1): 
    for i in range(len(P)):
        P[i] = xor(P[i],K1)
   
    for j in range(len(Sbox1)):
        Sbox1[j] = xor(Sbox1[j],K1)
        Sbox2[j] = xor(Sbox2[j],K1)
        Sbox3[j] = xor(Sbox3[j],K1)
        Sbox4[j] = xor(Sbox4[j],K1)
    
# FN FUNC
def fn(input_32):
    input = input_32.zfill(8)
    split = []
    for i in range(0,len(input),2):
        split.append(input[i:i+2])
        
    idc_1 = Sbox1[int(split[0],16)]
    idc_2 = Sbox2[int(split[1],16)]
    idc_3 = Sbox3[int(split[2],16)]
    idc_4 = Sbox4[int(split[3],16)]

    o1 = xor(idc_1,idc_2)
    o2 = xor(o1,idc_3)
    return xor(o2,idc_4)
    
def blowfish_encrypt(plaintext):
    
    init_p_s(P,K1)
    plaintext= plaintext.zfill(16)
    left = plaintext[0:8]
    right = plaintext[8:16]
    
    l_arr = []
    r_arr = []
    l_arr.append(left)
    r_arr.append(right)
    
    for i in range(4):
        l_xored = xor(left,P[i])
        fned = fn(l_xored)
        left = xor(right,fned)
        right = l_xored

        l_arr.append(left)
        r_arr.append(right)

    temp = left
    left = xor(right,P[5])
    right = xor(temp,P[4])
    
    print(f"LEFT ARRAY: {l_arr}")
    print(f"RIGHT ARRAY: {r_arr}")
    return left+right




def blowfish_decrypt(cipher):
    
    init_p_s(P,K1)

    cipher= cipher.zfill(16)
    left = cipher[0:8]
    right = cipher[8:16]
    
    temp = left
    left = xor(right,P[4])
    right = xor(temp,P[5])
    
    l_arr = []
    r_arr = []
    l_arr.append(left)
    r_arr.append(right)
    
    for i in range(3,-1,-1):
        fned = fn(right)
        temp_right = right
        right = xor(left,fned)
        
        left = xor(temp_right,P[i])
        
        l_arr.append(left)
        r_arr.append(right)
    
    print(f"LEFT ARRAY: {l_arr}")
    print(f"RIGHT ARRAY: {r_arr}")
    return left+right
#print(blowfish_encrypt(P11))
#print(blowfish_decrypt(C12))

# RC4
K21 = "40636BA3CF45D7BDD32E"  
P21 = 'C51A66120A10CA0908997BD293032B84D10D0841'  

K22 = 'EF7288A2AA702CB1EC5F'  
C22 = '2120208CEC193808014D848011E888A2521100D8'  


def hex_to_bytes(hex_string: str) -> list:
    return [int(hex_string[i:i+2], 16) for i in range(0, len(hex_string), 2)]

def bytes_to_hex(byte_list: list) -> str:
    return ''.join(f'{b:02X}' for b in byte_list)

def rc4_Init_S_T(key):
    S = []
    T = []
    keylen = len(key)
    for i in range(256):
        S.append(i)
        T.append(key[i % keylen])
    return np.array(S), np.array(T)

def rc4_Init_Permute_S(sArray: np.ndarray, tArray: np.ndarray):
    j = 0
    for i in range(256):
        j = (j + sArray[i] + tArray[i]) % 256
        sArray[i], sArray[j] = sArray[j], sArray[i]
    return sArray

def rc4_Generate_Keystream(length: int, sArray: np.ndarray):
    i = 0
    j = 0
    keystream = []
    for _ in range(length):
        i = (i + 1) % 256
        j = (j + sArray[i]) % 256
        sArray[i], sArray[j] = sArray[j], sArray[i]
        t = (sArray[i] + sArray[j]) % 256
        keystream.append(sArray[t])
    return keystream




def rc4_encrypt_decrypt(hex_input: str, hex_key: str) -> str:
    key_bytes = hex_to_bytes(hex_key)
    input_bytes = hex_to_bytes(hex_input)

    S, T = rc4_Init_S_T(key_bytes)
    S = rc4_Init_Permute_S(S, T)
    keystream = rc4_Generate_Keystream(len(input_bytes), S)
    #print(bytes_to_hex(keystream))
    
    result_bytes = [b ^ k for b, k in zip(input_bytes, keystream)]

    return bytes_to_hex(result_bytes)


# --- Encryption ---
C21 = rc4_encrypt_decrypt(P21, K21)
#print(f"Encrypted C21 = {C21}")

# --- Decryption ---
P22 = rc4_encrypt_decrypt(C22, K22)
#print(f"Decrypted P22 = {P22}")

# HMAC

    # STEPS:
    # 1. Decrypt M3 with custom cipher
    # 2. Split message and og HMAC
    # 3. Calculate HMAC from message
    # 4. Compare expected HMAC and og HMAC
    # 5. Decrypt message with RSA

K3 = '4E0EFD31'
M3 = 'ECC87B335A336485D19CD9B13B8F62548E943467'

custom_P = '902081C0'

def custom_encrypt(input,key):
    input = input.zfill(8)
    swapped = input[4:8] + input[0:4]
    swapped_bin = list(bin(int(swapped,16))[2:].zfill(32))

    shifted = np.roll(swapped_bin,-1)
    new = ''.join(shifted)
    newer = int(new,2)

    return f'{newer^int(key,16):08X}'

def custom_decrypt(input,key):
    xored = int(input,16)^int(key,16)
    swapped_bin = list(bin(xored)[2:].zfill(32))
    shifted = np.roll(swapped_bin,1)
    new = ''.join(shifted)
    newer = f'{int(new,2):08X}'

    return newer[4:8]+newer[0:4]

def block_chain_decrypt(ciphertext_hex, key_hex):
    output = ''
    prev_cipher = '00000000'  # IV = 0

    for i in range(0, len(ciphertext_hex), 8):
        cipher_block = ciphertext_hex[i:i+8]
        decrypted = custom_decrypt(cipher_block, key_hex)
        
        # XOR with previous ciphertext (or IV for first block)
        plain_int = int(decrypted, 16) ^ int(prev_cipher, 16)
        plain_hex = f'{plain_int:08X}'
        output += plain_hex
        prev_cipher = cipher_block  # Update chaining

    return output

X3 = block_chain_decrypt(M3,K3)

K_h=   0xF75B92CA

IV_h = 0x87FEB45A
ipad=  0x36363636
opad = 0x5C5C5C5C
og_HMAC = X3[32:]

#print(f"Encrypted Message = {X3[0:32]}")
#print(f"Received HMAC = {X3[32:]}")
#print()

Si = f'{ipad^K_h:08X}'
S0 = f'{opad^K_h:08X}'

m_Si = Si+ X3[0:32]

#print(f'INPUT TO FIRST HASH = {m_Si}')
blocks =[]

for i in range(0,len(m_Si),8):
    blocks.append(m_Si[i:i+8])

hash = IV_h
for b in blocks:
    hash = hash^int(b,16)

hash = f'{hash:0X}'
#print(f'FIRST HASH = {hash}')

m_S0 = S0 + hash

blocks =[]
for i in range(0,len(m_S0),8):
    blocks.append(m_S0[i:i+8])

hash = IV_h
for b in blocks:
    hash = hash^int(b,16)

hmac = f'{hash:0X}'
#print(f'SI  = {Si}')
#print(f'S0 = {S0}')
#print(f'Expected HMAC = {hmac}')
#print(f'Received HMAC = {og_HMAC}')

message = X3[:32]
dec = ""
for i in range(0,len(message),2):
    b= int(message[i:i+2],16)
    ans = pow(b,5,119)
    dec+= f'{ans:02X}'
#print(dec)


### KEY WRAPPING

#WRAP
K_41 = '634B0136'
K_E41 = 'B2890380'

# UNWRAP 
K_42W = 'A41675F30E41'
K_E42 = 'A6C2CD38'


n = 2
s = 3 * n

p = ['634B', '0136']

c = ['A41675', 'F30E41']
c = [ 'A416', '75F3' ,'0E41']
def keywrap():
    A = np.empty([s + 1],dtype='<U4')
    R = np.empty([s + 1, n],dtype='<U4')
    A[0]= 'A6A6'
    for i in range(1,n+1):
        R[0,i]=p[i-1]

    for t in range(1,s+1):
        w = custom_encrypt(A[t - 1] + R[t - 1, 1], K_E41)
     
        val_A =f'{t^int(w[:4],16):04X}'
        val_R = w[4:].zfill(4)
        R[t,n] = val_R
        A[t] = val_A
        for i in range(1,n):
            R[t,i] =R[t-1,i+1]
    
    C = A[s]
    print(f"A : {A}")
    print(f"R : {R}")
    for i in range(1, n):
        C += R[s, i]
    return C


def keyunwrap():
    A = np.empty([s + 1],dtype='<U4')
    R = np.empty([s + 1, n ],dtype='<U4')
    A[s] =  c[0]
        
    for i in range(1,n+1):
        R[s,i] = c[i]
    
    for t in range(s,0,-1):
        temp = f"{int(A[t],16)^t:04X}" + R[t,n]
        w = custom_decrypt(temp,K_E42)
        A[t-1] = w[:4]
        R[t-1,1] =w[4:].zfill(4)      
        for i in range(2, n + 1):
            R[t - 1, i] = R[t, i - 1]

    P = ''
    # n+1 instead of n
    for i in range(1, n + 1):
        # R[0,i] instead of R[s,i]
        P += R[0, i]
    print(f"A : {A}")
    print(f"R : {R}")
    return P

#print(keywrap())
print(keyunwrap())
