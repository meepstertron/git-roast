import os
import sys



# use git blame to get the recent commits
def get_git_blame(file_path):
    try:
        import subprocess
        result = subprocess.run(['git', 'blame', '-L', '1,1', file_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if result.returncode == 0:
            return result.stdout.decode('utf-8').strip()
        else:
            return "No git blame information available."
    except Exception as e:
        return str(e)
    except ImportError:
        return "git is not installed or not available in the PATH."
    

    if __name__ == "__main__":
        # Get the current file path
        current_file_path = os.path.abspath(__file__)
        
        # Get the git blame information
        blame_info = get_git_blame(current_file_path)
        
        # Print the git blame information
        print("Git Blame Information:")
        print(blame_info)