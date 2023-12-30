import pandas as pd
import folium

# Charger le fichier CSV
file_path = 'file_csv/classif_geo.csv'  # Remplacez par le chemin de votre fichier
data = pd.read_csv(file_path)

# Calculer la latitude et la longitude moyennes pour chaque département
data['Latitude'] = (data['Latitude la plus au nord'] + data['Latitude la plus au sud']) / 2
data['Longitude'] = (data['Longitude la plus à l’est'] + data['Longitude la plus à l’ouest']) / 2

# Créer la carte centrée sur la France
m = folium.Map(location=[46.2276, 2.2137], zoom_start=6)

# Définir une palette de couleurs pour les clusters
colors = ['red', 'green', 'blue', 'purple']

# Ajouter des marqueurs pour chaque département
for _, row in data.iterrows():
    # Taille du marqueur basée sur le nombre d'accidents (ajustée pour la visibilité)
    marker_size = row['nombre_accident'] / 2 if row['nombre_accident'] > 0 else 2

    folium.CircleMarker(
        location=[row['Latitude'], row['Longitude']],
        radius=marker_size,
        color=colors[int(row['clusters'])],
        fill=True,
        fill_color=colors[int(row['clusters'])],
        fill_opacity=0.7,
        popup=f"Departement: {row['Departement']}, Accidents: {row['nombre_accident']}, Cluster: {row['clusters']}"
    ).add_to(m)

# Enregistrer la carte dans un fichier HTML
output_file_path = 'classif.html'
m.save(output_file_path)
