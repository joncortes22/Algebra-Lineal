import os, sys, getpass
from tkinter import *
from tkinter import messagebox, ttk
import string

class Logic_Class:
    def __init__(self) -> None:
        #self.main_win()

        self.encrypt("MaTE MuSCUlOS", [[35,53,12],[12,21,5],[2,4,1]])

    def method(self):
        try:
            pass
        except Exception as method_error:
            error_line = method_error.__traceback__.tb_lineno
            print(f'Error in line {str(error_line)}')

    # WINDOW METHODS

    def main_win(self):
        try:
            root = Tk()
            root.geometry("400x300")
            root.title("MENÚ PRINCIPAL")
            root.resizable(0,0)

            lb_title = Label(root, text="MENÚ PRINCIPAL", font=("Arial", 15))
            lb_title.place(x=115, y=80)

            btn_encrypt = Button(root, text ="ENCRIPTAR", font=("Arial", 10), command=lambda:self.encrypt_win(root), height=1, width=15)
            btn_encrypt.place(x=60, y=160)

            btn_deencrypt = Button(root, text ="DESENCRIPTAR", font=("Arial", 10), height=1, width=15)
            btn_deencrypt.place(x=215, y=160)

            root.mainloop()
        except Exception as method_error:
            error_line = method_error.__traceback__.tb_lineno
            print(f'Error in line {str(error_line)}')

    def encrypt_win(self, root):
        try:
            root.destroy()
            root = Tk()
            root.geometry("400x300")
            root.title("ENCRIPTAR")
            root.resizable(0,0)

            lb_title = Label(root, text="ENCRIPTAR", font=("Arial", 15))
            lb_title.place(x=130, y=35)

            lb_phrase = Label(root, text="Frase:", font=("Arial", 10))
            lb_phrase.place(x=80, y=110)

            txt_phrase = Entry(root)
            txt_phrase.place(x=135, y=110)

            lb_key = Label(root, text="ENCRIPTAR", font=("Arial", 15))
            lb_key.place(x=130, y=35)

            root.mainloop()
        except Exception as method_error:
            error_line = method_error.__traceback__.tb_lineno
            print(f'Error in line {str(error_line)}')
        
    # LOGIC METHODS

    def mod_27(self, array:list):
        """Este método se usa para aplicar un mod27 a cada valor dentro de un array
        Args:
            key (list): Matriz con numeros base 10 sin modificaciones
        Returns:
            array (list): Matriz con cada valor modificado con su residuo del mod27
        """
        try:
            for row in enumerate(array):
                for col in enumerate(array[0]):
                    array[row[0]][col[0]] = array[row[0]][col[0]] % 27
            return array
        except Exception as method_error:
            error_line = method_error.__traceback__.tb_lineno
            print(f'Error in line {str(error_line)}')

    def transpose_array(self, array):
        """Este método se usa para aplicar una transposición a una matriz
         e.g [[1,2,3],[4,5,6]] pasa a [[1,4],[2,5],[3,6]]
        Args:
            array (list): Matriz deseada
        Returns:
            array (list): Matriz después de ser transpuesta
        """
        try:
            phrase_by_index = []
            for i, row in enumerate(array[0]):
                transported_row = []
                for x, index in enumerate(array):
                    transported_row.append(array[x][i])
                phrase_by_index.append(transported_row)
            return phrase_by_index
        except Exception as method_error:
            error_line = method_error.__traceback__.tb_lineno
            print(f'Error in line {str(error_line)}')

    def multiply_arrays(self, array1:list, array2:list):
        """Este método se usa para aplicar una multiplicación de matrices
        Args:
            array1 (list): Matriz a multiplicar 1
            array2 (list): Matriz a multiplicar 2
        Returns:
            product_array (list): Matriz con el producto de la multiplicación
        """
        try:
            product_array = []
            for column in enumerate(array2[0]):
                column_list = []
                for row_value in array1:
                    result = 0
                    row_counter = 0
                    for column_val in array2:
                        result += row_value[row_counter] * column_val[column[0]]
                        row_counter += 1
                    column_list.append(result)
                product_array.append(column_list)
            return product_array
        except Exception as method_error:
            error_line = method_error.__traceback__.tb_lineno
            print(f'Error in line {str(error_line)}')

    def char_to_value(self, alphabet, array):
        """Este método se usa para pasar las letras de una matriz a su valor posicional en el abecedario
            e.g 'A'->0
        Args:
            alphabet (list): Alfabeto en inglés, más un guión bajo '_'
            array (list): Matriz a con los caracteres a modificar
        Returns:
            array (list): Matriz con los nuevos valores
        """
        try:
            for i, row in enumerate(array):
                row_by_index = []
                for char in row:
                    for index, letter in enumerate(alphabet):
                        if char == letter:
                            row_by_index.append(index)
                array[i] = row_by_index
            return array
        except Exception as method_error:
            error_line = method_error.__traceback__.tb_lineno
            print(f'Error in line {str(error_line)}')

    def value_to_char(self, alphabet, array):
        """Este método se usa para pasar los valores posicionales de un abecedario a la letra que representa
            e.g 0->'A'
        Args:
            alphabet (list): Alfabeto en inglés, más un guión bajo '_'
            array (list): Matriz a con los caracteres a modificar
        Returns:
            array (list): Matriz con los nuevos valores
        """
        try:
            for row in enumerate(array):
                for col in enumerate(array[0]):
                    for index, letter in enumerate(alphabet):
                        if row[1][col[0]] == index:
                            array[row[0]][col[0]] = letter
                            break
            return array
        except Exception as method_error:
            error_line = method_error.__traceback__.tb_lineno
            print(f'Error in line {str(error_line)}')

    def array_to_string(self, array:list):
        """Este método se usa para pasar una matriz con letras a un solo string
            e.g [[A,'P'],['X','G']]->'APXG'
        Args:
            array (list): Matriz a con los valores a modificar
        Returns:
            encrypted_string (string): String unificado
        """
        try:
            encrypted_string = ''
            counter = 0
            for i in range(len(array[counter])):
                for x in range(len(array)):
                    encrypted_string += array[x][i]
                counter += 1
            
            return encrypted_string
        except Exception as method_error:
            error_line = method_error.__traceback__.tb_lineno
            print(f'Error in line {str(error_line)}')

    def encrypt(self, phrase:str, key:list):
        """Este método se usa para encriptar un string mediante el Cifrado de Hill
        Args:
            phrase (str): Frase que se quiere encriptar
            key (list): Matriz de orden 3 con la clave para la encripción
        """
        try:
            # PASAR EL STRING A MAYÚSULA Y SE CAMBIAN LOS ESPACIOS POR GUIONES BAJO
            phrase = phrase.upper().replace(' ', '_')

            # SI NO HACE GRUPOS DE 3 EXACTOS, SE SUMAN GUIONES BAJOS
            result = len(phrase) % 3
            phrase += "_" * (3 - result) if result != 0 else ""
            
            # DIVIDIR EL STRING EN GRUPOS DE 3
            phrase_array = [phrase[i:i+3] for i in range(0, len(phrase), 3)]

            # GUARDAR EL ALFABETO EN UNA LISTA
            alphabet = list(string.ascii_uppercase)
            alphabet += '_'

            # PASAR CADA CHAR DE UNA LISTA A SU EQUIVALENTE EN EL ALFABETO
            phrase_array = self.char_to_value(alphabet, phrase_array)

            # TRANSPORTAR UNA MATRIZ
            phrase_array = self.transpose_array(phrase_array)

            phrase_array = self.multiply_arrays(key, phrase_array)

            phrase_array = self.transpose_array(phrase_array)

            phrase_array = self.mod_27(phrase_array)

            phrase_array = self.value_to_char(alphabet, phrase_array)

            encrypted_string = self.array_to_string(phrase_array)
            print(encrypted_string)

        except Exception as method_error:
            error_line = method_error.__traceback__.tb_lineno
            print(f'Error in line {str(error_line)}')
    
if __name__ == "__main__":
    Logic_Class()