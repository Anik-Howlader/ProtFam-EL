"""
Data Preprocessing Script for Protein Classification
Prepares clean data for Week 2 modeling
"""

import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.model_selection import train_test_split
import pickle
import json

print("="*80)
print("PROTEIN CLASSIFICATION - DATA PREPROCESSING")
print("="*80)

# Load data
print("\n1. Loading datasets...")
df_full = pd.read_csv('data/raw/proteinas_20000_enriquecido.csv')
df_train_provided = pd.read_csv('data/raw/proteinas_train.csv')
df_test_provided = pd.read_csv('data/raw/proteinas_test.csv')

print(f"   Full dataset: {df_full.shape}")
print(f"   Provided train: {df_train_provided.shape}")
print(f"   Provided test: {df_test_provided.shape}")

# Define feature columns
feature_cols = [
    'Massa_Molecular',
    'Ponto_Isoelétrico', 
    'Hidrofobicidade',
    'Carga_Total',
    'Proporção_Polar',
    'Proporção_Apolar',
    'Comprimento_Sequência'
]
target_col = 'Classe'

# Prepare full dataset
print("\n2. Preparing features and target...")
X_full = df_full[feature_cols]
y_full = df_full[target_col]

# Encode labels
print("\n3. Encoding target labels...")
label_encoder = LabelEncoder()
y_full_encoded = label_encoder.fit_transform(y_full)

# Create label mapping
label_mapping = dict(zip(label_encoder.classes_, label_encoder.transform(label_encoder.classes_)))
print(f"   Label mapping: {label_mapping}")

# Scale features
print("\n4. Scaling features...")
scaler = StandardScaler()
X_full_scaled = scaler.fit_transform(X_full)
X_full_scaled_df = pd.DataFrame(X_full_scaled, columns=feature_cols, index=df_full.index)

# Prepare provided train/test splits
X_train_provided = df_train_provided[feature_cols]
y_train_provided = label_encoder.transform(df_train_provided[target_col])
X_train_provided_scaled = scaler.transform(X_train_provided)

X_test_provided = df_test_provided[feature_cols]
y_test_provided = label_encoder.transform(df_test_provided[target_col])
X_test_provided_scaled = scaler.transform(X_test_provided)

# Create alternative split using full dataset (80/20)
print("\n5. Creating alternative train/test split (80/20)...")
X_train_alt, X_test_alt, y_train_alt, y_test_alt = train_test_split(
    X_full_scaled, y_full_encoded, 
    test_size=0.2, 
    random_state=42, 
    stratify=y_full_encoded
)

print(f"   Alternative train: {X_train_alt.shape}")
print(f"   Alternative test: {X_test_alt.shape}")

# Save processed data
print("\n6. Saving processed datasets...")

# Provided splits
np.save('data/processed/X_train_provided.npy', X_train_provided_scaled)
np.save('data/processed/y_train_provided.npy', y_train_provided)
np.save('data/processed/X_test_provided.npy', X_test_provided_scaled)
np.save('data/processed/y_test_provided.npy', y_test_provided)

# Alternative splits
np.save('data/processed/X_train_alt.npy', X_train_alt)
np.save('data/processed/y_train_alt.npy', y_train_alt)
np.save('data/processed/X_test_alt.npy', X_test_alt)
np.save('data/processed/y_test_alt.npy', y_test_alt)

# Full scaled dataset
np.save('data/processed/X_full_scaled.npy', X_full_scaled)
np.save('data/processed/y_full_encoded.npy', y_full_encoded)

# Save scaler and encoder
with open('data/processed/scaler.pkl', 'wb') as f:
    pickle.dump(scaler, f)
    
with open('data/processed/label_encoder.pkl', 'wb') as f:
    pickle.dump(label_encoder, f)

# Save metadata
metadata = {
    'feature_names': feature_cols,
    'target_name': target_col,
    'label_mapping': {k: int(v) for k, v in label_mapping.items()},
    'n_classes': len(label_mapping),
    'n_features': len(feature_cols),
    'dataset_shapes': {
        'full': list(X_full_scaled.shape),
        'train_provided': list(X_train_provided_scaled.shape),
        'test_provided': list(X_test_provided_scaled.shape),
        'train_alt': list(X_train_alt.shape),
        'test_alt': list(X_test_alt.shape)
    }
}

with open('data/processed/metadata.json', 'w') as f:
    json.dump(metadata, f, indent=2)

print("\n" + "="*80)
print("PREPROCESSING COMPLETE")
print("="*80)
print("\nSaved files:")
print("  - X_train_provided.npy, y_train_provided.npy (16,000 samples)")
print("  - X_test_provided.npy, y_test_provided.npy (4,000 samples)")
print("  - X_train_alt.npy, y_train_alt.npy (48,000 samples)")
print("  - X_test_alt.npy, y_test_alt.npy (12,000 samples)")
print("  - X_full_scaled.npy, y_full_encoded.npy (60,000 samples)")
print("  - scaler.pkl, label_encoder.pkl, metadata.json")
print("\n✓ Ready for Week 2 modeling!")
