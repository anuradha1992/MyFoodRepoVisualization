## MyFoodRepo Food Hierarchy Visualization

Python Flask application for visualizing the MyFoodRepo food hierarchy.

Requirements:

- Flask==1.0.2,
- requests==2.18.4

An interactive and graphical visualization of the MyFoodRepo food hiearchy can be accessed at - http://visualizations.foodrepo.org

This is hosted at the Amazon EC2 server instance having the ip address - **52.28.115.103**

Path to the directory containing the code in the server - 
```
cd ../www/MyFoodRepoVisualization
```
###### Setting up configuration to access AWS EC2 instance

By being inside your user directory type the following on terminal:
```
~ anuradha$ cd .ssh
mv ../Documents/foodrepo-visualization.pem .
vim config
```
Add the following entry to config file:
```
host foodrepo
  Hostname 52.28.115.103
  IdentityFile ~/.ssh/foodrepo-visualization.pem
  User ubuntu
```
Then:
```
ssh foodrepo
```
But there comes the error:
```
Warning: Permanently added '52.28.115.103' (ECDSA) to the list of known hosts.
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@         WARNING: UNPROTECTED PRIVATE KEY FILE!          @
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
Permissions 0644 for '/Users/anuradha/.ssh/foodrepo-visualization.pem' are too open.
It is required that your private key files are NOT accessible by others.
This private key will be ignored.
Load key "/Users/anuradha/.ssh/foodrepo-visualization.pem": bad permissions
ubuntu@52.28.115.103: Permission denied (publickey).
```
Then you need to change the permission of the .pem file to readonly mode by typing in the following command:
```
chmod 400 foodrepo-visualization.pem
```
After than you need to remove 52.28.115.103 from the list of known hosts:
```
vim known_hosts
```
Remove the entry with 52.28.115.103. Then:
```
ssh foodrepo
```
You are now on the instance. To switch to sudo mode:
```
sudo su -
```
