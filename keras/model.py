import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import sys
import os
import tensorflow as tf
ModelCheckpoint = tf.keras.callbacks.ModelCheckpoint



from tensorflow.keras.applications import InceptionV3 # type: ignore
from tensorflow.keras.layers import GlobalAveragePooling2D, Dense # type: ignore
from tensorflow.keras.models import Model # type: ignore
from tensorflow.keras.callbacks import EarlyStopping, ReduceLROnPlateau, ModelCheckpoint # type: ignore
from sklearn.metrics import classification_report

# Import the utility functions
from animal_classification import get_data_generators, display_translated_labels

# Set the directory path for images

def inceptionv3_model():
    directory = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'csv', 'raw-img')

    # Get the data generators
    train_generator, validation_generator = get_data_generators(directory)

    # Display and translate class labels
    class_labels, translated_labels = display_translated_labels(train_generator)

    # Model setup
    img_height, img_width = 224, 224
    base_model = InceptionV3(weights='imagenet', include_top=False, input_shape=(img_height, img_width, 3))

    for layer in base_model.layers:
        layer.trainable = False

    x = base_model.output
    x = GlobalAveragePooling2D()(x)
    x = Dense(512, activation='relu')(x)
    predictions = Dense(len(class_labels), activation='softmax')(x)
    model = Model(inputs=base_model.input, outputs=predictions)

    model.compile(
        loss="categorical_crossentropy",
        optimizer='adam',
        metrics=["accuracy", "Precision", "Recall"])

    # Callbacks
    callbacks = [
        EarlyStopping(monitor='val_loss', patience=8, restore_best_weights=True),
        ReduceLROnPlateau(monitor='val_loss', factor=0.1, patience=5, min_lr=1e-6),
        # ModelCheckpoint('inceptionv3.keras', save_best_only=True) - had to comment out due to space
    ]

    # Training
    history = model.fit(train_generator,
                        validation_data=validation_generator,
                        epochs=5,
                        callbacks=callbacks)
    

    # After training

    y_test = validation_generator.classes
    y_pred = np.argmax(model.predict(validation_generator), axis=1)
    print(classification_report(y_test, y_pred, target_names=translated_labels))

    model.save('trained_animal_classifier.h5', save_format='h5')

    save_path = 'trained_animal_classifier.h5'
    model.save(save_path)
    return model

if __name__ == "__main__":
    inceptionv3_model()

