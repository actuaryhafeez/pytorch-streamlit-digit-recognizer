import torch
from PIL import Image
from torchvision.transforms import ToTensor
from model import ImageClassifier  # Import your ImageClassifier class

def predict(image_path):
    # Load the trained model
    clf = ImageClassifier()
    clf.load_state_dict(torch.load('model.pt', map_location=torch.device('cpu')))
    clf.eval()

    # Load and preprocess the image
    image = Image.open(image_path)
    img_tensor = ToTensor()(image).unsqueeze(0)

    # Make prediction
    with torch.no_grad():
        outputs = clf(img_tensor)
        predicted_class = torch.argmax(outputs).item()

    return predicted_class

if __name__ == "__main__":
    image_path = 'data/img_3.jpg'  # Replace with the actual image path
    predicted_class = predict(image_path)
    print(f"Predicted Class: {predicted_class}")
