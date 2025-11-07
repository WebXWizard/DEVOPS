# User Management
sudo adduser username                   # Add new user
sudo usermod -aG groupname username     # Add user to group
sudo deluser username                   # Remove user
groups username                         # List user's groups
id username                             # User ID and group information
sudo passwd username                    # Set user password
sudo usermod -s /bin/bash username      # Change user's shell

# Permission Management
chmod 755 file.txt                      # Set permissions (rwxr-xr-x)
chmod +x script.sh                      # Add execute permission
chmod -w file.txt                       # Remove write permission
chmod u+w,g-r,o=r file.txt              # Specific permission changes
chown user:group file.txt               # Change ownership
sudo chown -R user:group directory/     # Recursive ownership change
chgrp groupname file.txt                # Change group only

# Permission codes:
# 4 = read, 2 = write, 1 = execute
# 7 = 4+2+1 (rwx), 6 = 4+2 (rw-), 5 = 4+1 (r-x)
# First digit = owner, second = group, third = others
