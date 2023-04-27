# Obsidian metaadata snippet

How to use it:
1. Install obsidian meta bind plugin. (It allows you edit file metadata from reading mode using UI inputs)
2. Install execute code plugin. (It allows you execute code within note, and provides magic commands @vault_path and @note_path)
3. Download and install this snippet using `python -m pip install E:\home\prj\obsidian_metadata_snippet`
4. In code you can use it `import m5;ob_dict = m5.r(@vault_path, @note_path)`
5. Now you can parametrize code in obsidian notes using ob_dict values.