n = int(input(''))
eventos = []
for e in range(n):
    eventos.append(str(input('')).split(' '))

"""
tempo_resposta_usuario = 
{
    '2':{
        par_ok: False
        par_evento: ['R', 'E'],
        tempo: 12
    }
    '45':{
        par_ok: False
        par_evento: ['R', 'E'],
        tempo: 12
    }
}
"""
tempo_resposta_usuario = {}

# R - mensagem recebida
# E - mensagem enviada
# T - tempo entre eventos

tempo = 0
for e in eventos:
    if e[1] not in tempo_resposta_usuario.keys():
        if e[0] == 'T':
            for u in tempo_resposta_usuario.items():
                usuario = u[0]
                par_evento = u[1]['par_evento']
                tempo = u[1]['tempo']+int(e[1])
                tempo_resposta_usuario.update(
                    {
                        usuario:{
                            'par_ok':False,
                            'par_evento':par_evento,
                            'tempo':tempo
                        }
                    }
                )
        else:
            tempo_resposta_usuario.update(
            {
                e[1]:{
                    'par_ok':False,
                    'par_evento': [e[0]],
                    'tempo': 1
                }
            }
        )
    else:
        if e[0] == 'T':
            for u in tempo_resposta_usuario.items():
                usuario = u[0]
                par_ok = u[1]['par_ok']
                par_evento = u[2]['par_evento']
                tempo = u[3]['tempo']+int(e[1])
                tempo_resposta_usuario.update(
                    {
                        usuario:{
                            'par_ok':par_ok,
                            'par_evento':par_evento,
                            'tempo':tempo
                        }
                    }
                )
        else:
            for u in tempo_resposta_usuario.items():
                usuario = u[0]
                par_ok = u[1]['par_ok']
                par_evento = u[2]['par_evento']
                tempo = u[3]['tempo']+1
                tempo_resposta_usuario.update(
                    {
                        usuario:{
                            'par_evento':par_evento,
                            'tempo':tempo
                        }
                    }
                )


print(tempo_resposta_usuario)
