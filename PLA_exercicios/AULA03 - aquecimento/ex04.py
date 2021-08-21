cpf = input("CPF: ")
if len(cpf) < 11:
    cpf = cpf.zfill(11)
cpf = '{}.{}.{}-{}'.format(cpf[:3],cpf[3:6],cpf[6:9],cpf[9:])
print(cpf)