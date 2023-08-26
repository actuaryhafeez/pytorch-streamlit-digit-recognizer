import streamlit as st
import torch
from PIL import Image
from torchvision.transforms import ToTensor
from model import ImageClassifier

# Load the trained model
clf = ImageClassifier()
clf.load_state_dict(torch.load('model.pt', map_location=torch.device('cpu')))
clf.eval()

def predict(image):
    img_tensor = ToTensor()(image).unsqueeze(0)
    with torch.no_grad():
        outputs = clf(img_tensor)
        predicted_class = torch.argmax(outputs).item()
        return predicted_class

def main():
    st.title("Digit Image Classifier App")
    st.write("Upload an image and get a prediction from the trained model.")

    uploaded_image = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

    if uploaded_image is not None:
        image = Image.open(uploaded_image)

        # Set the desired width and height for the displayed image
        image_width = 275

        st.image(image, caption="Uploaded Image.", width=image_width)

        if st.button("Predict"):
            prediction = predict(image)
            st.write(f"Predicted Class: {prediction}")

if __name__ == "__main__":
    main()
