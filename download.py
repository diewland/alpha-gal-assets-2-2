from smart_download import *

#URL_DOWNLOAD = "https://cloudflare-ipfs.com/ipfs/Qma1kgKP8UESikt3RSm48pxx1xXwUAtKutG3aL9GbDsT3X/{}.png"
URL_DOWNLOAD = "https://ipfs.io/ipfs/Qma1kgKP8UESikt3RSm48pxx1xXwUAtKutG3aL9GbDsT3X/{}.png"
FROM_ID = 5001 # 1
TO_ID = 9999 # *** contract 0-9998 ***
OUTPUT_PATH = "./assets/{}.png"

smart_download(URL_DOWNLOAD, FROM_ID, TO_ID, OUTPUT_PATH)
