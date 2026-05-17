🌊 Oil Spill Detection on Sea Surface using Deep Learning<br>
📌 Project Overview<br>

This project focuses on detecting oil spills on sea surfaces using Computer Vision and Deep Learning techniques. The system analyzes SAR (Synthetic Aperture Radar) satellite images and classifies them as either:<br>

Oil Spill<br>
Clean Water<br>

The project combines OpenCV image processing with a Convolutional Neural Network (CNN) model for accurate oil spill detection.<br>

🚀 Features<br>
🛰️ Oil spill detection using SAR satellite images<br>
🧠 CNN-based deep learning model<br>
📷 Image preprocessing with OpenCV<br>
📊 Accuracy and F1-score evaluation<br>
🔍 Prediction on new test images<br>
💾 Trained model saving and loading<br>
🛠️ Technologies Used<br>
Technology	Purpose<br>
Python	Programming Language<br>
OpenCV	Image Processing<br>
TensorFlow / Keras	Deep Learning<br>
NumPy	Numerical Operations<br>
Matplotlib	Visualization<br>
Scikit-learn	Evaluation Metrics<br>
📊 Dataset<br>

The model is trained on SAR satellite images divided into two classes:<br>

train/<br>
   oil/<br>
   clean/<br>
Dataset Sources<br>
Kaggle Oil Spill Dataset<br>
Sentinel-1 SAR Images<br>
🧠 CNN Model Architecture<br>

The CNN model includes:<br>

Conv2D Layers<br>
MaxPooling Layers<br>
Flatten Layer<br>
Dense Layers<br>
Sigmoid Activation<br>
▶️ How to Train the Model<br>

Run:<br>

python train_model.py<br>

The model will:<br>

Load dataset<br>
Train CNN<br>
Calculate accuracy and F1 score<br>
Save trained model<br>
🔍 How to Predict New Images<br>

Run:<br>

python predict.py<br>

The model predicts:<br>

Oil Spill Detected<br>
Clean Water<br>
📈 Model Performance<br>
Metric	Value<br>
Training Accuracy	~91–97%<br>
F1 Score	~0.80+<br>
🧪 Evaluation Metrics<br>

The project uses:<br>

Accuracy<br>
Validation Accuracy<br>
Precision<br>
Recall<br>
F1 Score<br>
🌍 Applications<br>
Marine pollution monitoring<br>
Environmental protection<br>
Satellite-based surveillance<br>
Disaster management<br>
🔮 Future Improvements<br>
Real-time satellite monitoring<br>
U-Net segmentation model<br>
Drone integration<br>
Web dashboard deployment<br>
Mobile application support<br>
👥 Team Contributions<br>
Member	Responsibility<br>
Member 1	Dataset & Research<br>
Member 2	OpenCV & Image Processing<br>
Member 3	CNN Model Development<br>
Member 4	Testing & Evaluation<br>
Member 5	Documentation & Presentation<br>
💬 Conclusion<br>

This project demonstrates how Artificial Intelligence and Computer Vision can be used for environmental monitoring and automatic oil spill detection on sea surfaces with high accuracy.<br>

📜 License<br>

This project is developed for educational and research purposes.<br>
