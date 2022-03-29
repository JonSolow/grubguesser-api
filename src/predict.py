from model import CNN, LABELS



def predict_model(img_array):
    class_prob = CNN.predict(img_array)
    top_values_index = (-class_prob).argsort()[0][:10]
    top_guesses = [LABELS[i].title() for i in top_values_index]

    return top_guesses
