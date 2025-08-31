def file_read_write_challenge():
    """Reads a file and writes a modified version to a new file with error handling"""
    
    try:
        # Ask user for filename
        filename = input("Enter the filename to read: ")
        
        # Read the original file
        with open(filename, 'r') as file:
            content = file.read()
        
        print(f"Successfully read from '{filename}'")
        
        # Modify the content (example: convert to uppercase and add header)
        modified_content = f"=== MODIFIED VERSION ===\n\n{content.upper()}"
        
        # Create output filename
        output_filename = f"modified_{filename}"
        
        # Write modified content to new file
        with open(output_filename, 'w') as output_file:
            output_file.write(modified_content)
        
        print(f"Successfully wrote modified content to '{output_filename}'")
        print("Modification applied: Converted text to uppercase with header")
        
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found. Please check the filename and try again.")
    
    except PermissionError:
        print(f"Error: Permission denied. You don't have read access to '{filename}'.")
    
    except IsADirectoryError:
        print(f"Error: '{filename}' is a directory, not a file.")
    
    except UnicodeDecodeError:
        print(f"Error: Cannot read '{filename}' - it may be a binary file or use an unsupported encoding.")
    
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def error_handling_lab():
    """Demonstrates error handling for file operations"""
    
    while True:
        try:
            filename = input("\nEnter a filename to check (or 'quit' to exit): ")
            
            if filename.lower() == 'quit':
                print("Goodbye!")
                break
            
            # Try to open and read the file
            with open(filename, 'r') as file:
                content = file.read()
                print(f"File '{filename}' exists and can be read!")
                print(f"Preview: {content[:100]}..." if len(content) > 100 else f"Content: {content}")
                
        except FileNotFoundError:
            print(f"Error: File '{filename}' does not exist.")
        
        except PermissionError:
            print(f"Error: You don't have permission to read '{filename}'.")
        
        except IsADirectoryError:
            print(f"Error: '{filename}' is a directory.")
        
        except Exception as e:
            print(f"Unexpected error: {e}")

# Main program
if __name__ == "__main__":
    print("📝 File Read & Write Challenge")
    print("=" * 40)
    file_read_write_challenge()
    
    print("\n" + "🧪 Error Handling Lab")
    print("=" * 40)
    error_handling_lab()