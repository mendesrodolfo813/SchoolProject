import tensorflow as tf

# Define a simple neural network model using TensorFlow
model = tf.keras.Sequential([
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dense(10)
])

# Compile the model with appropriate loss function and optimizer
model.compile(optimizer='adam', loss=tf.keras.losses.sparse_categorical_crossentropy)

# Use TensorFlow's functional API to train the model
model.fit(x_train, y_train, epochs=5)
