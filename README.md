# Generate Import list

## Usage
Run commands go generate a list.
```
# Command Line Option

cd DIRECTORY/OF/TERRAFORM/WORKSPACE

echo "import: " > import.yaml
terraform plan -no-color |grep "# "| awk '{print("  - tag: "$2"\n   value:")}' >> import.yaml
```

Edit the `import.yaml` to change your import groups.

run 
```
LOCATION_OF_IMPORT_UTIL/import.py MYIMPORTGROUP
```

## What should happen.
The file `import.yaml` should have a copy of the resources that are set to be changed.
Update `import.yaml` with the correct value's for the import and break up your imports into groups.
This is not required but it does make it helpful to use the same import file if you have to add
additional keys or you need to control the rate you handle imports.

After `import.yaml` is read you will run `import.py` which will parse the file and run the import 
command 

