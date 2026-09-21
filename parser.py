import os

def load_and_chunk_codebase(repo_path, chunk_size=300, ignored_dirs=None, valid_extensions=None):
    """Local repo se code files scan karke unhe vector DB ke liye chunks mein divide karta hai."""
    if ignored_dirs is None:
        ignored_dirs = {'.git', 'venv', 'node_modules', '__pycache__', '.vscode', 'codevault_db'}
        
    if valid_extensions is None:
        valid_extensions = {'.py', '.js', '.ts', '.java', '.cpp', '.c', '.html', '.css'}
        
    documents = []
    
    for root, dirs, files in os.walk(repo_path):
        dirs[:] = [d for d in dirs if d not in ignored_dirs]
        
        for file in files:
            ext = os.path.splitext(file)[1].lower()
            if ext in valid_extensions:
                file_path = os.path.join(root, file)
                rel_path = os.path.relpath(file_path, repo_path)
                
                try:
                    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                        content = f.read()
                    
                    lines = content.split('\n')
                    current_chunk = []
                    current_size = 0
                    
                    for line_idx, line in enumerate(lines, 1):
                        current_chunk.append(line)
                        current_size += len(line)
                        
                        if current_size >= chunk_size:
                            chunk_text = "\n".join(current_chunk)
                            documents.append({
                                "file": rel_path,
                                "content": chunk_text,
                                "start_line": line_idx - len(current_chunk) + 1,
                                "end_line": line_idx
                            })
                            current_chunk = []
                            current_size = 0
                            
                    if current_chunk:
                        chunk_text = "\n".join(current_chunk)
                        documents.append({
                            "file": rel_path,
                            "content": chunk_text,
                            "start_line": line_idx - len(current_chunk) + 1,
                            "end_line": line_idx
                        })
                        
                except Exception as e:
                    print(f"⚠️ File reading error: {file_path} - {e}")
                    
    return documents

if __name__ == "__main__":
    print("🔍 CodeVault-AI Parser Test...")
    chunks = load_and_chunk_codebase(".")
    print(f"✅ Created {len(chunks)} code chunks successfully!")