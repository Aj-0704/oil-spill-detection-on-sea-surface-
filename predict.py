import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

model = load_model("oil_model.h5")

img = image.load_img("images/img1.jpg.jpg", target_size=(128,128))
img = image.img_to_array(img) / 255.0
img = np.expand_dims(img, axis=0)

pred = model.predict(img)

if pred[0][0] > 0.5:
    print("🚨 Oil Spill Detected")
else:
    print("✅ Clean Water")