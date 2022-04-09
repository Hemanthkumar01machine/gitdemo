def transmitter(data,sec):
    under_process=[]
    for section in range(0,len(data),sec):
        under_process.append(data[section:sec+section])

    binary_sum=bin(0)
    for i in range(len(under_process)):
        binary_sum=bin(int(binary_sum,2)+int(under_process[i] ,2))[2:]
        
    if len(binary_sum)>sec:
        var=len(binary_sum)-sec
        binary_sum=bin(int(binary_sum[0:var],2)+int(binary_sum[var:],2))[2:]
    if len(binary_sum)<sec:
        binary_sum="0"*(sec-len(binary_sum))+binary_sum

    checksum=""
    for i in binary_sum:
        if i=="0":
            checksum+="1"
        else:
            checksum+="0"

    transmission_data="".join(checksum)
    transmission_data+="".join(under_process)
    return checksum,transmission_data

def receiver(data,sec):
    under_process=[]
    for section in range(0,len(data),sec):
        under_process.append(data[section:sec+section])

    binary_sum=bin(0)
    for i in range(len(under_process)):
        binary_sum=bin(int(binary_sum,2)+int(under_process[i] ,2))[2:]

    if len(binary_sum)>sec:
        var=len(binary_sum)-sec
        binary_sum=bin(int(binary_sum[0:var],2)+int(binary_sum[var:],2))[2:]
    return binary_sum

def checking(checking_data):
    result=""
    for ele in checking_data:
        if ele=="1":
            result+="0"
        else:
            result+="1"

    if result=="0"*len(result):
        return "No Error!!!"
    else:
        return "There is an Error"

data="1010101010101010"
sec=4
transmitting=transmitter(data,sec)
print("Actual Data: ",transmitting[1])
print(checking(receiver(transmitting[1],sec)))  #No Error
print("Received Data: ",transmitting[1])


print("Transmitted Data: ",transmitting[1][:-1]+"1")
print(checking(receiver(transmitting[1]+"1010101010101011",sec)))   #Error at LSB


