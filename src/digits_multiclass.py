import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, label_binarize
from sklearn.metrics import confusion_matrix, classification_report, roc_curve, auc, precision_recall_curve, average_precision_score, ConfusionMatrixDisplay

# Fijar pseudoaleatoriedad
SEED = 42
np.random.seed(SEED)
tf.random.set_seed(SEED)

# Numero de clases 10, muestras 1797 muestras y 64 variables
dataset = load_digits()
X = dataset.data.astype(np.float32)
y = dataset.target.astype(np.int32)
class_names = [str(c) for c in dataset.target_names]

# Division del dataset Train 70 por ciento Val 15 por ciento Test 15 por ciento
X_train, X_temp, y_train, y_temp = train_test_split(X, y, test_size=0.3, random_state=SEED, stratify=y)
X_val, X_test, y_val, y_test = train_test_split(X_temp, y_temp, test_size=0.5, random_state=SEED, stratify=y_temp)

# Normalizacion con escalado estandar
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_val = scaler.transform(X_val)
X_test = scaler.transform(X_test)

# Modelo 3 con 2 capas ocultas 32 y 16 neuronas relu dropout 20 por ciento y salida softmax
inputs = tf.keras.Input(shape=(X_train.shape[1],))
x = tf.keras.layers.Dense(32, activation="relu")(inputs)
x = tf.keras.layers.Dropout(0.2)(x)
x = tf.keras.layers.Dense(16, activation="relu")(x)
x = tf.keras.layers.Dropout(0.2)(x)
outputs = tf.keras.layers.Dense(len(np.unique(y)), activation="softmax")(x)
model = tf.keras.Model(inputs, outputs)

# Compilacion del modelo con optimizador Adam y funcion de perdida
model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=0.005),
              loss=tf.keras.losses.SparseCategoricalCrossentropy(),
              metrics=["accuracy"])

# Uso de early stopping para reducir sobreajuste
early_stopping = tf.keras.callbacks.EarlyStopping(monitor="val_loss", patience=15, restore_best_weights=True)

# Entrenamiento del modelo
history = model.fit(X_train, y_train,
                    validation_data=(X_val, y_val),
                    epochs=200, batch_size=16,
                    callbacks=[early_stopping], verbose=1)

test_loss, test_acc = model.evaluate(X_test, y_test, verbose=0)
print(f"\nResultados Test -> Loss: {test_loss:.4f} | Accuracy: {test_acc:.4f}")

y_prob = model.predict(X_test, verbose=0)
y_pred = np.argmax(y_prob, axis=1)
print(classification_report(y_test, y_pred, target_names=class_names))

# Curvas de perdida y accuracy
plt.figure(figsize=(10, 4))
plt.subplot(1, 2, 1)
plt.plot(history.history["loss"], label="Train loss")
plt.plot(history.history["val_loss"], label="Val loss")
plt.title("Perdida Digits")
plt.legend()
plt.subplot(1, 2, 2)
plt.plot(history.history["accuracy"], label="Train acc")
plt.plot(history.history["val_accuracy"], label="Val acc")
plt.title("Exactitud Digits")
plt.legend()
plt.tight_layout()
plt.show()

# Matriz de confusion
disp = ConfusionMatrixDisplay.from_predictions(y_test, y_pred, display_labels=class_names, cmap=plt.cm.Purples)
disp.ax_.set_title("Matriz de Confusion Digits")
plt.show()

# Curvas ROC y PR multiclase
clases_unicas = np.unique(y)
y_test_bin = label_binarize(y_test, classes=clases_unicas)
plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
for i in range(len(clases_unicas)):
    fpr, tpr, _ = roc_curve(y_test_bin[:, i], y_prob[:, i])
    plt.plot(fpr, tpr, label=f'Clase {i}')
plt.title('ROC-AUC Multiclase Digits')
plt.legend(fontsize='x-small', ncol=2)
plt.subplot(1, 2, 2)
for i in range(len(clases_unicas)):
    precision, recall, _ = precision_recall_curve(y_test_bin[:, i], y_prob[:, i])
    plt.plot(recall, precision, label=f'Clase {i}')
plt.title('PR-AUC Multiclase Digits')
plt.legend(fontsize='x-small', ncol=2)
plt.tight_layout()
plt.show()

# Analisis de umbral de decision
umbral = 0.80
prob_maximas = np.max(y_prob, axis=1)
indecisos = np.sum(prob_maximas < umbral)
seguros = len(y_test) - indecisos
plt.figure(figsize=(6, 4))
plt.bar(["Alta Confianza", "Indecisos"], [seguros, indecisos], color=['#4CAF50', '#FF9800'])
plt.title("Desempeno segun Umbral de Decision Digits")
plt.ylabel("Numero de Muestras")
plt.show()

# github: https://github.com/gladisalfaro2005-star/Projects
# en comparacion con los tres moedlos comprobamos que entre más difícil es el problema, más capas se usan
# El modelo 1 lo hizo bien, el 2 clasifico muy bien a los pinguinos
# y el 3 pudo con los dígitos gracias al Dropout que evitó que se macheteara las respuestas y el early stopping ayudo mucho