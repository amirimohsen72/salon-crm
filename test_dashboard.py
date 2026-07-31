import os
os.environ['DEBUG'] = 'True'
os.environ['DJANGO_SETTINGS_MODULE'] = 'config.settings'
import django
django.setup()
from django.test import Client
from accounts.models import CustomUser as User

# Create or update admin user with known password
user, created = User.objects.get_or_create(username='admin', defaults={'email': 'admin@example.com'})
if created:
    user.set_password('admin123')
    user.save()
    with open('test_output.txt', 'w', encoding='utf-8') as f:
        f.write('Created new admin user\n')
else:
    user.set_password('admin123')
    user.save()
    with open('test_output.txt', 'w', encoding='utf-8') as f:
        f.write('Updated admin user password\n')

client = Client()
login_result = client.login(username='admin', password='admin123')
with open('test_output.txt', 'a', encoding='utf-8') as f:
    f.write('Login result: ' + str(login_result) + '\n')

resp = client.get('/dashboard/')
with open('test_output.txt', 'a', encoding='utf-8') as f:
    f.write('Dashboard status: ' + str(resp.status_code) + '\n')
    f.write('Dashboard URL: ' + str(resp.url if hasattr(resp, 'url') else 'N/A') + '\n')

if resp.status_code == 302:
    resp = client.get(resp.url)
    with open('test_output.txt', 'a', encoding='utf-8') as f:
        f.write('After redirect status: ' + str(resp.status_code) + '\n')

content = resp.content.decode('utf-8')
with open('test_output.txt', 'a', encoding='utf-8') as f:
    f.write('Contains rzrv: ' + str('رزروهای امروز' in content) + '\n')
    f.write('Contains tld: ' + str('تولدهای امروز' in content) + '\n')
    f.write('Contains bg-fade2-green: ' + str('bg-fade2-green' in content) + '\n')
    f.write('Contains bg-fade2-pink: ' + str('bg-fade2-pink' in content) + '\n')
    f.write('--- Content preview ---\n')
    f.write(content[:3000] + '\n')
print('Done')