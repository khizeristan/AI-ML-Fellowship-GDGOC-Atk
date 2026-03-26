# Part 1: What is a Neuron?
import numpy as np
import matplotlib.pyplot as plt

def neuron(inputs, weights, bias):
    total = sum(w*x for w, x in zip(weights, inputs)) + bias
    output = 1 / (1 + np.exp(-total))
    return output

inputs  = [1.0, 2.0, 3.0]
weights = [0.5, -0.3, 0.8]
bias    = 0.1

result = neuron(inputs, weights, bias)
print('Neuron output:', round(result, 4))


# Part 2: Perceptron
class Perceptron:
    def __init__(self, lr=0.1, epochs=100):
        self.lr = lr
        self.epochs = epochs

    def fit(self, X, y):
        self.w = np.zeros(X.shape[1])
        self.b = 0
        for _ in range(self.epochs):
            for xi, yi in zip(X, y):
                pred = 1 if np.dot(xi, self.w) + self.b >= 0 else 0
                err  = yi - pred
                self.w += self.lr * err * xi
                self.b += self.lr * err

    def predict(self, X):
        return [1 if np.dot(xi, self.w) + self.b >= 0 else 0 for xi in X]

X = np.array([[0,0],[0,1],[1,0],[1,1]])
y = np.array([0, 0, 0, 1])

p = Perceptron()
p.fit(X, y)
print('AND gate predictions:', p.predict(X))
print('Actual:              ', y.tolist())


# Part 3: Activation Functions
x = np.linspace(-5, 5, 100)

sigmoid = 1 / (1 + np.exp(-x))
relu    = np.maximum(0, x)
tanh    = np.tanh(x)

plt.figure(figsize=(12, 3))

plt.subplot(1,3,1)
plt.plot(x, sigmoid)
plt.title('Sigmoid'); plt.grid(True, alpha=0.3)

plt.subplot(1,3,2)
plt.plot(x, relu)
plt.title('ReLU'); plt.grid(True, alpha=0.3)

plt.subplot(1,3,3)
plt.plot(x, tanh)
plt.title('Tanh'); plt.grid(True, alpha=0.3)

plt.suptitle('Activation Functions')
plt.tight_layout()
plt.show()


# Part 4: ANN from Scratch
class SimpleANN:
    def __init__(self, lr=0.5):
        self.lr = lr
        np.random.seed(42)
        self.W1 = np.random.randn(2, 4)
        self.b1 = np.zeros((1, 4))
        self.W2 = np.random.randn(4, 1)
        self.b2 = np.zeros((1, 1))

    def sigmoid(self, z):
        return 1 / (1 + np.exp(-np.clip(z, -500, 500)))

    def forward(self, X):
        self.A1 = self.sigmoid(X @ self.W1 + self.b1)
        self.A2 = self.sigmoid(self.A1 @ self.W2 + self.b2)
        return self.A2

    def train(self, X, y, epochs=3000):
        losses = []
        for i in range(epochs):
            out = self.forward(X)
            loss = np.mean((out - y)**2)
            losses.append(loss)

            d2 = (out - y) * out * (1 - out)
            d1 = (d2 @ self.W2.T) * self.A1 * (1 - self.A1)

            self.W2 -= self.lr * self.A1.T @ d2
            self.W1 -= self.lr * X.T @ d1
        return losses

X_xor = np.array([[0,0],[0,1],[1,0],[1,1]])
y_xor = np.array([[0],[1],[1],[0]])

ann = SimpleANN(lr=0.5)
losses = ann.train(X_xor, y_xor, epochs=3000)

preds = (ann.forward(X_xor) > 0.5).astype(int)
print('XOR Predictions:', preds.flatten().tolist())
print('Actual:         ', y_xor.flatten().tolist())

plt.plot(losses)
plt.title('Training Loss')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.grid(True, alpha=0.3)
plt.show()


# Part 5: Data Preprocessing
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import pandas as pd

np.random.seed(42)
df = pd.DataFrame({
    'age':    np.random.randint(20, 60, 100),
    'income': np.random.randint(30000, 100000, 100),
    'label':  np.random.randint(0, 2, 100)
})

print('Dataset shape:', df.shape)
print(df.head())

X = df[['age','income']].values
y = df['label'].values

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

print('\nBefore scaling mean:', X.mean(axis=0).round(1))
print('After  scaling mean:', X_scaled.mean(axis=0).round(3))

X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.2, random_state=42
)

print(f'Train: {X_train.shape}, Test: {X_test.shape}')


# Part 6: CNN
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

(X_tr, y_tr), (X_te, y_te) = keras.datasets.cifar10.load_data()
X_tr, X_te = X_tr / 255.0, X_te / 255.0

names = ['airplane','car','bird','cat','deer','dog','frog','horse','ship','truck']
print('Train shape:', X_tr.shape)

plt.figure(figsize=(12, 3))
for i in range(10):
    plt.subplot(2, 5, i+1)
    plt.imshow(X_tr[i])
    plt.title(names[y_tr[i][0]], fontsize=8)
    plt.axis('off')
plt.tight_layout()
plt.show()

model_cnn = keras.Sequential([
    layers.Conv2D(32, (3,3), activation='relu', input_shape=(32,32,3)),
    layers.MaxPooling2D(2,2),
    layers.Conv2D(64, (3,3), activation='relu'),
    layers.MaxPooling2D(2,2),
    layers.Flatten(),
    layers.Dense(64, activation='relu'),
    layers.Dense(10, activation='softmax')
])

model_cnn.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
model_cnn.summary()

history = model_cnn.fit(X_tr, y_tr, epochs=5, batch_size=64, validation_split=0.1)
_, acc = model_cnn.evaluate(X_te, y_te)
print(f'Test Accuracy: {acc*100:.2f}%')


# Part 7: Image Augmentation
from tensorflow.keras.preprocessing.image import ImageDataGenerator

datagen = ImageDataGenerator(
    rotation_range=20,
    horizontal_flip=True,
    zoom_range=0.2
)

sample = X_tr[:1]
plt.figure(figsize=(12, 3))
plt.subplot(1,6,1)
plt.imshow(sample[0])
plt.title('Original')
plt.axis('off')

i = 2
for batch in datagen.flow(sample, batch_size=1):
    plt.subplot(1,6,i)
    plt.imshow(batch[0])
    plt.axis('off')
    i += 1
    if i > 6:
        break

plt.tight_layout()
plt.show()


# Part 8: Transfer Learning
from tensorflow.keras.applications import MobileNetV2

base = MobileNetV2(input_shape=(96,96,3), include_top=False, weights='imagenet')
base.trainable = False

model_tl = keras.Sequential([
    base,
    layers.GlobalAveragePooling2D(),
    layers.Dense(64, activation='relu'),
    layers.Dense(10, activation='softmax')
])

model_tl.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
model_tl.summary()

X_tr_r = tf.image.resize(X_tr[:3000], (96,96)).numpy()
X_te_r = tf.image.resize(X_te[:500],  (96,96)).numpy()

history_tl = model_tl.fit(X_tr_r, y_tr[:3000], epochs=3, batch_size=32, validation_split=0.1)
_, tl_acc = model_tl.evaluate(X_te_r, y_te[:500])
print(f'Transfer Learning Accuracy: {tl_acc*100:.2f}%')


# Part 9: Fine-Tuning
base.trainable = True
for layer in base.layers[:-20]:
    layer.trainable = False

model_tl.compile(
    optimizer=keras.optimizers.Adam(1e-5),
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

history_ft = model_tl.fit(X_tr_r, y_tr[:3000], epochs=3, batch_size=32, validation_split=0.1)
_, ft_acc = model_tl.evaluate(X_te_r, y_te[:500])
print(f'After Fine-Tuning Accuracy: {ft_acc*100:.2f}%')


# Part 10: MNIST ANN + CNN
(X_train, y_train), (X_test, y_test) = keras.datasets.mnist.load_data()

X_train, X_test = X_train / 255.0, X_test / 255.0

ann_model = keras.Sequential([
    layers.Flatten(input_shape=(28,28)),
    layers.Dense(128, activation='relu'),
    layers.Dropout(0.2),
    layers.Dense(64, activation='relu'),
    layers.Dense(10, activation='softmax')
])

ann_model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
h_ann = ann_model.fit(X_train, y_train, epochs=5, batch_size=128, validation_split=0.1)
_, ann_acc = ann_model.evaluate(X_test, y_test)
print(f'ANN Accuracy: {ann_acc*100:.2f}%')

X_train_c = X_train.reshape(-1, 28, 28, 1)
X_test_c  = X_test.reshape(-1, 28, 28, 1)

cnn_model = keras.Sequential([
    layers.Conv2D(32, (3,3), activation='relu', input_shape=(28,28,1)),
    layers.MaxPooling2D(2,2),
    layers.Conv2D(64, (3,3), activation='relu'),
    layers.MaxPooling2D(2,2),
    layers.Flatten(),
    layers.Dense(64, activation='relu'),
    layers.Dropout(0.3),
    layers.Dense(10, activation='softmax')
])

cnn_model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
h_cnn = cnn_model.fit(X_train_c, y_train, epochs=5, batch_size=128, validation_split=0.1)
_, cnn_acc = cnn_model.evaluate(X_test_c, y_test)
print(f'CNN Accuracy: {cnn_acc*100:.2f}%')