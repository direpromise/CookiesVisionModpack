import json
import os

def update_manifest():
    dependencies_file = 'dependencies.txt'
    manifest_file = 'manifest.json'

    try:
        with open(dependencies_file, 'r') as deps_file:
            dependencies = deps_file.read().splitlines()

        with open(manifest_file, 'r') as manifest:
            manifest_data = json.load(manifest)
            manifest_data["dependencies"] = dependencies

        with open(manifest_file, 'w') as updated_manifest:
            json.dump(manifest_data, updated_manifest, indent=2)
        
        print(f"Manifest '{manifest_file}' updated with dependencies from '{dependencies_file}'.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    update_manifest()
