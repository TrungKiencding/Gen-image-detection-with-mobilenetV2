import tensorflow as tf
import numpy as np


model = tf.keras.models.load_model("model/model.h5")

# Define target dimensions matching model's input shape (224x224)
target_size = (128, 128)
image_path = "image/test.jpg"

# Load the image and resize it to the target dimensions
image_raw = tf.io.read_file(image_path)

# Convert the PIL image to a NumPy array
image_tensor = tf.image.decode_image(image_raw, channels=3)

image_resized = tf.image.resize(image_tensor, target_size)
# Optional: Normalize the image (if your model was trained on normalized images)
image_normalized = image_resized / 255.0

# Add a new axis to create a batch of one image
image_batch = tf.expand_dims(image_normalized, axis=0)

# Predict using your pre-loaded model
predictions = model.predict(image_batch)

output = 1 / (1 + np.exp(-predictions))
if output > 0.5:
    label = "AI"
else:
    label = "Not AI"
print("Predictions:", label)

