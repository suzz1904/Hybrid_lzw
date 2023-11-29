import io
import dataCompression
while(1):
    print("Click '1' to continue with lzw compression \n")
    choice=int(input())
    if choice == 1:
        
        print("LZW Compression\n")
        dataCompression.CompressDecompressData()

    else:
        exit()


