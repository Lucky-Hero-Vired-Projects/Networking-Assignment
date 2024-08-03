# Deploying a Website on Nginx Inside a Virtual Machine

## Step 1: Downloading a Ubuntu Image
Visit https://www.osboxes.org/ 

or directly copy paste this link in browser and enter, it will start downloading
https://sourceforge.net/projects/osboxes/files/v/vb/55-U-u/22.04/64bit.7z/download

Download a Ubuntu 22.04 image
## Step 2: Set Up the Virtual Machine
```
1. Open VirtualBox.

2. Click on "New" to create a new VM.

3. Name = Ubuntu-22.04, select "Linux" as the type and "Ubuntu (64-bit)" as the version.

4. Allocate memory (RAM) for the VM 2048 MB.

5. Choose "Create a virtual hard disk now" and follow the prompts to create a virtual hard disk.

6. Choose HardDisk type as "VDI(Virtual Disk Image)"

7. Choose Storage on Physical Hard Disk "Dynamically Allocated"

8. Choose file location and size (~10GB space)

9. Click on Create, VM starts creating.
```

### Installing Ubuntu on Created Ubuntu-22.04 vm
```
1. Click on VM(Ubuntu-22.04)

2. On Main screen click on settings

   a.  Under Storage, in the Storage Device section, click on "Empty." In the next box that appears, find the Optical Drive section, click on the circular icon to the right of it, and select "Choose Disk File."

   b. Under Network, Enable Adapter 2 and choose Host-only Adapter

3. Click on "file" of Virtual Box mail top line dashboard and choose Host Network Manager

   a. select DHCP Server

   b. Copy server address

   c. Click Adapter

   d. Replace IP address with server address(copied one)

   e. Apply changes and close it.

4. Select the downloaded Ubuntu image as the startup disk and start the VM.

5. Install Ubuntu

6. Follow the on-screen instructions to install Ubuntu 22.04.

7. Once the installation is complete, restart the VM and log in to your new Ubuntu system.
```

## Step 3: Install Nginx

1. Open a terminal in the Ubuntu VM.

2. Update the package list:
```
    sudo apt update
```
3. Install Nginx:
```
   sudo apt install nginx
```

4. Start the Nginx service:
```
   sudo systemctl start nginx
```

5. Enable Nginx to start on boot:
```
   sudo systemctl enable nginx
```

## Step 4: Host a Website

1. Create a simple HTML file to host on Nginx:
```
   sudo touch /var/www/html/index.html
```
2. Add the following content into index.html file:
```
     <!DOCTYPE html>
     <html>
     <head>
         <title>Welcome to Nginx on Ubuntu!</title>
     </head>
     <body>
       <h1>Hello, world!</h1>
       <p>This is a test page served by Nginx on Ubuntu.</p>
     </body>
     </html>
```
## Step 5: Access the Website

Open a web browser on your host machine.
Enter the IP address of the Ubuntu VM to access the website. To get Ipaddress login inti vm, and enter "ifconfig"

## Scanning the Virtual Machine Using Nmap

1. Install Nmap on your host machine (Windows). 

   Download and install Nmap from the official website.

   https://nmap.org/dist/nmap-7.95-setup.exe

2. Scan the VM
 
Open a cmd on host machine.

Run the following command to scan the VM:

nmap -sV <VM_IP_ADDRESS>

ex: nmap -sV 192.168.81.14

3. Analyze the Output

The output of the Nmap scan will display the open ports and the services running on those ports.

Example Output
```
Starting Nmap 7.95 ( https://nmap.org ) at 2024-08-03 12:34 EDT
Nmap scan report for <VM_IP_ADDRESS>
Host is up (0.00076s latency).
Not shown: 997 closed ports
PORT    STATE SERVICE     VERSION
22/tcp  open  ssh         OpenSSH 8.2p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
80/tcp  open  http        nginx 1.18.0 (Ubuntu)
443/tcp open  ssl/http    nginx 1.18.0 (Ubuntu)
```
In this example, ports 22 (SSH), 80 (HTTP), and 443 (HTTPS) are open, and the services running on these ports are displayed.