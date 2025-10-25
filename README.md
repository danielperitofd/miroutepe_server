# 🚀 Deploy do Projeto Django `miroutepe_server` com Gunicorn, Nginx e Cloudflare Tunnel

Este guia documenta passo a passo como configurar e publicar o projeto Django `miroutepe_server` em um servidor Ubuntu com domínio personalizado via Cloudflare Tunnel.

---

## 📁 Estrutura do Projeto

/var/www/miroutepe_server/ 
├── core/ 
│ ├── static/ 
│ └── templates/ 
├── miroutesite/ 
│ └── settings.py 
├── manage.py 
├── staticfiles/ ← gerado por collectstatic 
└── .venv/

---

## 🧰 Pré-requisitos

- Python 3.10+
- Git
- Cloudflared
- Nginx
- systemd
- Domínio configurado na Cloudflare

---

## 🧱 Etapas de Configuração

### 1. Clonar o Projeto

```bash
cd /var/www/
git clone https://github.com/danielperitofd/miroutepe_server

2. Criar Ambiente Virtual e Instalar Dependências
cd miroutepe_server
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

3. Configurar settings.py
DEBUG = False
ALLOWED_HOSTS = ['miroutepe.com.br', 'www.miroutepe.com.br']

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'core' / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'

4. Coletar Arquivos Estáticos
python3 manage.py collectstatic

Isso copia os arquivos de core/static/ para staticfiles/.

🔧 Configuração de Serviços
5. Gunicorn
Crie o arquivo /etc/systemd/system/gunicorn-miroutesite.service:

[Unit]
Description=Gunicorn daemon for Django project miroutepe
After=network.target

[Service]
User=www-data
Group=www-data
WorkingDirectory=/var/www/miroutepe_server
ExecStart=/var/www/miroutepe_server/.venv/bin/gunicorn --workers 3 --bind 127.0.0.1:8001 miroutesite.wsgi:application

[Install]
WantedBy=multi-user.target

Ative o serviço:
sudo systemctl daemon-reload
sudo systemctl enable gunicorn-miroutesite
sudo systemctl start gunicorn-miroutesite

6. Nginx
Crie o arquivo /etc/nginx/sites-available/miroutepe:

server {
    listen 80;
    server_name miroutepe.com.br www.miroutepe.com.br;

    location /static/ {
        alias /var/www/miroutepe_server/staticfiles/;
    }

    location / {
        proxy_pass http://127.0.0.1:8001;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}

Ative o site:
sudo ln -s /etc/nginx/sites-available/miroutepe /etc/nginx/sites-enabled/
sudo systemctl restart nginx

7. Cloudflare Tunnel
Crie o arquivo /etc/cloudflared/config.yml:

tunnel: c8daecb0-a25e-47d3-aedf-4f6e58981468
credentials-file: /etc/cloudflared/c8daecb0-a25e-47d3-aedf-4f6e58981468.json

ingress:
  - hostname: miroutepe.com.br
    service: http://localhost:80
  - service: http_status:404


Inicie o serviço:
sudo systemctl enable cloudflared
sudo systemctl start cloudflared

🔐 Permissões
sudo chown -R www-data:www-data /var/www/miroutepe_server/staticfiles
sudo chown -R root:root /etc/nginx/sites-available/
sudo chown -R root:root /etc/systemd/system/
sudo chown -R root:root /etc/cloudflared/

🧪 Testes Finais
Acesse: https://miroutepe.com.br
Teste: https://miroutepe.com.br/static/css/style.css
Use Ctrl+F5 para forçar o navegador a recarregar os arquivos


💾 Backup de Arquivos Importantes
cp /var/www/miroutepe_server/miroutesite/settings.py ~/backups_miroutepe/settings.py.bkp
cp /etc/systemd/system/gunicorn-miroutesite.service ~/backups_miroutepe/gunicorn-miroutesite.service.bkp
cp /etc/nginx/sites-available/miroutepe ~/backups_miroutepe/nginx-miroutepe.bkp
cp /etc/cloudflared/config.yml ~/backups_miroutepe/cloudflared-config.yml.bkp


📤 Subir para o GitHub
cd /var/www/miroutepe_server
git add .
git commit -m "Deploy completo com configurações de produção"
git push origin main

🧠 Observações
Use python3 manage.py collectstatic sempre que alterar arquivos estáticos.
Reinicie o Cloudflare Tunnel se fizer alterações no config.yml.
Use Ctrl+F5 para limpar cache do navegador.

