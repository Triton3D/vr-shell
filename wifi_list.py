import subprocess
cmd_wifi_networks_list='netsh wlan show networks'
out=subprocess.Popen(cmd_wifi_networks_list,shell=True,stdout=subprocess.PIPE)
wifi_networks=out.stdout.readlines()
##print(wifi_networks)
for item in wifi_networks:
    if item.find(b'SSID')!=-1:
        print(item+b'!')
