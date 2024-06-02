# Import random and string modules
import random
import string

# Define a function to generate a random string of a given length
def random_string(length):
  return "".join(random.choice(string.ascii_letters) for i in range(length))

# Define a list of possible titles
titles = ["Manager", "Engineer", "Analyst", "Consultant", "Director", "Officer", "Specialist", "Coordinator", "Assistant", "Intern"]

# Define a list of possible organizational units
ous = ["Sales", "Marketing", "Finance", "HR", "IT", "Operations", "R&D", "Legal", "Customer Service", "Administration"]

# Define the domain name of the organization
domain = "example.com"

# Open a file to write the LDIF data
with open("sample.ldif", "w") as f:
  # Loop 50 times to generate 50 entries
  for i in range(50):
    # Generate a random first name and last name
    first_name = random_string(random.randint(3, 10))
    last_name = random_string(random.randint(3, 10))
    # Generate a common name by concatenating the first name and last name
    cn = first_name + " " + last_name
    # Generate a mail address by using the first name, last name, and domain name
    mail = first_name + "." + last_name + "@" + domain
    # Generate a random title by choosing from the list of titles
    title = random.choice(titles)
    # Generate a random organizational unit by choosing from the list of ous
    ou = random.choice(ous)
    # Generate a distinguished name by using the cn and the domain name
    dn = "cn=" + cn + ",dc=" + domain.replace(".", ",dc=")
    # Write the LDIF data to the file
    f.write(f"dn: {dn}\n")
    f.write("objectClass: person\n")
    f.write("objectClass: organizationalPerson\n")
    f.write("objectClass: inetOrgPerson\n")
    f.write(f"cn: {cn}\n")
    f.write(f"sn: {last_name}\n")
    f.write(f"mail: {mail}\n")
    f.write(f"title: {title}\n")
    f.write(f"ou: {ou}\n")
    f.write("\n")
# Close the file
f.close()
