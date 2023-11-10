import time
try:
  import pypresence
except ModuleNotFoundError:
  print("PyPresence module not found. Trying to install")
  import os
  try:
    os.system("pip3 install pypresence")
  except:
    print("Install failed. Press CTRL-C to quit")
    while True: pass


APP_IDS={
  1:'1152230287137308773',  #Elderscrolls 6
  2:'1152131176174190652',  #GTA 6
  3:''
}
print('''
+---------------------------+
| ScottishPuffin's Fake RPC |
|       COPYRIGHT 2023      |
+---------------------------+

OPTIONS:
========
1) The Elder Scrolls VI: Hammerfell
2) Grand Theft Auto VI
3) Custom
''')
option=0
limg='logo'
while not option in APP_IDS.keys():
  try:
    option = int(input("Pick an option [1-3]: "))
    if option == 3: 
      APP_IDS[3] = input("Custom app id")
      limg = input("Discord application large_image name: ")
  except:
    option = 0
print("Creating RPC Instance")
RPC = pypresence.Presence(APP_IDS[option])
starttime=int(time.time())
print("Connecting RPC Instance")
RPC.connect()
RPC.update(details="Just started playing",large_image=limg)
print("RPC Started, press CTRL-C to quit")
while True:
  try:
    print("RPC Updated")
    time_elapsed = int(time.time())-starttime
    if time_elapsed < 59:
      RPC.update(details="Just started playing",large_image="logo")
    elif time_elapsed < 3599:
      RPC.update(details="for %s minutes"%(int(time_elapsed/60)),large_image="logo")
    else:
      RPC.update(details="for %s hours"%(int(time_elapsed/3600)),large_image="logo")
    time.sleep(15)
  except KeyboardInterrupt:
    print("Quitting!")
    quit()
