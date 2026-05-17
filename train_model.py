from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense

# Data
train_datagen = ImageDataGenerator(rescale=1./255, validation_split=0.2)


train_generator = train_datagen.flow_from_directory(
    'train',
    target_size=(128,128),
    batch_size=32,
    class_mode='binary',
    subset='training'
)
val_generator = train_datagen.flow_from_directory(
    'train',
    target_size=(128,128),
    batch_size=32,
    class_mode='binary',
    subset='validation'
)
# Model
model = Sequential()
model.add(Conv2D(32, (3,3), activation='relu', input_shape=(128,128,3)))
model.add(MaxPooling2D(2,2))
model.add(Conv2D(64, (3,3), activation='relu'))
model.add(MaxPooling2D(2,2))
model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Train
model.fit(train_generator, epochs=20, validation_data=val_generator)
from sklearn.metrics import classification_report, f1_score
import numpy as np

# true labels (from generator)
y_true = val_generator.classes

# predicted labels
y_pred = model.predict(val_generator)
y_pred = (y_pred > 0.5).astype(int)

# F1 Score
f1 = f1_score(y_true, y_pred)

print("F1 Score:", f1)

# Full report
print(classification_report(y_true, y_pred))

# Save model
model.save("oil_model.h5")

print("✅ Model trained & saved!")