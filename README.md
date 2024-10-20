


# Student Exam Performance Prediction

This project focuses on predicting student exam performance using machine learning techniques. The web-based application is built with Flask and follows a modular programming structure. It includes data ingestion, preprocessing, model training, and a prediction pipeline.

## Project Overview

The project leverages machine learning to predict student performance based on various input features. The entire system is modular, allowing for easy maintenance and scalability. This README provides a comprehensive overview of the project structure, the components involved, and the steps to run the application.

## File Structure

```bash
├── artifact/
│   ├── data.csv                    # Raw dataset
│   ├── model.pkl                   # Model pickle file
│   ├── preprocessing.pkl           # Preprocessing pickle file
│   ├── test.csv                    # Test dataset
│   ├── train.csv                   # Train dataset
├── notebook/
│   ├── EDA.ipynb                   # Exploratory Data Analysis (EDA) notebook
│   ├── Performance.ipynb           # Model performance analysis
│   ├── Model_Training.ipynb        # Model training notebook
├── src/
│   ├── component/
│   │   ├── data_ingestion.py       # Data ingestion script
│   │   ├── data_transformation.py  # Data transformation script
│   │   ├── model_trainer.py        # Model training script
│   ├── pipeline/
│   │   ├── predict_pipeline.py     # Prediction pipeline script
│   ├── exception.py                # Custom error handling
│   ├── logger.py                   # Logging utility
│   ├── utils.py                    # Utility functions
├── static/
│   ├── styles.css                  # CSS file for front-end
├── template/
│   ├── index.html                  # HTML template
├── app.py                          # Main Flask application
├── application.py                  # Entry point of the application
├── setup.py                        # Local version control setup
```

### Key Components

- **artifact/**: This folder contains the dataset (`data.csv`), trained model (`model.pkl`), and other files such as the preprocessing pickle and split datasets for training and testing.
  
- **notebook/**: Contains Jupyter notebooks used for Exploratory Data Analysis (EDA), model training, and performance evaluation.

- **src/**: Houses the core logic of the application, including data ingestion, transformation, and model training. Additionally, it includes the pipeline for predictions, and files for custom error handling, logging, and utility functions.

- **static/**: Contains static resources like the CSS files used for styling the web pages.

- **template/**: Includes the HTML template for rendering the web interface using Flask.

- **app.py**: The main file that runs the Flask application and handles user interactions.

- **application.py**: A wrapper around the `app.py` to initialize the entire application.

- **setup.py**: Manages local version control.

## Getting Started

### Prerequisites

- Python 3.7+
- Flask
- Pandas
- Scikit-learn
- Pickle

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/student-exam-prediction.git
    cd student-exam-prediction
    ```

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Set up the application using `setup.py` for local version control:

    ```bash
    python setup.py install
    ```

### Running the Application

After installation, run the following command to start the Flask server:

```bash
python app.py
```

Access the web application by navigating to:

```
http://localhost:5000/predictdata
```

### Prediction Pipeline

The application allows users to input student data through a form, and it predicts exam performance based on the trained model. The prediction pipeline ensures smooth data flow, starting from data ingestion to prediction output.

## Exploratory Data Analysis (EDA)

EDA was performed in the `notebook/EDA.ipynb` file using Jupyter notebooks. This step included the following:

- Overview of the dataset (`data.csv`), identifying key statistical metrics.
- Data visualization to identify trends and distributions.
- Feature selection and correlation analysis for model training.
  
The dataset contains various features related to student demographics, study time, previous exam scores, and more.

## Model Training

The model training process is documented in the `notebook/Model_Training.ipynb` file. Key steps include:

- Data preprocessing (handling missing values, encoding categorical features, etc.).
- Training multiple machine learning models and evaluating their performance.
- The best-performing model was serialized using `pickle` and saved as `model.pkl`.

## Custom Error Handling and Logging

The project uses custom error handling and logging:

- **exception.py**: Handles custom exceptions and improves the robustness of the application.
  
- **logger.py**: Logs all events during data processing, model training, and prediction. The logs are stored for debugging purposes.

## CSS and HTML

The front-end of the application is designed with HTML (in the `template/` folder) and styled with CSS (in the `static/` folder).

## Future Work

- **Model Optimization**: Improving the current model's accuracy through hyperparameter tuning and exploring more complex algorithms.
- **Deployment**: Deploying the model on cloud services like AWS or Google Cloud for scalability.
- **Feature Expansion**: Adding more input features to improve prediction accuracy and provide better insights into student performance.



