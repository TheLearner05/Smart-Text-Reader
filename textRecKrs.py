import numpy as np
import keras_ocr
from matplotlib import pyplot as plt

# keras-ocr will automatically download pretrained
# weights for the detector and recognizer.
pipeline = keras_ocr.pipeline.Pipeline()

# List of three example images
images = [keras_ocr.tools.read(img) for img in [
    r'L:\textDetection-Recognition\image2.jpg']]

# Print shape...
print(np.shape(images))

# Each list of predictions in prediction_groups is a list of
# (word, box) tuples.
prediction_groups = pipeline.recognize(images)

# Plot the predictions
fig, axs = plt.subplots(nrows=len(images), figsize=(20, 20))
for ax, image, predictions in zip(axs, images, prediction_groups):
    keras_ocr.tools.drawAnnotations(
        image=image, predictions=predictions, ax=ax)
