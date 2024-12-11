import requests
import argparse

print("Test workflow python script going in")



# Create the parser
parser = argparse.ArgumentParser(description="Process the input parameters.")

# Define the arguments that you expect to pass from the command
parser.add_argument('--requested-by', type=str, required=True, help="The user who requested the schema swap")
parser.add_argument('--source-object', type=str, required=True, help="The source object")
parser.add_argument('--target-object', type=str, required=True, help="The target object")

# Parse the arguments
args = parser.parse_args()

# Collect the parameters
requested_by = args.requested_by
source_object = args.source_object
target_object = args.target_object

# Print the collected parameters (optional, for debugging)
print(f"Requested by: {requested_by}")
print(f"Source object: {source_object}")
print(f"Target object: {target_object}")
