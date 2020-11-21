import pandas as pd, matplotlib.pyplot as plt, matplotlib as mpl

df = pd.read_csv("fr-esr-enquete-ressources-electroniques-etablissements.csv", sep = ';')

dfapc = pd.read_csv("fr_apc.csv")

reading_price, apc_price = {}, {}

for year in range(2015, 2019) : 
	reading_price[str(year)] = df.loc[ df["Millesime"] == year, "Valeur"].sum()
	apc_price[str(year)] = dfapc.loc[ dfapc["period"] == year, "euro"].sum()
	
print("to read")
[print(f"{k}\t{reading_price[k]}") for k in reading_price]

print("to publish")
[print(f"{k}\t{apc_price[k]}") for k in apc_price]

plt.style.use('seaborn-pastel')
fig, ax = plt.subplots()
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)


ax.ticklabel_format(style='plain')
#set , as thousand separator
ax.yaxis.set_major_formatter(mpl.ticker.StrMethodFormatter('€{x:,.0f}'))
#ax.figure( figsize =(4,3))
ax.bar(reading_price.keys(), reading_price.values(), label = "to read" )

ax.bar(apc_price.keys(), apc_price.values(), bottom = list(reading_price.values()), label = "to publish" )

#remove origin
yticks = ax.yaxis.get_major_ticks()
yticks[0].label1.set_visible(False)

#set grid
ax.grid(color='grey', linestyle='--', linewidth=0.5)
plt.gca().xaxis.grid(False)


#legend
plt.legend(loc="upper left")
plt.title("French expenditure (which we know) about scientific publishing", fontsize = 18, y = 1.08)
plt.show()


#print(len(df2015))