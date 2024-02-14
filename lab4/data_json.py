import json

with open('sample_data.json') as file:
    json_data = json.load(file)





print("Interface Status")
print("================================================================================")
print("DN                                                 Description           Speed    MTU")  
print("-------------------------------------------------- --------------------  ------  ------")

data=json_data["imdata"]

for item in data:
    nt_item = item["l1PhysIf"]
    att = nt_item["attributes"]
    dn = att["dn"]
    speed = att["speed"]
    mtu = att["mtu"]
    output = ""
    if(len(dn)==42):
        print(dn + " "*30  +speed+"   "+ mtu)
    else:
        print(dn + " "*31 + speed + "   " + mtu)
    