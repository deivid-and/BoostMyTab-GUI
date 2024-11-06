import os
import sys
import subprocess
import threading

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.abspath("."))
    return os.path.join(base_path, relative_path)

SCRIPT_PATHS = {
    "Manage_Unnecessary_Processes": resource_path('scripts/Manage_Unnecessary_Processes'),
    "Performance_Optimization": resource_path('scripts/Performance_Optimization'),
    "System_Management": resource_path('scripts/System_Management')
}

def run_script(script_name, category, async_run=False):
    script_dir = SCRIPT_PATHS.get(category)
    if not script_dir:
        error_msg = f"Invalid script category: {category}"
        return {"status": "error", "message": error_msg}

    script_path = os.path.join(script_dir, script_name)

    if not os.path.exists(script_path):
        error_msg = f"Script not found: {script_path}"
        return {"status": "error", "message": error_msg}

    def execute():
        try:
            env = os.environ.copy()
            env['PATH'] = os.pathsep.join([
                resource_path('scripts/adb'),
                env.get('PATH', '')
            ])

            result = subprocess.run(
                script_path,
                capture_output=True,
                text=True,
                shell=True,
                check=True,
                cwd=script_dir,
                timeout=120,
                env=env
            )
            if result.returncode == 0:
                success_message = f"Script executed successfully. Output: {result.stdout}"
                output = {"status": "success", "message": success_message, "output": result.stdout}
            else:
                error_message = f"Script executed with errors. Error: {result.stderr}"
                output = {"status": "error", "message": error_message, "output": result.stderr}
        except subprocess.TimeoutExpired:
            error_msg = "Script execution timed out."
            output = {"status": "error", "message": error_msg}
        except subprocess.CalledProcessError as e:
            error_msg = f"Failed to execute script. Error: {e.stderr}"
            output = {"status": "error", "message": error_msg}
        except Exception as e:
            error_msg = f"Unexpected error: {str(e)}"
            output = {"status": "error", "message": error_msg}
        return output

    if async_run:
        thread = threading.Thread(target=execute)
        thread.start()
        return {"status": "success", "message": f"Script {script_name} started successfully in the background."}
    else:
        return execute()
