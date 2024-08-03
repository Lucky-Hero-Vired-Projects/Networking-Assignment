# Deploying the website on Localhost or EC2 Nginix 
To deploy website I'm using Nginx as a webserver

## Deploying Nginx in Ubuntu Machine
### Steps:
1. sudo apt update --> update all the packages in vm
2. sudo apt install nginx -y --> Installing Nginx package 
3. Creating Simple HTML website
    
    a. After Nginx Installation goto
      ```
      cd /var/www/html
      ```
    b. Create a HTML file  
       
       ```
       sudo touch index.html
       ```
    
    c. Add This content in index.html
    ```
     <!DOCTYPE html>
     <html>
     <head>
        <title>Awesome Web</title>
     </head>
     <body>
        <h1>Welcome to Awesome Web</h1>
     </body>
     </html>
    ```
4. Creating a new configuration file for your website
    ```
    sudo nano /etc/nginx/sites-available/awesomeweb

    Add the following configuration in awesomeweb file

    server {
        listen 80;
        listen [::]:80;
        server_name awesomeweb.com

        root /var/www/html;

        # Load configuration files for the default server block.
        include /etc/nginx/default.d/*.conf;

        error_page 404 /404.html;
        location = /404.html {
        }

        error_page 500 502 503 504 /50x.html;
        location = /50x.html {
        }

       location / {

           proxy_pass http://54.185.212.132:80;
           proxy_set_header Host $host;
           proxy_set_header X-Real-IP $remote_addr;
           proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
           proxy_set_header X-Forwarded-Proto $scheme;

          }
      }
    ```

5. Enable the new website for awsomeweb
   ```
    sudo ln -s /etc/nginx/sites-available/awesomeweb /etc/nginx/sites-enabled/
   ```
6. Test the Nginx configuration for syntax errors 
   ```
     sudo nginx -t
    ```
7. Reload Nginx to apply the changes
   ```
   sudo systemctl reload nginx
   ```
8. Configuring Local DNS to access via browser with http://awesomeweb.com
   ```
   Edit the hosts file to map the DNS name to localhost

   sudo nano /etc/hosts
    
   Add this line

   127.0.0.1   awesomeweb.com
   ```
9. Testing the website with http://awesomeweb.com 

