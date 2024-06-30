import subprocess
import ctypes, os
import time
print('VKplay net Fix 1.0\n')
print('Github > https://github.com/ErkinKraft\n')
try:
    def is_admin():
        try:
            return os.getuid() == 0
        except AttributeError:
            return ctypes.windll.shell32.IsUserAnAdmin() != 0
    if is_admin()== True:
        pass
    else:
        print('Error, please run olt as administrator')
        time.sleep(3)
        exit(0)
    try:

        interface_name = \
        subprocess.run("wmic nic get NetConnectionID", capture_output=True, text=True).stdout.splitlines()[
            1].strip()

    except:
        print('Network interface detection error')
        interface_name = input('Please enter the name of the network interface manually > ')

    dns_servers = ["8.8.8.8", "8.8.4.4"]

    for server in dns_servers:
        subprocess.run(
            ["netsh", "interface", "ipv4", "set", "dns", "name=", interface_name, "source=static", "addr=", server])

    print('Fix successfully')
    time.sleep(3)
except:

    print('Fix failed')
    time.sleep(3)

