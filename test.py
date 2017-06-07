import subprocess
def CheckInternetConnection():
    cmd = 'ping ya.ru'
    import subprocess
    PIPE = subprocess.PIPE
    p = subprocess.Popen(cmd, shell=True, stdin=PIPE, stdout=PIPE,
            stderr=subprocess.STDOUT)
    buf = p.stdout.read()
    return 'TTL' in str(buf)
