import argparse
import pandas as pd
import pickle

# Load the trained model using pickle
with open('modelo_entrenado.pkl', 'rb') as model_file:
    loaded_model = pickle.load(model_file)

def make_predictions(model, input_data):
    # Make predictions using the model
    predictions = model.predict(input_data)
    return predictions

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Predict Pulsars from a CSV file")
    parser.add_argument("input_data", help="Path to the input CSV file containing data for prediction")

    args = parser.parse_args()

    # Load the input data
    input_data = pd.read_csv(args.input_data)

    # Make predictions
    predictions = make_predictions(loaded_model, input_data)

    # Print the predictions
    print("Predictions:")
    print(predictions)
