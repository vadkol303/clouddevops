1. `apt-get update` — срабатывает.  
2. Заменяем резолвер на localhost:  
   ```bash
   echo "nameserver 127.0.0.1" > /etc/resolv.conf
   ```  
3. Проверяем содержимое:  
   ```bash
   cat /etc/resolv.conf
   # nameserver 127.0.0.1
   ```  
4. Теперь `apt-get update` упадёт из-за невозможности резолва:  
   ```bash
   apt-get update
   # Temporary failure resolving 'archive.ubuntu.com'
   ```
