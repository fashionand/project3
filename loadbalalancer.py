import sys
import random
import netaddr

class loadbalalancer:
    list_servers = {}
    position=0
    def __init__(self,list_servers):
        self.list_servers =[]
        self.weight=[]
        self.position=0

    def _choiceServer(self,list_index):
        accumulative_weight = 0
        for server, weight in zip(self.list_servers, self.weight):
            accumulative_weight+=weight
            if(list_index<accumulative_weight):
                return server
        return 0
    def add_server(self, servers,weights):
        self.list_servers=(servers)
        self.weight=weights
    def RoundRobin(self):
        if(len(self.list_servers)==0): 
            return 0
        result=self._choiceServer(self.position)
        if(self.position is sum(self.weight)-1):
            self.position=0
        else:
            self.position+=1
        return result
    def Random(self):
        x=random.randint(0,sum(self.weight)-1)
        return self._choiceServer(x)
    def WeightHash(self,ipaddress):
        ip = netaddr.IPAddress(ipaddress)
        #print 'transformer', ip.value,ip.value%sum(self.weight)
        return self._choiceServer(ip.value%sum(self.weight))
if __name__ == "__main__":
    rb=loadbalalancer(3)
    rb.add_server(["192.168.0.1","192.168.0.2","192.168.0.3"],[2,2,5])
    
    for m in xrange(20):
        #print rb.RoundRobin()
        #print rb.Random()
        rm=random.randint(0,127)
        mock_ip="127.0.0."+str(rm)
        print rb.WeightHash(mock_ip)