import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from joblib import dump

# Simulamos un dataset
data = pd.DataFrame({
    'score': [9.0, 7.5, 4.0, 5.5, 3.0, 8.5, 6.0, 2.5, 4.5, 9.5],
    'errores': [1, 2, 5, 3, 6, 0, 2, 7, 4, 1],
    'tiempo': [60, 75, 120, 90, 130, 55, 80, 140, 110, 50],
    'riesgo': ['bajo', 'medio', 'alto', 'medio', 'alto', 'bajo', 'medio', 'alto', 'alto', 'bajo']
})

# Codificamos la variable objetivo
label_encoder = LabelEncoder()
data['riesgo_encoded'] = label_encoder.fit_transform(data['riesgo'])

# Separar variables y etiquetas
X = data[['score', 'errores', 'tiempo']]
y = data['riesgo_encoded']

# Dividir en entrenamiento y test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Entrenamiento del modelo
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Guardar el modelo y el codificador
dump(model, 'modelo_alzheimer.pkl')
dump(label_encoder, 'label_encoder.pkl')

print("✅ Modelo entrenado y guardado correctamente.")
