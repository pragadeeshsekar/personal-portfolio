# Pragadeesh Sekar Portfolio

This project is a Flask-based portfolio site built from resume content and prepared for simple production deployment with Gunicorn.

## Project structure

- `app.py` contains the Flask application entrypoint.
- `templates/index.html` contains the portfolio page template.
- `static/styles.css` contains the portfolio styling.
- `requirements.txt` lists the app dependencies.
- `Procfile` defines the production startup command for platforms that support it.
- `run.sh` starts the app with Gunicorn for production use.
- `nginx/portfolio.conf.sample` is a sample Nginx reverse proxy config for HTTPS on the same EC2 instance.

## Run locally

1. Create and activate a virtual environment.
2. Install dependencies.
3. Start the Flask development server.

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

Open `http://127.0.0.1:5000` in your browser.

## Run in production

Install dependencies and start the app with Gunicorn:

```bash
pip install -r requirements.txt
gunicorn --bind 0.0.0.0:5000 app:app
```

Or use the included startup script:

```bash
./run.sh
```

The Flask app also reads the `PORT` environment variable, which makes it compatible with common deployment platforms.

## Deployment notes

- `Procfile` uses `gunicorn app:app` for production startup.
- `app.py` binds to `0.0.0.0` and uses `PORT` when provided by the hosting platform.
- Keep `FLASK_DEBUG=false` in production.

## Nginx reverse proxy on EC2

This project includes a sample Nginx config at `nginx/portfolio.conf.sample` for serving HTTPS on the same EC2 instance and forwarding requests to Gunicorn on port `5000`.

Before using it:

- Replace `example.com` and `www.example.com` with your real domain.
- Replace the certificate paths with your actual TLS certificate files.
- Keep Gunicorn running locally on `127.0.0.1:5000`.

Typical setup steps on Ubuntu EC2:

```bash
sudo cp nginx/portfolio.conf.sample /etc/nginx/sites-available/portfolio.conf
sudo ln -s /etc/nginx/sites-available/portfolio.conf /etc/nginx/sites-enabled/portfolio.conf
sudo nginx -t
sudo systemctl reload nginx
```

If you use Certbot, update the SSL certificate paths after the certificate is issued.

## Certbot steps for maintainers

These steps assume:

- the app is running on the EC2 instance with Gunicorn on port `5000`
- your domain DNS already points to the EC2 public IP
- Nginx is installed and reachable on ports `80` and `443`

### 1. Install Certbot

For Ubuntu-based EC2 instances:

```bash
sudo apt update
sudo apt install -y certbot python3-certbot-nginx
```

### 2. Copy and enable the Nginx site config

```bash
sudo cp nginx/portfolio.conf.sample /etc/nginx/sites-available/portfolio.conf
sudo ln -s /etc/nginx/sites-available/portfolio.conf /etc/nginx/sites-enabled/portfolio.conf
sudo nginx -t
sudo systemctl reload nginx
```

Before this step, make sure you replaced `example.com` and `www.example.com` in the sample config with your actual domain names.

### 3. Request the certificate with Certbot

```bash
sudo certbot --nginx -d example.com -d www.example.com
```

Certbot will:

- validate domain ownership
- issue the TLS certificate
- usually update the Nginx config automatically for HTTPS

### 4. Verify renewal is configured

Check the renewal timer or run a dry run:

```bash
sudo certbot renew --dry-run
```

### 5. Reload Nginx after validation

```bash
sudo nginx -t
sudo systemctl reload nginx
```

### Maintainer notes

- Ensure the EC2 security group allows inbound `80` and `443`.
- Ensure the domain A record points to the correct EC2 public IP before running Certbot.
- If you keep the sample certificate paths, update `example.com` in those paths to match the real domain.
- If Certbot rewrites the Nginx file, keep the reverse proxy `location /` block pointing to `http://127.0.0.1:5000`.
- Re-run `sudo certbot --nginx -d yourdomain -d www.yourdomain` if the domain configuration changes later.

## Optional next improvements

- Add a downloadable PDF resume link.
- Add a simple contact form or analytics integration if needed.
