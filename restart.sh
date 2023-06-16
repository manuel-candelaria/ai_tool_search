# Stop flask-resume-template SERVICE
# Stop nginx server
sudo systemctl stop aitoolsearch
sudo systemctl stop  nginx

# restar service
#restart nginx
sudo systemctl daemon-reload
sudo systemctl start aitoolsearch
sudo systemctl enable aitoolsearch
sudo systemctl start nginx
sudo systemctl enable nginx
sudo systemctl restart nginx