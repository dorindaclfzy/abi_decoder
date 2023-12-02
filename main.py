import decoder
import konfig

if __name__ == '__main__':
    decoder.decodeABI(
        rpc=konfig.rpc, 
        address=konfig.address,
    )
