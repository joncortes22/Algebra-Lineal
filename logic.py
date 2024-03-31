import os, sys, getpass
from tkinter import *
from tkinter import messagebox, ttk
import string

class Logic_Class:
    def __init__(self) -> None:
        #self.main_win()
        self.alphabet = list(string.ascii_uppercase)
        self.alphabet += '_'
       
        text = "ALGEBRA LINEAL"
        key = [[35,53,12],[12,21,5],[2,4,1]]

        print(f'TEXTO: {text}')
        print(f'CLAVE: {key}')
        message = self.encrypt(text, key)
        print(f'TEXTO ENCRIPTADO: {message}')
        deencrypted = self.deencrypt(message, key)
        print(f'TEXTO DESENCRIPTADO: {deencrypted}')

    # BASE METHOD
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

    # MAIN METHODS
            
    def encrypt(self, phrase:str, key:list):
        """Este método se usa para encriptar un string mediante el Cifrado de Hill
        Args:
            phrase (str): Frase que se quiere encriptar e.g 'PROFESOR ADRIAN'
            key (list): Matriz de orden 3 con la clave para la encripción
            e.g [[35,53,12],[12,21,5],[2,4,1]]
        Return:
            encrypted_string (str): String encriptado e.g BNEJSRCHOMNCEC
        """
        try:
            # PASAR EL STRING A MAYÚSULA Y SE CAMBIAN LOS ESPACIOS POR GUIONES BAJO
            phrase = phrase.upper().replace(' ', '_')

            # SI NO HACE GRUPOS DE 3 EXACTOS, SE SUMAN GUIONES BAJOS
            result = len(phrase) % 3
            phrase += "_" * (3 - result) if result != 0 else ""
            
            # DIVIDIR EL STRING EN GRUPOS DE 3
            phrase_array = [phrase[i:i+3] for i in range(0, len(phrase), 3)]
            "['ALG', 'EBR', 'A_L', 'INE', 'AL_']"

            # PASAR CADA CHAR DE UNA LISTA A SU EQUIVALENTE EN EL ALFABETO
            phrase_array = self.char_to_value(self.alphabet, phrase_array)
            "[[0, 11, 6], [4, 1, 17], [0, 26, 11], [8, 13, 4], [0, 11, 26]]"

            # TRANSPORTAR LA MATRIZ
            phrase_array = self.transpose_array(phrase_array)
            "[[0, 4, 0, 8, 0], [11, 1, 26, 13, 11], [6, 17, 11, 4, 26]]"

            # MULTIPLICAR RAIZ DE VALORES CON LA CLAVE GENERADA
            phrase_array = self.multiply_arrays(key, phrase_array)
            "[[655, 261, 50], [397, 154, 29], [1510, 601, 115], [1017, 389, 72], [895, 361, 70]]"

            # TRANSPORTAR LA MATRIZ NUEVAMENTE
            phrase_array = self.transpose_array(phrase_array)
            "[[655, 397, 1510, 1017, 895], [261, 154, 601, 389, 361], [50, 29, 115, 72, 70]]"

            # APLICAR MOD27 PARA GENERAR VALORES NUMÉRICOS ENCRIPTADOS
            phrase_array = self.mod_27(phrase_array)
            "[[7, 19, 25, 18, 4], [18, 19, 7, 11, 10], [23, 2, 7, 18, 16]]"
            
            # PASAR VALORES NÚMERICOS ENCRIPTADOS A LETRAS
            phrase_array = self.value_to_char(self.alphabet, phrase_array)
            "[['H', 'T', 'Z', 'S', 'E'], ['S', 'T', 'H', 'L', 'K'], ['X', 'C', 'H', 'S', 'Q']]"

            # PASAR LAS LETRAS ENCRIPTADAS DENTRO DEL ARRAY A UN SOLO STRING
            encrypted_string = self.array_to_string(phrase_array)
            "HSXTTCZHHSLSEKQ"

            return encrypted_string

        except Exception as method_error:
            error_line = method_error.__traceback__.tb_lineno
            print(f'Error in line {str(error_line)}')
    
    def deencrypt(self, phrase:str, key:list):
        """Este método se usa para desencriptar un string mediante el Cifrado de Hill
        Args:
            phrase (str): Frase encriptada
            key (list): Matriz de orden 3 con la clave para la encripción
            e.g [[35,53,12],[12,21,5],[2,4,1]]
        """
        try:
            # INICIALIZAR STRING
            encrypted_string = ''

            # DIVIDIR EL STRING ENCRIPTADO EN GRUPOS DE 3
            encrypted_string = [phrase[i:i+3] for i in range(0, len(phrase), 3)]
            "['HSX', 'TTC', 'ZHH', 'SLS', 'EKQ']"

            # PASAR CADA VALOR DE UNA LISTA A SU EQUIVALENTE EN EL ALFABETO
            encrypted_string = self.char_to_value(self.alphabet, encrypted_string)
            "[[7, 18, 23], [19, 19, 2], [25, 7, 7], [18, 11, 18], [4, 10, 16]]"

            # TRANSPORTAR LA MATRIZ
            encrypted_string = self.transpose_array(encrypted_string)
            "[[7, 19, 25, 18, 4], [18, 19, 7, 11, 10], [23, 2, 7, 18, 16]]"

            # SACAR INVERSA DE LA CLAVE
            inversed_key = self.gauss_jordan(key)
            "[[1, -5, 13], [-2, 11, -31], [6, -34, 99]]"

            # APLICAR MOD 27 A LA CLAVE
            key = self.mod_27(inversed_key)
            "[[1, 22, 13], [25, 11, 23], [6, 20, 18]]"

            # MULTIPLICAR LA CLAVE (CON MOD27 YA APLICADO) CON LA MATRIZ DE VALORES
            encrypted_string = self.multiply_arrays(key, encrypted_string)
            "[[702, 902, 816], [463, 730, 530], [270, 863, 416], [494, 985, 652], [432, 578, 512]]"

            # TRANSPORTAR EL RESULTADO
            encrypted_string = self.transpose_array(encrypted_string)
            "[[702, 463, 270, 494, 432], [902, 730, 863, 985, 578], [816, 530, 416, 652, 512]]"

            # APLICAR MOD 27 AL RESULTADO DE ESTA TRANSPOSICIÓN
            encrypted_string = self.mod_27(encrypted_string)
            "[[0, 4, 0, 8, 0], [11, 1, 26, 13, 11], [6, 17, 11, 4, 26]]"
            
            # PASAR LOS VALORES DE LA MATRIZ A SU EQUIVALENTE POSICIONAL EN EL ABECEDARIO
            encrypted_string = self.value_array_to_string(encrypted_string)
            ""
            
            # RETORNAR TEXTO DESENCRIPTADO
            return encrypted_string

        except Exception as method_error:
            error_line = method_error.__traceback__.tb_lineno
            print(f'Error in line {str(error_line)}')
        
        # LOGIC METHODS

    def mod_27(self, array:list):
        """Este método se usa para aplicar un mod27 a cada valor dentro de un array

        Args:
            array (list): Matriz con números base 10 sin modificaciones

        Returns:
            array (list): Matriz con cada valor modificado con su residuo del mod27
        """
        try:
            # Itera sobre cada fila de la matriz
            for row_index, row in enumerate(array):
                # Itera sobre cada elemento de la fila
                for col_index, value in enumerate(row):
                    # Aplica la operación módulo 27 a cada valor
                    # y lo reemplaza en la matriz original
                    array[row_index][col_index] = value % 27
            
            # Devuelve la matriz modificada
            return array
    
        except Exception as method_error:
            # Maneja cualquier error que pueda ocurrir durante la ejecución del método
            error_line = method_error.__traceback__.tb_lineno
            print(f'Error in line {str(error_line)}')

    def transpose_array(self, array):
        """Este método se usa para aplicar una transposición a una matriz.
        Args:
            array (list): Matriz deseada que se va a transponer.
        Returns:
            array (list): Matriz después de ser transpuesta.
        """
        try:
            # Inicializa una lista vacía para almacenar la matriz transpuesta
            transposed_array = []
            
            # Cicla sobre las columnas de la matriz original
            for i in range(len(array[0])):
                # Inicializa una lista vacía para almacenar la fila transpuesta
                transported_row = []
                # Cicla sobre las filas de la matriz original
                for row in array:
                    # Agrega el elemento correspondiente de la fila original a la fila transpuesta
                    transported_row.append(row[i])
                # Agrega la fila transpuesta a la matriz transpuesta
                transposed_array.append(transported_row)
            
            return transposed_array
        
        except Exception as method_error:
            # Maneja cualquier error que pueda ocurrir durante la ejecución del método
            error_line = method_error.__traceback__.tb_lineno
            print(f'Error in line {str(error_line)}')

    def multiply_arrays(self, array1:list, array2:list):
        """Este método se utiliza para realizar la multiplicación de dos matrices.
        Args:
            array1 (list): Matriz 1 a multiplicar.
            array2 (list): Matriz 2 a multiplicar.
        Returns:
            product_array (list): Matriz resultante de la multiplicación.
        
        """
        try:
            product_array = []  # Lista para almacenar la matriz resultante
            for column in enumerate(array2[0]):  # Ciclar sobre las columnas de la segunda matriz
                column_list = []  # Lista para almacenar los elementos de cada columna resultante
                for row_value in array1:  # Ciclar sobre las filas de la primera matriz
                    result = 0  # Inicializar el valor del elemento resultante de la multiplicación
                    row_counter = 0  # Contador para acceder a los elementos de cada fila
                    for column_val in array2:  # Ciclar sobre las columnas de la segunda matriz
                        result += row_value[row_counter] * column_val[column[0]] 
                        # Multiplicar los elementos correspondientes y sumar al resultado
                        row_counter += 1  # Incrementar el contador de fila
                    column_list.append(result)  # Agregar el resultado a la lista de elementos de la columna
                product_array.append(column_list)  # Agregar la lista de elementos de la columna a la matriz resultante
            return product_array  # Devolver la matriz resultante
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

    def matriz_identidad(self, n):
        """
        Función para crear una matriz identidad de tamaño n x n.
        """
        identidad = []  # Lista para almacenar la matriz identidad
        for i in range(n):
            fila = [0] * n  # Inicializa una fila de ceros de tamaño n
            fila[i] = 1     # Establece el elemento en la posición diagonal a 1
            identidad.append(fila)  # Agrega la fila a la matriz identidad
        return identidad

    def gauss_jordan(self, matriz):
        """
        Función para calcular la inversa de una matriz utilizando el método de Gauss-Jordan.
        """
        n = len(matriz)  # Obtiene el tamaño de la matriz
        identidad = self.matriz_identidad(n)  # Genera la matriz identidad del mismo tamaño
        
        # Concatenar la matriz original con la matriz identidad
        for i in range(n):
            matriz[i] += identidad[i]  # Agrega cada fila de la matriz identidad a la fila correspondiente de la matriz original
        
        # Escalonamiento
        for i in range(n):
            # Hacer que el pivote sea 1
            pivot = matriz[i][i]  # El pivote es el elemento diagonal en la fila actual
            for j in range(i, n*2):
                matriz[i][j] /= pivot  # Divide toda la fila actual por el pivote para hacerlo 1
            # Hacer ceros en las otras filas
            for k in range(n):
                if k != i:  # Evita operar en la fila actual
                    factor = matriz[k][i]  # El factor es el elemento en la misma columna que el pivote pero en una fila diferente
                    for j in range(i, n*2):
                        matriz[k][j] -= factor * matriz[i][j]  # Resta el producto del factor y el elemento correspondiente en la fila actual de la fila k
        
        # Extraer la matriz inversa
        inversa = []
        for i in range(n):
            fila_inversa = [int(elem) for elem in matriz[i][n:]]  # Extrae la parte de la fila que corresponde a la matriz inversa
            inversa.append(fila_inversa)
        
        return inversa


    def value_array_to_string(self, array:list):
            """Este método se usa para convertir una matriz de valores
                numéricos en una cadena de caracteres.
            Args:
                array (list): Matriz con valores numéricos que
                representan posiciones en el alfabeto.
            Returns:
                str: Cadena de caracteres que representa las
                letras correspondientes a los valores numéricos en la matriz.
            """
            try:
                # Inicializa una lista para almacenar los valores ordenados de la matriz
                ordered_list = []

                # Cicla sobre las columnas de la matriz
                for col in range(len(array[0])):
                    # Cicla sobre las filas de la matriz
                    for row in range(len(array)):
                        # Agrega cada valor de la matriz a la lista ordenada
                        ordered_list.append(array[row][col])

                # Inicializa una cadena final para almacenar
                # las letras correspondientes a los valores
                final_string = ''        

                # Cicla sobre cada valor en la lista ordenada
                for value in ordered_list:
                    # Busca el índice del valor en el alfabeto
                    # y agrega la letra correspondiente a la cadena final
                    for index, letter in enumerate(self.alphabet):
                        if value == index:
                            final_string += letter

                # Devuelve la cadena final con las letras
                # correspondientes a los valores numéricos
                return final_string

            except Exception as method_error:
                # Maneja cualquier error que pueda ocurrir durante la ejecución del método
                error_line = method_error.__traceback__.tb_lineno
                print(f'Error in line {str(error_line)}')

if __name__ == "__main__":
    Logic_Class()