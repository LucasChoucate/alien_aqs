# Alien Invasion

Jogo 2D desenvolvido em Python com Pygame durante a disciplina de
**AQS (Análise e Qualidade de Software)**. O jogador controla uma nave,
dispara contra uma frota de alienígenas e pode se movimentar pela tela.

## Requisitos

- Python 3.10 ou superior
- Pygame

## Instalação

No PowerShell, na pasta raiz do projeto, instale a dependência principal:

```powershell
py -m pip install pygame
```

Para executar os testes, instale também o Pytest e o plugin de mocks:

```powershell
py -m pip install pytest pytest-mock
```

## Como executar

Clone o repositório e entre na pasta do projeto. Em seguida, execute:

```powershell
py src\alien_invasion.py
```

## Controles

| Ação | Teclas |
| --- | --- |
| Mover para a esquerda | `A` ou `Seta para a esquerda` |
| Mover para a direita | `D` ou `Seta para a direita` |
| Disparar | `Barra de espaço` |
| Sair | Fechar a janela |

## Testes

Na raiz do projeto (dentro do src não vai funcionar), execute:

```powershell
py -m pytest
```

## Estrutura do projeto

```text
alien_aqs/
├── images/                # Imagens usadas no jogo
├── src/
│   ├── alien_invasion.py  # Ponto de entrada da aplicação
│   ├── settings.py        # Configurações do jogo
│   ├── ship.py            # Nave do jogador
│   ├── alien.py           # Alienígena
│   ├── fast_alien.py      # Alienígena rápido
│   ├── bullet.py          # Projéteis
│   ├── fleet_manager.py   # Gerenciamento da frota
│   └── game_renderer.py   # Renderização da tela
└── tests/                 # Testes automatizados
```