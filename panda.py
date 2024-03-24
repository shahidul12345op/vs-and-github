# import pandas as pd
# city=['dhaka','rangpur','barishal']
# df=pd.DataFrame(city,index=[1,2,3],columns=['city'])
# print(df)
# city2=['cumilla','rajshahi','sylhet']
# df2=pd.DataFrame(zip(city,city2),columns=['city','city2'])
# print(df2)

import pandas as pd
name=['Shahidul','Emon','Jidan','Rafi','Rabib','Riyan']
id  =[111,143,243,428,643,333]
homeTown=['Tangail','Rangpur','Narayanganj','Tangail','Kustia','Tangial']
semester=['5th','5th','5th','5th','3rd','1st']
df=pd.DataFrame(zip(name,id,homeTown,semester),columns=['Name','ID','HomeTown','Semester'])
print(df)