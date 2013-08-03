#-------------------------------------------------------------------------------
# Name:        network programming  (create a socket and connect to a server)
# Purpose:
#
# Author:      D1617 64
#
# Created:     04-08-2013
# Copyright:   (c) D1617 64 2013
# Licence:     <PFH01>
#-------------------------------------------------------------------------------
import socket #import module socket
socket.setdefaulttimeout(2)  #set default time out
s=socket.socket() #create a new socket
s.connect(("206.183.110.42",21))  #connect to the server
info=s.recv(1024)
print(info)
