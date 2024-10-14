from PIL import Image
import numpy as np

def main():
    # carregar a imagem original
    img = Image.open("simple_icon.png")

    # converter a imagem em dados binários
    img_data = np.array(img)
    binary_data = img_data.tobytes()

    # mostra o tamanho da imagem
    print("/n", img_data.shape, "/n")
    # salvar os dados binários em um arquivo
    with open("original_img.bin", "wb") as file:
        file.write(binary_data)

    # copiar o arquivo binário
    with open ("original_img.bin", "rb") as original_file:
        data = original_file.read()

    with open("copy_img.bin", "wb") as copy_file:
        copy_file.write(data)

    # manipulação dos dados do arquivo binário cópia
    # exemplo: Inverter os bytes
    with open("copy_img.bin", "rb") as file:
        data = bytearray(file.read())

    with open("copy_img.bin", "wb") as file:
        file.write(data)

    # carregar e mostrar a imagem manipulada
    modified_data = np.frombuffer(data, dtype=np.uint8).reshape(img_data.shape)

    # inverter todos os bytes
    modified_data = np.fliplr(modified_data)

    modified_img = Image.fromarray(modified_data)
    modified_img.show()

if __name__ == "__main__":
    main()