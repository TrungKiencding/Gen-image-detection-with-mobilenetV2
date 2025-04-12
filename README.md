# Gen AI Detection Program

This project focuses on building a program to detect AI-generated images using a fine-tuned MobileNetV2 model trained on the AI-vs-human-generated dataset. The goal is to differentiate between human-created and AI-generated images effectively.

## Project Structure

├── model/model.h5 # Folder contain finetuned model
├── image/ # Directory to store input images for detection
├── app.py # Main script to run the detection program
├── gen-image-detection.ipynb # Jupyter notebook for training and experimenting with the model


## Features

- **Model Architecture**: MobileNetV2, fine-tuned for image classification.
- **Dataset**: AI-vs-human-generated dataset used for training and evaluation.
- **Detection Program**: A Python script (`app.py`) that takes input images and predicts whether they are AI-generated or human-created.

## Requirements

To run this project, you need:

- Python 3.8 or higher
- TensorFlow 2.x
- Jupyter Notebook
- Other dependencies listed in `requirements.txt`

## Installation and Setup

Follow these steps to set up the project:

1. **Clone the Repository**  
   Clone this repository to your local machine:
```
git clone <repository-url>
cd <repository-name>
```


2. **Set Up a Virtual Environment**  
Create a virtual environment for Python dependencies:
```
python -m venv env
```


3. **Activate the Virtual Environment**  
- On Windows:
  ```
  .\env\Scripts\activate
  ```
- On macOS/Linux:
  ```
  source env/bin/activate
  ```

4. **Install Dependencies**  
Install the required Python packages:
```
pip install -r requirements.txt
```

## Usage Instructions

### Training the Model
You can train or evaluate the model using the Jupyter notebook (`gen-image-detection.ipynb`). Open the notebook in Jupyter and follow the instructions provided inside.

### Running the Detection Program
Use `app.py` to detect whether images in the `image/` directory are AI-generated or human-created:
```
python app.py
```

The program will output predictions for each image in the directory.

## Contributing

We welcome contributions! If you have suggestions, improvements, or bug fixes, feel free to submit an issue or create a pull request.

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for more details.

### Contact

If you have any questions or need assistance, feel free to reach out via GitHub issues.

