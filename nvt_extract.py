import subprocess
import xml.etree.ElementTree as ET
import csv
import os

get_families = "gvm-cli --gmp-user '[REDACTED]' --gmp-password '[REDACTED]' socket -X '<get_nvt_families/>' > /tmp/nvtfamily.xml"
subprocess.run(get_families, shell=True)

# parse the XML document
tree = ET.parse('/tmp/nvtfamily.xml')
root = tree.getroot()

# find all the family elements and print their names
nvt_families = []
for family in root.findall('.//family'):
    name = family.find('name').text
    nvt_families.append(name)

for nvt_family in nvt_families:
    command = f"gvm-cli --gmp-user '[REDACTED]' --gmp-password '[REDACTED]' --timeout 300 socket -X '<get_nvts family=\"{nvt_family}\" details=\"1\"/>' > /tmp/nvt_{nvt_family.replace(' ', '_')}.xml"
    subprocess.run(command, shell=True)
    print(f"Created nvt_{nvt_family.replace(' ', '_')}.xml")
	
print('All nvt families xml files created.')	
xml_dir = '/tmp'

# Path to the output CSV file
csv_file = 'nvts.csv'

# Create a list to hold the data
data = []

# Loop through the XML files in the directory
for filename in os.listdir(xml_dir):
    if filename.endswith('.xml'):
        # Parse the XML file
        tree = ET.parse(os.path.join(xml_dir, filename))
        root = tree.getroot()

        # Extract the name and cvss_base values
        for nvt in root.iter('nvt'):
            name = nvt.find('name').text
            cvss_base = nvt.find('cvss_base').text

            # Add the data to the list
            data.append([name, cvss_base])

# Write the data to the CSV file
with open(csv_file, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Name', 'CVSS Base'])
    writer.writerows(data)

print('nvts.csv created.')
