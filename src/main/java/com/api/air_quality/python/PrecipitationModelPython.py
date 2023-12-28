from py4j.java_gateway import JavaGateway
import numpy as np
import pickle


class PrecipitationModelPython:
    def __init__(self):
        self.gateway = JavaGateway()
        self.java_model = self.gateway.entry_point
        with open("../../../../../../../AI_Models/precipitation_model.pkl", 'rb') as f:
            self.model = pickle.load(f)

    def predict_precipitation(self, features):
        try:
            features_2d = np.array(features).reshape(1, -1)
            prediction = self.model.predict(features_2d)
            return self.java_model.receivedPrecipitationPrediction(prediction[0])
        except Exception as e:
            return str(e)


if __name__ == "__main__":
    precipitation_model = PrecipitationModelPython()
    test_data = precipitation_model.java_model.predict()
    result = precipitation_model.predict_precipitation(test_data)
    print(result)