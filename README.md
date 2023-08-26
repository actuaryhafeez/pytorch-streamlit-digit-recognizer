# pytorch-streamlit-digit-recognizer
PyTorch Streamlit Digit Recognizer

# Description 
This repository contains a simple digit recognition app built using PyTorch and Streamlit. The app allows users to upload images of hand-drawn digits and uses a trained deep learning model to predict the digit's value.

# Features
- Built using PyTorch and Streamlit.
- Trained deep learning model for digit recognition.
- User-friendly interface for uploading images.
- Real-time predictions displayed on the app.

# App Preview
Here are some GIFs showcasing the functionality of the app:
![GIF 1](./data/gif1.gif)
![GIF 2](./data/gif2.gif)
![GIF 3](./data/gif3.gif)

# How to Use
Clone the repository:

    git clone https://github.com/yourusername/pytorch-streamlit-digit-recognizer.git

Install the required dependencies:

    pip install -r requirements.txt

Run the Streamlit app:

    streamlit run app.py
    
Upload an image containing a hand-drawn digit from the "data" directory.

Click the "Predict" button to see the model's prediction.

# About the Model
The digit recognition model is trained on the MNIST dataset using PyTorch. It consists of convolutional layers followed by a fully connected layer. The model has been trained to achieve accurate digit classification.

# Try It Out
Feel free to clone this repository and try out the digit recognition app yourself. If you have any questions or suggestions, please don't hesitate to open an issue or submit a pull request.

# Project Structure 

    pytorch-streamlit-digit-recognizer/
        ├── data/
        ├── app.py/
        ├── requirements.txt/
        ├── README.md/
        ├── model.py
        ├── pedict.py
        ├── model.pt
        ├── LICENSE/

        

# License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

This project adheres to the [Open Source Initiative's](https://opensource.org) definition of open source software and the [Open Source Initiative's Approved License List](https://opensource.org/licenses/alphabetical).

# Contributions
Contributions are welcome! If you find any issues or bugs, feel free to open an issue or submit a pull request.

