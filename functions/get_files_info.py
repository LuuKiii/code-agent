import os

def get_files_info(working_dir, directory="."):
    abs_working_dir = os.path.abspath(working_dir)
    abs_access_dir = os.path.abspath(os.path.join(working_dir, directory))
    
    if not os.path.commonprefix([abs_working_dir, abs_access_dir]) == abs_working_dir:
        return f'Error: Cannot list "{abs_access_dir}" as it is outside the permitted working directory'
    
    if not os.path.isdir(abs_access_dir):
        return f'Error: "{abs_access_dir}" is not a directory'
    

    try:
        items_data_list = []
        for item_name in os.listdir(abs_access_dir):
            item_path = os.path.join(abs_access_dir, item_name)
            items_data_list.append(f"- {item_name}: file_size={os.path.getsize(item_path)} bytes, is_dir={not os.path.isfile(item_path)}")

        return "\n".join(items_data_list)

    except Exception as error:
        return f"Error: {str(error)}"