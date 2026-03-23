import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix, classification_report

# fijar pseudoaleatoridad
SEED = 42
np.random.seed(SEED)
tf.random.set_seed(SEED)

# cargar datasets
iris = load_iris()
X = iris.data.astype(np.float32) # caracteristicas
y = iris.data.astype(np.int32) # etiquetas
class_names = iris.target_names # nombres de las clases

print("Nombre de las clases", class_names)
print("Shape de X:", X.shape)
print("Shape de Y:", y.shape)

#Division del dataset
X_train, X_temp, y_train, t_temp = train_test_split(
    X, y, 
    test_size=0.3,
    random_state = SEED,
    stratify = y_temp
)

print("Shape del dataset")
print("Train:", X_train.shape, y_train.shape)
print("Val:", X_val.shape, y_val.shape)
print("Test:", X_test.shape, y_test.shape)

#Escalado
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_val = scaler.transform(X_val)
X_test = scaler.transform(X_test)

#modelo
def buid_model(input_dim):
    
    inputs = tf.keras.Input(shape=(input_dim,))
    x = tf.keras.layers.Dense(
        64,
        activation="relu",
        kernel_regularizer=tf.keras.regularizers.l2(1e-4)
        )(inputs)
    x = tf.keras.Dropout(0.25)(x)
    x = tf.keras.layers.Dense(
        32,
        activation="relu",
        kernel_regularizer=tf.keras.regularizers.l2(1e-4)
        )(inputs)
    x = tf.keras.Dropout(0.20)(x)
    x = tf.keras.layers.Dense(
        3,
        activation="softmax"
        )(x) 
    return tf.keras.Model(inputs, outputs)

model = build_model(X_train.shape(1))
model.summary()

# compilacion
lr = 0.01
model.compile(
    optimizer=tf.keras.optimizers.Adam(learning_rate = lr),
    loss=tf.keras.losses.SparseCategoricalCrossentropy(),
    metrics=["accuracy"]
)

print("\nResumen del modelo \t")
model.summary()

#callbacks
callbacks = [
        tf.keras.callbacks.EarlyStopping(
        monitor="val_loss",
        patience=10, # despues de 10 epocas
        restore_best_weights=True)
]
    
# entrenamiento
history = model.fit(
    X_train, y_train,
    validation_data=(X_val, y_val),
    epochs=150,
    batch_size=16,
    callbacks=callbacks,
    verbose=1 
)

  
