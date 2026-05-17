import cv2
import os

# 👉 INPUT & OUTPUT folders
input_folder = "images"      
output_folder = "output"    

# 👉 Output folder create (agar nahi hai)
os.makedirs(output_folder, exist_ok=True)

# 👉 Loop through all images
for file in os.listdir(input_folder):
    if file.endswith(".jpg") or file.endswith(".png"):
        path = os.path.join(input_folder, file)

        img = cv2.imread(path)
        if img is None:
            print(f"❌ Skipped (can't read): {file}")
            continue

        # Preprocessing
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(gray, (5,5), 0)
        _, thresh = cv2.threshold(blur, 60, 255, cv2.THRESH_BINARY_INV)

        # Contours
        contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        # Draw boxes
        for cnt in contours:
            if cv2.contourArea(cnt) > 500:
                x, y, w, h = cv2.boundingRect(cnt)
                cv2.rectangle(img, (x,y), (x+w,y+h), (0,0,255), 2)

        # Save result
        out_path = os.path.join(output_folder, file)
        cv2.imwrite(out_path, img)

        print(f"✅ Processed: {file}")

print("🎉 Done! Check output folder.")
_, thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)