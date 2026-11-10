import os

def execute_user_command():
    print("--- Command Executor ---")
    # User se input le raha hai
    user_command = input("Enter a command to run: ")
    
    # VULNERABILITY: Command Injection (CWE-78)
    # User ka input direct os.system mein ja raha hai
    os.system(user_command)

if __name__ == "__main__":
    execute_user_command()