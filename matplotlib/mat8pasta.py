import matplotlib.pyplot as plt
araclar=["Fiat","Ford","BMW","Mercedes"]
fiyatlar=[100,300,500,900]
aralik=[0.2,0,0,0]
renker=["red","yellow","hotpink","blue"]
plt.pie(fiyatlar,labels=araclar,startangle=90,explode=aralik,colors=renker,autopct="%1.1f%%")
plt.show()