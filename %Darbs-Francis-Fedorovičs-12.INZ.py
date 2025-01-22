import requests

url = "https://jsonplaceholder.typicode.com/users/"
response = requests.get(url)
#Pārbauda, un izdrukā cik kopā ir ierakstu
if response.status_code == 200:
    atbilde = response.json()
    print(len(atbilde))
#Funkcija apstrādā visus lietotājus un Sarakstā ir tikai lietotajvārda vērtības
users = []
for user in atbilde:
    users.append(user["username"])
print(users)
#Izveido funkciju, kas atrod visus lietotājus, kuriem e-pasta adresē ir norādīts domēns
mails = []
for user in atbilde:
    if "@april.biz" in user["email"]:
        mails.append(user["username"])
print(mails)
#Izveido sarakstu ar unikālajām pilsētām, kurās dzīvo lietotāji (bez atkārtojumiem)
cit = []
for user in atbilde:
    for oompa in user["address"]:
        if oompa["city"] not in cit:
            cit.append(oompa["city"])
print(cit)
#Izveido vārdnīcu, kurā parādīts, cik lietotājiem mājaslapas URL beidzas ar norādīto domēni
