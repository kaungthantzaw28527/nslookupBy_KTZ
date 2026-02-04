import dns.resolver
import socket

def nslookupbyKTZ():
    print("="*30)
    userinputdomain = input("Enter Domain : ").strip()
    print("---- information ------")
    try:
        ip_address = socket.gethostbyname(userinputdomain)
        print(f"[*] IPv4 Address : {ip_address}")
    except:
        print("[!] Could not resolve IPv4 address.")

    try:
        mx_records = dns.resolver.resolve(userinputdomain, 'MX')
        for mx in mx_records:
            print(f"[*] Mail Server  : {mx.exchange} (Priority: {mx.preference})")
    except:
        print("[ ] No MX records found.")

    try:
        ns_records = dns.resolver.resolve(userinputdomain, 'NS')
        for ns in ns_records:
            print(f"[*] Name Server  : {ns.to_text()}")
    except:
        print("[ ] No NS records found.")
    
    print("="*30)

if __name__ == "__main__":
    nslookupbyKTZ()

#owner = kaunglinux.dev@gmail.com,kaungthantzaw28527@gmail.com
#owner's git account = kaungthantzaw28527 , kaung-linux
