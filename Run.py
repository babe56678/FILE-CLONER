import os,sys
import time
import platform
def xoss(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.06)
def Run():
        bit = platform.architecture()[0]
        if bit == '64bit':
            xoss("\x1b[1;92m[●] Congratulations ! Your Device Support this Tools 🍼🙂")
            xoss('\x1b[1;94m[●] Follow Team Github Account 🎈')
            os.system('xdg-open https://github.com/Dccs-team')
            import FILE64
        elif bit == '32bit':
            xoss("\n\x1b[1;92m[●] Congratulations ! Your Device Support this Tools 🍼🙂")
            xoss('\x1b[1;94m[●] Follow Team Github Account 🎈')
            os.system('xdg-open https://github.com/Dccs-team')
            import FILE32
        else:
            exit('\033[1;31m[●] Connection Or Network Error 🤕')
Run()
