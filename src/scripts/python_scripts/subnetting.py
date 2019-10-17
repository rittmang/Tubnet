import math
import sys
def next_power_of_2(x):
    return 1 if x == 0 else 2**(x - 1).bit_length()

def string_to_ip(ip_addr_bin_1):
    ip = str(int(ip_addr_bin_1[0:8:1],2))+"."+str(int(ip_addr_bin_1[8:16:1],2))+"."+str(int(ip_addr_bin_1[16:24:1],2))+"."+str(int(ip_addr_bin_1[24:32:1],2))
    return ip

def and1(ip_addr_bin_1,subnet_mask_bin_1):
    listi = list(ip_addr_bin_1)
    for i in range(0,len(ip_addr_bin_1)):
        listi[i] = str(int(listi[i]) & int(subnet_mask_bin_1[i]))
    str1 = ''.join(listi)
    return str1

def add_binary_nums(x, y): 
        max_len = max(len(x), len(y)) 
        x = x.zfill(max_len) 
        y = y.zfill(max_len) 
        result = '' 
        carry = 0 
        for i in range(max_len - 1, -1, -1): 
            r = carry 
            r += 1 if x[i] == '1' else 0
            r += 1 if y[i] == '1' else 0
            result = ('1' if r % 2 == 1 else '0') + result 
            carry = 0 if r < 2 else 1     # Compute the carry. 
          
        if carry !=0 : result = '1' + result 
  
        return result.zfill(max_len)


def do_stuff(s,u):
    prefix_length=0
    ip_addr_bin = ""
    while True:
        ip_address = s
        print("Your IP is ",s)
        a = ip_address.split('.')
        ip_addr_bin = format(int(a[0]),'b').rjust(8,'0')+format(int(a[1]),'b').rjust(8,'0')+format(int(a[2]),'b').rjust(8,'0')+format(int(a[3]),'b').rjust(8,'0')

        print("IP in binary = ",ip_addr_bin)
        if(len(a) == 4):
            if(int(a[0]) <= 255 and int(a[1]) <= 255 and int(a[2]) <= 255 and int(a[3]) <= 255):

                if(int(a[0]) in range(1,127) and int(a[3]) in range(1,255)):
                    print(ip_address," belongs to Class A"," with subnet 255.0.0.0")
                    prefix_length = 8
                elif(int(a[0]) in range(128,192) and int(a[1]) >= 1 and int(a[3]) in range(1,255)):
                    print(ip_address, " belongs to Class B", " with subnet 255.255.0.0")
                    prefix_length = 16
                elif (int(a[0]) in range(192, 224) and int(a[2]) in range(1,255) and int(a[3]) in range(1, 255)):
                    print(ip_address, " belongs to Class C", " with subnet 255.255.255.0")
                    prefix_length = 24
                elif (int(a[0]) in range(224, 240)):
                    print(ip_address, " belongs to Class D", " with subnet reserved for multicasting")
                elif (int(a[0]) in range(240, 255) and int(a[3]) in range(1, 255)):
                    print(ip_address, " belongs to Class E", " reserved for research")
            break
        else:
            print("Enter a valid IPv4 address")
            continue
    #print("Your default prefix length is ",prefix_length)
    #print("Change? Y:N")
    #opt = input()
    #if opt == 'Y':
    #   prefix_length = int(input("Enter prefix length:"))

    number_of_subnets = next_power_of_2(int(u))
    print("Closest subnets obtained=",number_of_subnets," while entered was ",u)
    add_bits = int(math.log2(number_of_subnets))
    prefix_length += add_bits
    subnet_mask_bin = "1"*prefix_length+"0"*(32-prefix_length)

    prefix_length-=add_bits
    print("Subnet Mask = ",subnet_mask_bin," ",string_to_ip(subnet_mask_bin))

    number_of_addresses = 2**(32-prefix_length)

    addresses_per_block = int(number_of_addresses / number_of_subnets)
    print("Thus, addresses per subnet = ",addresses_per_block)
    #To check total addresses in network: print(number_of_addresses)

    n_sub = 32 - int(math.log2(addresses_per_block))
    number_of_positions_cleared = int(math.log2(addresses_per_block))
    range_start,range_end=[],[] #lists to hold the starts and ends of lists in order, so returning is easy
    start_ip = and1(ip_addr_bin,subnet_mask_bin).ljust(32,'0')

    for i in range(1,number_of_subnets+1):
        range_start.append(string_to_ip(start_ip))
        last_ip = bin(int(start_ip,2)+int("{0:b}".format(addresses_per_block-1),2))
        last_ip = last_ip[2:].rjust(32,'0')
        range_end.append(string_to_ip(last_ip))
        start_ip = add_binary_nums(last_ip,"1")
    return range_start,range_end
    
if __name__ == '__main__':
    ss = [
        "192.168.1.1"
    ]
    u=5 #u is number of subnets basically
    for s in ss:
        range_start,range_end = do_stuff(s,u)
        print('Output of {} = {},{}'.format(s,range_start,range_end))

