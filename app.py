import os

# Function for create file 
def create_file(filename):
    try:
        with open(filename,'x') as f:
            print("File Name {filename}: Created Successfully!!")
    except FileExistsError:
        print(f"File Name {filename} already exists!")
    except Exception as E:
        print("An error occurred!")

# Function for view all file in Directory
def view_all_files():
    files = os.listdir()
    if not files:
        print("NO Filse in Directory! ")
    else:
        print("Files in Directory!!")
        for file in files:
            print(file)

# Function for delete file
def delete_file(filename):
    try:
        os.remove(filename)
        print(f"{filename} has been deleted successfully!")
    except FileNotFoundError:
        print(f"File name {filename} not found")
    except Exception as e:
        print("An error occurred")

#Function for read file
def read_file(filename):
    try:
        with open('sample.txt',"r") as f:
            content = f.read()
            print(f"Content of file'{filename}':\n{content}")
    except FileNotFoundError:
        print(f"{filename} doesn`t exist!")
    except Exception as e:
        print("An error occureed!")

#Function to edit a file
def edit_file(filename):
    try:
        with open('sample.txt','a') as f:
            content = input("Enter content to append in the file:  ")
            f.write(content + "\n") 
            print(f"File '{filename}'updated succesfully. ")      
    except FileNotFoundError:
        print(f"{filename} dosesn`t exist")
    except Exception as e:
        print("An Error occurred!")    

# Main function to handele user choices
def main():
    while True:
        print(" FILE MANAGEMENT APP")
        print("1: Create File")
        print("2: View All File")
        print("3: Delete File")
        print("4: Read File")
        print("5: Edit File")
        print("6: Exit File")
        
        choice = int(input("Enter your choice(1-6) = "))

        if choice == 1:
            filename = input("Enter the file-name to create =")
            create_file(filename)
        
        elif choice == 2:
            view_all_files()
            
        elif choice == 3:
            filename = input("Enter the file name you want to delete =")
            delete_file(filename)

        elif choice == 4:
            filename = input("Enter the name of file want to read =")
            read_file(filename)

        elif choice == 5:
            filename = input("Enter the name of file you want to edit = ")
            edit_file(filename)

        elif choice == 6:
            print("Cloosing the app....")
            break

        else:
            print("In-valid syntax")

if __name__ == "__main__":
    main()




