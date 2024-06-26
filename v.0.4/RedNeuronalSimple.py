import os
from keras.models import load_model  # TensorFlow is required for Keras to work
from PIL import Image, ImageOps  # Install pillow instead of PIL
import numpy as np

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

def ModeloNeuronal(Ruta_de_modelo_etiquetas,Modelo,Etiquetas,Archivo):
    # Disable scientific notation for clarity
    np.set_printoptions(suppress=True)

    # Load the model
    model = load_model(os.path.join(os.getcwd(),'__modelos__',f'{Ruta_de_modelo_etiquetas}',f"{Modelo}.h5"), compile=False)

    # Load the labels
    class_names = open(os.path.join(os.getcwd(),'__modelos__',f'{Ruta_de_modelo_etiquetas}',f"{Etiquetas}.txt"), "r", encoding='utf-8').readlines()

    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    # Replace this with the path to your image

    image = Image.open(os.path.join(os.getcwd(),'__fotos_sad__',f'{Archivo}')).convert("RGB")
    # resizing the image to be at least 224x224 and then cropping from the center

    size = (224, 224)
    image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)

    # turn the image into a numpy array
    image_array = np.asarray(image)

    # Normalize the image
    normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1

    # Load the image into the array
    data[0] = normalized_image_array

    # Predicts the model
    prediction = model.predict(data)
    index = np.argmax(prediction)
    class_name = class_names[index]
    confidence_score = prediction[0][index]

    ops = class_name
    return ops.split()[1]
    # print(ops.split()[1])

# RSP = ModeloNeuronal('IdentificacionSuministro','ConjuntosSuministro','Suministro','Imagen_007.jpg')
# RSP = ModeloNeuronal('TipoMedidores','Tipo','Medidores','Imagen_010.jpg')
# print(RSP)
    