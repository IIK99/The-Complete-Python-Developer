from imageai.Classification import ImageClassification
import os

exec_path = os.getcwd()

prediction = ImageClassification()
# Menggunakan model ResNet
prediction.setModelTypeAsResNet50()
model_path = os.path.join(exec_path, 'resnet50_weights_tf_dim_ordering_tf_kernels.h5')  # Path ke model ResNet

if not os.path.isfile(model_path):
    raise FileNotFoundError(f"Model file not found at {model_path}. Please ensure the file exists.")

prediction.setModelPath(model_path)
prediction.loadModel()

predictions, probabilities = prediction.classifyImage(os.path.join(exec_path, 'house.jpg'), result_count=5)
for eachPred, eachProb in zip(predictions, probabilities):
    print(f'{eachPred} : {eachProb}')
