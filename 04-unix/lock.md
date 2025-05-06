1. `docker run -it --rm ubuntu bash` - вход в контейнер
2. `apt-get update` — срабатывает.  
3. Заменяем резолвер на localhost:  
   ```bash
   echo "nameserver 127.0.0.1" > /etc/resolv.conf
   ```  
4. Проверяем содержимое:  
   ```bash
   cat /etc/resolv.conf
   # nameserver 127.0.0.1
   ```  
5. Теперь `apt-get update` упадёт из-за невозможности резолва:  
   ```bash
   apt-get update
   # Temporary failure resolving 'archive.ubuntu.com'
   ```
