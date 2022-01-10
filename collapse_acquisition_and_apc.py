import pandas as pd, matplotlib.pyplot as plt, matplotlib as mpl

## from https://data.enseignementsup-recherche.gouv.fr/explore/dataset/fr-esr-enquete-ressources-electroniques-etablissements/information/
df = pd.read_csv("fr-esr-enquete-ressources-electroniques-etablissements.csv", sep = ';')

# from https://treemaps.intact-project.org/apcdata/openapc/#institution/country=FRA
dfapc = pd.read_csv("fr_apc.csv")

reading_price, apc_price = {}, {}

for year in range(2015, 2019) : 
	reading_price[str(year)] = df.loc[ df["Millesime"] == year, "Valeur"].sum()
	apc_price[str(year)] = dfapc.loc[ dfapc["period"] == year, "euro"].sum()
	
print("to read")
[print(f"{k}\t{reading_price[k]}") for k in reading_price]

print("to publish")
[print(f"{k}\t{apc_price[k]}") for k in apc_price]


# do graph
plt.style.use('seaborn-pastel')
fig, ax = plt.subplots(figsize=(10, 6), dpi = 100)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)


ax.ticklabel_format(style='plain')
#set , as thousand separator
ax.yaxis.set_major_formatter(mpl.ticker.StrMethodFormatter('€{x:,.0f}'))


# put data inside the graph
ax.bar(reading_price.keys(), reading_price.values(), label = "to read (online scientific resources)" )
ax.bar(apc_price.keys(), apc_price.values(), bottom = list(reading_price.values()), label = "to publish (APC)" )



#remove origin
yticks = ax.yaxis.get_major_ticks()
yticks[0].label1.set_visible(False)

#set grid
ax.grid(color='grey', linestyle='--', linewidth=0.5)
plt.gca().xaxis.grid(False)
plt.gca().set_ylim([0, 130000000]) # set ymax

# display and change legend order
handles, labels = ax.get_legend_handles_labels()
order = [1, 0]
ax.legend([handles[idx] for idx in order],[labels[idx] for idx in order], 
    bbox_to_anchor=(0.5, 0.7), fontsize = 15, loc="upper center", borderaxespad =1.7)


plt.title("French spending on scientific publishing", fontsize = 24, y = 0.99)
plt.savefig("french_spending.png")

#print(len(df2015))