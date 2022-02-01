import pandas as pd

#vytvorenie a otvorenie súboru do ktorého pôjde export s údajmi o počte udalostí pre daného zákazníka
f = open("D:\Work\_TEMP\IS\cust.txt", "w")

#načítanie súboru s tiketmi za 2021 v móde bez hlavičky do dataframu
data = pd.read_excel('D:\Work\_TEMP\IS\is21_utf.xlsx',header=None)

#vyfiltrovanie každého 3 riadku do nového dataframu ako názov zákazníka
df_cust = data[data.index % 3 == 0] 

#vytvorenie dictionary kde key=zákazník , value=počet tiketov
dict_c={}

#vytvorenie pomocneho listu pre vyčítanie hodnôt z dataframu so zákazníkmi
list_c=[]

#priradenie hodnôt z dataframu (hodnoty su typu list) so zákazníkmi do pomocného listu
list_c=df_cust.values.tolist()

#print (list[0:25])

#vytvorenie pomocneho listu kvoli uprave dat v list_c , ktorý je list listov
key_list=[]

#transformacia listu listov, na list hodnôt
key_list = [item for sublist in list_c for item in sublist ]

#alfanumericke zoradenie listu
key_list=sorted(key_list)

#priradenie klúča=zákazníka do slovníka ak sa nenachádza a priradenie value=0 , ak sa nachádza pripočítanie value+=1 
for key in key_list:
    if key not in dict_c:
        dict_c[key]=0
    if key in dict_c:
        dict_c[key]=dict_c[key]+1

#vytvorenie dictionary , zoradenie descending podľa value            
sorted_dict = {}

#vytvorenie listu , priradenie klúčov z dict_c , sorted podľa value as ascending
sorted_keys = sorted(dict_c, key=dict_c.get)  
print (dict_c)
print (sorted_keys)
#inverzia listu , zmena na descending
sorted_keys = sorted_keys[::-1]

#priradenie value pre kluc zo zoradených klucov podla value as desc v dict sorted_dict :: z dictionary dict_c podla kluca
for w in sorted_keys:
    sorted_dict[w] = dict_c[w]

#pre kazdy kluc v sorted_keys vykonat write s value z daneho kluca do riadku , nasledne nextline 
for key in sorted_dict:\
    f.write(" {:>3d} zaznam :: {}  \n".format(sorted_dict[key] , key ))

#zatvorenie suboru s vystupom 
f.close()
          
