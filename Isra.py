

def main():
    filename = "Isra.py"  

    
        with open(Isra.py, 'r') as file:
            content = file.read()

        
        modified_content = content.upper()

        
        new_filename = "Isra.py_modified.txt"

       
        with open(new_filename, 'w') as new_file:
            new_file.write(modified_content)

        


