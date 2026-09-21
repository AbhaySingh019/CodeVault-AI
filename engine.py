import onnxruntime as ort
import numpy as np
from database import search_code

class LocalCodeVaultEngine:
    def __init__(self):
        print("⚡ Initializing Local AI Execution Engine...")
        # Check for available hardware execution providers (NPU/CPU)
        providers = ort.get_available_providers()
        print(f"⚙️ Available Providers: {providers}")
        
    def analyze_security_vulnerabilities(self, code_snippet):
        """Simple offline rules + context engine for instant security audits."""
        vulnerabilities = []
        
        # Security checks
        if "eval(" in code_snippet or "exec(" in code_snippet:
            vulnerabilities.append("⚠️ CRITICAL: Dynamic Code Execution (eval/exec) detected. Risk of Code Injection.")
        if "hardcoded" in code_snippet.lower() or "password =" in code_snippet.lower() or "api_key =" in code_snippet.lower():
            vulnerabilities.append("⚠️ HIGH: Potential hardcoded secret or API key detected.")
        if "subprocess" in code_snippet and "shell=True" in code_snippet:
            vulnerabilities.append("⚠️ HIGH: Command Injection risk with shell=True in subprocess.")
            
        return vulnerabilities

    def query_codebase(self, user_query):
        """Retrieves code context from LanceDB and produces local analysis."""
        # Step 1: Local Vector Retrieval
        results = search_code(user_query, top_k=2)
        
        if not results:
            return "No matching code context found in local codebase."
            
        context_str = ""
        audits = []
        
        for idx, res in enumerate(results, 1):
            context_str += f"\n--- Match {idx} [{res['file']} (Lines {res['start_line']}-{res['end_line']})] ---\n"
            context_str += res['text'] + "\n"
            
            # Audit retrieved chunk
            found_vulns = self.analyze_security_vulnerabilities(res['text'])
            if found_vulns:
                audits.extend(found_vulns)
                
        response = f"🔍 **Retrieved Local Code Context:**\n{context_str}\n"
        
        if audits:
            response += "\n🚨 **Local Security Audit Findings:**\n" + "\n".join(audits)
        else:
            response += "\n✅ **Security Audit:** No immediate high-risk patterns detected in matched chunks."
            
        return response

if __name__ == "__main__":
    engine = LocalCodeVaultEngine()
    print("\n--- Testing Local Engine Query ---")
    query = "code chunking logic"
    out = engine.query_codebase(query)
    print(out)