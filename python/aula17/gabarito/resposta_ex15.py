def verifica_balanceamento(s):
    def auxiliar(s, aberto):
        if not s:
            return aberto == 0
        if aberto < 0:
            return False
        if s[0] == '(':
            return auxiliar(s[1:], aberto + 1)
        elif s[0] == ')':
            return auxiliar(s[1:], aberto - 1)
        return auxiliar(s[1:], aberto)
    
    return auxiliar(s, 0)

# Testes
print(verifica_balanceamento("()")) # True
print(verifica_balanceamento("(())")) # True
print(verifica_balanceamento("(()())")) # True
print(verifica_balanceamento(")(")) # False
print(verifica_balanceamento("(()")) # False
print(verifica_balanceamento("())(")) # False