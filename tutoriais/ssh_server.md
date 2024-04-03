# Tutorial SSH Server

1. Liberar Guest Additions:
- URL: https://www.virtualbox.org/manual/ch04.html
- Baixar VBoxGuestAdditions.iso (7.0.14)
- sh ./VBoxLinuxAdditions.run

2. Liberar IP nas maquinas virtuais:
- URL: https://www.makeuseof.com/how-network-two-virtual-machines-with-virtualbox/
- Na aba network, NAT -> Adapter Brigde

3. Instalar SSH SERVER
- URL: https://www.cyberciti.biz/faq/ubuntu-linux-install-openssh-server/
- sudo apt install openssh-server
- sudo systemctl enable ssh
- sudo ufw allow ssh

4. Rodar SSH SERVER
- sudo systemctl start ssh
- sudo systemctl stop ssh
- sudo systemctl restart ssh
- sudo systemctl status ssh

5. Liberar apenas para PUBLIC KEY!
- /etc/ssh/sshd_config
- PubkeyAuthentication yes
- AuthorizedKeysFile      .ssh/authorized_keys .ssh/authorized_keys2
- PasswordAuthentication no
- PermitEmptyPasswords no

6. Gerar chave
- uRL: https://docs.github.com/pt/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent
- ssh-keygen -t rsa -b 4096 -C "your_email@example.com"

7. Adicionar a lista de permissão
- Jogar "id_rsa.pub" gerado no client para o arquivo ~/.ssh/authorized_keys do servidor
