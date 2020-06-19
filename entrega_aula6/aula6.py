from imageai.Detection import ObjectDetection
import os

resultadoTxt = open('resultado_txt.txt', 'w')
path = input("Informe o caminho da imagem: ")

execution_path = os.getcwd()

detector = ObjectDetection()
detector.setModelTypeAsRetinaNet()
detector.setModelPath( os.path.join(execution_path , "resnet50_coco_best_v2.0.1.h5"))
detector.loadModel()
detectados = detector.detectObjectsFromImage(input_image=os.path.join(execution_path , path), output_image_path=os.path.join(execution_path , "resultado_img.jpg"), minimum_percentage_probability=30)

for objeto in detectados:
    resultadoTxt.write(objeto["name"] + ": " + str(int(objeto["percentage_probability"])) + "%\n")

resultadoTxt.close()