import numpy as np
import seaborn as sns
import pandas
import matplotlib.pyplot as plt

sns.set()

#https://www.data.gouv.fr/fr/datasets/repartition-de-la-consommation-denergie-primaire-en-france-focus-energie-renouvelable/
data = pandas.read_csv("repartition-de-la-consommation-denergie-primaire-en-france-focus-energie-renouve.csv", sep=";")

data_per_energy = data.groupby('type')

data_wind = data_per_energy.get_group('Wind power (standardized)')
data_wind = data_wind.sort_values(by=['annee'])

data_hydraulic = data_per_energy.get_group('Hydraulic (standardized)')
data_hydraulic = data_hydraulic.sort_values(by=['annee'])

data_hydraulic = data_per_energy.get_group('Hydraulic (standardized)')
data_hydraulic = data_hydraulic.sort_values(by=['annee'])

fig, axs = plt.subplots(2)
fig.suptitle('Vertically stacked subplots')
axs[0].plot(data_wind["annee"], data_wind["part_d_energie_renouvelable"])
axs[1].plot(data_hydraulic["annee"], data_hydraulic["part_d_energie_renouvelable"])

plt.show()

plt.plot(data_wind["annee"], data_wind["part_d_energie_renouvelable"], label = "line 1")
plt.plot(data_hydraulic["annee"], data_hydraulic["part_d_energie_renouvelable"], label = "line 2")
plt.legend()
plt.show()