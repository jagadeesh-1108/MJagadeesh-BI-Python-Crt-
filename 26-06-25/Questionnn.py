#write a py program to count how many genes belongs to each family from the given data and visualize it using bar chart 
import pandas as pd
import matplotlib.pyplot as plt

# Sample data: (gene_id, family)
data = [
    ('gene1', 'Kinase'),
    ('gene2', 'GPCR'),
    ('gene3', 'Kinase'),
    ('gene4', 'Phosphatase'),
    ('gene5', 'GPCR'),
    ('gene6', 'Kinase'),
    ('gene7', 'Ion Channel'),
    ('gene8', 'Phosphatase'),
    ('gene9', 'Kinase'),
    ('gene10', 'GPCR'),
    ('gene11', 'Nuclear Receptor'),
    ('gene12', 'Kinase'),
    ('gene13', 'Ion Channel'),
    ('gene14', 'Kinase'),
    ('gene15', 'Phosphatase'),
]

# Create DataFrame
df = pd.DataFrame(data, columns=['gene_id', 'family'])

# Count genes per family
family_counts = df['family'].value_counts().reset_index()
family_counts.columns = ['family', 'count']

# Create bar chart
plt.figure(figsize=(10, 6))
plt.bar(family_counts['family'], family_counts['count'], color='skyblue')

# Customize chart
plt.title('Number of Genes per Family', fontsize=14)
plt.xlabel('Gene Family', fontsize=12)
plt.ylabel('Number of Genes', fontsize=12)
plt.xticks(rotation=45, ha='right')  # Rotate labels for better readability
plt.tight_layout()  # Adjust layout to prevent clipping of labels
plt.show()