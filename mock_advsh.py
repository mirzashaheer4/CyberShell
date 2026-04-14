import sys
import os
import platform

def main():
    print(">> CYBERSHELL MOCK ENGINE // STATUS: SIMULATED")
    print(">> NOTE: You are running on Windows. The C-based engine is disabled.")
    print(">> Type any command to see a mock response.")
    
    while True:
        try:
            cwd = os.getcwd()
            user = os.getlogin()
            prompt = f"{user}@windows:{cwd}$ "
            sys.stdout.write(prompt)
            sys.stdout.flush()
            
            line = sys.stdin.readline()
            if not line:
                break
                
            cmd = line.strip().lower()
            if not cmd:
                continue
                
            if cmd == "exit":
                print("Closing mock session...")
                break
                
            if cmd == "help":
                print("MOCK SHELL HELP:")
                print("  ls      - List files (Simulated)")
                print("  clear   - Clear screen (Simulated)")
                print("  exit    - Close shell")
                print("  [ANY]   - Standard commands are passed to the OS if possible.")
            
            # For other commands, just try to run them via subprocess if they are common utilities
            # Otherwise, just mock a response.
            if cmd in ["ls", "dir"]:
                for f in os.listdir("."):
                    print(f)
            else:
                print(f"Executing '{cmd}' in simulated environment...")
                # We could run actual OS commands here, but for a "mock" shell we just echo.
                
        except EOFError:
            break
        except Exception as e:
            print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
