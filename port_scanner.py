import os
import sys
import time
import socket
import argparse
import datetime
from time import gmtime, strftime

port_list = ["TCP Port Service Multiplexer (TCPMUX)", "Remote Job Entry (RJE)", "ECHO", "Message Send Protocol (MSP)", "FTP — Data",
"FTP — Control", "SSH Remote Login Protocol", "Telnet", "Simple Mail Transfer Protocol (SMTP)", "MSG ICP", "Time", "Host Name Server (Nameserv)",
"WhoIs", "Login Host Protocol (Login)", "Domain Name System (DNS)", "Trivial File Transfer Protocol (TFTP)", "Gopher Services", "Finger", "HTTP", "X.400 Standard",
"SNA Gateway Access Server", "POP2", "POP3", "Simple File Transfer Protocol (SFTP)", "SQL Services", "Newsgroup (NNTP)", "NetBIOS Name Service",
"NetBIOS Datagram Service","Interim Mail Access Protocol (IMAP)","NetBIOS Session Service", "SQL Server", "SNMP", "Border Gateway Protocol (BGP)",
"Gateway Access Control Protocol (GACP)", "Internet Relay Chat (IRC)", "Directory Location Service (DLS)","Lightweight Directory Access Protocol (LDAP)",
"Novell Netware over IP", "HTTPS","Simple Network Paging Protocol (SNPP)","Microsoft-DS","Apple QuickTime","DHCP Client","DHCP Server","SNEWS","MSN",
"SOCKS"
]

banner = ("""\033[1;32m
  ____   ___  ____ _____   ____   ____    _    _   _ _   _ _____ ____  
 |  _ \\ / _ \\|  _ \\_   _| / ___| / ___|  / \\  | \\ | | \\ | | ____|  _ \\ 
 | |_) | | | | |_) || |   \\___ \\| |     / _ \\ |  \\| |  \\| |  _| | |_) |
 |  __/| |_| |  _ < | |    ___) | |___ / ___ \\| |\\  | |\\  | |___|  _ < 
 |_|    \\___/|_| \\_\\|_|   |____/ \\____/_/   \\_\\_| \\_|_| \\_|_____|_| \\_\
                                                                       
            
            |---------- Coded by nightowl -------------|\033[0m
""")

def main():
	os.system("clear")
	print(banner)
	args = argparse.ArgumentParser()
	args.add_argument("--ip", help="Enter to ip address")
	user_args = vars(args.parse_args())
	ip = str(user_args["ip"])
	try:
		question = str(input("[+] Do you wanna start (y/n)-> "))
		if(question == "y" or question == "Y"):
			port_scanner(ip)
		elif(question == "n" or question == "N"):
			exit_func(ip)
	except KeyboardInterrupt:
		sys.exit(0)


def port_scanner(ip):
	try:
		start_time = datetime.datetime.now().strftime("%H:%M:%S")
		total = 0
		print("\n[+] Port Scanner Started...\n")
		print("[+] Start Time -> ",start_time,"\n")
		print("\t---------------------------------\n")
		print("\tPORT NUMBER     |     DESCRIPTION\n")
		print("\t---------------------------------\n")
		for port_number in range(0, 1081):
			sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			result = sock.connect_ex((ip, port_number))
			if result == 0:
				if port_number == 1:
					print("\t",port_number , " -> " ,"\t",port_list[0])
					total = total + 1
				if port_number == 5:
					print("\t",port_number, " -> ","\t",port_list[1])
					total = total + 1
				if port_number == 7:
					print("\t",port_number, " -> ","\t",port_list[2])
					total = total + 1
				if port_number == 18:
					print("\t",port_number, " -> ","\t",port_list[3])
					total = total + 1
				if port_number == 20:
					print("\t",port_number, " -> ","\t",port_list[4])
					total = total + 1
				if port_number == 21:
					print("\t",port_number, " -> ","\t",port_list[5])
					total = total + 1
				if port_number == 22:
					print("\t",port_number, " -> ","\t",port_list[6])
					total = total + 1
				if port_number == 23:
					print("\t",port_number, " -> ","\t",port_list[7])
					total = total + 1
				if port_number == 25:
					print("\t",port_number, " -> ","\t",port_list[8])
					total = total + 1
				if port_number == 29:
					print("\t",port_number, " -> ","\t",port_list[9])
					total = total + 1
				if port_number == 37:
					print("\t",port_number, " -> ","\t",port_list[10])
					total = total + 1
				if port_number == 42:
					print("\t",port_number, " -> ","\t",port_list[11])
					total = total + 1
				if port_number == 43:
					print("\t",port_number, " -> ","\t",port_list[12])
					total = total + 1
				if port_number == 49:
					print("\t",port_number, " -> ","\t",port_list[13])
					total = total + 1
				if port_number == 53:
					print("\t",port_number, " -> ","\t",port_list[14])
					total = total + 1
				if port_number == 69:
					print("\t",port_number, " -> ","\t",port_list[15])
					total = total + 1
				if port_number == 70:
					print("\t",port_number, " -> ","\t",port_list[16])
					total = total + 1
				if port_number == 79:
					print("\t",port_number, " -> ","\t",port_list[17])
					total = total + 1
				if port_number == 80:
					print("\t",port_number, " -> ","\t",port_list[18])
					total = total + 1
				if port_number == 103:
					print("\t",port_number, " -> ","\t",port_list[19])
					total = total + 1
				if port_number == 108:
					print("\t",port_number, " -> ","\t",port_list[20])
					total = total + 1
				if port_number == 109:
					print("\t",port_number, " -> ","\t",port_list[21])
					total = total + 1
				if port_number == 110:
					print("\t",port_number, " -> ","\t",port_list[22])
					total = total + 1
				if port_number == 115:
					print("\t",port_number, " -> ","\t",port_list[23])
					total = total + 1
				if port_number == 118:
					print("\t",port_number, " -> ","\t",port_list[24])
					total = total + 1
				if port_number == 119:
					print("\t",port_number, " -> ","\t",port_list[25])
					total = total + 1
				if port_number == 137:
					print("\t",port_number, " -> ","\t",port_list[26])
					total = total + 1
				if port_number == 139:
					print("\t",port_number, " -> ","\t",port_list[27])
					total = total + 1
				if port_number == 143:
					print("\t",port_number, " -> ","\t",port_list[28])
					total = total + 1
				if port_number == 150:
					print("\t",port_number, " -> ","\t",port_list[29])
					total = total + 1
				if port_number == 156:
					print("\t",port_number, " -> ","\t",port_list[30])
					total = total + 1
				if port_number == 161:
					print("\t",port_number, " -> ","\t",port_list[31])
					total = total + 1
				if port_number == 179:
					print("\t",port_number, " -> ","\t",port_list[32])
					total = total + 1
				if port_number == 190:
					print("\t",port_number, " -> ","\t",port_list[33])
					total = total + 1
				if port_number == 194:
					print("\t",port_number, " -> ","\t",port_list[34])
					total = total + 1
				if port_number == 197:
					print("\t",port_number, " -> ","\t",port_list[35])
					total = total + 1
				if port_number == 389:
					print("\t",port_number, " -> ","\t",port_list[36])
					total = total + 1
				if port_number == 396:
					print("\t",port_number, " -> ","\t",port_list[37])
					total = total + 1
				if port_number == 443:
					print("\t",port_number, " -> ","\t",port_list[38])
					total = total + 1
				if port_number == 444:
					print("\t",port_number, " -> ","\t",port_list[39])
					total = total + 1
				if port_number == 445:
					print("\t",port_number, " -> ","\t",port_list[40])
					total = total + 1
				if port_number == 458:
					print("\t",port_number, " -> ","\t",port_list[41])
					total = total + 1
				if port_number == 546:
					print("\t",port_number, " -> ","\t",port_list[42])
					total = total + 1
				if port_number == 547:
					print("\t",port_number, " -> ","\t",port_list[43])
					total = total + 1
				if port_number == 563:
					print("\t",port_number, " -> ","\t",port_list[44])
					total = total + 1
				if port_number == 569:
					print("\t",port_number, " -> ","\t",port_list[45])
					total = total + 1
				if port_number == 1080:
					print("\t",port_number, " -> ","\t",port_list[46])
					total = total + 1
		print("\n[+] Total Open Ports -> ", total, "\n")
		finish_time = datetime.datetime.now().strftime("%H:%M:%S")
		print("\n[+] Finish Time -> ", finish_time, "\n")

	except socket.error as sock_err:
		print("[-] Error -> ", sock_err)


def exit_func(ip):
	try:
		exit_question = str(input("[+] Do you wanna exit (y/n)-> "))
		if(exit_question == "y" or exit_question == "Y"):
			print("\n\n[+] Exiting...\n")
			print("[", end="", flush=True)
			for time_count in range(0,6):
				time.sleep(0.6)
				print("#", end="", flush=True)
			print("]\n")
			sys.exit()
		elif(exit_question == "n" or exit_question == "N"):
			port_scanner(ip)
	except KeyboardInterrupt:
		sys.exit(0)

if __name__ == '__main__':
	main()