import streamlit as st
import tensorflow as tf
from PIL import Image
import numpy as np
import os
import random
from tensorflow import keras

ModelCheckpoint = tf.keras.callbacks.ModelCheckpoint
save_model = keras.models.save_model
load_model = keras.models.load_model

def load_trained_model():
    try:
        model = tf.keras.models.load_model('trained_animal_classifier.h5', compile=False)
        st.write("Model loaded successfully")  # Debug print
        return model
    except Exception as e:
        st.error(f"Error loading model: {e}")
        return None

def preprocess_image(image, target_size=(224, 224)):
    """Preprocess the uploaded image for model prediction."""
    try:
        img = image.resize(target_size)
        img_array = np.array(img) / 255.0  # Normalize pixel values
                
        img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension
        return img_array
    except Exception as e:
        st.error(f"Error preprocessing image: {e}")
        return None

def predict_animal(model, image, class_labels):
    """Predict the animal in the image and return top predictions."""
    try:
        predictions = model.predict(image)
        
        # Debug: print raw predictions
        # st.write("Raw predictions:", predictions)
        
        top_indices = predictions[0].argsort()[-3:][::-1]  # Get top 3 predictions
        
        top_predictions = []
        for idx in top_indices:
            label = class_labels[idx]  # Get the corresponding label
            confidence = predictions[0][idx] * 100
            top_predictions.append((label, confidence))
        
        return top_predictions
    except Exception as e:
        st.error(f"Error making prediction: {e}")
        return None

def main():
    st.title("Animal Image Classifier")
    
    # Load the pre-trained model
    model = load_trained_model()
    
    if model is None:
        st.error("Failed to load the model")
        st.stop()
    
    # Define animal directories
    animal_image_directories = {
        "dog": "cane",
        "horse": "cavallo",
        "elephant": "elefante",
        "butterfly": "farfalla",
        "chicken": "gallina",
        "cat": "gatto",
        "cow": "mucca",
        "sheep": "pecora",
        "spider": "ragno",
        "squirrel": "scoiattolo",
    }

    # Collect images
    all_image_files = []
    for animal, folder_name in animal_image_directories.items():
        directory = os.path.join('csv', 'raw-img', folder_name)
        if os.path.exists(directory):
            images = [os.path.join(directory, f) for f in os.listdir(directory) if f.endswith(('.jpeg', '.jpg', '.png'))]
            all_image_files.extend(images)

    # Button to select a random image
    if st.button("Show Random Image"):
        if not all_image_files:
            st.error("No images found in the specified directories.")
        else:
            random_image_path = random.choice(all_image_files)
            st.image(random_image_path, caption=f"Randomly Selected Image")
            
            # Open the image
            try:
                image = Image.open(random_image_path)
                
                # Preprocess the image
                preprocessed_image = preprocess_image(image)
                
                if preprocessed_image is not None:
                    # Load class labels
                    class_labels = list(animal_image_directories.keys())
                    
                    # Make prediction
                    predictions = predict_animal(model, preprocessed_image, class_labels)
                    
                    # Display predictions
                    if predictions:
                        st.subheader("Prediction Results")
                        for label, confidence in predictions:
                            st.write(f"{label}: {confidence:.2f}%")
                    else:
                        st.error("Failed to get predictions")
            except Exception as e:
                st.error(f"Error processing image: {e}")
    else:
        st.info("Click 'Show Random Image' to view an image.")

if __name__ == "__main__":
    main()

