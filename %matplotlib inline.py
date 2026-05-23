%matplotlib inline
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style('whitegrid')
df = pd.read_excel('Pokemon.xlsx')

type_counts = df['Type 1'].value_counts().nlargest(10)

plt.figure(figsize=(12,6))
sns.barplot(x=type_counts.index, y=type_counts.values, palette='tab10')
plt.title('Top 10 Type 1 de Pokémon - Conteo')
plt.xlabel('Type 1')
plt.ylabel('Cantidad')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()