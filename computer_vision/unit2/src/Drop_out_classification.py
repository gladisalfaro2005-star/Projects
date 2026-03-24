import numpy as np
import pandas as pd
import tensorflow as tf
from sklearn.model_selection import train_test_split 
from sklearn.preprocessing import StandardScaler 
from sklearn.utils.class_weight import compute_class_weight 
from sklearn.metrics import confusion_matrix, classification_report
import matplotlib.pyplot as plt

SEED = 42
np.random.seed(SEED)
tf.random.set_seed(SEED)
tf.keras.utils.set_random_seed(SEED)

df_dropout = pd.read_csv(r"C:\Users\gladi\Projects\unit2\src\student_dropout_dataset_v3.csv")
df_dropout = df_dropout.dropna()

y_raw = df_dropout['Dropout']
y = pd.Categorical(y_raw).codes.astype(np.int32)

X_df = df_dropout.drop(['Student_ID', 'Dropout'], axis=1, errors='ignore')
X_df = pd.get_dummies(X_df, drop_first=True)
X = X_df.values.astype(np.float32)

X_train, x_temp, y_train, y_temp = train_test_split(X, y, test_size=0.3, stratify=y, random_state=SEED)
X_val, X_test, y_val, y_test = train_test_split(x_temp, y_temp, test_size=0.5, stratify=y_temp, random_state=SEED)

scaler = StandardScaler()
X_train_s = scaler.fit_transform(X_train)
X_val_s = scaler.transform(X_val) 
X_test_s = scaler.transform(X_test) 

cw = compute_class_weight(class_weight='balanced', classes=np.unique(y_train), y=y_train)
class_weight = {0: float(cw[0]), 1: float(cw[1])}

def build_model(input_dim):
  inputs = tf.keras.Input(shape=(input_dim,))
  x = tf.keras.layers.Dense(16, activation="relu", kernel_regularizer=tf.keras.regularizers.l2(1e-3))(inputs)
  x = tf.keras.layers.Dropout(0.3)(x)
  x = tf.keras.layers.Dense(8, activation="relu", kernel_regularizer=tf.keras.regularizers.l2(1e-3))(x)
  x = tf.keras.layers.Dropout(0.2)(x)
  outputs = tf.keras.layers.Dense(1, activation="sigmoid")(x) 
  return tf.keras.Model(inputs, outputs)

model = build_model(X_train_s.shape[1])

metrics = [tf.keras.metrics.AUC(curve="ROC", name="Auc_ROC"), tf.keras.metrics.AUC(curve="PR", name="Auc_PR")]
model.compile(optimizer=tf.optimizers.Adam(1e-4), loss="binary_crossentropy", metrics=metrics)
callbacks = [tf.keras.callbacks.EarlyStopping(monitor="val_Auc_ROC", mode="max", patience=20, restore_best_weights=True)]

history = model.fit(X_train_s, y_train, validation_data=(X_val_s, y_val), epochs=300, batch_size=64, class_weight=class_weight, callbacks=callbacks, verbose=0)

plt.figure()
plt.plot(history.history["loss"])
plt.plot(history.history["val_loss"])
plt.title("Perdida - Modelo STUDENT DROPOUT")
plt.legend(["Train", "Validation"]) 
plt.show()

testing_data_results = model.evaluate(X_test_s, y_test, verbose=0)
y_est_prob = model.predict(X_test_s).ravel()

print("\n--- UMBRAL 0.6 ---")
y_est_bin_50 = (y_est_prob >= 0.6).astype(int)
print(classification_report(y_test, y_est_bin_50))
print(confusion_matrix(y_test, y_est_bin_50))

print("\n--- UMBRAL 0.3 ---")
y_est_bin_30 = (y_est_prob >= 0.3).astype(int)
print(classification_report(y_test, y_est_bin_30))
print(confusion_matrix(y_test, y_est_bin_30))


# La columna precision indica la proporción de predicciones positivas que realmente son correctas. Con el umbral de 0.6, la precisión es 0.89 para la clase 0 y 0.51 para la clase 1, lo que indica que el modelo es más preciso al identificar la clase 0 que la clase 1. Con el umbral de 0.3 la 
# precisiónde la clase 0 es 0.95 y  para la clase 1 baja a 0.35

#github:https://github.com/gladisalfaro2005-star/Projects
#Dataset: www.kaggle.com/datasets/meharshanali/student-dropout-prediction-dataset/versions/1?resource=download