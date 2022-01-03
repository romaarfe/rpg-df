import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

names = ['DARIUS', 'ELANA', 'JO', 'THE MEN', 'WALKER']
health = [78, 70, 70, 78, 90]
stress = [2, 2, 4, 2, 3]
strenght = [39, 35, 35, 39, 45]
speed = [32, 39, 36, 43, 36]
intellect = [33, 42, 24, 37, 20]
combat = [40, 21, 28, 37, 40]
sanity = [25, 40, 30, 20, 25]
fear = [30, 25, 35, 85, 30]
body = [35, 25, 30, 40, 35]
armor = [40, 25, 35, 25, 40]
classe = ['Marine', 'Scientist', 'Teamster', 'Android', 'Marine']

mothership = {'Nome': names, 'Saúde': health, 'Estresse': stress,
              'Força': strenght, 'Velocidade': speed, 'Intelecto': intellect, 
              'Combate': combat, 'Sanidade': sanity, 'Medo': fear, 
              'Corpo': body, 'Armadura': armor, 'Classe': classe}

resume = pd.DataFrame(mothership)

#resume.index = ['Marine', 'Scientist', 'Teamster', 'Android', 'Marine']

sns.set_style('darkgrid')
sns.set_palette('bright')

fig, axes = plt.subplots(2, 5, figsize=(35, 10))
fig.suptitle('Análise do Grupo')

sns.barplot(x='Saúde', y='Nome', data=resume, ax=axes[0, 0])
sns.barplot(x='Estresse', y='Nome', data=resume, ax=axes[1, 0])
sns.barplot(x='Força', y='Nome', data=resume, ax=axes[0, 1])
sns.barplot(x='Velocidade', y='Nome', data=resume, ax=axes[0, 2])
sns.barplot(x='Intelecto', y='Nome', data=resume, ax=axes[0, 3])
sns.barplot(x='Combate', y='Nome', data=resume, ax=axes[0, 4])
sns.barplot(x='Sanidade', y='Nome', data=resume, ax=axes[1, 1])
sns.barplot(x='Medo', y='Nome', data=resume, ax=axes[1, 2])
sns.barplot(x='Corpo', y='Nome', data=resume, ax=axes[1, 3])
sns.barplot(x='Armadura', y='Nome', data=resume, ax=axes[1, 4])

plt.show()