import os


class Files:
    def __init__(self, downloads_folder=r"C:\Users\VMRanjan\Downloads", base_file_name="Selenium_", extension=".pdf"):
        self.downloads_folder = downloads_folder
        self.base_file_name = base_file_name
        self.extension = extension

    def get_last_version(self):
        """
        Get the latest available version number by scanning the files in the downloads folder.
        """
        existing_versions = []
        # List all files in the downloads folder and look for ones matching the base file name and extension
        for filename in os.listdir(self.downloads_folder):
            if filename.startswith(self.base_file_name) and filename.endswith(self.extension):
                try:
                    # Extract the version number from the file name (e.g., Selenium_657.pdf)
                    version = int(filename[len(self.base_file_name):-len(self.extension)])
                    existing_versions.append(version)
                except ValueError:
                    continue
        # If no versions are found, return 0 (meaning no files downloaded yet)
        return max(existing_versions, default=0)

    def get_next_version(self):
        """
        Get the next available version by adding 1 to the last known version.

        """
        last_version = self.get_last_version()
        return last_version + 1

    def rename_downloaded_file(self):
        """
        Renames the most recently downloaded file to the next version.
        """
        # Get the next version number
        next_version = self.get_next_version()

        # Path of the most recent file
        old_file_path = os.path.join(self.downloads_folder, f"{self.base_file_name}{next_version - 1}{self.extension}")

        # Path for the new file (renamed)
        new_file_path = os.path.join(self.downloads_folder, f"{self.base_file_name}{next_version}{self.extension}")

        print(f"Next available version: {next_version}")
        print(f"Attempting to rename: {old_file_path} -> {new_file_path}")

        # Check if the old file exists and rename it
        if os.path.exists(old_file_path):
            os.rename(old_file_path, new_file_path)
            print(f"File renamed to {new_file_path}")
        else:
            print(f"File {old_file_path} not found!")
        return new_file_path
