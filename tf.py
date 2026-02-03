import os

def list_files(startpath):
    # Folders to ignore to keep the output clean
    exclude = {'.git', '__pycache__', '.pytest_cache', 'env', 'venv', '.dockerignore'}
    
    print(f"Project Structure for: {os.path.basename(os.getcwd())}")
    print("=" * 40)
    
    for root, dirs, files in os.walk(startpath):
        # Filter out excluded directories
        dirs[:] = [d for d in dirs if d not in exclude]
        
        level = root.replace(startpath, '').count(os.sep)
        indent = ' ' * 4 * (level)
        print(f"{indent}{os.path.basename(root)}/")
        
        sub_indent = ' ' * 4 * (level + 1)
        for f in files:
            if f not in exclude:
                print(f"{sub_indent}{f}")

if __name__ == "__main__":
    list_files(os.getcwd())