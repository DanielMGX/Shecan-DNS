import tkinter as tk
import subprocess
import sys
import webbrowser

DNS_SERVER_1 = '178.22.122.100'
DNS_SERVER_2 = '185.51.200.2'
DEFAULT_DNS = 'dhcp'

def get_dns_status():
    
    output = subprocess.run('netsh interface ip show dns "Ethernet"', capture_output=True, text=True, shell=True)
    lines = output.stdout.strip().split('\n')
    for line in lines:
        if 'Configuration for interface "Ethernet"' in line:
            if 'Statically Configured DNS Servers' in lines[lines.index(line)+1]:
                return ' DNS: \u2713'  
    return ' DNS: \u2718'  

def set_custom_dns():
    
    subprocess.run(f'netsh interface ip set dns "Ethernet" static {DNS_SERVER_1} primary', shell=True)
    subprocess.run(f'netsh interface ip add dns "Ethernet" {DNS_SERVER_2} index=2', shell=True)
    dns_status_label.config(text=get_dns_status(), fg='green')

def set_auto_dns():
    
    subprocess.run(f'netsh interface ip set dns "Ethernet" {DEFAULT_DNS}', shell=True)
    dns_status_label.config(text=get_dns_status(), fg='red')

def launch_website():
    
    webbrowser.open('https://shecan.ir/')


root = tk.Tk()
root.title("DNS Settings")
root.geometry("300x150")
root.configure(bg="#7b4dff")


dns_status_label = tk.Label(root, text=get_dns_status(), bg='#7b4dff', fg='white', font=('Arial', 14, 'bold'))
dns_status_label.pack(pady=10)


custom_dns_button = tk.Button(root, text="Set shecan DNS", command=set_custom_dns)
custom_dns_button.pack()


auto_dns_button = tk.Button(root, text="Set Auto DNS", command=set_auto_dns)
auto_dns_button.pack()


launch_website_button = tk.Button(root, text="Launch shecan.ir", command=launch_website)
launch_website_button.pack(pady=10)


root.mainloop()