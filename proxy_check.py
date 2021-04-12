import requests
import sys

args = sys.argv
args.remove(sys.argv[0])

index = 0

if len(args) < 1:
	print("[!] ERROR: at least one argument is requiered")
	usage()
	exit()

for arg in args:
	index = index + 1
	if arg == "-f" or arg == "--filename":
		filename = args[index]
	elif arg == "-p" or arg == "--protocol":
		proto = args[index]
	elif arg == "-o" or arg == "--output":
		output_filename = args[index]
	elif arg == "-t" or arg == "--timeout":
		timeout = args[index]

try:
	with open(filename, "r") as f:
		proxy_list = f.read().split("\n")
except:
	print("[!] ERROR: wrong path for proxies file")
	exit()

output_file = open(output_filename, "w")


url = "https://google.com" #TODO: this most be able to change

for proxy in proxy_list:
	try:
		r = requests.get(url, proxies = {proto: f"{proto}://{proxy}"}, timeout = int(timeout))
		if r.ok:
			print(f"[+] {proxy}: Ok")
			output_file.write(proxy+"\n")
		else:
			print(f"[-] {proxy}: time out")
	except Exception as ex:
		print(ex)