import tensorflow as tf
from tensorflow.keras import layers, models

class MyClassifier(layers.Layer):
    def __init__(self, num_classes):
        super(MyClassifier, self).__init__()
        self.num_classes = num_classes
    
    def build(self, input_shape):
        shape = (input_shape[0], input_shape[1])
        x = layers.Input(shape=shape)
        self.model = models.Sequential()
        self.model.add(layers.Dense(32, activation='relu', kernel_regularizer=tf.keras.regularizers.l2(0.01)))
        self.model.add(layers.Dense(self.num_classes))
        
    def call(self, inputs):
        y_pred = self.model(inputs)
        return y_pred

model = MyClassifier(num_classes=10)
