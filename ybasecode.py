import base64

# BASIC TEMPLATE OF HOW ENCODE/DECODE WORKS STEP BY STEP------------------------
# code = base64                     -> honestly its just a holder for everything
# dl = "hey"                        -> value for input
# dd = code.a85encode(dl.encode())  -> the machine to put it into coded bytes 
# do = code.a85decode(dd)           -> the machine to get bytes to normal bytes 
# ld = do.decode()                  -> the bytes to str
# print()                         -> the check to make sure it worked 
#-------------------------------------------------------------------------------
# Encoding
class ENCODER:
    coder = base64
    def encode_a85(input:str):
        return ENCODER.coder.a85encode(input.encode())
# Decoding
class DECODER:
    coder = base64

    def decode_a85(input:bytes):
        return ENCODER.coder.a85decode(input).decode()
# Test Area
if __name__ == "__main__":
    ins = ENCODER.encode_a85("hello world")
    out = DECODER.decode_a85(ins)
    print(out)